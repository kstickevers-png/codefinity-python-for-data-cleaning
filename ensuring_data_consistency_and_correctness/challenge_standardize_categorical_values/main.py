import pandas as pd

def standardize_column_case(df, column_name):
    df = df.copy()
    df[column_name] = df[column_name].str.lower()
    return df

data = {
    "Response": ["Yes", "no", "YES", "No", "yes", "NO", "nO", "YeS"]
}
df = pd.DataFrame(data)
result = standardize_column_case(df, "Response")
print(result)
