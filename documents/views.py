import stat
import os
import mimetypes

from django import http
from django import shortcuts
from django.utils.translation import ugettext_lazy as _

from signals import document_pre_download
from exceptions import DownloadForbidden
from models import Document


def document_download(request, object_id):
    document = shortcuts.get_object_or_404(Document, pk=object_id)

    try:
        document_pre_download.send(sender=document_download, request=request,
            document=document)
    except DownloadForbidden:
        return http.HttpResponseForbidden(_(u"""
            Your are not allowed to download this document. If you think that
            you should download it, please contact support
            """.strip()))

    statobj = os.stat(document.file.path)
    mimetype, encoding = mimetypes.guess_type(document.file.path)
    mimetype = mimetype or 'application/octet-stream'
    with open(document.file.path, 'rb') as f:
        response = http.HttpResponse(f.read(), mimetype=mimetype)
    if stat.S_ISREG(statobj.st_mode):
        response["Content-Length"] = statobj.st_size
    if encoding:
        response["Content-Encoding"] = encoding
    response["Content-Disposition"] = 'attachement; filename=' + unicode(
        document)
    return response
