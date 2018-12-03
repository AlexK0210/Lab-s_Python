from app import app
import unittest, os


class FlaskTest(unittest.TestCase):
    def setUp(self):

        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    """
    def test_no_page(self):
        response = self.app.get('/no')
        self.assertEqual(response.status_code, 200)
    """

    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_page_render(self):
        response = self.app.get('/')
        self.assertIn(b'HYPEBEAST STORE', response.data)

    def test_user_page(self):
        response = self.app.get('/shirts')
        self.assertEqual(response.status_code, 200)

    def test_user_page_render(self):
        response = self.app.get('/shirts')
        self.assertIn(b'HYPEBEAST STORE', response.data)

    def test_booking_page(self):
        response = self.app.get('/shirt/<product_id>')
        self.assertEqual(response.status_code, 200)

    def test_booking_page_render(self):
        response = self.app.get('/receipt')
        self.assertIn(b'HYPEBEAST STORE', response.data)

    def test_return_page(self):
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_return_page_render(self):
        response = self.app.get('/contact')
        self.assertIn(b'HYPEBEAST STORE', response.data)

if __name__ == '__main__':
    unittest.main()