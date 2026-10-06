import torch
from torchvision import models, transforms
from PIL import Image


# Load pretrained ResNet-50
model = models.resnet50(
    weights=models.ResNet50_Weights.DEFAULT
)

# Remove the final classification layer
model = torch.nn.Sequential(
    *list(model.children())[:-1]
)

# Put model in evaluation mode
model.eval()


# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])


# Load image
image = Image.open("dog.jpeg").convert("RGB")


# Convert image into a tensor
image_tensor = transform(image)


# Add batch dimension
image_tensor = image_tensor.unsqueeze(0)


# Extract features
with torch.no_grad():
    features = model(image_tensor)


print("Feature shape:", features.shape)
print("Number of features:", features.numel())