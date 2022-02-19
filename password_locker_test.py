import unittest

from setuptools import setup
from password_locker import User

class UserTest(unittest.TestCase):
    '''
    Create a test class to define test cases for the User class
    '''
    def setUp(self):
        '''
        Method will run before test methods run
        '''
        self.newUser = User('Jay Marshall', 'uyuqfdfiwiq')

    def test_initialization(self):
        '''
        Checks if object initialization done correctly
        '''
        self.assertEqual(self.newUser.userName,'Jay Marshall')
        self.assertEqual(self.newUser.passWord, 'uyuqfdfiwiq')

if __name__=='__main__':
    unittest.main()


