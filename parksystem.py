# Assignment: Park system**
### Design a software that designs recharge card e.g 1771-1017-1663-9911
    ## -> Create Dealer account/pwd/balance(wallet)
    ## -> Ask for unit you want to print and how much
    ## -> Print card #100 and sell to dealer at the rate of 80naira
    ## -> #200 card = #160, #100 = #80.

## recharge card - store, print units, price, discount.

card_stored = []
user_account = {}

def addCustomer():
    collect_name = input("Enter contact name: ")
    collect_org = input("Enter user Organization: ")
    collect_email = input("Enter your email address: ")
    collect_pass = input("Enter your password: ")
    user_account[collect_org] = [collect_name, collect_org, collect_email, collect_pass]
    # first_store['User_Organiz'] = collect_org
    # first_store['user_Name'] = collect_name
    print(user_account)
    loginCustomer()
    contd = input("Do you wanna purchase Airtime? Yes or No? ")
    if contd.lower() == 'yes':
        createCode()
    else:
        print('<<<<< Good Bye, Login when you want to buy Airtime!')
        loginCustomer()

    # phoneNum_Store.append(first_store)

    #print(f"{collect_num} has been successfully added to your phone book as {collect_name}")

def loginCustomer():
    collect_org = input("Login Panel >>> Enter your Organization name: ")
    for i in user_account.keys():
        if i == collect_org:
            for v in user_account.values():
                collect_email = input("Enter your email address: ")
                collect_pass = input("Enter your password: ")
                if collect_email == user_account[collect_org][2] and collect_pass == user_account[collect_org][3]:
                    print(f"Hello {user_account[collect_org][1]}, ")
                else:
                    print("Email or Password Incorrect")
        else:
            print("Sorry your Organization is not registered")
    
import random
def createCode():
    price = input('Price of card? ')
    unitz = input(f'How many units of #{price} card? ')
    if price == '200':
        for lo in range(int(unitz)):
            card = random.randrange(20000000000,29999999999)
            card_stored.append(card)
        Agreed = input(f'You will be charged {int(unitz) * 160} naira. Proceed? Y or N ')
        print(card_stored)
    elif price == '100':
        for lo in range(int(unitz)):
            card = random.randrange(10000000000,19999999999)
            card_stored.append(card)
        Agreed = input(f'You will be charged {int(unitz) * 80} naira. Proceed? Y or N ')
        if Agreed.lower() == 'y':
            print(card_stored)
        else:
            exit
    else:
        print("We don't have that price now!")
# random.shuffle()

while True:
    print('<<<<<<<< Welcome to Airtime Treez >>>>>>>>>>')
    progra = input('1. Create User 2. Login User 3. Purchase Airtime ')
    if progra == '1':
        addCustomer()
    elif progra == '2':
        loginCustomer()
    elif progra == '3':
        createCode()
    else:
        break
