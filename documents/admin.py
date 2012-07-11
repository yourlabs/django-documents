from django.contrib import admin

from models import Document
from forms import DocumentAdminForm


class DocumentAdmin(admin.ModelAdmin):
    form = DocumentAdminForm
admin.site.register(Document, DocumentAdmin)
