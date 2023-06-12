import pandas as pd
import numpy as np
import nibabel as nib
import nrrd
import matplotlib.pyplot as plt


df = pd.read_csv('/home/tianyu/Desktop/labels.csv')  # read csv file
print(df['label'])  # select column and print

img = nib.load('/home/tianyu/Desktop/nnUNetBase/nnUNet_raw_data_base/nnUNet_raw_data/Task004_Hippocampus/labelsTr/hippocampus_003.nii.gz')
data = img.get_fdata()
# print(type(data))
# print(np.size(data))
# print(np.any(data))

data2, header = nrrd.read('/home/tianyu/Desktop/DATA00_49-003/DATA_001.nrrd')
# plt.imshow(data2[:,:,111], cmap='gray')
# plt.show()

data3, header = nrrd.read('/home/tianyu/Desktop/MASK/MASK_001.nrrd')
# int(len(data3))
# print(int(len(data3[0][0])))
# for i in range(len(data3[0][0])):
#     if np.any(data3[:,:,i]):
#         print(i)

# plt.imshow(data3[:,:,111], cmap='gray')
# plt.show()


nii_image = nib.load('/home/tianyu/Desktop/nnUNetBase/nnUNet_raw_data_base/nnUNet_raw_data/Task004_Hippocampus/labelsTr/hippocampus_001.nii.gz')
nii_image2 = nib.load('/home/tianyu/Desktop/Task501_Test1/imagesTr/test1_002.nii.gz')
nii_image3 = nib.load('/home/tianyu/Desktop/Task501_Test1/labelsTr/test1_002.nii.gz')
# 获取图像数据和元数据
# image_data = nii_image.get_fdata()
# image_affine = nii_image.affine
#
# for i in range(len(image_data[0][0])):
#     if np.any(image_data[:,:,i]):
#         print(i)
# # 显示图像切片
# plt.imshow(image_data[:, :, 23], cmap='gray')  # 显示z轴切片，这里选择z=50
# plt.axis('off')  # 关闭坐标轴
# plt.show()

image2 = nii_image2.get_fdata()
image3 = nii_image3.get_fdata()

for i in range(len(image3[0][0])):
    if np.any(image3[:, :, i]):
        print(i)

plt.imshow(image2[:, :, 111], cmap='gray')  # 显示z轴切片
plt.axis('off')  # 关闭坐标轴
plt.show()

plt.imshow(image3[:, :, 111], cmap='gray')  # 显示z轴切片
plt.axis('off')  # 关闭坐标轴
plt.show()
