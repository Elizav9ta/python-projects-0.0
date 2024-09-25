def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words

# Example usage:
user_input = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(user_input)
print(reversed_sentence)
