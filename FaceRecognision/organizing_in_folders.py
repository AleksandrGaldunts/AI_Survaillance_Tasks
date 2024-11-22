import os
import shutil

dataset_path = "captured_images"
output_folder = "training_data"

# Ensure the output folder exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the dataset path
for filename in os.listdir(dataset_path):
    # Get the prefix name (e.g., "Alik" or "Bulvers") from the filename
    name_prefix = filename.split('_')[0]

    # Create a folder named after the prefix in the training data directory
    subject_folder = os.path.join(output_folder, name_prefix)
    if not os.path.exists(subject_folder):
        os.makedirs(subject_folder)

    # Move the file to the respective person's folder
    source_path = os.path.join(dataset_path, filename)
    destination_path = os.path.join(subject_folder, filename)
    shutil.move(source_path, destination_path)

print("Files have been organized into folders by name in the training_data directory.")
