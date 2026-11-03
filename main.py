import security_tools

valid = False

while not valid:
    password = input("Please enter a password: ")
    if security_tools.check(password):
        print("Password accepted")
        valid = True
    else:
        print(f"Password doesn't match the minimum requirement, please use this password instead: {security_tools.random_password()}")

valid = False

while not valid:
    ip = input("Please enter an IP address: ")
    if security_tools.validate_ip(ip):
        print("Valid IP address")
        valid = True
    else:
        print("Invalid IP address")