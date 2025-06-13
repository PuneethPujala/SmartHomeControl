from user import User

Users=[
    User("karthik","1234"),
    User("puneeth","4321"),
    User("prakash","1432"),
    User("manideepak","1342")
]
entry_user=input("Enter your username:")
matched_user=None
for user in Users:
    if user.get_username()==entry_user:
        matched_user=user
        break
if matched_user:
    attempts=3
    while attempts>0:
        entry_password=input("Enter your access_code:")
        if matched_user.authenticate(entry_password):
            print("Access granted")
            break
        else:
            attempts-=1
            print("Incorrect password. Remaining attempts:",attempts)
    if attempts==0:
        print("Access denied")
    
else:
    print("User not found")
