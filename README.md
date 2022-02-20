## User Stories
The user would like to.... :
* To create an account for the application or log into the application.
* Store their login credentials for various accounts created.
* Generate a new password for an account not yet created and store it with the account name.   
* Delete stored account login credentials no longer in usee.
* Copy account credentials to the clipboard


## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.6
* pyperclip
* pip
#### Cloning
* Open Terminal {Ctrl+Alt+T}
* git clone "https://github.com/jerushaotieno/password-locker.git"
* cd Password-Locker

* code . or atom . based on the text editor you have.

### Running the Application
* To run the application, open the cloned file in terminal and run the following commands:

        $ chmod +x interface.py
        $ ./interface.py

* To run tests for the application: 
    $ python3 passlock_test.py

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Open the application on the terminal | Run the command "$ ./interface.py"| Hi Welcome to your Password Manager... <br>* SU ---  Sign Up * SI ---  Sign In |
| Select  CNC| Enter username and password| Hi {userName}, account created succesfully! Your password is: {passWord}" |
| Select SI  | Enter password and username signed up with | Abbreviations menu to help you navigate through the application |
| Store a new credential in the application | Enter "CNC" | Enter Account, username, password<br>choose "TP" to enter a password of choice or "gp" for a random password to be generated by the application on your behalf |
| Display all saved credentials | Enter "DC" | Lists all credentials stored or prompts the message "No credentials saved yet" |
| Search for a saved credential based on account name | Enter "SC" | Enter the Account Name to search for e.g. "Gmail" to return account details|
| Delete an existing credential no longer in use or needed | Enter "DLC" | Enter the account name of theaccount credentials to delete to return True if the account exists and False if it does not |

## Technologies Used

* python3.6
 
## Known Bugs
* There are no known bugs currently. Pull requests allowed in case of a bug.

## Contact Information 
jerushaotienocoding@gmail.com

## License
* *MIT License:*
* Copyright (c) 2022 **Jerusha Otieno**