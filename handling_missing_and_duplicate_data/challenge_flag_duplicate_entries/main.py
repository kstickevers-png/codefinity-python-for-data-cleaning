import pandas as pd

def flag_duplicates(df):
    df = df.copy()
    df["is_duplicate"] = df.duplicated()
    return df

data = {
    "name": ["Alice", "Bob", "Alice", "Charlie", "Bob"],
    "age": [25, 30, 25, 35, 30]
}
df = pd.DataFrame(data)
df = flag_duplicates(df)
print(df)
