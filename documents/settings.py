import os
import os.path

from django.conf import settings

UPLOAD_TO = settings.DOCUMENT_UPLOAD_TO

if not os.path.exists(UPLOAD_TO):
    os.makedirs(UPLOAD_TO)
    os.chmod(UPLOAD_TO, 0700)
