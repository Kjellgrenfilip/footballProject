import os
import matplotlib.pyplot as plt

label_map = {
    0: "ball",
    1: "keeper",
    2: "player",
    3: "referee"
}

train_labels_dir = "-"

class_count = {}

for filename in os.listdir(train_labels_dir):
    file_path = os.path.join(train_labels_dir, filename)
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                try:
                    class_label = int(line.split()[0])
                    class_name = label_map[class_label]
                    class_count[class_name] = class_count.get(class_name, 0) + 1
                except (ValueError, IndexError):
                    pass  
    except UnicodeDecodeError:
        print(f"UnicodeDecodeError: Unable to read file '{file_path}'")

print(class_count)

#plot pie chart
labels = list(class_count.keys())
counts = list(class_count.values())
plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title('Class distribution')
plt.show()
