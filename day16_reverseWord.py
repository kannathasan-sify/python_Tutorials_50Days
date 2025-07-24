# WordReverser.py

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

# Example usage
sentence = input("Enter a sentence: ")
result = reverse_words(sentence)
print("Reversed words:", result)
