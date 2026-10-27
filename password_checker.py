print("Password Strength Checker")

password = input("Please enter your password (8 characters): ")
symbols = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
has_symbol = False
has_number = False


for char in password:
    if char in symbols:
        has_symbol = True
    elif char.isdigit():
        has_number = True


if len(password) == 0:
    print("Password cannot be empty.")
elif len(password) < 8:
    print("Password must be at least 8 characters long.")
elif not has_number:
    print("Password must contain at least one number.")
elif not has_symbol:
    print("Password must contain at least one symbol.")
else:
    print("Password is strong.")
