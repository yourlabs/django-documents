from django.core import urlresolvers
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.contenttypes.models import ContentType

from genericm2m.models import RelatedObjectsDescriptor, RelatedObject

from .settings import UPLOAD_TO

__all__ = ['Document', 'get_related_documents']

fs = FileSystemStorage(location=UPLOAD_TO)


class Document(models.Model):
    file = models.FileField(storage=fs, upload_to=UPLOAD_TO)
    related = RelatedObjectsDescriptor()

    def __unicode__(self):
        return self.file.name[len(UPLOAD_TO) + 1:]

    def get_download_url(self):
        return urlresolvers.reverse('documents_document_download', args=(
            self.pk,))


def get_related_documents(model):
    object_type = ContentType.objects.get_for_model(model)
    parent_type = ContentType.objects.get_for_model(Document)

    relations = RelatedObject.objects.filter(object_type=object_type,
        object_id=model.pk, parent_type=parent_type)

    return Document.objects.filter(pk__in=relations.values_list('parent_id'))
