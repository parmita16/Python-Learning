import pandas as pd

data = {
    "Name": ["Ram", "Sita", "Hari", "Gita"],
    "Age": [20, 21, 19, 22],
    "Marks": [80, 90, 75, 85]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Save DataFrame
df.to_csv("students.csv", index=False)

print("\nCSV file created successfully.")

# Read CSV file
new_df = pd.read_csv("students.csv")

print("\nData read from CSV:")
print(new_df)

print("\nStudents with marks greater than 80:")
print(new_df[new_df["Marks"] > 80])