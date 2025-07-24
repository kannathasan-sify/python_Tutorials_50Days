# VowelCounter.py

def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0

    for char in word:
        if char in vowels:
            count += 1

    return count

# Example usage
word = input("Enter a word: ")
vowel_count = count_vowels(word)
print("Number of vowels in the word:", vowel_count)
