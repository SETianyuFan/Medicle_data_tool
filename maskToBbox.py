import os
import csv
import nrrd
import numpy as np
import nibabel as nib

def mask_to_bbox(mask):
    z, y, x = np.where(mask != 0)
    return [np.min(x), np.min(y), np.min(z), np.max(x), np.max(y), np.max(z)]

directory = "/home/tianyu/Desktop/MedicalDataBase/Taskfirst/MASK"

bboxs = []

listnrrd = os.listdir(directory)
listnrrd.sort()

for filename in listnrrd:

    if filename.endswith(".nrrd"):

        # 加载nrrd文件中的数据
        #nib = nib.load(os.path.join(directory, filename))
        data, header = nrrd.read(os.path.join(directory, filename))

        #data = nib.get_fdata()
        # 将mask转换为bbox
        bbox = mask_to_bbox(data)

        bboxs.append([filename[5:8]] + bbox)


with open("bboxs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for bbox in bboxs:
        writer.writerow(bbox)


