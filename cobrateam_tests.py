import os
import index
import unittest
import tempfile

class CobraTeamTestCase(unittest.TestCase):

    def setUp(self):
        self.app = index.app.test_client()
            
    def test_index(self):
        request = self.app.get('/')
        assert 'Projects' in request.data
        
if __name__ == '__main__':
    unittest.main()
