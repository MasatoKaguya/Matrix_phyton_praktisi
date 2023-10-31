import numpy as np
matriks = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 10, 11], [12, 13, 14, 15]])
matriks_reshape = np.reshape(matriks, (2, 8))
print("==== Matriks Reshape ===")
print(matriks_reshape) 