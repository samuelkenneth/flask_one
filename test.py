import unittest
from dashf import app
class BasicTestCase(unittest.TestCase):
    def test_home(self):
            tester = app.test_client(self)
            response = tester.get('/', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'hello, this is our first flask website 2')
if __name__ == '__main__':
    unittest.main()
