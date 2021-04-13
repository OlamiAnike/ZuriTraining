# In order to improve on my former mock ATM , I will be creating the folllowing functions:
# initialization function(init), login function, register function, generate account number function, 
# bank operations function, withdrawal function, deposit function, complaint function and  logout function

# The initialization function will enable old users to login, provided, the name is among the allowed users list,
# that is the allowed users in the former mock test and if not an existing user, you will be prompted to register 
# a new account

# login function will prompt both old users and existing users to provide their email and password in order to login

# register function will ask the new user for the following information:
#  first name, last name, email, password and secret password

# The bank operations function  will ask the user to choose one of the options:
# withdrawal, deposit, complaint logout and exit

#The user will be directed to the function of any of the options the user chooses from the above

#the generate account number will be used to generate an account number for the new user. 

import random 

database = {}


def init():

    isValidOptionSelected = False
    print('Welcome to bank Zuri Automated Teller Machine')

    while isValidOptionSelected == False:
        
        existingUser = int(input( 'Are you an existing user: (1) Yes, (2) No \n'))

        if(existingUser == 1):
            isValidOptionSelected == True
            name = input("What is your name? \n ")
            allowedUsers = ['Olamide', 'Stephen', 'Grace']

            if(name in allowedUsers):
                isValidOptionSelected == True   
                login()

            else:
                print('name not valid')

        elif(existingUser == 2):
            isValidOptionSelected == True
            register()
            
        else:
            print('Sorry, you have selected the wrong option') 



def login():


   print('****** Login ********')
   
   isLoginSuccessful = False 

   while isLoginSuccessful == False:
       existingUserEmail = int(input( 'Are you an old user? : (1) Yes, (2) No \n'))
       
       if (existingUserEmail == 1):
           isLoginSuccessful == True
           email = input('What is your email? \n')
           allowedEmail =['ola@gmail', 'stevo@yahoo', 'grace@zuri']
           allowedPassword = ['Olamzy', 'Stevo', 'Gwagon']

           if (email in allowedEmail):
               password = input("Your password? \n ")

               if(password in allowedPassword):
                   print('Welcome to your account' )

                   from datetime import date

                   today = date.today()
                   print("Date :", today)

                   from datetime import datetime

                   now = datetime.now()
                   current_time = now.strftime("%H:%M:%S")
                   print("Current Time :", current_time)
                   bankOperations()


       elif(existingUserEmail == 2):
           isLoginSuccessful == True
           emailFromNewUser = input('What is your email address? \n')
           password = input('What is your password \n')

           for accountNumber, userDetails in database.items():
               email = emailFromNewUser
               
               if (email == emailFromNewUser):
                   if(userDetails[3] == password):
                       print('Welcome to your account!')
                       isLoginSuccessful = True 

                       from datetime import date

                       today = date.today()
                       print("Date :", today)

                       from datetime import datetime

                       now = datetime.now()
                       current_time = now.strftime("%H:%M:%S")
                       print("Current Time :", current_time)
                       bankOperations()

               else:
                    login()
 

def register():

    print('***** Register *****')

    firstName = input('What is your first name? \n')
    lastName = input('What is your last name? \n')
    email = input('Enter your email address: \n')
    password = input('Enter your password: \n')
    secretPassword = input('Enter a secret password for your account: \n')

    accountNumber = generateAccountNumber()

    database [accountNumber] = [firstName, lastName, email, password, secretPassword]

    print('Congratulations! Your account has beeen created')
    print(' == ===== ==== === ==')
    print('Your account number is: %d' % accountNumber)
    print('Please keep your account number in a safe place')
    print('== ===== ==== === ==')

    login()

def generateAccountNumber():
    return random.randrange(1111111111,9999999999)


def bankOperations():
    print('These are your available options:')
    isSelectedOptionValid = False
    while isSelectedOptionValid == False:
        selectedOption = int(input('What would you like to do? (1) deposit (2) withdrawal (3) complaint (4) logout (5)exit \n'))

        if (selectedOption == 1):
             isSelectedOptionValid = True
             deposit()
        elif(selectedOption == 2):
            isSelectedOptionValid = True
            withdrawal()
        elif(selectedOption == 3):
            isSelectedOptionValid = True
            complaint()
        elif(selectedOption == 4):
            isSelectedOptionValid = True
            logout()
        elif(selectedOption == 5): 
            exit()
        else:
            print('Invalid Option Selected')


def deposit():
    print('You selected the deposit option')
    deposit = int(input('How much would you like to deposit \n'))
    print('You have deposited %d' % deposit)
    print('Your current balance is %d' % deposit)
    print('Thank you for banking with us' )
    bankOperations() 

def withdrawal():
    print('You selected the withdrawal option')
    withdrawal = int(input('How much would you like to withdraw? \n'))
    print('You have withdrawn %d' % withdrawal)
    print('Thank you for banking with us' )
    bankOperations() 

def complaint():

    print('You selected the complaint option')
    complaint = input('What issue would you ike to complain? \n')
    print('Your issue of %s has been noted and we will get back to you.' %complaint )
    print('Thank you for banking with us' )
    bankOperations() 


def logout():
    login()




init()