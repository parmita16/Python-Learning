import pandas as pd

data = {
    "Employee": ["Ram", "Sita", "Hari", "Gita", "John"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 45000, 60000, 55000, 48000]
}

df = pd.DataFrame(data)

print("Employee Data:")
print(df)

print("\nEmployees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nEmployees sorted by salary:")
print(df.sort_values("Salary"))

print("\nEmployees sorted by highest salary:")
print(df.sort_values("Salary", ascending=False))