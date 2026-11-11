from random import randint    #Import randint for event ID generation
from datetime import datetime    #Import datetime for event time logging
event_history = []    #Define a dictionary to record event logs

def authenticate(username,password):    #Define a function called authenticate that will verify user credentials
    if username == "admin" and password == "admin123":    #check if the entered crendential is equal to the correct one
        return True    #Set value to True to exit the while loop since the user entered the correct credentials
    else:
        return False    #Credentials are invalid

valid = False    #Initialize the value of valid to False, which will be used to control the loop until the correct username and password are entered.

while not valid:    #Loop until the user enters the correct credentials
    username = input("\nPlease enter your username: ")    #Prompt user to enter username
    password = input("Please enter your password: ")    #Prompt user to enter password
    event_id = randint(1000,9999)    #generate a random value for event id
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    #store current time to timestamp
    if authenticate(username,password):    #Check if the correct credentials is entered
        status = "Login Successful"    #Record successful login attempt
        valid = True    #set value of valid to True to exit the while loop since the user has entered correct credentials
    else:
        status = "Login Failed"    #set value of status to "Login Failed"
        print("Invalid username or password")    #Tell the user that they entered the incorrect username or password
    print(status)        #Tell the user whether successful login or not
    print(f"Event ID: {event_id}\nUsername: {username}\nIP Address: 192.168.1.25\nEvent: {status}\nTimestamp: {timestamp}\n")    #Display the event log to user
    log_entry = {    #define a dictionary called log_entry to store the latest event log
        "Event ID": event_id,
        "Username": username,
        "IP Address": "192.168.1.25",
        "Event": status,
        "Timestamp": timestamp
    }
    event_history.append(log_entry)    #add the latest event log to event_history list
    
print("\nEvent History:")    #Display all recorded event logs

for event in event_history:    #define a for loop to show all recorded event logs
    print(f"ID: {event['Event ID']} | User: {event['Username']} | IP address: 192.168.1.25 | Event: {event['Event']} | Time: {event['Timestamp']}")    #Display event log in predefined format
