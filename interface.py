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

def createNewCredential(accountName,userName,passWord):
    '''
    Function creates new credentials for a user's account
    '''
    newCredential = Credentials(accountName, userName, passWord)
    return newCredential

def saveCredentials(Credentials):
    '''
    Function saves user credentials to the credentials directory
    '''
    Credentials. saveCredentials()

def displayCredentials():
    '''
    Function returns saved user credentials
    '''
    return Credentials.displayCredentials()

def deleteCredentials(Credentials):
    '''
    Function deletes existing user credentials from the credentials directory
    '''
    Credentials.deleteCredentials()

def searchCredentials(accountName):
    '''
    Function finds user credentials using given account name and returns the specific account
    '''
    return Credentials.searchCredentials(accountName)

def credendtialsExist(accountName):
    '''
    Function checks if user credentials exist and returns a True or False value
    '''
    return Credentials.credentialsExist(accountName)



