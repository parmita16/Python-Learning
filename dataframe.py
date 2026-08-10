import pandas as pd

data = {
    "Name": ["Ram", "Sita", "Hari", "Gita"],
    "Age": [20, 21, 19, 22],
    "Marks": [80, 90, 75, 85]
}

df = pd.DataFrame(data)

print(df)