
from versioning.models import Revision

def revisions_for_object(instance):
    return Revision.objects.get_for_object(instance)
