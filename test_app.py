import unittest
from application import application

class FlaskAppTest(unittest.TestCase):

    def setUp(self):
        application.testing = True
        self.client = application.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        
    def test_home_page_content(self):
        """Check if page contains expected heading"""
        response = self.client.get("/")
        self.assertIn(b"TechNova Solutions", response.data)

    def test_button_exists(self):
        """Verify button text exists"""
        response = self.client.get("/")
        self.assertIn(b"Check Application", response.data)

    def test_footer_exists(self):
        """Verify footer content"""
        response = self.client.get("/")
        self.assertIn(b"AWS EC2", response.data)


if __name__ == "__main__":
    unittest.main()
