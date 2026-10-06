import torch
import torch.nn as nn


# Our tiny vocabulary
vocab_size = 10

# Convert each word ID into a smaller vector
embedding_dim = 256

# Size of LSTM's internal representation
hidden_size = 512


# Word embedding layer
embedding = nn.Embedding(
    vocab_size,
    embedding_dim
)


# LSTM
lstm = nn.LSTM(
    input_size=embedding_dim,
    hidden_size=hidden_size,
    batch_first=True
)


# Convert LSTM output into vocabulary scores
output_layer = nn.Linear(
    hidden_size,
    vocab_size
)


# Example token IDs
tokens = torch.tensor([
    [1, 2, 3]
])


# Convert token IDs into embeddings
embedded_words = embedding(tokens)


print("Token shape:")
print(tokens.shape)

print("\nEmbedding shape:")
print(embedded_words.shape)


# Pass embeddings through LSTM
lstm_output, hidden = lstm(embedded_words)


print("\nLSTM output shape:")
print(lstm_output.shape)


# Predict vocabulary scores
word_scores = output_layer(lstm_output)


print("\nWord scores shape:")
print(word_scores.shape)