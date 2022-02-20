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

def signInUser(userName, passWord):
    '''
    Function checks if user exists before letting them log into the application
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

def generatePassword():
    '''
    generates a random password for a user
    '''
    autoPassword=Credentials.generatePassword()
    return autoPassword

def copyPassword(accountName):
    '''
    Import pyperclip framework then create a function to copy user emails and passwords
    '''
    return Credentials.copyPassword(accountName)

#main function

def passwordLocker():
    print('Welcome to your password manager...\n Please enter one of these short codes to proceed. \n SU --- Sign Up \n SI --- Sign In \n')
    shortCode=input("").lower().strip()
    if shortCode == "su":
        print("Sign Up")
        print('-' * 50)
        userName = input("Username: ")

        while True:
            print(" TP - To type your own pasword:\n GP - To generate a random Password")
            passwordChoice = input().lower().strip()
            if passwordChoice == 'tp':
                passWord = input("Enter Password\n")
                break
            elif passwordChoice == 'gp':
                passWord = generatePassword()
                break
            else:
                print("Invalid password. Please try again")

        saveUser(createNewUser(userName,passWord))

        print('-' * 50)

        print(f"Hi {userName}, account created succesfully! Your password is: {passWord}")

        print('-' * 50)

    elif shortCode == "si":
        print("-"*50)
        print("Enter Username and Password to log in:")
        print('-' * 50)

        userName = input('Username: ')
        passWord = input('Password: ')
        signIn = signInUser(userName, passWord)
        if signInUser == signIn:
            print(f"Hi {userName}, Welcome to your PassWord Manager")  
            print('\n')

    while True:
        print("Use these short codes:\n CNC - Create a new credential \n DC - Display Credentials \n SC - Search a credential \n GP - Generate randomn password \n DC - Delete credential \n CA - Close account \n")
        shortCode = input().lower().strip()
        if shortCode == "cnc":
            print("Create New Credential")
            print("-" * 50)
            print("Account name ....")
            accountName = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print('TP - To create your own pasword \n GP - To generate a random Password')
                passWordChoice = input().lower().strip()
                if passWordChoice == 'tp':
                    passWord = input('Enter your own password \n')
                    break
                elif passWordChoice == 'gp':
                    passWord = generatePassword()
                    break
                else:
                    print('Invalid password please try again')

            saveCredentials(createNewCredential(accountName, userName, passWord))
            print('\n')
            print(f"Account Credential for: {accountName} - Username: {userName} - Password:{passWord} created succesfully")
            print('\n')
            
        elif shortCode == 'dc':
            if displayCredentials():
                print('Here are your accounts: ')
                 
                print('-' * 50)
                print('-' * 50)
                for accountName in displayCredentials():
                    print(f" Account:{accountName.accountName} \n Username:{userName} \n Password:{passWord}")
                    print('-' * 50)
                print('-' * 50)
            else:
                print('No credentials saved yet...')

        elif shortCode == 'sc':
            print('Enter Account Name to search for')
            searchName = input().lower()
            if searchCredentials(searchName):
                searchCredential = searchCredentials(searchName)
                print(f"Account Name : {searchCredentials.accountName}")
                print('-' * 50)
                print(f"User Name: {searchCredentials.userName} Password :{searchCredentials.passWord}")
                print('-' * 50)
            else:
                print("This credential does not exist")
                print('\n')

        elif shortCode == 'dlc':
            print('Enter name of account credentials yo delete')
            searchName = input().lower()
            if searchCredential(searchName):
                searchCredential = searchCredentials(searchName)
                print("-"*50)
                searchCredentials.deleteCredentials()
                print('\n')
                print(f"Credentials for {searchCredentials.accountName} account deleted!")
                print('\n')
            else:
                print("The credential chosen does not exist")

        elif shortCode == 'gp':

            passWord = generatePassword()
            print(f" {passWord} generated. you can visit your account")

        elif shortCode == 'ca':
            print("It was a pleasure having you. See you next time!")
            break
        else:
                print("Invalid entry")
    else:
        print("Please enter a valid entry to proceed")

if __name__ == '__main__':
    passwordLocker()            
        
