import os
import shutil
import random

# Paths
dataset_path = "dataset"
images_path = os.path.join(dataset_path, "images")
labels_path = os.path.join(dataset_path, "labels")

# Output folders
output_path = "data_set"

splits = ["train", "val", "test"]

for split in splits:
    os.makedirs(os.path.join(output_path, split, "images"), exist_ok=True)
    os.makedirs(os.path.join(output_path, split, "labels"), exist_ok=True)

# Get all image files
images = [f for f in os.listdir(images_path) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Shuffle images
random.shuffle(images)

# Split ratios
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

total = len(images)

train_end = int(total * train_ratio)
val_end = train_end + int(total * val_ratio)

train_files = images[:train_end]
val_files = images[train_end:val_end]
test_files = images[val_end:]

# Function to move files
def move_files(file_list, split):
    for file in file_list:
        img_src = os.path.join(images_path, file)
        label_file = file.replace(".jpg", ".txt").replace(".png", ".txt").replace(".jpeg", ".txt")
        label_src = os.path.join(labels_path, label_file)

        img_dst = os.path.join(output_path, split, "images", file)
        label_dst = os.path.join(output_path, split, "labels", label_file)

        shutil.copy(img_src, img_dst)

        if os.path.exists(label_src):
            shutil.copy(label_src, label_dst)
        else:
            print(f"⚠️ Label missing for {file}")

# Move files
move_files(train_files, "train")
move_files(val_files, "val")
move_files(test_files, "test")

print("✅ Dataset split completed!")