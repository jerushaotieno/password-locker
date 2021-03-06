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

class CredentialsTest(unittest.TestCase):
    '''
    Test class to define test cases for the credentials class
    '''
    def setUp(self):
        '''
        Method will run before credentials test methods run
        '''
        self.newCredential = Credentials('YouTube', 'Jay Marshall', 'dgwyiwydcgig')

    def test_initialization(self):
        '''
        Test case checks if new credentials instance has occurred correctly
        '''
        self.assertEqual(self.newCredential.accountName, 'YouTube')
        self.assertEqual(self.newCredential.userName,'Jay Marshall')
        self.assertEqual(self.newCredential.passWord, 'dgwyiwydcgig')

    def saveCredentialsTest(self):
        '''
        Test case checks if the credentials object has been saved to the credentials directory
        '''
        self.newCredential.saveCredentials()
        self.assertEqual(len(Credentials.CredentialsDirectory),1)

    def tearDown(self):
        '''
        Method to clean up after each test case runs
        '''
        Credentials.CredentialsDirectory = []

    def testSaveMultipleAccounts(self):
        '''
        test case to check if multiple credentials can be saved to the credentials directory
        '''
        self.newCredential.saveCredentials()
        testCredential = Credentials('Gmail', 'Mano Lay', 'iyfayafyvgag')
        testCredential.saveCredentials()
        self.assertEqual(len(Credentials.CredentialsDirectory),2)

    def testDeleteCredentials(self):
        '''
        Test method to delete a users credentials from the credentials directory
        '''
        self.newCredential.saveCredentials()
        testCredential = Credentials('Gmail', 'Mano Lay', 'iyfayafyvgag')
        testCredential.saveCredentials()

        self.newCredential.deleteCredentials()
        self.assertEqual(len(Credentials.CredentialsDirectory),1)

    def testSearchCredentials(self):
        '''
        Test case to find a credential using the account name and to display the results of the search
        '''
        self.newCredential.saveCredentials()
        testCredential = Credentials('Gmail', 'Mano Lay', 'iyfayafyvgag') 
        testCredential.saveCredentials()

        searchedCredential = Credentials.searchCredentials('Gmail')

        self.assertEqual(searchedCredential.accountName,testCredential.accountName)

    def testCredentialsExist(self):
        '''
        Test checks and returns True if a credential exists else it returns False if it does not exist
        '''
        self.newCredential.saveCredentials()
        searchCredential = Credentials('Gmail', 'Mano Lay', 'iyfayafyvgag')  
        searchCredential.saveCredentials()
        credentialsFound = Credentials.credentialsExist('Gmail')
        self.assertTrue(credentialsFound)

    def testDisplayCredentials(self):
        '''
        Method displays all credentials saved by a user
        '''

        self.assertEqual(Credentials.displayCredentials(), Credentials.CredentialsDirectory)

    

if __name__=='__main__':
    unittest.main()


