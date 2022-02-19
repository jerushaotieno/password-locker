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
