import os
import shutil
import random

# Path to the BCCD dataset
data_dir = 'BCCD_Dataset'
images_dir = os.path.join(data_dir, 'BCCD\\JPEGImages')
labels_dir = os.path.join(data_dir, 'YOLO_Annotations')

# Create directories for train and val splits
train_images_dir = os.path.join(data_dir, 'train/images')
train_labels_dir = os.path.join(data_dir, 'train/labels')
val_images_dir = os.path.join(data_dir, 'val/images')
val_labels_dir = os.path.join(data_dir, 'val/labels')

os.makedirs(train_images_dir, exist_ok=True)
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Get list of all image files
image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]

# Shuffle the image files
random.shuffle(image_files)

# Split the data into 80% train and 20% val
split_idx = int(len(image_files) * 0.8)

train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

# Move files to train and val directories
for file in train_files:
    shutil.move(os.path.join(images_dir, file), os.path.join(train_images_dir, file))
    shutil.move(os.path.join(labels_dir, file.replace('.jpg', '.txt')), os.path.join(train_labels_dir, file.replace('.jpg', '.txt')))

for file in val_files:
    shutil.move(os.path.join(images_dir, file), os.path.join(val_images_dir, file))
    shutil.move(os.path.join(labels_dir, file.replace('.jpg', '.txt')), os.path.join(val_labels_dir, file.replace('.jpg', '.txt')))

print("Dataset split completed!")
