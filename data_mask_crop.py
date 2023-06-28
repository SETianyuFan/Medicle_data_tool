import os
import nibabel as nib
import numpy as np
import nrrd
import pandas as pd

df = pd.read_csv('bboxs.csv', header=None)

vector2 = df.iloc[:, 1].values  # z_min
vector3 = df.iloc[:, 2].values  # y_min
vector4 = df.iloc[:, 3].values  # x_min
vector5 = df.iloc[:, 4].values  # z_max
vector6 = df.iloc[:, 5].values  # y_max
vector7 = df.iloc[:, 6].values  # x_max

print(vector2)

data_dir = '/home/tianyu/Desktop/MedicalDataBase/Task98_testSec/imagesTr'
mask_dir = '/home/tianyu/Desktop/MedicalDataBase/Task98_testSec/labelsTr'
save_dir = '/home/tianyu/Desktop/imagesTr_cropped2'
test_tmp = '/home/tianyu/Desktop/issdfsf'

i = 0
list = os.listdir(data_dir)
list.sort()

for filename in list:
    if filename.endswith('.nii.gz'):

        data_img = nib.load(os.path.join(data_dir, filename))
        mask_img = nib.load(os.path.join(mask_dir, filename))

        

        data_array = data_img.get_fdata()
        data_array_cropped = data_array[vector4[i]:vector7[i]+1, vector3[i]:vector6[i]+1, vector2[i]:vector5[i]+1]

        mask_array = mask_img.get_fdata()
        mask_array_cropped = mask_array[vector4[i]:vector7[i]+1, vector3[i]:vector6[i]+1, vector2[i]:vector5[i]+1]

        cropped_data = data_array_cropped * mask_array_cropped

        new_img = nib.Nifti1Image(cropped_data, data_img.affine, data_img.header)
        nib.save(new_img, os.path.join(save_dir, filename))
        if i == 1:
            nib.save(nib.Nifti1Image(data_array_cropped, data_img.affine, data_img.header), os.path.join(test_tmp, 'data.nii.gz'))
            nib.save(nib.Nifti1Image(mask_array_cropped, data_img.affine, data_img.header), os.path.join(test_tmp, 'mask.nii.gz'))

        i += 1
        print(f'{i}')