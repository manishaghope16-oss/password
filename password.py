import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password length must be at least 4 characters."

    # Character sets
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # Special characters

    # Ensure at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest with random choices from all sets
    all_chars = letters + digits + symbols
    password += random.choices(all_chars, k=length - 3)

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return ''.join(password)

# Main program
try:
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")

