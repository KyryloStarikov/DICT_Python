import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
file_path = '/mnt/data/hearing_test.csv'
data = pd.read_csv(file_path)
print(data.head())
test_result_counts = data['test_result'].value_counts()
print(test_result_counts)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['age'], data['physical_score'], data['test_result'], c=data['test_result'], cmap='coolwarm')
ax.set_xlabel('Age')
ax.set_ylabel('Physical Score')
ax.set_zlabel('Test Result')
plt.show()
X = data[['age', 'physical_score']]
y = data['test_result']
scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)
model = LogisticRegression()
model.fit(scaled_X, y)
y_pred = model.predict(scaled_X)
accuracy = accuracy_score(y, y_pred)
print(f'Model Accuracy: {accuracy:.4f}')