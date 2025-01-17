import os
import nibabel as nib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 定义文件夹路径
source_folder = "/home/tianyu/Desktop/MedicalDataBase/Task98_testSec/imagesTr"
bbox_folder = "/home/tianyu/Desktop/labelTr_bbox"
output_folder = "/home/tianyu/Desktop/imagesTr_cropped2"

# for filename in os.listdir(source_folder):
#     if filename.endswith(".nii.gz"):
#
#         source_nii = nib.load(os.path.join(source_folder, filename))
#         bbox_nii = nib.load(os.path.join(bbox_folder, filename))
#
#         source_data = source_nii.get_fdata()
#         bbox_data = bbox_nii.get_fdata()
#
#         # 获取bbox坐标
#         coords = np.where(bbox_data == 1)
#
#         # 切片源图像
#         #sliced_image_data = source_data[coords]
#         sliced_image_data = source_data * bbox_data
#
#
#         sliced_image_nii = nib.Nifti1Image(sliced_image_data, bbox_nii.affine)
#
#
#         nib.save(sliced_image_nii, os.path.join(output_folder, filename))
#
#         print(filename)

# 指定你要遍历的目录
directory = '/home/tianyu/Desktop/MedicalDataBase/Task98_testSec/labelsTr'
directory2 = '/home/tianyu/Desktop/labelTr_bbox0'
data_dir = '/home/tianyu/Desktop/MedicalDataBase/Task98_testSec/imagesTr'
mask_dir = '/home/tianyu/Desktop/MedicalDataBase/Task98_testSec/labelsTr'

expand_margin = 5

sum_x = 0
sum_y = 0
sum_z = 0

vector_x = np.zeros(100)
vector_y = np.zeros(100)
vector_z = np.zeros(100)

# 遍历目录中的每个文件
i = 0
for filename in sorted(os.listdir(directory)):
    if filename.endswith('.nii.gz'):
        filepath = os.path.join(directory, filename)

        # 加载 mask
        img = nib.load(filepath)
        mask = img.get_fdata()

        # 提取 mask 的 bbox
        # rows, cols, slices = np.where(mask)
        # xmin, xmax = np.min(rows), np.max(rows)
        # ymin, ymax = np.min(cols), np.max(cols)
        # zmin, zmax = np.min(slices), np.max(slices)

        # 找到mask的坐标
        xs, ys, zs = np.where(mask)
        # 扩展bbox的边界
        xmin = max(0, xs.min() - expand_margin)
        xmax = min(mask.shape[0], xs.max() + expand_margin)
        ymin = max(0, ys.min() - expand_margin)
        ymax = min(mask.shape[1], ys.max() + expand_margin)
        zmin = max(0, zs.min() - expand_margin)
        zmax = min(mask.shape[2], zs.max() + expand_margin)

        print('*',xmax,ymax,zmax,'*',xmin,ymin,zmin,'\n')

        vector_x[i] = xmax - xmin
        vector_y[i] = ymax - ymin
        vector_z[i] = zmax - zmin

        sum_x = sum_x + xmax - xmin
        sum_y = sum_y + ymax - ymin
        sum_z = sum_z + zmax - zmin

        image_nib = nib.load(os.path.join(source_folder, filename))
        image_data = image_nib.get_fdata()

        # 创建一个新的 mask
        # new_mask = np.zeros(mask.shape)
        # new_mask[xmin:xmax + 1, ymin:ymax + 1, zmin:zmax + 1] = 1
        new_mask = mask[xmin:xmax + 1, ymin:ymax + 1, zmin:zmax + 1]
        new_image = image_data[xmin:xmax + 1, ymin:ymax + 1, zmin:zmax + 1]
        new_image = new_image * new_mask


        # 保存新的 mask 为 .nii.gz 文件
        new_img = nib.Nifti1Image(new_mask, image_nib.affine, image_nib.header)
        new_filename = filename  # 或者你可以指定任何你想要的文件名
        new_filepath = os.path.join(output_folder, new_filename)
        nib.save(new_img, new_filepath)

        print(f'Processed {filename}')
