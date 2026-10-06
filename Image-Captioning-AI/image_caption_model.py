import torch
import torch.nn as nn


class ImageCaptioningModel(nn.Module):

    def __init__(
        self,
        vocab_size,
        embedding_dim=256,
        hidden_size=512
    ):

        super().__init__()

        # Convert image features from ResNet
        # into the LSTM hidden-state size
        self.image_to_hidden = nn.Linear(
            2048,
            hidden_size
        )

        # Convert image features into
        # the LSTM cell-state size
        self.image_to_cell = nn.Linear(
            2048,
            hidden_size
        )

        # Convert word IDs into word embeddings
        self.embedding = nn.Embedding(
            vocab_size,
            embedding_dim
        )

        # LSTM processes the sequence of words
        self.lstm = nn.LSTM(
            input_size=embedding_dim,
            hidden_size=hidden_size,
            batch_first=True
        )

        # Convert LSTM output into vocabulary scores
        self.output_layer = nn.Linear(
            hidden_size,
            vocab_size
        )


    def forward(self, image_features, captions):

        # Create initial hidden state from image
        hidden = self.image_to_hidden(
            image_features
        )

        # Create initial cell state from image
        cell = self.image_to_cell(
            image_features
        )

        # LSTM expects:
        # [number_of_layers, batch_size, hidden_size]

        hidden = hidden.unsqueeze(0)
        cell = cell.unsqueeze(0)

        # Convert caption token IDs
        # into word embeddings
        embedded_words = self.embedding(
            captions
        )

        # Feed words + image information
        # into the LSTM
        lstm_output, _ = self.lstm(
            embedded_words,
            (hidden, cell)
        )

        # Predict a vocabulary score
        # for every word position
        word_scores = self.output_layer(
            lstm_output
        )

        return word_scores


# -----------------------------------
# Test the model
# -----------------------------------

vocab_size = 10

model = ImageCaptioningModel(
    vocab_size=vocab_size
)


# Fake ResNet output
image_features = torch.randn(
    1,
    2048
)


# Example caption:
# <START> a dog
captions = torch.tensor([
    [1, 2, 3]
])


# Run the model
output = model(
    image_features,
    captions
)


print("Input caption shape:")
print(captions.shape)

print("\nModel output shape:")
print(output.shape)