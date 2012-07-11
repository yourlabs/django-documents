from django.conf.urls import patterns, url

urlpatterns = patterns('documents.views',
    url('(?P<object_id>\d+)/download/$', 'document_download',
        name='documents_document_download'),
)
