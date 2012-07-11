import autocomplete_light
from autocomplete_light.contrib.generic_m2m import GenericModelForm, \
    GenericModelMultipleChoiceField

from .widgets import DocumentAdminFileWidget
from .models import Document


class DocumentForm(GenericModelForm):
    related = GenericModelMultipleChoiceField(
        widget=autocomplete_light.MultipleChoiceWidget(
            'AutocompleteDocumentRelations'))

    class Meta:
        model = Document


class DocumentAdminForm(DocumentForm):
    class Meta:
        widgets = {
            'file': DocumentAdminFileWidget,
        }
