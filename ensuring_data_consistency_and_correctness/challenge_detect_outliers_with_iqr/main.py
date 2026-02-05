import pandas as pd

def detect_outliers_iqr(series):
    data = series
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1

# Define outlier bounds
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    

# Flag outliers
    is_outlier = (data < lower_bound) | (data > upper_bound)

    return is_outlier

# Example usage:
data = {
    "score": [10, 12, 13, 14, 15, 16, 17, 18, 100, 110]
}
df = pd.DataFrame(data)
outliers = detect_outliers_iqr(df["score"])
print(outliers)
