from random import randint
from datetime import datetime
event_history = []

def authenticate(username,password):
    if username == "admin" and password == "admin123":
        return True
    else:
        return False

valid = False

while not valid:
    username = input("\nPlease enter your username: ")
    password = input("Please enter your password: ")
    event_id = randint(1000,9999)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if authenticate(username,password):
        status = "Login Successful"
        print(status)
        valid = True
        print(f"Event ID: {event_id}\nUsername: {username}\nIP Address: 192.168.1.25\nEvent: {status}\nTimestamp: {timestamp}\n")
    else:
        status = "Login Failed"
        print("Invalid username or password")
        print(f"Event ID: {event_id}\nUsername: {username}\nIP Address: 192.168.1.25\nEvent: {status}\nTimestamp: {timestamp}\n")
    log_entry = {
        "Event ID": event_id,
        "Username": username,
        "IP Address": "192.168.1.25",
        "Event": status,
        "Timestamp": timestamp
    }
    event_history.append(log_entry)
print("\nEvent History:")

for event in event_history:
    print(f"ID: {event['EVENT ID']} | User: {event['Username']} | IP address: 192.168.1.25 | Event: {event['Event']} | Time: {event['Timestamp']}")
