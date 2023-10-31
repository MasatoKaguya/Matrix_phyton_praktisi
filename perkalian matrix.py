import numpy as np
matriks1 = np.array([[1, 2], [3, 4]])
matriks2 = np.array([[5, 6], [7, 8]])

print("\n==== Perkalian matriks ====".upper())
print("Hasil perkalian matriks: ", np.dot(matriks1, matriks2))
print()

# 3. transpose matriks
matriks = np.array([[6, 5], [1, 3], [2, 4]])
print("==== Transpose matriks ====")
print(np.transpose(matriks))
print()