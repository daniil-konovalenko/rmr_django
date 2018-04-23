import django.test

from django.contrib.auth.models import User, AnonymousUser
from django.http import HttpResponse
from django.test import RequestFactory

from rmr import ClientError
from rmr.views.decorators.auth import authentication_required


class TestAuthenticationRequired(django.test.SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User(username='test', password='password')
    
    def test_authenticated(self):
        
        @authentication_required
        def view(r):
            return HttpResponse()
           
        request = self.factory.get('/')
        request.user = self.user
        
        response = view(request)
        
        self.assertEqual(response.status_code, 200)
    
    def test_not_authenticated(self):
        @authentication_required
        def view(r):
            return HttpResponse()
        
        request = self.factory.get('/')
        request.user = AnonymousUser()
        
        with self.assertRaises(ClientError) as context:
            response = view(request)
        
        exception = context.exception
        self.assertEqual(exception.http_code, 401)
        self.assertEqual(exception.code, 'authentication_required')
        self.assertEqual(exception.message, 'Authentication required')
