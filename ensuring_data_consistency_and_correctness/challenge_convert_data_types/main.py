import pandas as pd

def convert_column_to_float(df, column_name):
    df = df.copy()
    df[column_name] = df[column_name].astype(float)
    return df[column_name]

# Example usage:
data = {
    'product': ['A', 'B', 'C'],
    'cost': ['12.5', '9.8', '7.0'],
    'stock': ['100', '200', '150']
}
df = pd.DataFrame(data)

df['cost'] = convert_column_to_float(df, 'cost')
print(df['cost'])
print(df.dtypes)
