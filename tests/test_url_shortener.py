import unittest
from app import create_app

class URLShortenerTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_valid_url_shortening(self):
        response = self.client.post('/shorten', json={"url": "https://google.com"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("short_url", response.get_json())

    def test_invalid_url(self):
        response = self.client.post('/shorten', json={"url": "google"})
        self.assertEqual(response.status_code, 400)

    def test_redirect(self):
        # First shorten
        res = self.client.post('/shorten', json={"url": "https://example.com"})
        code = res.get_json()["short_url"].split("/")[-1]
        
        # Then test redirect
        response = self.client.get(f'/{code}')
        self.assertEqual(response.status_code, 302)

if __name__ == '__main__':
    unittest.main()
