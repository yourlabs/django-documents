.. image:: https://secure.travis-ci.org/yourlabs/django-autocomplete-light.png?branch=master

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

Demo
----

Run the demo of a release in a temporary folder::

    DOCUMENTS_VERSION="0.0.3"

    cd /tmp
    rm -rf django-documents documents_env
    virtualenv documents_env
    source documents_env/bin/activate
    pip install django-documents==$DOCUMENTS_VERSION
    git clone https://github.com/yourlabs/django-documents.git
    cd django-documents/test_project
    git checkout $DOCUMENTS_VERSION
    pip install -r requirements.txt
    ./manage.py runserver

Login with test / test.

Or current development sources (might be broken)::

    cd /tmp
    rm -rf django-documents documents_env
    virtualenv documents_env
    source documents_env/bin/activate
    pip install -e git+https://github.com/yourlabs/django-documents.git#egg=documents
    cd documents_env/src/documents/test_project
    pip install -r requirements.txt
    ./manage.py runserver

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

**Set settings.DOCUMENTS_UPLOAD_TO** to the absolute path where uploads should
be stored. This must be a private directory.

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

Display documents related to a model
------------------------------------

Use get_related_documents() from Python::

    from documents.models import get_related_documents

    your_model = YourModel.objects.get(pk=XXX)

    related_documents = get_related_documents(your_model)

Or from a template::

    {% load documents_tags %}

    {% for document in your_model|get_related_documents %}
        {{ document }}
    {% endfor %}

Note that get_related_documents() returns a QuerySet, ie. you can get a count::

    get_related_documents(your_model).count()

Or from a template::

    {% with related_documents=your_model|get_related_documents %}
        {{ related_documents.count }}
    {% endwith %}

Resources
---------

- `Mailing list graciously hosted
  <http://groups.google.com/group/yourlabs>`_ by `Google
  <http://groups.google.com>`_
- `Git graciously hosted
  <https://github.com/yourlabs/django-documents/>`_ by `GitHub
  <http://github.com>`_,
- `Package graciously hosted
  <http://pypi.python.org/pypi/django-documents/>`_ by `PyPi
  <http://pypi.python.org/pypi>`_,
- `Continuous integration graciously hosted
  <http://travis-ci.org/yourlabs/django-documents>`_ by `Travis-ci
  <http://travis-ci.org>`_
