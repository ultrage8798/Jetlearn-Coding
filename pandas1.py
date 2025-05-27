import pandas as pd

df = pd.DataFrame({
    "Name": ["Vikram Nair", "Tom Brouwers"],
    "Age": [12,14],
    "City": ["SLC", "Amsterdam"]
})

#print(df.head(1))
#print(df.info())
#print(df.describe())
#print(df["Name"])
#print(df["Age"].max())
#print(type(df["Age"]))
#print(df["Age"].shape)

data = pd.read_csv("titanic.csv")
print(data.head())
#print(data.info())