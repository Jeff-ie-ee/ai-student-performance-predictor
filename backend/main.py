import pandas as pd

df = pd.read_csv("data/student-mat.csv", sep=";")

print("Dataset loaded successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nTarget column G3:")
print(df["G3"].describe())