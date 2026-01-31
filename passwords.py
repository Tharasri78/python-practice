master_pwd = input("Enter your master password: ")

def view():
    with open('password.txt', 'r') as f:
        for line in f:
            print(line.strip())

def add():
    name = input("Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
         f.write(name + "|" + pwd +"\n")

while True:
    user_input = input("Do you wanna view or add the password or q to quit: ").lower()

    if user_input == "q":
        print("bye...")
        break
    elif user_input == "view":
        view()
    elif user_input == "add":
        add()
    else:
        print("Invalid option")
        continue
