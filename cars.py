profile = {}
profile["username"] = "user123"
profile["age"] = 20
profile["email"] = "user123@gmail.com"

def register():
    username = input("Enter username:")
    email = input("Enter email:")
    password = input("Enter password:")

# stores in a dictionary
    profile["username"] = username
    profile["email"] = email
    profile["password"] = password

def get_profile():
    # prints the user profile
    print(profile)

def change_username():
    new_username = input("Enter new username:")
    profile["username"] = new_username

register()
get_profile()

change_username()
get_profile()



