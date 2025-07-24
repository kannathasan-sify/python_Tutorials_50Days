# SimpleCipher.py

def shift_letter(char):
    if char.isalpha():
        if char.islower():
            return chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        elif char.isupper():
            return chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
    else:
        return char  # Non-alphabetic characters remain unchanged

def simple_cipher(text):
    result = ""
    for char in text:
        result += shift_letter(char)
    return result

# Example usage
if __name__ == "__main__":
    word = input("Enter a word: ")
    print("Shifted word:", simple_cipher(word))
