# TextStatistics.py

def count_statistics(text):
    characters = len(text)
    words = len(text.split())
    sentences = text.count('.') + text.count('!') + text.count('?')
    
    return characters, words, sentences

# Example usage
if __name__ == "__main__":
    paragraph = input("Enter a paragraph:\n")
    characters, words, sentences = count_statistics(paragraph)

    print("\nText Statistics:")
    print("Characters:", characters)
    print("Words:", words)
    print("Sentences:", sentences)
