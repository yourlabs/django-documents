from django.conf.urls import patterns, include, url

import autocomplete_light
autocomplete_light.autodiscover()

# project-specific overrides
import autocomplete_light_registry

# project specific document permissions
import documents
def document_security(sender, request, document, **kwargs):
    if not request.user.is_staff:
        raise documents.DownloadForbidden()
documents.document_pre_download.connect(document_security)

# test_project specific hack
import os.path
from documents.settings import UPLOAD_TO
from documents.models import Document
for document in Document.objects.all():
    name = document.file.name.split('/')[-1]
    # the setting varies depending on where the project was checked out
    document.file = os.path.join(UPLOAD_TO, name)
    document.save()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^test_project/', include('test_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^documents/', include('documents.urls')),
)
