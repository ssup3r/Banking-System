import getpass
import questionary
import time
import authdb

def login():
    pass
class register():
    def register_username():
        register_username = questionary.text("Register Username:").ask()
        return register_username
    def register_password():
        register_password = getpass.getpass("Register Password:")
        return register_password
    time.sleep(2)