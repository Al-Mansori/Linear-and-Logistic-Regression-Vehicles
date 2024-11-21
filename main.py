import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# a) Load dataset
df = pd.read_csv('co2_emissions_data.csv')


# b) Perform analysis
#   i) check for missing values
if df.size == df.count().sum():
    print("there are no missing values in the dataset")
else:
    print(f"there are {df.size - df.count().sum()
                       } missing values in the dataset")

#   ii) check whether numerical features have the same scale
numerical_features = df.select_dtypes([float, int])
numerical_input_features = numerical_features.drop(["CO2 Emissions(g/km)"], axis=1)  # revise
numerical_features_max = numerical_input_features.max().values
numerical_features_min = numerical_input_features.min().values


is_same_scale = True
for max_val, min_val in zip(numerical_features_max, numerical_features_min):
    for other_max_val, other_min_val in zip(numerical_features_max, numerical_features_min):
        if abs(max_val - other_max_val) > 5 or abs(min_val - other_min_val) > 5:
            is_same_scale = False
            break
    if not is_same_scale:
        break

if is_same_scale:
    print("numeric features have the same scale")
else:
    print("numeric features DON'T have the same scale")


# numerical_features may need to include the "CO2 Emissions(g/km)" label as well
# confirm from Shehab then act accordingly

# iii) visualize a pairplot in which diagonal subplots are histograms
sb.set_theme(style='ticks')
pairplot_diagonal_histograms = sb.pairplot(
    numerical_features, height=3, aspect=1.2)


# iv) visualize a correlation heatmap between numeric columns
correlation_matrix = numerical_features.corr()
plt.figure(figsize=(12, 8))
correlation_heatmap = sb.heatmap(
    correlation_matrix, annot=True, cmap='coolwarm', center=0)

plt.show()


# print(df.size)
# print(df.count().sum())


# print(df.describe())
# print(df.groupby('category').mean())
# print(df.to_csv())


# print(df.index)
# print(df.columns)
# print(df.dtypes)
# print(df.info)
# print(df.select_dtypes(float))
# print(df.values)
# print(df.axes)
# print(df.ndim)
# print(df.size)
# print(df.empty)
# print(df.groupby('Make')['Cylinders'].mean())
