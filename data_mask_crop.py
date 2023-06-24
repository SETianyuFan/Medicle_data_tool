import os
import nibabel as nib
import numpy as np
import nrrd

start_coord = np.array([40, 0, 130])
end_coord = np.array([740, 700, 830])

data_dir = '/home/tianyu/Desktop/MedicalDataBase/Task98_testSec/imagesTr'
mask_dir = '/home/tianyu/Desktop/MedicalDataBase/Task98_testSec/labelsTr'
save_dir = '/home/tianyu/Desktop/imagesTr_cropped2'
i = 0
for filename in os.listdir(data_dir):
    if filename.endswith('.nii.gz'):

        i += 1
        print(f'{i}')

        data_img = nib.load(os.path.join(data_dir, filename))
        mask_img = nib.load(os.path.join(mask_dir, filename))

        data_array = data_img.get_fdata()
        data_array_cropped = data_array[start_coord[0]:end_coord[0], start_coord[1]:end_coord[1], start_coord[2]:end_coord[2]]
        mask_array = mask_img.get_fdata()
        mask_array_cropped = mask_array[start_coord[0]:end_coord[0], start_coord[1]:end_coord[1], start_coord[2]:end_coord[2]]

        cropped_data = data_array_cropped * mask_array_cropped

        new_img = nib.Nifti1Image(cropped_data, data_img.affine, data_img.header)
        nib.save(new_img, os.path.join(save_dir, filename))