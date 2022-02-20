from password_locker import User, Credentials

#user-side functions

def createNewUser(userName, passWord):
    '''
    Function creates a new user with a username and password
    '''
    newUser = User(userName, passWord)
    return newUser

def saveUser(User):
    '''
    Function saves a new user
    '''
    User.saveUser()

def displayUser():
    '''
    Function displays an existing user
    '''
    return User.displayUser()

def userLogin(userName, passWord):
    '''
    Function checks if a user exists then lets them log into the application
    '''
    checkUser = Credentials.verifyUser(userName, passWord)
    return checkUser

#credential-side functions

