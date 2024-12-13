import albumentations as A
from albumentations.pytorch import ToTensorV2
import cv2

transform = A.Compose([
    A.RandomRotate90(),
    A.HorizontalFlip(),
    A.VerticalFlip(),
    A.RandomBrightnessContrast(),
    A.Resize(640, 640),
    ToTensorV2(),
])

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    augmented = transform(image=image)
    return augmented['image']
