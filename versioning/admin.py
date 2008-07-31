
from django.contrib import admin

from versioning.models import Revision

class RevisionAdmin(admin.ModelAdmin):
    list_display = ("content_type", "object_pk", "created_at")
    list_filter = ("created_at", "content_type",)

admin.site.register(Revision, RevisionAdmin)
