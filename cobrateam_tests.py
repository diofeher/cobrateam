import os
import index
import unittest
import tempfile

class CobraTeamTestCase(unittest.TestCase):

    def setUp(self):
        self.app = index.app.test_client()
            
    def test_index(self):
        request = self.app.get('/')
        assert 'Dorgas Manolo' in request.data
        
    def test_staff(self):
        request= self.app.get('/staff')
        assert 'Team' in request.data
        
    def test_challenges(self):
        request= self.app.get('/challenges')
        assert 'challenges' in request.data

    def test_contact(self):
        request= self.app.get('/contact')
        assert 'contact' in request.data

if __name__ == '__main__':
    unittest.main()