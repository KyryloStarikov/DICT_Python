import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
np.random.seed(0)
x = np.linspace(0, 1, 100)[:, np.newaxis]
y = np.sin(2 * np.pi * x) + np.random.normal(scale=0.1, size=x.shape)
x_train, x_test = x[:80], x[80:]
y_train, y_test = y[:80], y[80:]
degrees = [1, 2, 3, 6]
for degree in degrees:
    poly_features = PolynomialFeatures(degree=degree)
    x_train_poly = poly_features.fit_transform(x_train)
    x_test_poly = poly_features.transform(x_test)
    model = LinearRegression()
    model.fit(x_train_poly, y_train)
    y_pred = model.predict(x_test_poly)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    print(f"Степень полинома: {degree}")
    print(f"RMSE: {rmse:.2f}")
    print(f"Коэффициент детерминации R^2: {r2:.2f}")
    print("-" * 30)