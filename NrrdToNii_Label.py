import pandas as pd
import numpy as np
import nibabel as nib
import os
import nrrd

nrrd_label_path = '/home/tianyu/Desktop/MedicalDataBase/Taskfirst/MASK'
nifti_label_path = '/home/tianyu/Desktop/tmp3'
nifti_label_base_filename = 'testThird_'
nifti_label_last_filename = '.nii.gz'
i = 1
# df = pd.read_csv('/home/tianyu/Desktop/Taskfirst/labels.csv')
# main_label_list = df['label']
# k = 0
for nrrd_data_filename in sorted(os.listdir(nrrd_label_path)):

    nrrd_data_filepath = os.path.join(nrrd_label_path, nrrd_data_filename)
    nrrd_data_data, nrrd_data_header = nrrd.read(nrrd_data_filepath)

    # k = k + 1

    nifti_data_num_filename = str(i).zfill(3)
    i = i + 1

    nifi_data_filename = nifti_label_base_filename + nifti_data_num_filename + nifti_label_last_filename
    nifti_data_filepath = os.path.join(nifti_label_path, nifi_data_filename)

    nifti_data_img = nib.Nifti1Image(nrrd_data_data, affine=np.eye(4))
    nib.save(nifti_data_img, nifti_data_filepath)