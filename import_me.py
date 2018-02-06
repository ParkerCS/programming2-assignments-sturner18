def information(name, login):
    name = input("Enter your username:")
    if name == "Simone Turner":
        login = input("Enter your password:")
        if login == "HappyCoding":
            print("Welcome")
        else:
            print("Incorrect")
            done = True
    else:
        print("Access Denied")
        done = True