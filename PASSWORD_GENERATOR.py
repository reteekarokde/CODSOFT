import random
import string

def generate_password(length):
    if length < 4:  # Ensure the password has at least one character from each group
        return "Password length must be at least 4."
    
    # Define character pools
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password includes at least one character from each pool
    all_characters = upper + lower + digits + special
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password with random characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Main program
try:
    num_passwords = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the desired password length: "))

    if length < 4:
        print("Password length must be at least 4.")
    else:
        print("\nGenerated Passwords:")
        for i in range(num_passwords):
            print(f"Password {i + 1}: {generate_password(length)}")
except ValueError:
    print("Invalid input! Please enter a number.")
