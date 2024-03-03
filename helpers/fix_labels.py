import os

import torch
import torch.nn as nn
import torch.optim as optim
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np


def draw_boxes(image_path, labels_path):
    # Load the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Load YOLOv5 labels
    with open(labels_path, 'r') as file:
        lines = file.readlines()

    # Define a color map for 17 different classes
    colors = plt.cm.get_cmap('tab20', 17)

    for line in lines:
        # Example YOLOv5 label format: "class x_center y_center width height"
        data = line.split()
        class_id = int(data[0])
        x_center, y_center, width, height = map(float, data[1:])

        # Convert YOLO coordinates to image coordinates
        image_width, image_height = image.shape[1], image.shape[0]
        x_min = int((x_center - width / 2) * image_width)
        y_min = int((y_center - height / 2) * image_height)
        x_max = int((x_center + width / 2) * image_width)
        y_max = int((y_center + height / 2) * image_height)

        # Get color for the current class
        color = np.array(colors(class_id)[:3]) * 255

        # Draw bounding box on the image with a unique color for each class
        thickness = 2
        image = cv2.rectangle(image, (x_min, y_min), (x_max, y_max), color, thickness)

    # Display the image in the Jupyter Notebook
    plt.imshow(image)
    plt.axis('off')
    plt.show()
    
import os
from tqdm import tqdm

def modify_labels_v3(input_path, output_path):
    labels_mapping = {
        '0': '2',
        '1': '2',
        '2': '1',
        '3': '1',
        '4': '0',
        '5': '3',
        '6': '3',
        '7': '-' #does not matter because its being removed
    }
    
    labels_mapping2 = {
        '0': '2',
        '1': '2',
        '2': '2',#refs
        '3': '2',
        '4': '2',
        '5': '2',
        '6': '0',#ball
        '7': '2',
        '8': '2',
        '9': '3', #gk
        '10': '2',
        '11': '-', #manager
        '12': '2',
        '13': '2',
        '14': '3',
        '15': '2',
        '16':'2'     
    }

    # Read the lines from the input file
    with open(input_path, 'r') as f:
        lines = f.readlines()

    # Modify lines if necessary
    modified_lines = []
    for line in lines:
        label = line.split()[0]
        if label == '0': #only ball
            modified_lines.append(line)

    # Check if any modifications were made
    if not modified_lines:
        print(f"No changes made to file: {input_path}")
        return

    # Write modified lines to the output file
    with open(output_path, 'w') as f:
        for line in modified_lines:
            f.write(line)

    print("Labels changed.")
    print()


def modify_labels_v2(input_path, output_path):
    labels_mapping = {
        '0': '2',
        '1': '2',
        '2': '1',
        '3': '1',
        '4': '0',
        '5': '3',
        '6': '3',
        '7': '-' #does not matter because its beeing removed
    }
    
    labels_mapping2 = {
        '0': '2',
        '1': '2',
        '2': '2',#refs
        '3': '2',
        '4': '2',
        '5': '2',
        '6': '0',#ball
        '7': '2',
        '8': '2',
        '9': '3', #gk
        '10': '2',
        '11': '-', #manager
        '12': '2',
        '13': '2',
        '14': '3',
        '15': '2',
        '16':'2'     
    }
    
    #names: ['Black-White', 'Dark Blue', 'Dark Red', 'Light Blue', 'White-Blue',
    # 'White-Red', 'ball', 'black', 'blue', 'gk', 'green', 'manager', 'orange', 'purple', 'red', 'white', 'yellow']
    

    print("Labels changed.")
    # labels_path = dataset_path

    # for label_file_name in tqdm(os.listdir(labels_path)):
    label_file_path = input_path

    with open(label_file_path, 'r') as f:
        lines = f.readlines()

    with open(output_path, 'w') as f:
        for line in lines:
            label = line.split()[0]
            if label == '0': #only ball
                #line = line.replace(label, labels_mapping[label], 1)
                f.write(line)
            #continue  # Skip the line with label '7'
            

    print()
    

import os

def compare_file_names(folder_txt, folder_png):
    # Get the list of .txt files in the first folder
    txt_files = [file for file in os.listdir(folder_txt) if file.endswith('.txt')]

    # Get the list of .png files in the second folder
    png_files = [file for file in os.listdir(folder_png) if file.endswith('.png')]
    
    print(png_files)
    # Compare file names and print matching pairs
    matching_pairs = set(txt_files) & set(png_files)
    for match in matching_pairs:
        print(f"Match found: {os.path.join(folder_txt, match)} and {os.path.join(folder_png, match[:-3] + 'png')}")




if __name__ == "__main__":
    
    #input_labels_path = "/Users/filipkjellgren/Documents/Programmering/tents_project/test/663.txt"
    #output_directory = "/Users/filipkjellgren/Documents/Programmering/tents_project/test/1.txt"


    folder_path = ''
    new_folder_path = ''
    #iterate map
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            #avoid oeverwriting
            temp_output_path = new_folder_path + '/' + filename

            #modify lab
            modify_labels_v3(file_path, temp_output_path)

            #replace
            #os.replace(temp_output_path, file_path)
            
    folder_path_txt = ''
    folder_path_png = ''

   