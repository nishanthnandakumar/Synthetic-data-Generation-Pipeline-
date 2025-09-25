from PIL import Image
import os

# Define input and output folders
input_folder = '/root/output/'
output_folder = '/root/src/output/'
os.makedirs(output_folder, exist_ok=True)

# Define the crop box: (left, upper, right, lower)
crop_box = (325, 315, 775, 385)  # Example: crop from (100,50) to (500,400)

# Loop over first 100 images in the folder
for i, filename in enumerate(sorted(os.listdir(input_folder))):
    
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with Image.open(input_path) as img:
            cropped_img = img.crop(crop_box)
            cropped_img.save(output_path)

        print(f"Cropped and saved: {output_path}")