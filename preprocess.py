import pandas as pd
import os

def load_and_preprocess_data():
    # Load Excel files
    df1 = pd.read_excel("gm1.xlsx")
    df2 = pd.read_excel("gm2.xlsx")
    df3 = pd.read_excel("gm3.xlsx")
    df4 = pd.read_excel("gm4.xlsx")
    df5 = pd.read_excel("gm5.xlsx")

    # Combine all data
    df_all = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

    # Clean and normalize
    df_all = df_all.drop_duplicates()
    df_all["text"] = df_all["text"].fillna("").str.lower()
    df_all["title"] = df_all["title"].str.lower()
    df_all["categoryName"] = df_all["categoryName"].str.lower()

    # Save to CSV
    df_all.to_csv("cleaned_restaurants.csv", index=False)
    print("✅ Saved to 'cleaned_restaurants.csv'")

if __name__ == "__main__":
    load_and_preprocess_data()
