class User:
    '''
    Create a user class to generate new instances of a user
    '''

    User = []
    UserDirectory = []

    def __init__(self, userName, passWord):
        '''
        Method to define the properties of a user
        '''
        self.userName = userName
        self.passWord = passWord

    def saveUser(self):
        '''
        Method to save a new user instance in the user directory
        '''
        User.UserDirectory.append(self)

class Credentials:
    '''
    Create a credentials class for creating new credential objects
    '''
    CredentialsDirectory = []
    @classmethod

    def verifyUser(cls, userName, passWord):
        '''
        Method to verify if the user is an already existing user in the user directory
        '''
        existingUser = ''
        for user in User.UserDirectory:
            if (User.UserDirectory == userName and User.passWord == passWord):
                existingUser == user.UserName
        return existingUser

    def __init__(self, accountName, userEmail, userName, passWord):
            '''
            Method defining user credentials to be stored
            '''
            self.accountName = accountName
            self.userEmail = userEmail
            self.userName = userName
            self.passWord = passWord
            
    def saveCredentials(self):
        '''
        Method to store new credential details to the user directory
        '''
        Credentials.CredentialsDirectory.append(self)

    def deleteCredentials(self):
        '''
        Method to delete existing credentials from the credentials directory
        '''
        Credentials.CredentialsDirectory.remove(self)

    @classmethod
    def searchCredentials(cls, accountName):
        '''
        Method searches for an account name and returns account matching that name
        '''
        for credential in cls.CredentialsDirectory:
            if credential.accountName == accountName:
                return credential

    @classmethod
    def credentialsExist(cls, accountName):
        '''
        Method to check if entered credentials exist in the credentials directory 
        '''
        for credential in cls.CredentialsDirectory:
            if credential.accountName == accountName:
                return True
        return False

    @classmethod
    def displayCredentials(cls):
        """
        Method to return all entries in the credentials directory
        """
        return cls.CredentialsDirectory


