def word_count(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Create a dictionary to hold word counts
    count_dict = {}
    
    # Count each word's occurrences
    for word in words:
        if word in count_dict:
            count_dict[word] += 1  # Increment count if word is already in dictionary
        else:
            count_dict[word] = 1  # Initialize count if it's the first occurrence

    # Print the word count for each word
    for word, count in count_dict.items():
        print(f"{word}: {count}")

# Input and function call
sentence = input("Enter any sentence: ")
word_count(sentence)
