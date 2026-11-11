print("Welcome for testing my security tool.")  #Welcome message for the user

max_attempts = 10   #defining the maximum number of attempts for the whole program. This variable is used in the security_event_counter, brute_force_simulation, and login_authentication functions to limit the number of attempts a user can make.

def security_event_counter():   #define a function called security_event_counter that will count the number of correct and incorrect password entries made by the user.
    print("\n\nWelcome to the Security Event Counter.\nYou will be prompted to enter passwords ten times. The program will count how many times you entered the correct password and how many times you entered the incorrect password.")   #Program description for the user
    correct_count = 0   #set the initial count of correct password entries to zero
    incorrect_count = 0 #set the initial count of incorrect password entries to zero
    for i in range(max_attempts):   #loop through the range of max_attempts (10) and prompt the user to enter a password each time.
        password = input(f"Please enter the {i+1} password: ")  #Prompt the user to enter a password and tell them the number of the password they are entering (1st, 2nd, 3rd, etc.)
        if password == "Password123":   #check if the entered password is equal to the correct password 
            correct_count = correct_count + 1   #increment the count of correct password entries by one
            print("Correct password entered.")  #Confirm to the user that they entered the correct password
        else:
            incorrect_count = incorrect_count + 1   #increment the count of incorrect password entries by one
            print("Incorrect password entered.")    #Tell the user that they entered the incorrect password

    print(f"Total percentage of incorrect passwords entered: {incorrect_count/max_attempts*100:.2f}%")  #Print the total percentage of incorrect password entries made by the user.
    if incorrect_count > 5: #If the user entered the incorrect password more than 5 times, print a security alert message to indicate a potential security threat.
        print(f"Security Alert: You have entered the incorrect password {incorrect_count} times. This may indicate a potential security threat.")

def brute_force_simulation():   #define a function that will simulate a brute-force attack by prompting the user to enter passwords until they enter the correct password or exceed the maximum number of attempts.
    print("\n\nWelcome to the Brute-Force Simulation.\nYou will be prompted to enter passwords until you enter the correct password or exceed the maximum ten attempts.") #Describe the purpose of the function to the user
    count = 0   #set the initial count of password attempts to zero
    valid = False   #set the initial value of valid to False, which will be used to control the while loop that prompts the user to enter passwords.
    while not valid:    #loop until the user enters the correct password or exceeds the maximum number of attempts
        password = input(f"Attempt {count + 1}: Please enter the password: ")   #Prompt the user to enter a password and tell them the number of the attempt they are on (1st, 2nd, 3rd, etc.)
        if password == "Password123":   #check if the entered password is equal to the correct password
            print("Correct password entered. Thanks for trying.")   #Confirm to the user that they entered the correct password.
            valid = True    #set valid to True to exit the while loop since the user entered the correct password
        else:   
            count = count +1    #increment the count of password attempts by one
            print("Incorrect password entered.")    #Tell the user that they entered the incorrect password
            if count == max_attempts:   #Check if the user has exceeded the maximum number of attempts
                valid = True    #set valid to True to exit the while loop since the user has exceeded the maximum number of attempts
                print("Maximum number of attempts exceeded. Thank you for trying. Go back to the main menu now")    #Tell the user that they have exceeded the maximum number of attempts. 


def login_authentication(): #define a function that will simulate a login authentication process by prompting the user to enter their username and password until they enter the correct credentials or exceed the maximum number of attempts.

    print("\n\nWelcome to the Login Authentication.\nYou will be prompted to enter your username and password. The program will check if the credentials are correct. Your account will be locked if you enter incorrect credential three times.") # Describe the function to the user
    valid = False   #initialize a variable called valid to False, which will be used to control the while loop
    count = 0   #initialize a variable called count to zero.
    while not valid:
        username = input("Please enter your username: ")    #Prompt the user to enter their username
        password = input("Please enter your password: ")    #Prompt the user to enter their password
        if username == "admin" and password == "Password123":   #check if the entered username and password are equal to the correct credentials
            print("Login successful.")  #Confirm to the user that they have successfully logged in.
            valid = True    #set valid to True to exit the while loop since the user has successfully logged in
        else:
            count = count + 1   #increment the count of login attempts by one
            print("Login failed. Invalid username or password.")    #Tell the user that they have entered invalid credentials
            if count == 3:   #check if the user has exceeded the maximum number of login attempts
                valid = True    #set valid to True to exit the while loop since the user has exceeded the maximum number of login attempts
                print("Maximum number of login attempts exceeded. Access denied. Account is frozen immediately. Please try again after 24 hours.")  #Tell the user that they have exceeded the maximum number of login attempts and that their account is frozen for 24 hours.


valid = False   #initialize a variable called valid to False, which will be used to control the while loop.

while not valid:
    password = input("Please enter your password to continue: ")    #Prompt the user to enter their password to continue using the security tool.
    if password == "admin123":  #check if the entered password is equal to the correct password
        valid = True    #set valid to True to exit the while loop since the user has entered the correct password
        print("Access granted.")    #Confirm to the user that they have been granted access to the security tool.
    else:
        print("Invalid password. Please try again.")    #Tell the user that they have entered an invalid password and prompt them to try again.

options = 0 #initialize a variable called options to zero, which will be used to store the user's menu selection.
valid = False   #initialize a variable called valid to False, which will be used to control the while loop that prompts the user to select an option from the menu.

while not valid:
    options = input("\n\nPlease select one of the following options:\n1. Security Event Counter\n2. Brute-Force Simulation\n3. Login Authentication\n4. Exit\n")    #Prompt the user to select an option from the menu and store their selection in the options variable.
    if options == "1":  #check if the user selected option 1 (Security Event Counter)
        print("Security Event Counter selected.")   #Confirm to the user that they have selected the Security Event Counter option.
        security_event_counter()    #Call the security_event_counter function to execute the Security Event Counter functionality.
    elif options == "2":    #check if the user selected option 2 (Brute-Force Simulation)
        print("Brute-Force Simulation selected.")   #Confirm to the user that they have selected the Brute-Force Simulation option.
        brute_force_simulation()    #Call the brute_force_simulation function to execute the Brute-Force Simulation functionality.
    elif options == "3":    #check if the user selected option 3 (Login Authentication)
        print("Login Authentication selected.")   #Confirm to the user that they have selected the Login Authentication option.
        login_authentication()  #Call the login_authentication function to execute the Login Authentication functionality.
    elif options == "4":    #check if the user selected option 4 (Exit)
        print("Thank you for using the security tool")  #Thank the user for using the security tool.
        valid = True    #set valid to True to exit the while loop since the user has selected the Exit option.
    else:
        print("Invalid option. Please try again.")   #Tell the user that they have entered an invalid option and prompt them to try again.
