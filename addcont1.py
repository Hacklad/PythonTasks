# ## Add contact number and name, search contact, delete contact
phoneNum_Store = []
first_store = {}

def addPhone():
    collect_num = input("Enter to add phone number: ")
    collect_name = input("Enter contact name: ")
    collect_org = input("Enter user Organization: ")
    first_store[collect_name] = [collect_num, collect_org]
    # first_store['User_Organiz'] = collect_org
    # first_store['user_Name'] = collect_name
    print(first_store)
    # phoneNum_Store.append(first_store)

    print(f"{collect_num} has been successfully added to your phone book as {collect_name}")
    

def viewPhone():
    for i,v in first_store.items():
        if i == False:
            print("We have no records")
        else:
            print(f"Name: {i} | Phone: {v[0]}")

def deletePhone():
    del_num = input("Enter the name of contact you want to delete ")
    if del_num in first_store.keys():       
        delete = first_store.pop(del_num)
        print(f"{del_num} deleted.")

def searchnum():
    search_num = input("Enter the number you want to search: ")
    for z in phoneNum_Store:
        if z['user_Name'] == search_num:
            print(z)


print("Welcome to your Phone Book")
while True:
    actions = input("Enter - 1. View Contact 2. Add Contact 3. Delete Contact 4. Search Contact 5. Exit >>> ")
    if actions == '1':
        viewPhone()
    elif actions == '2':
        addPhone()
    elif actions == '3':
        deletePhone()
    elif actions == '3':
        searchnum()
    else:
        break

