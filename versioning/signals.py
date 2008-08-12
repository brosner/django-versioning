
import sha

from django.contrib.contenttypes.models import ContentType

from versioning import _registry
from versioning.models import Revision

def pre_save(instance, **kwargs):
    """
    """
    model = kwargs["sender"]
    fields = _registry[model]
    
    original = model._default_manager.get(pk=instance.pk)
    ct = ContentType.objects.get_for_model(model)
    
    # TODO: dont hard-code [0]
    sha1 = sha.new(getattr(instance, fields[0]))
    
    rev = Revision(sha1=sha1.hexdigest(), object_pk=instance.pk,
                   content_type=ct)
    rev.save()
