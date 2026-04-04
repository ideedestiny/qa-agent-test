def is_valid_email(email):
    return "@" in email and "." in email

def is_valid_age(age):
    return isinstance(age, int) and 0 < age < 120
