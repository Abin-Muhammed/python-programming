import random
import string

def generate_password(length):
    
    # Function to Generate a strong, secure password of a given length.
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Print the introduction and instructions
    print("Welcome to the Password Generator!")
    print("----------------------------------")
   
    # Get user input for password length
    password_length = int(input("Enter the length of the password (minimum 8): "))
    
    # Ensure the password length is at least 8 characters
    if password_length < 8:
        print("Password length should be at least 8.")
        return
    
    # Get user input for the number of passwords to generate
    num_passwords = int(input("Enter the number of passwords to generate: "))
    
    # Generate and print the passwords
    for i in range(num_passwords):
        password = generate_password(password_length)
        print(f"Password {i+1}: {password}")

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()
