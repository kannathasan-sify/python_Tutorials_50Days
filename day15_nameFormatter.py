# NameFormatter.py

def format_name(full_name):
    # Split the full name into parts
    parts = full_name.strip().split()

    if len(parts) < 2:
        print("Please enter at least a first and last name.")
        return

    first = parts[0]
    last = parts[-1]  # handles middle names too

    print("Original Name     :", full_name)
    print("First Name        :", first)
    print("Last Name         :", last)
    print("Format 1 (First Last):", first + " " + last)
    print("Format 2 (Last, First):", last + ", " + first)
    print("Format 3 (Initials)   :", first[0].upper() + "." + last[0].upper() + ".")

# Example usage
full_name = input("Enter your full name: ")
format_name(full_name)
