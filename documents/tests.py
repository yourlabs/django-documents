from django.test import TestCase
from django.contrib.auth.models import User, Group

from models import get_related_documents


class GetRelatedDocumentsTestCase(TestCase):
    fixtures = ['test_fixtures']

    def test_get_related_documents(self):
        fixtures = (
            {
                'model': User.objects.get(username='hsum'),
                'document_ids': [2],
            },
            {
                'model': User.objects.get(username='hwolf'),
                'document_ids': [1, 2],
            },
            {
                'model': Group.objects.get(name='bluesmen'),
                'document_ids': [1],
            },
        )

        for fixture in fixtures:
            result = get_related_documents(fixture['model'])
            self.assertEquals(list(result.values_list('pk', flat=True)),
                fixture['document_ids'])
