import random
import string

def generate_password(length=8):
    # Define possible characters: lowercase, uppercase, digits, and special symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

# Example usage:
password_length = int(input("Enter password length: "))
password = generate_password(password_length)

print(f"Generated Password: {password}")
