import os
import numpy as np
import nibabel as nib

directory = '/home/tianyu/Desktop/tmp2'
directory2 = '/home/tianyu/Desktop/labelTr_bbox0'

expand_margin = 0

for filename in sorted(os.listdir(directory)):
    if filename.endswith('.nii.gz'):
        filepath = os.path.join(directory, filename)

        # 加载 mask
        img = nib.load(filepath)
        mask = img.get_fdata()

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

        new_mask = np.zeros(mask.shape)
        new_mask[xmin:xmax + 1, ymin:ymax + 1, zmin:zmax + 1] = 1

        new_img = nib.Nifti1Image(new_mask, img.affine, img.header)
        new_filename = filename  # 或者你可以指定任何你想要的文件名
        new_filepath = os.path.join(directory2, new_filename)
        nib.save(new_img, new_filepath)

        print(f'Processed {filename}')