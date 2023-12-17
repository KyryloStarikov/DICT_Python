import numpy as np

# Завдання 1
vector = np.array([1, 2, 3])
vector_type = vector.dtype
print("Завдання 1 - Тип даних вектору:", vector_type)

# Завдання 2
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Завдання 2 - Матриця:\n", matrix)

# Завдання 3
zero_matrix = np.zeros((4, 5))
print("Завдання 3 - Матриця нулів:\n", zero_matrix)

# Завдання 4
identity_matrix = np.identity(3)
print("Завдання 4 - Єдинична матриця:\n", identity_matrix)

# Завдання 5
matrix_size = matrix.shape
print("Завдання 5 - Розмір матриці:", matrix_size)

# Завдання 6
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[-1, -2, -3], [-4, -5, -6]])
addition = A + B
subtraction = A - B
print("Завдання 6 - Додавання матриць:\n", addition)
print("Завдання 6 - Віднімання матриць:\n", subtraction)

# Завдання 7
elementwise_multiplication = A * B
print("Завдання 7 - Поелементне множення матриць:\n", elementwise_multiplication)

# Завдання 8
A_plus_2 = A + 2
print("Завдання 8 - Прибавлення 2 до кожного елемента матриці A:\n", A_plus_2)

# Завдання 9
matrix_multiplication = np.dot(A, np.array([[1, 1], [1, 1], [1, 1]]))
print("Завдання 9 - Матричне множення:\n", matrix_multiplication)

# Завдання 10
v = np.array([1, 2, 3])
u = np.array([1, 1, 1])
euclidean_norm_v = np.linalg.norm(v)
euclidean_norm_u = np.linalg.norm(u)
print("Завдання 10 - Евклідова норма вектора v:", euclidean_norm_v)
print("Завдання 10 - Евклідова норма вектора u:", euclidean_norm_u)

# Завдання 11
vector = np.array([11, 22, 33, 44, 55])
slice_vector = vector[-2:]
print("Завдання 11 - Зріз останніх двох елементів вектора:", slice_vector)
