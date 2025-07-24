# EmailUsernameExtractor.py

def extract_username(email):
    if '@' in email:
        return email.split('@')[0]
    else:
        return "Invalid email address"

# Example usage
if __name__ == "__main__":
    email = input("Enter an email address: ")
    username = extract_username(email)
    print("Username:", username)
