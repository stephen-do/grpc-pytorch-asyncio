import torchvision.transforms as T
import torch

from typing import List
from PIL import Image
from torchvision.models import resnet34, ResNet34_Weights

preprocess = T.Compose(
    [
        T.Resize((224, 224)),
        T.ToTensor(),
        T.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
    ]
)
model = resnet34(weights=ResNet34_Weights.IMAGENET1K_V1).eval()


@torch.no_grad()
def inference(images: List[Image.Image]) -> List[int]:
    batch = torch.stack([preprocess(image) for image in images])
    logits = model(batch)
    preds = logits.argmax(dim=1).tolist()
    return preds


if __name__ == "__main__":
    image = Image.open("./examples/tuyendn3.jpg")
    print(inference([image]))
