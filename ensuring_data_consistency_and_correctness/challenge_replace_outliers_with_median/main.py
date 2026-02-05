import pandas as pd

def replace_outliers_with_median(df, column, outlier_mask):
   
    # 1) compute median of the non-outliers
    median_value = df.loc[~outlier_mask, column].median()
    # 2) replace only the outlier cells in place
    df.loc[outlier_mask, column] = median_value
    # no return needed

# Example usage
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "score": [85, 90, 300, 88, 92]
}
df = pd.DataFrame(data)
outlier_mask = df["score"] > 150

replace_outliers_with_median(df, "score", outlier_mask)
print(df)
