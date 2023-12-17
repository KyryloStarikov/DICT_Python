import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
X, Y = make_regression(n_samples=100, n_features=1, n_informative=1,
                       noise=10, random_state=10)
def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)
def gradients(X, y, y_pred):
    return -2 * np.dot(X.T, (y - y_pred)) / len(y)
def gradient_descent(X, y, learning_rate=0.1, epsilon=0.0001):
    weights = np.zeros(X.shape[1])
    bias = 0
    iteration = 0
    while True:
        y_pred = np.dot(X, weights) + bias
        grad_w = gradients(X, y, y_pred)
        grad_b = -2 * np.mean(y - y_pred)
        new_weights = weights - learning_rate * grad_w
        new_bias = bias - learning_rate * grad_b
        if np.all(np.abs(new_weights - weights) < epsilon) and np.abs(new_bias - bias) < epsilon:
            break

        weights = new_weights
        bias = new_bias
        iteration += 1

    return weights, bias, iteration
weights_gd, bias_gd, iterations_gd = gradient_descent(X, Y)
model = LinearRegression()
model.fit(X, Y)
weights_sklearn = model.coef_
bias_sklearn = model.intercept_
print("Градиентный спуск:")
print("Веса:", weights_gd)
print("Смещение (bias):", bias_gd)
print("Количество итераций:", iterations_gd)

print("\nLinearRegression из sklearn:")
print("Веса:", weights_sklearn)
print("Смещение (bias):", bias_sklearn)
