"""
Signals for this application.

document_pre_download
    Emited by documents.views.document_download, providing request and document
    arguments. If the reciever raises a documents.exceptions.DownloadForbidden
    then the view will return 503.
"""

from django import dispatch

document_pre_download = dispatch.Signal(providing_args=['request', 'document'])
