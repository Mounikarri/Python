# Get input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words and count occurrences
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1

# Display the word counts
for word, count in word_count.items():
    print(f"{word}: {count}")
