import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import KFold
# 读取csv文件
df = pd.read_csv('/home/tianyu/Desktop/MedicalDataBase/Taskfirst/labels.csv')
csv_data = df['label']
csv_list = df['label'].tolist()
csv_listnp = np.array(csv_list)

kfold = KFold(n_splits=5)

for train_indices, test_indices in kfold.split(csv_listnp):

    train_data = csv_listnp[train_indices]
    test_data = csv_listnp[test_indices]

    train_M = 0
    train_B = 0
    for item in train_data:
        if item == 'M':
            train_M += 1
        else:
            train_B += 1

    print(f'train set: M:{train_M}, B:{train_B}')

    test_M = 0
    test_B = 0
    for item in test_data:
        if item == 'M':
            test_M += 1
        else:
            test_B += 1

    print(f'test set: M:{train_M}, B:{train_B}')