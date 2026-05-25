import cv2
import numpy as np
import os

image_paths = [
    "pancard_1.jpg",
    "pancard_2.jpg",
    "pancard_3.jpg",
    "pancard_4.jpg",
    "pancard_5.jpg",
    "pancard_6.jpg"
]

output_dir = "pan_aug_100"
os.makedirs(output_dir, exist_ok=True)
 
def augment(img):
    h, w = img.shape[:2]

    angle = np.random.uniform(-20, 20)
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1)
    img = cv2.warpAffine(img, M, (w, h))

    img = cv2.convertScaleAbs(img, alpha=np.random.uniform(0.8,1.2), beta=np.random.randint(-40,40))

    if np.random.rand() > 0.5:
        img = cv2.GaussianBlur(img, (5,5), 0)

    if np.random.rand() > 0.5:
        img = cv2.flip(img, 1)

    return img

count = 0

while count < 100:
    for path in image_paths:
        if count >= 100:
            break
        img = cv2.imread(path)
        aug = augment(img)
        cv2.imwrite(f"{output_dir}/img_{count}.jpg", aug)
        count += 1