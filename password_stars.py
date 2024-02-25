MINIMUM_PASSWORD_LENGTH = 5


def main():
    """Get password from the users and display in stars."""
    password = get_invalid_password()
    display_asterisks(password)


def get_invalid_password():
    """Check the password meets the minimum_length."""
    password = get_password()
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Invalid password, should be at least {MINIMUM_PASSWORD_LENGTH} characters")
        password = get_password()
    return password


def display_asterisks(password):
    """Display stars using length of password."""
    print("Password: ", "*" * len(password))


def get_password():
    """Get password from user."""
    password = input("Enter password: ")
    return password


main()
