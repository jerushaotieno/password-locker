import unittest

from setuptools import setup
from password_locker import User

class UserTest(unittest.TestCase):
    '''
    Test class to define test cases for the User class
    '''
    def setUp(self):
        '''
        Method will run before test methods run
        '''
        self.newUser = User('Jay Marshall', 'uyuqfdfiwiq')

    def test_initialization(self):
        '''
        Test case checks if object initialization done correctly
        '''
        self.assertEqual(self.newUser.userName,'Jay Marshall')
        self.assertEqual(self.newUser.passWord, 'uyuqfdfiwiq')

    def test_saveUser(self):
        '''
        Test case checks if new user instance is saved by checking the length of the user directory
        '''
        self.newUser.saveUser()
        self.assertEqual(len(User.UserDirectory),1)


if __name__=='__main__':
    unittest.main()


