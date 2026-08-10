import pandas as pd

# Create data
data = {
    "Name": ["Ram", "Sita", "Hari", "Gita", "John"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [80, 90, 75, 85, 95],
    "City": ["Kathmandu", "Pokhara", "Kathmandu", "Lalitpur", "Pokhara"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display complete DataFrame
print("Original Data:")
print(df)

# Display first 3 rows
print("\nFirst 3 rows:")
print(df.head(3))

# Display last 2 rows
print("\nLast 2 rows:")
print(df.tail(2))

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display shape
print("\nShape:")
print(df.shape)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display only Name column
print("\nNames:")
print(df["Name"])

# Display Name and Marks
print("\nName and Marks:")
print(df[["Name", "Marks"]])

# Average marks
print("\nAverage Marks:")
print(df["Marks"].mean())

# Highest marks
print("\nHighest Marks:")
print(df["Marks"].max())

# Lowest marks
print("\nLowest Marks:")
print(df["Marks"].min())

# Total marks
print("\nTotal Marks:")
print(df["Marks"].sum())

# Students with marks greater than 80
print("\nStudents with marks greater than 80:")
print(df[df["Marks"] > 80])

# Students from Kathmandu
print("\nStudents from Kathmandu:")
print(df[df["City"] == "Kathmandu"])

# Students older than 20
print("\nStudents older than 20:")
print(df[df["Age"] > 20])

# Add Result column
df["Result"] = ["Pass", "Pass", "Pass", "Pass", "Pass"]

print("\nAfter adding Result:")
print(df)

# Sort by Marks
print("\nSorted by Marks:")
print(df.sort_values("Marks"))

# Sort from highest to lowest
print("\nMarks from highest to lowest:")
print(df.sort_values("Marks", ascending=False))

# Group by City and calculate average marks
print("\nAverage Marks by City:")
print(df.groupby("City")["Marks"].mean())