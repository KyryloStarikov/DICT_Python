import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df_data = pd.read_csv('players_20.csv')
print(df_data.head())
print("Розмірність даних:", df_data.shape)

# Отримання назв стовпців
df_columns = list(df_data.columns)

# Видалення непотрібних стовпців
useless_columns = ['dob', 'sofifa_id', 'player_url', 'long_name', 'body_type', 'real_face', 'loaned_from', 'nation_position', 'nation_jersey_number']
df_dropped = df_data.drop(columns=useless_columns)

# Операції над даними
last_five_rows_weight = df_dropped.tail()[['weight_kg']]
first_five_rows_name_weight = df_dropped.head()[['short_name', 'weight_kg']]
df_dropped['height_m'] = df_dropped['height_cm'] / 100
df_dropped['BMI'] = df_dropped['weight_kg'] / df_dropped['height_m']**2
first_five_rows_name_bmi = df_dropped.head()[['short_name', 'BMI']]
n = 10
first_n_rows_name_bmi = df_dropped.head(n)[['short_name', 'BMI']]

# Візуалізація
plt.hist(df_dropped['age'], bins=30, color='blue', edgecolor='black')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


