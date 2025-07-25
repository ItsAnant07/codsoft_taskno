import random
import string

def generate_secure_password(length):
    characters = string.ascii_letters + string.digits
    # Generate password with combination of letters and digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("             Password Generator              ")
    try:
        # User input
        length = int(input("Enter the password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            # Generate and display password
            password = generate_secure_password(length)
            print("Generated Password is:", password)
    except ValueError:
        print("Invalid number")

if __name__ == "__main__":
    main()