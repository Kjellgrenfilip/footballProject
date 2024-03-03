import os
import random
import shutil

# Define paths to images and labels folders
images_folder = ""
labels_folder = ""

# Create directories for training, validation, and testing sets
train_folder = ""
val_folder = ""
test_folder = ""
os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Create images and labels subfolders within train, val, and test folders
train_images_folder = os.path.join(train_folder, "images")
train_labels_folder = os.path.join(train_folder, "labels")
val_images_folder = os.path.join(val_folder, "images")
val_labels_folder = os.path.join(val_folder, "labels")
test_images_folder = os.path.join(test_folder, "images")
test_labels_folder = os.path.join(test_folder, "labels")
os.makedirs(train_images_folder, exist_ok=True)
os.makedirs(train_labels_folder, exist_ok=True)
os.makedirs(val_images_folder, exist_ok=True)
os.makedirs(val_labels_folder, exist_ok=True)
os.makedirs(test_images_folder, exist_ok=True)
os.makedirs(test_labels_folder, exist_ok=True)

#get list of image files and label files
image_files = os.listdir(images_folder)
label_files = os.listdir(labels_folder)

#filter out files that are not images or labels
image_files = [f for f in image_files if f.endswith('.jpg') or f.endswith('.png')]
label_files = [f for f in label_files if f.endswith('.txt')]

#shuffle the lists to ensure randomness and replication ability
random.shuffle(image_files)

#calculate split sizes
total_images = len(image_files)
train_split = int(total_images * 0.7)
val_split = int(total_images * 0.2)
test_split = total_images - train_split - val_split

#split image and label files
train_images = image_files[:train_split]
val_images = image_files[train_split:train_split + val_split]
test_images = image_files[train_split + val_split:]

#function to copy files from source to destination folder
def copy_files(file_list, source_folder, dest_folder):
    for file_name in file_list:
        source_path = os.path.join(source_folder, file_name)
        dest_path = os.path.join(dest_folder, file_name)
        shutil.copy(source_path, dest_path)

#copy images to corresponding folders
copy_files(train_images, images_folder, train_images_folder)
copy_files(val_images, images_folder, val_images_folder)
copy_files(test_images, images_folder, test_images_folder)

#function to find corresponding label files for given image files
def find_corresponding_labels(image_files, label_files):
    corresponding_labels = []
    for image_file in image_files:
        image_name, _ = os.path.splitext(image_file)
        for label_file in label_files:
            label_name, _ = os.path.splitext(label_file)
            if image_name == label_name:
                corresponding_labels.append(label_file)
                break
    return corresponding_labels

#find corresponding label files for each set
train_labels = find_corresponding_labels(train_images, label_files)
val_labels = find_corresponding_labels(val_images, label_files)
test_labels = find_corresponding_labels(test_images, label_files)

#fopy label files to corresponding folders
copy_files(train_labels, labels_folder, train_labels_folder)
copy_files(val_labels, labels_folder, val_labels_folder)
copy_files(test_labels, labels_folder, test_labels_folder)

print("Splitting completed successfully.")
