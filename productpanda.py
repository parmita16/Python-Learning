import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Laptop", "Phone", "Watch"],
    "Price": [80000, 50000, 40000, 75000, 55000, 15000],
    "Quantity": [2, 5, 3, 1, 4, 10]
}

df = pd.DataFrame(data)

print("Product Data:")
print(df)

# Calculate total revenue
df["Revenue"] = df["Price"] * df["Quantity"]

print("\nRevenue:")
print(df)

print("\nTotal Revenue:")
print(df["Revenue"].sum())

print("\nAverage Price:")
print(df["Price"].mean())

print("\nProducts with price greater than 50000:")
print(df[df["Price"] > 50000])

print("\nProducts sorted by revenue:")
print(df.sort_values("Revenue", ascending=False))

print("\nTop 2 products by revenue:")
print(df.sort_values("Revenue", ascending=False).head(2))