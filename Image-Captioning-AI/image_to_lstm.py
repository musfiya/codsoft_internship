import torch
import torch.nn as nn


# -----------------------------
# Model dimensions
# -----------------------------

resnet_features = 2048
hidden_size = 512


# -----------------------------
# Convert image features
# into LSTM hidden state
# -----------------------------

image_to_hidden = nn.Linear(
    resnet_features,
    hidden_size
)


# -----------------------------
# Fake ResNet output
# -----------------------------

image_features = torch.randn(1, 2048)

print("ResNet feature shape:")
print(image_features.shape)


# -----------------------------
# Create initial hidden state
# -----------------------------

hidden_state = image_to_hidden(image_features)

print("\nLSTM hidden state shape:")
print(hidden_state.shape)