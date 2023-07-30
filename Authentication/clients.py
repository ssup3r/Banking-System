import pwinput
import questionary


def login():
    try:
        user = input("Enter your Username: ")
        pwd = pwinput.pwinput("Enter your Password: ")
    except:
        print("An error have occured!")
        if questionary.confirm("Retry?").ask():
            login()
        else:
            exit()

# def register():
    # try:
        # reguser = input("Enter your Username: ")


login() 