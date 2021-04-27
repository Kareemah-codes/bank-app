












#ONLINE BANKING

acc_name = []
savings = []
current = []
acc_info = {
              "Name": acc_name,
              "savings" : savings,
              "current" : current
          }

def open_acc():
    """Opens a savings and current account"""
    x = input("What is your name? ")
    acc_name.append(x.title())
    # Initial money in savings
    y = float(input("How much would you like to open your savings account with? "))
    savings.append(y)

    # Initial money in current
    z = float(input("How much do you want to set up your current account with? "))
    current.append(z)

# Deposit in savings account
def deposit_savings():
    """Deposit money in savings account"""
    deposit = float(input("How much would you like to deposit?"))
    for no in savings:
        no += deposit
        savings[0] = no

#Deposit money in current account
def deposit_current():
    """Deposit money in current account"""
    deposit = float(input("How much would you like to deposit?"))
    for no in current:
        no += deposit
        current[0] = no

#Withdraw money from savings
def withdraw_savings():
    """Withdraw from savings"""
    withdraw = float(input("How much would you like to withdraw?"))
    for no in savings:
        no -= withdraw
        savings[0] = no
    acc_status()
    if withdraw > savings[0]:
      print("Insufficient funds!,the amount you want to withdraw is more than money in your account")
      try_again = input("Do you want to try again?")
      if try_again == "y":
        withdraw_current()
      elif try_again == "n":
        print("Thanks for your patronage!")
#Withdraw money from current

def withdraw_current():
    """Withdraw from savings"""
    withdraw = float(input("How much would you like to withdraw?"))
    for no in current:
      no -= withdraw
      current[0] = no
    if withdraw > current[0]:
      print("Insufficient funds!,the amount you want to withdraw is more than money in your account")
      try_again = input("Do you want to try again?")
      if try_again == "y":
        withdraw_current()
      elif try_again == "n":
        print("Thanks for your patronage!")

# Access account
def access_acc():
    """Access savings or current account to withdraw or deposit
    Note;This fuction contains a culmination of the savings and withdrawal functions"""
    acc_type = input("Savings or Current [s/c]")
    if acc_type == "s":
        trans_type = input("Would you like to deposit or withdraw money? d/w")
        if trans_type == "d":
            deposit_savings()
            acc_status()
        elif trans_type == "w":
            withdraw_savings()
            acc_status()
        else:
            print("you can only withdraw or deposit")

    elif acc_type == "c":
        trans_type = input("Would you like to deposit or withdraw money? d/w")
        if trans_type == "d":
            deposit_current()
            acc_status()
        elif trans_type == "w":
            withdraw_current()
            acc_status()
        else:
            print("you can only withdraw or deposit")
 # Account Status
def acc_status():
    """Prints out current information about an account"""
    print("\nAccount Information")
    for info in acc_info:
        print(info, ":", acc_info[info])

#Perform another function
def another_transaction():
    """Peforms another transaction after one has been done"""
    perform_transaction = input("Would you like to perform another transaction?y/n")
    if perform_transaction == "y":
        trans = input("Kindly pick what you would like to do \n"
                      "Access account =>  a \n"
                      "Check account balance => b \n")
        if trans == "a":
            access_acc()
            another_transaction()
        elif trans == "b":
            acc_status()
            another_transaction()
    if perform_transaction == "n":
        print("Thanks for your patronage!")

print("Welcome to UBA Online Banking Platform")
acc_present = input("Do you have an account with us? y/n ")

if acc_present == "y":
       acc_name = input("What is your name? ")
#Open account if you don't have one
elif acc_present == "n":
    open_acc_decision = input("Would you like to open an account ? y/n ")
    if open_acc_decision == "y":
        open_acc()
        acc_status()
#Access account after opening one
        continue_trans = input("\nWould you like to access your access your account? y/n ")
        if continue_trans == "y":
            access_acc()
            another_transaction()
        elif continue_trans == "n":
            print("Thanks for opening an account with us!")
    elif open_acc_decision == "n":
      print("Maybe next time")

else:
    print("Pick y or n")



