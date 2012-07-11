from django.contrib import admin

from models import Document
from forms import DocumentForm


class DocumentAdmin(admin.ModelAdmin):
    form = DocumentForm
admin.site.register(Document, DocumentAdmin)
