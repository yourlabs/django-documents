django-documents
================

This simple app provides:

- a Document model with:

  - a generic many to many relation
  - a file field that uploads to a private directory
  - a method get_download_url()
- a view to download a document which allows custom security checks through a
  signal
- a signal, document_pre_download, that is emited by the download view, and
  which responds with 503 if emiting the signal raises a DownloadForbidden
  exception
- clean admin integration
- south support

Install django-generic-m2m
--------------------------

Refer to `django-generic-m2m installation documentation
<http://django-generic-m2m.readthedocs.org/en/latest/installation.html#installation>`_, do "Installation" and "Adding to your Django Project".

Install autocomplete_light
--------------------------

Refer to `django-autocomplete-light installation documentation
<http://django-autocomplete-light.readthedocs.org/en/latest/quick.html#quick-install>`_, do "Quick install" and "Quick admin integration".

Install django-documents
------------------------

Download the lastest release::

    pip install django-documents

Or install the development version::

    pip install -e git+https://github.com/yourlabs/django-documents.git#egg=documents

Add to settings.INSTALLED_APPS::

    'documents',

If using south, run::

    ./manage.py migrate

Else, run::

    ./manage.py syncdb

Add to urls.py::

    url(r'^documents/', include('documents.urls')),

**Set settings.UPLOAD_TO** to the absolute path where uploads should be stored.
This must be private.

Prepare the generic many to many autocomplete
---------------------------------------------

Register a `generic autocomplete
<http://django-autocomplete-light.readthedocs.org/en/latest/generic.html#autocompletegeneric>`_,
with name "AutocompleteDocumentRelations". There is an example in `test_project
<https://github.com/yourlabs/django-documents/blob/master/test_project/test_project/autocomplete_light_registry.py>`_ which is imported in `urls.py
<https://github.com/yourlabs/django-documents/blob/master/test_project/test_project/urls.py>`_.
Refer the `django-autocomplete-light documentation about the registry
<http://django-autocomplete-light.readthedocs.org/en/latest/forms.html#module-autocomplete_light.registry>`_
for alternative methods.

If the project already uses django-generic-m2m and django-autocomplete-light, a
good solution is to re-register the project's generic autocomplete with
name='AutocompleteDocumentRelations', ie.::

    # your project specific autocomplete
    class AutocompleteProject(autocomplete_light.AutocompleteGenericBase):
        # ....

    # register for your project needs
    autocomplete_light.register(AutocompleteProject)

    # registery for documents relations
    autocomplete_light.register(AutocompleteProject,
        name='AutocompleteDocumentRelations')

Secure your documents
---------------------

Connect to document_pre_import, for example::

    # project specific document permissions
    import documents
    def document_security(sender, request, document, **kwargs):
        if not request.user.is_staff:
            raise documents.DownloadForbidden()
    documents.document_pre_download.connect(document_security)
