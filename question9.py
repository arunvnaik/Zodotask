import random
import string

def generate_password(length=12):
    # Define the character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Ensure the password has at least one character from each set
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with a mix of all characters
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the resulting password to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

# Example usage:
print(generate_password())  
print(generate_password(16))  
