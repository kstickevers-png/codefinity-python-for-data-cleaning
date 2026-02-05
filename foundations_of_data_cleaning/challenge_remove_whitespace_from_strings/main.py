import pandas as pd

def strip_whitespace(df):
    df_cleaned = df.copy()
    for col in df_cleaned.select_dtypes(include="object").columns:
        df_cleaned[col] = df_cleaned[col].str.strip()
    return df_cleaned

data = {
    "Fruit": [" apple", "banana ", "  cherry ", "date"],
    "Color": [" red", "yellow ", " red ", "brown"],
    "Count": [10, 5, 7, 3]
}

df = pd.DataFrame(data)
cleaned_df = strip_whitespace(df)
print(cleaned_df)