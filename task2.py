import numpy as np

# Завдання 1
vector = np.array([1, 2, 3])
vector_type = vector.dtype

# Завдання 2
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Завдання 3
zero_matrix = np.zeros((4, 5))

# Завдання 4
identity_matrix = np.identity(3)

# Завдання 5
matrix_size = matrix.shape

# Завдання 6
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[-1, -2, -3], [-4, -5, -6]])
addition = A + B
subtraction = A - B

# Завдання 7
elementwise_multiplication = A * B

# Завдання 8
A_plus_2 = A + 2

# Завдання 9
matrix_multiplication = np.dot(A, np.array([[1, 1], [1, 1], [1, 1]]))

# Завдання 10
v = np.array([1, 2, 3])
u = np.array([1, 1, 1])
euclidean_norm_v = np.linalg.norm(v)
euclidean_norm_u = np.linalg.norm(u)

# Завдання 11
vector = np.array([11, 22, 33, 44, 55])
slice_vector = vector[-2:]
