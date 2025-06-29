# from pathlib import Path
# import cv2
# images_path=list(Path("Too_large_images").glob('*.*'))

# for i in range(len(images_path)):
#     image=cv2.imread(images_path[i])
#     h,w=image.shape[:2]
#     new_image=cv2.resize(image,(h//2,w//2))
#     cv2.imwrite(f"outputs/{images_path[i]}",new_image)
import cv2
import os

input_folder = 'Too_large_images'
output_folder = 'outputs'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Failed to read {image_path}")
            continue

        h, w = image.shape[:2]
        new_image = cv2.resize(image, (int(w / 2), int(h / 2)))

        # ✅ Keep extension and save correctly
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, new_image)

        print(f"Saved: {output_path}")
