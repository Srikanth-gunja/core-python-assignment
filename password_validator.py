def password_validator(password):
    if  len(password) < 10 or len(password) >15:
        return "password length should min 10 and max of 15 chars"
    if not any(c.islower() for c in password):
        return "password should have atleast a lower case letter"
    if not any(c.isdigit() for c in password):
        return "password should have atleast a digit letter"
    if not any(c.isupper() for c in password):
        return "password should have atleast a upper case letter"
    if not any(c in ['@','#','$','!','%','^','&','*','(',')'] for c in password):
        return "No Special Character found in password"
    if len(password) != len(password.strip()):
        return "No white spaces should be present "
    else:
        return "Valid Password"
print(password_validator("#SRikNtH@34"))