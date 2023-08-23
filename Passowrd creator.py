def is_valid_password(password):
    if len(password) < 11:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    if not any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for char in password):
        return False
    return True

def main():
    while True:
        password = input("Create a password with at least 10 characters and one symbol: ")
        
        if is_valid_password(password):
            print("Password is valid.")
            break
        else:
            print("Password is not valid. Please try again.")

if __name__ == "__main__":
    main()
