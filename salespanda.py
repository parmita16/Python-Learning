import pandas as pd

data = {
    "Product": [
        "Laptop", "Phone", "Laptop",
        "Tablet", "Phone", "Tablet"
    ],

    "Category": [
        "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics", "Electronics"
    ],

    "City": [
        "Kathmandu", "Pokhara", "Kathmandu",
        "Pokhara", "Kathmandu", "Lalitpur"
    ],

    "Sales": [
        80000, 50000, 75000,
        40000, 55000, 45000
    ]
}

df = pd.DataFrame(data)

print("Sales Data:")
print(df)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nSales by City:")
print(df.groupby("City")["Sales"].sum())

print("\nAverage Sales by City:")
print(df.groupby("City")["Sales"].mean())

print("\nSales by Product:")
print(df.groupby("Product")["Sales"].sum())

print("\nHighest Sales:")
print(df.sort_values("Sales", ascending=False).head(1))