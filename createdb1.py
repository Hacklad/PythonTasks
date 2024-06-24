## Create a db storing list of usernames of an org, phone and email. Store in dic, then the dictionary stored in a list. 

db_com = []
dict_com = {}
active = True
while active == True:
    username = input("\n Enter your username: ")
    phone = int(input("\n Enter your phone number: "))
    email = input("\n Enter your email: ")

    dict_com['username'] = username
    dict_com['phone'] = phone
    dict_com['email'] = email
    db_com.append(dict_com)
    if len(db_com) == 3:
        active = False
# print(dict_com)
print(f"\n {db_com}\n")
