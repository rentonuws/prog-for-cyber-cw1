from random import randint
from datetime import datetime

def authenticate(username,password):
    if username == "admin" and password == "admin123":
        return True
    else:
        return False

valid = False

while not valid:
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if authenticate(username,password):
        print("Login sucessful")
        valid = True
        print(f"Event ID: {randint(1000,9999)}\nUsername: {username}\nIP Address: 192.168.1.25\nEvent: Login Successful\nTimestamp: = {datetime.now()}")
    else:
        print("Invalid username or password")
        print(f"Event ID: {randint(1000,9999)}\nUsername: {username}\nIP Address: 192.168.1.25\nEvent: Login Failed\nTimestamp: = {datetime.now()}")