import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 读取csv文件
df = pd.read_csv('bboxs.csv', header=None)

# # 将dataframe转换为numpy矩阵
# matrix = df.values
#
# # 打印矩阵
# print(matrix)

vector2 = df.iloc[:, 1].values  # 列索引从0开始，所以第2列的索引是1
vector3 = df.iloc[:, 2].values
vector4 = df.iloc[:, 3].values
vector5 = df.iloc[:, 4].values
vector6 = df.iloc[:, 5].values
vector7 = df.iloc[:, 6].values

# # 打印向量
# print("Vector 2:", vector2)
# print("Vector 3:", vector3)
# print("Vector 4:", vector4)
# print("Vector 5:", vector5)
# print("Vector 6:", vector6)
# print("Vector 7:", vector7)

vectorX = vector5 - vector2
vectory = vector6 - vector3
vectorz = vector7 - vector4

print("vecter x", vectorX)
print("vector y", vectory)
print("vector z", vectorz)

max_x = -1
max_y = -1
max_z = -1

for i, k in enumerate(vectorX):
    if max_x < vectorX[i] : max_x = vectorX[i]
    if max_y < vectory[i] : max_y = vectory[i]
    if max_z < vectorz[i] : max_z = vectorz[i]

print("*"*10)
print(f'max_x_length = {max_x}')
print(f'max_y_length = {max_y}')
print(f'max_z_length = {max_z}')

print('*'*10)
print(f'max_x = {max(vector5)}')
print(f'max_y = {max(vector6)}')
print(f'max_z = {max(vector7)}')
print(f'min_x = {min(vector2)}')
print(f'min_y = {min(vector3)}')
print(f'min_z = {min(vector4)}')
# 创建直方图
# plt.hist(vectorz, bins='auto')  # 如果你知道你想要多少个箱子，你可以将 'auto' 替换为一个整数。
#
# plt.title("Value y distribution")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
#
# plt.show()