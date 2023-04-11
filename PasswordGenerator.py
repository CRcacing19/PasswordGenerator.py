import random
import string

def generate_password(length):
    """Generate a random password of specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage:
print(generate_password(12)) # Generates a random 12-character password
