from django.contrib.auth.models import User, Group

import autocomplete_light


class AutocompleteDocumentRelations(
    autocomplete_light.AutocompleteGenericBase):

    choices = (
        User.objects.all(),
        Group.objects.all(),
    )

    search_fields = (
        ('username', 'email', 'first_name', 'last_name'),
        ('name',),
    )

autocomplete_light.register(AutocompleteDocumentRelations)
