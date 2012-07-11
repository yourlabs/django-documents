from django.core import urlresolvers
from django.db import models
from django.core.files.storage import FileSystemStorage

from genericm2m.models import RelatedObjectsDescriptor

from .settings import UPLOAD_TO


fs = FileSystemStorage(location=UPLOAD_TO)


class Document(models.Model):
    file = models.FileField(storage=fs, upload_to=UPLOAD_TO)
    related = RelatedObjectsDescriptor()

    def __unicode__(self):
        return self.file.name[len(UPLOAD_TO) + 1:]

    def get_download_url(self):
        return urlresolvers.reverse('documents_document_download', args=(
            self.pk,))
