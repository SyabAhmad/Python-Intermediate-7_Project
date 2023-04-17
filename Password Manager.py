print("Password Generator in Python")

def savingPassword():
    try:
        accountName = input("Enter Account Name: ")
        accountPassword = input("Account Password: \n")

        with open("accountPasswordDatabase.txt", 'a') as file:
            file.write(f'\n{accountName} | {accountPassword}')
            print("Password Saved in Database")
    except IOError:
        print(IOError)

def viewingDatabase():
    try:
        with open("accountPasswordDatabase.txt", 'r') as file:
            readingFile = file.readlines()
            for line in readingFile:
                print(line.strip())
            print("Password Read from Database")
    except IOError:
        print(IOError)

def searchByAccountName():
    name = input("Enter Name of the account you want to search: ")
    with open("accountPasswordDatabase.txt", 'r') as file:
        readingFile = file.readlines()
        accountFound = False
        for line in readingFile:
            afterSplitting = line.split("|")
            accountName = afterSplitting[0].strip()
            if name == accountName:
                print(f"Account Found\n {afterSplitting[0]} | {afterSplitting[1].strip()}")
                accountFound = True
                break
        if not accountFound:
            print("Account Does Not Exist")

def manu():
    print("1: To Add Password")
    print("2: To View Database")
    print("3: Search by Account Name")
    answer = int(input())
    if answer == 1:
        savingPassword()
        manu()
    elif answer == 2:
        viewingDatabase()
        manu()
    elif answer == 3:
        searchByAccountName()
        manu()
    else:
        print("Incorrect Password")
        manu()

manu()
