def check(password): #define a function called check that takes a password as an argument
    allowcha = '@#!"£$%' #define a string of allowed symbols for the password
    dig = 0 #define a variable called dig and set it to 0 to count the number of digits in the password
    UAlph = 0 #define a variable called UAlph and set it to 0 to count the number of uppercase letters in the password
    LAlph = 0 #define a variable called LAlph and set it to 0 to count the number of lowercase letters in the password
    Symb = 0 #define a variable called Symb and set it to 0 to count the number of allowed symbols in the password
    
    if len(password) < 10: #check if the password is less than 10 characters long
        return False

    for i in password:
        if i.isupper(): #count the number of uppercase letters
            UAlph = UAlph + 1
        elif i.islower(): #count the number of lowercase letters
            LAlph = LAlph + 1
        elif i.isdigit(): #count the number of digits
            dig = dig + 1
        elif i in allowcha: #count the number of allowed symbols
            Symb = Symb + 1
        elif i == " ": #check any spaces in the password
            return False

    return UAlph >= 1 and LAlph >=1 and dig >=2 and Symb >=1 #Return True if the password meets the criteria, otherwise return False

def validate_ip(ip): #define a function called validate_ip that checks if an IP address is valid
    ip = ip.replace(" ","") #remove any spaces from the IP address
    dot = 0 #define a variable called dot and set it to 0 to count the number of dots in the IP address
    for check in ip: #iterate through each character in the IP address
        if check == ".": #increment the dot variable by 1 if the character is a dot
            dot = dot + 1 
        elif not check.isdigit(): #check if the character is not a digit, return False
            return False
    if dot == 3: #validate the value if there are 3 dots in the IP address
        parts = ip.split(".") #split the IP address into parts using the dot as a delimiter
        for part in parts: #iterate through each part of the IP address
            if part == "" or int(part) > 255:          #check for empty values or values greater than 255
                return False #return False if any part is empty or greater than 255
        return True #return True if the IP address is valid
    else: #return False if there are not exactly 3 dots in the IP address
        return False

def random_password():  #define a function called random_password that generates a random password
    import random  #import the random module to generate random numbers
    import string  #import the string module to access string constants

    password_length = random.randint(10,16) #random password length between 10 and 16 characters
    allowed_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '@#!"£$%' #allowed characters for the password
    
    valid = False
    
    while not valid:
        ran_password = "" #set ran_password to an empty string
        for i in range(password_length): #generate a random password of the specified length
            ran_password = ran_password + random.choice(allowed_chars) #append a random character from the allowed characters to the password
        valid = check(ran_password) #check if the generated password meets the criteria defined in the check function
    return ran_password #return the generated password if it meets the criteria