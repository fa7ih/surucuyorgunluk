import cv2
import torch
import torchvision.transforms as transforms
from timm import create_model
import numpy as np
from PIL import Image
import winsound 

class LeViTModel(torch.nn.Module):
    def __init__(self, num_classes):
        super(LeViTModel, self).__init__()
        self.backbone = create_model('levit_384', pretrained=False, num_classes=num_classes)

    def forward(self, x):
        return self.backbone(x)
model_path = "C:\\Users\\Fatih\\OneDrive\\Masaüstü\\Proje Yapay zeka\\veri\\LevitModel\\levit_model_fold_3.pth"
num_classes = 2
model = LeViTModel(num_classes=num_classes)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

cap = cv2.VideoCapture(0)  #0 bilgisayar kamerası 1 telefon kamerası

if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamadı!")
        break

    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    input_tensor = transform(img).unsqueeze(0) 

    with torch.no_grad():
        output = model(input_tensor)
        prediction = torch.argmax(output, dim=1).item()

    if prediction == 1: 
        cv2.putText(frame, "", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        winsound.Beep(1000, 500)  
    else:  
        cv2.putText(frame, "NORMAL", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
