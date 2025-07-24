# InitialExtractor.py

def extract_initials(full_name):
    # Split the full name by spaces
    words = full_name.strip().split()
    
    # Extract the first letter of each word and capitalize it
    initials = ''.join(word[0].upper() for word in words if word)
    
    return initials

# Example usage
if __name__ == "__main__":
    name = input("Enter full name: ")
    result = extract_initials(name)
    print("Initials:", result)
