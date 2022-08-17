from urllib import response
from flask_testing import TestCase
from flask import current_app, url_for
from app import app
from routes.usuarios import usuarios

class MainTest(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        print("TESTING...")
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])
    
    def test_hello_get(self):
        response = self.client.get(url_for('hiworld'))
        self.assert200(response)

    '''def test_hello_post(self):
        fake_form={
            'username' : 'fake',
            'password' : 'fake_password'
        }
        response = self.client.post(url_for('hiworld'),data=fake_form)
        self.assertRedirects(response,url_for('test_form'))
    '''