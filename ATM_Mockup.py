import random

database = {}

def init():
    print("Welcome to bankPHP")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no)?\n"))

    if(haveAccount == 1):
        login()
    elif(haveAccount == 2):
        register()
    else:
        print("You have selected invalid option")
        init()


def login():

    accountNumberFromUser = int(input("Enter your account number? "))
    password = input("Enter your password? ")
    for accountNumber in database.items():
        for userDetails in database.items():
            if(accountNumber == accountNumberFromUser):
                if(userDetails[3] == password):
                    bankOperation(userDetails)
                else:
                    print("Invalid account or password")
    return bankOperation(userDetails)



def register():
    print("*** Register here ***")

    email = input("Enter an email:\n ")
    first_name = input("Enter your first name?\n ")
    last_name = input("Enter your last name?\n ")
    password = input("Enter a password:\n ")
    print("Registration successful")

    accountNumber = generateAccountNumber()


    database[accountNumber] = [first_name, last_name, email, password]

    print("Your account number is",accountNumber)

    login()


def bankOperation(user):
    print("Welcome",user[1][0],user[1][1])
    selectedOption = int(input("What would you like to do? \n (1) deposit\n (2) withdrawal\n (3) transfer\n (4) logout \n "))

    if(selectedOption == 1):
        depositOperation()
    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        transferOperation()
    elif(selectedOption == 4):
        logout()
    else:
        print("Not a valid option")
        bankOperation(user)

def withdrawalOperation():
    amount = int(input("How much would you like to withdraw?\n"))
    print("Your transaction is processing!")
    print("Your withdrawal of",amount,"was successful Please take out your cash ")

def depositOperation():
    amount = int(input("How much would you like to deposit?\n"))
    print("You have deposited",amount)

def transferOperation():
    recipientAccount = int(input("Enter the recipient's account number:"))
    amount = int(input("Enter an amount: "))
    print("You have successfully transferred",recipientAccount,"to",amount)

def logout():
    print("You have successfully logged out")
    print("To perform another transaction enter your detials again!")
    login()



def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


init()
