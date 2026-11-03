def check(password): #define a function called check that takes a password as an argument
    allowcha = '!"£$%'
    dig = 0
    UAlph = 0
    LAlph = 0
    Symb = 0    
    
    if len(password) < 10:
        return False

    for i in password:
        if i.isupper():
            UAlph = UAlph + 1
        elif i.islower():
            LAlph = LAlph + 1
        elif i.isdigit():
            dig = dig + 1
        elif i in allowcha:
            Symb = Symb + 1
        elif i == " ":
            return False

    if UAlph >= 1 and LAlph >=1 and dig >=2 and Symb >=1:
        return True
    else:
        return False

def validate_ip(ip):
    ip = ip.replace(" ","")
    dot = 0
    for check in ip:
        if check == ".":
            dot = dot + 1
        elif not check.isdigit():
            return False
    if dot == 3:
        parts = ip.split(".")
        for part in parts:
            if part == "":
                return False
            elif int(part) > 255:
                return False
        return True
    else:
        return False

def random_password():
    import string #import the string module to access string constants
    import random #import the random module to generate random numbers

    password_length = random.randint(10,16) #random password length between 10 and 16 characters
    allowed_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '!"£$%' #allowed characters for the password
    valid = False
    while not valid:
        ran_password = "" #set ran_password to an empty string
        for i in range(password_length): #generate a random password of the specified length
            ran_password = ran_password + random.choice(allowed_chars) #append a random character from the allowed characters to the password
        valid = check(ran_password) #check if the generated password meets the criteria defined in the check function
    return ran_password