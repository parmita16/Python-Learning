import pandas as pd

# Create data
data = {
    "Name": ["Ram", "Sita", "Hari", "Gita"],
    "Age": [20, 21, 19, 22],
    "Marks": [80, 90, 75, 85]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Data:")
print(df)

print("\nFirst 2 rows:")
print(df.head(2))

print("\nColumn names:")
print(df.columns)

print("\nShape:")
print(df.shape)

print("\nMarks:")
print(df["Marks"])

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nStudents with marks greater than 80:")
print(df[df["Marks"] > 80])