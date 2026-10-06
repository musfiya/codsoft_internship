caption = "a dog is standing on the beach"


# Add special tokens
caption = "<START> " + caption + " <END>"


# Split into words
words = caption.lower().split()


# Create vocabulary
vocabulary = {}

for word in words:

    if word not in vocabulary:
        vocabulary[word] = len(vocabulary) + 1


print("Vocabulary:")
print(vocabulary)


# Convert words to numbers
token_ids = [vocabulary[word] for word in words]


print("\nWords:")
print(words)

print("\nToken IDs:")
print(token_ids)