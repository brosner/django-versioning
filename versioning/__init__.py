
from versioning.utils import revisions_for_object

registry = []

class AlreadyRegistered(Exception):
    pass

def register(model):
    """
    """
    from django.db.models import signals as model_signals
    
    from versioning.signals import pre_save
    
    if model in registry:
        raise AlreadyRegistered
    registry.append(model)
    
    model_signals.pre_save.connect(pre_save, sender=model)
