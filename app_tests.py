import os
from app import app
from app import db
import unittest
import tempfile

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.testing = True
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.config['DATABASE'])

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_get_api_request(self):
        result = self.app.get('/api/clients/')
        self.assertEqual(result.status_code, 200)
        result = self.app.get('/api/products/')
        self.assertEqual(result.status_code, 200)
        result = self.app.get('/api/all_requests/')
        self.assertEqual(result.status_code, 200)

    def test_post_api_request(self):
        result = self.app.post('/api/request/', data=dict(
            title="Title",
            description="Description",
            client=2,
            product=2,
            priority=3,
            date="2017-08-12",
        ), follow_redirects=True)
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()