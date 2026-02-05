import pandas as pd

def standardize_column_lowercase(df, column_name):
    new_df = df.copy()
    new_df[column_name] = new_df[column_name].str.lower()
    return new_df

data = {
    "fruit": ["Apple", "banana", "ORANGE", "apple", "Banana", "orange"],
    "quantity": [5, 3, 4, 2, 1, 6]
}
df = pd.DataFrame(data)
result = standardize_column_lowercase(df, "fruit")
print(result)
