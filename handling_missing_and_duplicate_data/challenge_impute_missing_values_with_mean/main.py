import pandas as pd

def impute_with_mean(df, column):
    df_filled_mean = df.copy()
    df_filled_mean[column] = df_filled_mean[column].fillna(df_filled_mean[column].mean())# Your code here
    return df_filled_mean

# Example usage:
data = {
    "id": [1, 2, 3, 4, 5],
    "score": [85, None, 78, None, 92]
}
df = pd.DataFrame(data)
df_imputed = impute_with_mean(df, "score")
print(df_imputed)
