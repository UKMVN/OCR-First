import torch
import torch.nn as nn
from torchvision import transforms, models
from torchvision.models import mobilenet_v3_small, MobileNet_V3_Small_Weights
from PIL import Image
import json, os, time, sys

class SceneDetector:
    def __init__(self, model=os.path.join(os.getcwd(), 'models', 'scene_detector.pth'), meta=os.path.join(os.getcwd(), 'models', 'meta.json')) -> None:
        self.device = torch.device('cpu')
        self.transform = transforms.Compose(
            [
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
            ]
        )

        if not os.path.exists(meta): raise FileNotFoundError("Meta path not found")
        with open(meta, "r") as f: self.class_names = json.load(f).get("classes", [])
        if not self.class_names: raise ValueError("Meta-class not found")

        self.model = mobilenet_v3_small()
        self.model.classifier[3] = nn.Linear(self.model.classifier[3].in_features, len(self.class_names))
        if not os.path.exists(model): raise FileNotFoundError("Model path not found")

        checkpoint = torch.load(model, map_location=self.device)
        self.model.load_state_dict(checkpoint["model_state"])
        self.model = self.model.to(self.device)
        self.model.eval()

    def do_predict(self, image: Image.Image) -> dict:
        if image is None: return {"status": False, "message": "No image found"}
        try: image = image = Image.open(image.stream)
        except Exception as e: return {"status": False, "message": f"Can't process image"}

        try:
            with torch.no_grad():
                input_tensor = self.transform(image).unsqueeze(0).to(self.device)
                outputs = self.model(input_tensor)
                _, predicted_idx = torch.max(torch.nn.functional.softmax(outputs, dim=1), 1)
                result = self.class_names[predicted_idx.item()]

            return {"status": True, "result": result}

        except Exception as e: return {"status": False, "message": str(e)}