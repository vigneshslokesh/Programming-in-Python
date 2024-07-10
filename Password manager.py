
master_pwd = input('What is the master password? ')


def view():
    pass



def add():
    pass
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt','a') as f:
        f.write(name +"|"+ pwd+"\n")




while True:
    mode = input("Would you like to add a new password or view existing passwords (view, add)\n").lower()
    if mode == "view":
        view()
    if mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue