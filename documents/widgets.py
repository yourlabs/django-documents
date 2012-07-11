from django import forms
from django.utils.html import escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget


class DocumentAdminFileWidget(AdminFileWidget):
    """
    Replacement for Django's AdminFileWidget which displays the file name and
    download url rather than using the file path for both.
    """

    def render(self, name, value, attrs=None):
        substitutions = {
            'initial_text': self.initial_text,
            'input_text': self.input_text,
            'clear_template': '',
            'clear_checkbox_label': self.clear_checkbox_label,
        }
        template = u'%(input)s'
        substitutions['input'] = super(forms.ClearableFileInput, self).render(
            name, value, attrs)

        if value and hasattr(value, "url"):
            template = self.template_with_initial
            url = value.instance.get_download_url()
            label = force_unicode(value.instance)

            substitutions['initial'] = (u'<a href="%s">%s</a>'
                                        % (escape(url),
                                           escape(label)))

        return mark_safe(template % substitutions)
