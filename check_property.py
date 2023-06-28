import pandas as pd
import os
import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

directory = '/home/tianyu/Desktop/MedicalDataBase/Task98_testSec/labelsTr'
df = pd.read_csv('/home/tianyu/Desktop/MedicalDataBase/Taskfirst/labels.csv')
csv_data = df['label']
csv_list = df['label'].tolist()
i = 0
m_list = []
b_list = []
bins = 10
for filename in sorted(os.listdir(directory)):
    if filename.endswith('.nii.gz'):
        filepath = os.path.join(directory, filename)
        img = nib.load(filepath)
        mask = img.get_fdata()
        xs, ys, zs = np.where(mask)
        print(f"label: {csv_list[i]}  size: {len(xs)}")
        if csv_list[i] == 'M':
            m_list.append(len(xs))
        else:
            b_list.append(len(xs))
        i += 1

print(f'final M label size: {m_list}')
print(f'final B label size: {b_list}')

i_list = [1, 2, 3]
for i in i_list:
    m_list.pop(m_list.index(min(m_list)))
    b_list.pop(b_list.index(min(b_list)))
    m_list.pop(m_list.index(max(m_list)))
    b_list.pop(b_list.index(max(b_list)))

plt.hist(m_list, bins='auto', edgecolor='black')
plt.title('Number Distribution')
plt.xlabel('Number')
plt.ylabel('m_Frequency')
plt.show()

plt.hist(b_list, bins='auto', edgecolor='black')
plt.title('Number Distribution')
plt.xlabel('Number')
plt.ylabel('b_Frequency')
plt.show()

