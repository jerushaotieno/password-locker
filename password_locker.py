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

    def deleteUser(self):
        '''
        Method to delete an existing user instance from the user directory
        '''
        User.UserDirectory.remove(self)

class Credentials:
    '''
    Create a credentials class for creating new credential objects
    '''
    credentialsDirectory = []
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
            
