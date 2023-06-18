import questionary
from Authentication import client
import os
from termcolor import colored

folder_name = "Configuration"
main_directory = os.path.dirname(os.path.abspath(__file__))
configuration_folder = os.path.join(main_directory, "Configuration")
creation_path_folder = os.path.join(main_directory, folder_name)

class check_for_neccessary_files:
    def check_for_configuration_folder():
        if os.path.isdir(configuration_folder):
            print(colored("✓ Configuration Folder found", "green"))
        else:
            print(colored("✗ Configuration Folder not found", "red"))
            print("Would you like to create the configuration folder?")
            create_folder_confirmation = questionary.confirm("Declining will result in program termination!").ask()
            if create_folder_confirmation:
                try:
                    os.makedirs(creation_path_folder)
                    print(colored("✓ Configuration Folder created", "green"))
                except:
                    print(colored("✗ Failed to create configuration folder", "red"))
                    exit()
            else:
                print(colored("Terminating....", "red"))
                exit()
    def check_for_config_file():
        if os.path.isfile(os.path.join(configuration_folder, "config.yml")):
            print(colored("✓ Configuration File found", "green"))
        else:
            print(colored("✗ Configuration File not found", "red"))
            print("Would you like to create config.yml?")
            create_file_confirmation = questionary.confirm("Declining will result in program termination!").ask()
            if create_file_confirmation:
                try:
                    open(os.path.join(configuration_folder, "config.yml"), "w")
                    print(colored("✓ Configuration File created", "green"))
                except:
                    print(colored("✗ Failed to create configuration file", "red"))
                    exit()
            else:
                print(colored("Terminating....", "red"))
                exit()

def login_choices():
    operation_select = questionary.select(
        "Welcome to Super's Banking System",
        choices=["Login", "Register", "Exit"],
    ).ask()

    if operation_select == "Login":
        client.login()
    elif operation_select == "Register":
        client.register()
    elif operation_select == "Exit":
        exit()
    else:
        print("Invalid Operation")

check_for_neccessary_files.check_for_configuration_folder()
check_for_neccessary_files.check_for_config_file()
login_choices()