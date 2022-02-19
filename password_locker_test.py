import unittest

from setuptools import setup
from password_locker import User
from password_locker import Credentials

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

    def test_deleteUser(self):
        '''
        Test case checks if existing user account is deleted by checking the length of the user directory
        '''
        self.newUser.deleteUser()
        self.assertEqual(len(User.UserDirectory),0)

class CredentialsTest(unittest.TestCase):
    '''
    Test class to define test cases for the credentials class
    '''
    def setUp(self):
        '''
        Method will run before credentials test methods run
        '''
        self.newCredentials = User('YouTube', 'jaymarshall@gmail.com', 'Jay Marshall', 'dgwyiwydcgig')

    def test_initialization(self):
        '''
        Test case checks if object initialization done correctly
        '''
        self.assertEqual(self.newCredentials.accountName, 'YouTube')
        self.assertEqual(self.newCredentials.userEmail, 'jaymarshall@gmail.com')
        self.assertEqual(self.newCredentials.userName,'Jay Marshall')
        self.assertEqual(self.newCredentials.passWord, 'dgwyiwydcgig')

if __name__=='__main__':
    unittest.main()


