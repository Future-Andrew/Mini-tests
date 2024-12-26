import socket

def get_computer_name():
    return socket.gethostname()

computer_name = get_computer_name()
print(f"Computer Name: {computer_name}")

import os

def get_current_username():
    return os.getlogin()

current_username = get_current_username()
print(f"Current User: {current_username}")