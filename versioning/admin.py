
from django.contrib import admin
from django import forms
from django.contrib.contenttypes import generic
from django.utils.safestring import mark_safe

from versioning.models import Revision

class DeltaWidget(forms.Widget):
    """
    Render a delta in a form.
    TODO: this needs some more work.
    """
    def render(self, name, data, attrs):
        return mark_safe(data.replace("\n", "<br />"))

class RevisionInline(generic.GenericTabularInline):
    model = Revision
    ct_field = "content_type"
    ct_fk_field = "object_pk"
    extra = 0
    fields = ("delta",)
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "delta":
            kwargs["widget"] = DeltaWidget
            return db_field.formfield(**kwargs)
        super(RevisionInline, self).formfield_for_dbfield(db_field, **kwargs)

class RevisionAdmin(admin.ModelAdmin):
    list_display = ("sha1", "content_type", "object_pk", "created_at")
    list_filter = ("created_at", "content_type",)

admin.site.register(Revision, RevisionAdmin)
