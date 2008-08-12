
import sha

from django.contrib.contenttypes.models import ContentType

from versioning import _registry
from versioning.diff import unified_diff
from versioning.models import Revision

def pre_save(instance, **kwargs):
    """
    """
    model = kwargs["sender"]
    fields = _registry[model]
    
    original = model._default_manager.get(pk=instance.pk)
    ct = ContentType.objects.get_for_model(model)
    
    diff = []
    for field in fields:
        original_data = getattr(original, field)
        new_data = getattr(instance, field)
        data_diff = unified_diff(original_data.splitlines(),
                                 new_data.splitlines(), context=3)
        diff.extend(["--- %s.%s" % (model.__name__, field),
                     "+++ %s.%s" % (model.__name__, field)])
        for line in data_diff:
            diff.append(line)
    
    delta = "\n".join(diff)
    sha1 = sha.new(delta)
    rev = Revision(sha1=sha1.hexdigest(), object_pk=instance.pk,
                   content_type=ct, delta=delta)
    rev.save()
