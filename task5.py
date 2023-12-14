import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
x = np.random.rand(100, 1) * 10
y = 2 * x + 5 + np.random.randn(100, 1) * 2
N = len(x)
alpha_1 = np.sum(y * x) / N
alpha_2 = np.sum(x**2) / N
m_x = np.mean(x)
m_y = np.mean(y)
omega_1 = (alpha_1 - m_x * m_y) / (alpha_2 - m_x**2)
omega_0 = m_y - omega_1 * m_x
plt.scatter(x, y, color='blue', label='Данные')
plt.plot(x, omega_1 * x + omega_0, color='red', label='Подогнанная линия')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Линейная регрессия методом наименьших квадратов')
plt.legend()
plt.show()

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x, y)
model_omega_1 = model.coef_[0][0]
model_omega_0 = model.intercept_[0]
print("Параметры модели LinearRegression:")
print("omega_1 (наклон):", model_omega_1)
print("omega_0 (пересечение):", model_omega_0)