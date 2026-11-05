def validate_ip(ip):    #defined a function to validate the IP address entered by the user
    ip = ip.replace(" ","") #Removing any spaces in the IP address entered by the user
    dot = 0 #setting a variable to zero to count the number of dots in the IP address
    for check in ip:    #Checking how many dots are in the IP address entered by the user
        if check == ".":    #Incrementing the dot variable by 1 if a dot is found in the IP address
            dot = dot + 1
        elif not check.isdigit():   #Returning False if any character in the IP address is not a digit or a dot
            return False
    if dot == 3:    #checking if the number of dots in the IP address is equal to 3, which is a valid format for an IP address
        parts = ip.split(".")   #Splitting the IP address into its four parts using the dot as a delimiter
        for part in parts: #Checking each part of the IP address
            if part == "" or int(part) > 255:   #returning False if any part of the IP address is empty or greater than 255, which is an invalid value for an IP address
                return False
        return True #Returning True if the IP address is valid
    else:
        return False    #Returning False if the number of dots in the IP address is not equal to 3, which is an invalid format for an IP address

valid = False   #Initializing a variable to False to indicate that the IP address entered by the user is not valid yet

while not valid:    #Looping until the user enters a valid IP address
    ip = input("Please enter an IP address: ")  #Prompting the user to enter an IP address
    if validate_ip(ip): #Calling the validate_ip function to check if the IP address entered by the user is valid
        print("Valid IP address")   #Printing a message to indicate that the IP address entered by the user is valid
        valid = True    #Setting the valid variable to True to exit the loop since the user has entered a valid IP address
    else:
        print("Invalid IP address")    #Printing a message to indicate that the IP address entered by the user is invalid
