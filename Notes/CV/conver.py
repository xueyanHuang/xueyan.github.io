import json
import numpy as np
import cv2
import os
import sys

def label_to_val(label):
    label_map = {'fish': 1, 'longfish': 2, 'fatfish': 3}
    return label_map.get(label, 0)

json_dir = 'D:/imgjson'
mask_dir = 'D:/img/imgmask'

for json_file in os.listdir(json_dir):
    if json_file.endswith('.json'):
        with open(os.path.join(json_dir, json_file)) as file:
            data = json.load(file)

        height, width = data['imageHeight'], data['imageWidth']
        mask = np.zeros((height, width), dtype=np.uint8)
        
        for shape in data['shapes']:
            label = shape['label']
            label_val = label_to_val(label)
            points = np.array(shape['points'])
            cv2.fillPoly(mask, [points.astype(np.int32)], color=label_val)

        mask_filename = os.path.splitext(os.path.basename(json_file))[0] + '_mask.png'
        cv2.imwrite(os.path.join(mask_dir, mask_filename), mask)