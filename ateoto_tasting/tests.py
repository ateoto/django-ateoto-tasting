from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse

from ateoto_tasting.models import *

class ModelsTestCase(TestCase):
    fixtures = ['ateoto-tasting-testdata.json']

    def setUp(self):
        pass

    def test_

class ViewsTestCase(TestCase):
    def test_index(self):
        #resp = self.client.get(reverse('ateoto-tasting-index'))
        #self.assertEqual(resp.status_code, '200')
        pass
