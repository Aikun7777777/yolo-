import numpy as np
import cv2 as cv
import xml.etree.ElementTree as ET
from os.path import join



m = { 0 : "xmin",
      1 : "ymin",
      2 : "xmax",
      3 : "ymax" }
names = ['NG']
# names= ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
#         'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
#         'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
#         'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
#         'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
#         'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
#         'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
#         'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
#         'hair drier', 'toothbrush']
def create_xml_file(img_name, keep_boxes):
    root = ET.Element("annotation")
    ET.SubElement(root, "filename").text = img_name.split("/")[-1]
    img = cv.imread(img_name)
    try:
        h, w, _ = img.shape
    except:
        h, w = 1944, 2592

    size = ET.SubElement(root, "size")
    ET.SubElement(size, "width").text = str(w)
    ET.SubElement(size, "height").text = str(h)
    ET.SubElement(size, "depth").text = str(1)

    assert isinstance(keep_boxes, np.ndarray)

    for box in keep_boxes:
        assert len(box) == 5
        o = ET.SubElement(root, "object")
        bndbox = ET.SubElement(o, "bndbox")

        for i in range(len(box)):
            if i == len(box) - 1:
                # record class
                #===============
                i2 = box[i]
                names_label = names[i2]
                ET.SubElement(o, "name").text = str(names_label)
                #===============
                # ET.SubElement(o, "name").text = str(box[i])
                ET.SubElement(o, "difficult").text = str(0)
            else:
                ET.SubElement(bndbox, m[i]).text = str(box[i])

    tree = ET.ElementTree(root)
    tree.write(join(img_name.split("/")[-1].replace("jpg", "xml")))



scale_w,scale_h = 2592, 1944
def write_xml(results, path):
    if len(results):
        boxes, scores, labels = results
        boxes[:, 0::2]
        boxes[:, 1::2]
        cls_loc = np.concatenate([boxes, labels[:, None]], -1).astype(np.int16)

    else:
        cls_loc = np.zeros((0, 5))
    create_xml_file(path, cls_loc)

