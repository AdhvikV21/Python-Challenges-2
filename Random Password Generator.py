import random
import string

def generate_strong_password(length=16):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_characters = lowercase + uppercase + digits + special
    password_list = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)]

    random.shuffle(password_list)
    return "".join(password_list)

strong_password = generate_strong_password()
print(strong_password)