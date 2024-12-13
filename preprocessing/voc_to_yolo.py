import os
import xml.etree.ElementTree as ET

def convert_voc_to_yolo(xml_folder, output_folder, classes):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for xml_file in os.listdir(xml_folder):
        if not xml_file.endswith(".xml"):
            continue

        tree = ET.parse(os.path.join(xml_folder, xml_file))
        root = tree.getroot()
        img_width = int(root.find("size/width").text)
        img_height = int(root.find("size/height").text)

        yolo_data = []
        for obj in root.findall("object"):
            cls_name = obj.find("name").text
            cls_id = classes.index(cls_name)

            bbox = obj.find("bndbox")
            xmin = int(bbox.find("xmin").text)
            ymin = int(bbox.find("ymin").text)
            xmax = int(bbox.find("xmax").text)
            ymax = int(bbox.find("ymax").text)

            x_center = (xmin + xmax) / 2 / img_width
            y_center = (ymin + ymax) / 2 / img_height
            width = (xmax - xmin) / img_width
            height = (ymax - ymin) / img_height
            yolo_data.append(f"{cls_id} {x_center} {y_center} {width} {height}")

        with open(os.path.join(output_folder, xml_file.replace(".xml", ".txt")), "w") as f:
            f.write("\n".join(yolo_data))

convert_voc_to_yolo(
    xml_folder="BCCD_Dataset/BCCD/Annotations",
    output_folder="BCCD_Dataset/YOLO_Annotations",
    classes=["RBC", "WBC", "Platelets"]
)
