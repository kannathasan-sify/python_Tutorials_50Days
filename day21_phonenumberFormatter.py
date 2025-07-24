# PhoneFormatter.py

def format_phone_number(number):
    if len(number) == 10 and number.isdigit():
        return f"({number[:3]}) {number[3:6]}-{number[6:]}"
    else:
        return "Invalid input. Please enter a 10-digit number."

# Example usage
if __name__ == "__main__":
    phone = input("Enter a 10-digit phone number: ")
    formatted = format_phone_number(phone)
    print("Formatted Phone Number:", formatted)
