
from versioning.utils import revisions_for_object

_registry = {}

class AlreadyRegistered(Exception):
    pass

def register(model, fields=None):
    """
    """
    from django.db import models
    from django.db.models import signals as model_signals
    from versioning.signals import pre_save
    
    opts = model._meta
    
    if fields is None:
        raise TypeError, "You must give at least one field."
    else:
        for field in fields:
            f = opts.get_field(field)
            if not isinstance(f, models.TextField):
                raise TypeError, "versioning cannot handle anything other " \
                                 "than a TextField. %s is of type %s" % \
                                 (field, type(f))
    
    if model in _registry:
        raise AlreadyRegistered
    _registry[model] = fields
    
    model_signals.pre_save.connect(pre_save, sender=model)
