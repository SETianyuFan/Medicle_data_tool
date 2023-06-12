import pandas as pd
import numpy as np
import nibabel as nib
import os
import nrrd

nrrd_data_path = '/home/tianyu/Desktop/Taskfirst/DATA'
nifti_data_path = '/home/tianyu/Desktop/Task501_testSec/imagesTr'
nifti_data_base_filename = 'testSec_'
nifti_data_last_filename = '.nii.gz'
i = 1

for nrrd_data_filename in sorted(os.listdir(nrrd_data_path)):

    nrrd_data_filepath = os.path.join(nrrd_data_path, nrrd_data_filename)
    nrrd_data_data, nrrd_data_header = nrrd.read(nrrd_data_filepath)

    nifti_data_num_filename = str(i).zfill(3)
    i = i + 1

    nifi_data_filename = nifti_data_base_filename + nifti_data_num_filename + nifti_data_last_filename
    nifti_data_filepath = os.path.join(nifti_data_path, nifi_data_filename)

    nifti_data_img = nib.Nifti1Image(nrrd_data_data, affine=np.eye(4))
    nib.save(nifti_data_img, nifti_data_filepath)

