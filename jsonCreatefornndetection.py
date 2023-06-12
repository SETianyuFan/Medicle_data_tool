import json
import os
import csv
import pandas as pd

data1 = {
    "instances": {
        "1": 0
    }
}

data2 = {
    "instances": {
        "1": 1
    }
}

df = pd.read_csv('/home/tianyu/Desktop/MedicalDataBase/Taskfirst/labels.csv')

# 获取名为'label'的列，并转换为列表
label_list = df['label'].tolist()
i = 0

package_path = '/home/tianyu/Desktop/tmp'

for filename in os.listdir('/home/tianyu/Desktop/nnUNetBase/nnUNet_raw_data_base/nnUNet_raw_data/Task098_testSec/labelsTr'):
    json_filename = filename[:-6] + "json"
    if label_list[i] == "M":
        with open(os.path.join(package_path, json_filename), 'w') as f:
            json.dump(data1, f)
    else:
        with open(os.path.join(package_path, json_filename), 'w') as f:
            json.dump(data2, f)

    i = i + 1