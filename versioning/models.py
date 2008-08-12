
from datetime import datetime

from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

from versioning.managers import RevisionManager

class Revision(models.Model):
    """
    A single revision for an object.
    """
    sha1 = models.CharField(max_length=40)
    object_pk = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType)
    content_object = generic.GenericForeignKey("object_pk", "content_type")
    created_at = models.DateTimeField(default=datetime.now)
    delta = models.TextField()
    
    objects = RevisionManager()
    
    def __unicode__(self):
        return self.sha1
