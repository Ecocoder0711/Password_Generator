import string
import secrets

def Password_generator():
    if length < 4 :
        raise ValueError("Password lenght should be at least 4 characters.")
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(character) for _ in range(length))
    return password