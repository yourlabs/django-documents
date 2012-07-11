from django.db import models

from genericm2m.models import RelatedObjectsDescriptor

from .settings import UPLOAD_TO

class Document(models.Model):
    file = models.FileField(upload_to=UPLOAD_TO)
    related = RelatedObjectsDescriptor()
