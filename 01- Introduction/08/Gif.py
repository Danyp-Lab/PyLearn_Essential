import os

import cv2
import imageio

# Define the Dir the images
image_dir = "images"

# Get the list of files in the directory
file_list = os.listdir(image_dir)

# Sort the file list
file_list.sort()

# Initialize an empty list to store the images
images = []

# Loop over the files in the sorted list
for file in file_list:
    # Construct the full file path
    file_path = os.path.join(image_dir, file)

    # Read the image file
    img = cv2.imread(file_path)

    # Check if the image file was correctly read
    if img is None:
        print(f"Error reading file {file_path}")
        continue

    # Resize the image
    img = cv2.resize(img, (768, 1024))

    # Append the image to the list
    images.append(img)

# Save the images as a GIF
imageio.mimsave("MaxPayne2.gif", images)
