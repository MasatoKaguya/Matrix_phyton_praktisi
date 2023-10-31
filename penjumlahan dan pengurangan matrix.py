import os

# 1. penjumlahan dan pengurangan matriks
os.system('cls')
import numpy as np

matriks1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriks2 = np.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]])

print("==== Penjumlahan dan Pengurangan ====")
for x in range(0, len(matriks1)):
    for y in range(0, len(matriks1[0])):
        print (matriks1[x][y] + matriks2[x][y], end=' '),
print()