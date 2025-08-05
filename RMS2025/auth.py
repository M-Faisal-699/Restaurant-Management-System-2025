
import json

def user_authentication():
    print("1.Sign Up")
    print("2.Sign In")
    print("3.Exit")
    option = int(input("Select any option:"))

    if option == 1:
        print("\n--- Sign Up ---")
        userdata = {}
        userdata["username"] = input("Enter username: ")
        userdata["password"] = input("Enter password: ")
        with open("userdata.json", "w") as file:
            file.write(json.dumps(userdata, indent=4))
        print("Sign Up Successful! Welcome Admin")

    elif option == 2:
        print("\n--- Sign In ---")
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            with open("userdata.json", "r") as file:
                userdata = json.load(file)
            if userdata["username"] == username and userdata["password"] == password:
                print("Login Successful! Welcome Admin")
            else:
                print("Invalid Try Again")
        except FileNotFoundError:
            print("No user registered. Please sign up first.")

    elif option == 3:
        print("Exit")
    else:
        print("Invalid Try Again")

