from datetime import datetime

from django.contrib.sites.models import Site
from django.core.cache import cache
from django.http import HttpResponse
from django.test import TestCase

from visitor.models import Visitor

class BaseTestCase(TestCase):
        
    def tearDown(self):
        super(BaseTestCase,self).setUp()        
        cache.clear()

class VisitorModelTest(BaseTestCase):

    def test_create_visitor(self):

        count = Visitor.objects.count()
        visitor = Visitor.objects.create(
            visitor_key = 'abcdefg',
            last_session_key = 'hijklmnop'
        )
        visitor.save()
        self.assertTrue(count < Visitor.objects.count())

    """ test on possibly deprecated method
    def test_manager_create_from_ip(self):
        ip = '127.0.0.1'
        visitor = Visitor.objects.create_from_ip(ip)
        self.assertEquals(Visitor.objects.count(), 1)
        
        visitor = Visitor.objects.create_from_ip(ip)
        self.assertEquals(Visitor.objects.count(), 1)        
    """