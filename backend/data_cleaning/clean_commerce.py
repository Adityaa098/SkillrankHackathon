import pandas as pd

df = pd.read_csv(r"E:\SkillRankHackathon\backend\datasets\E-commerce_dataset.csv", encoding="ISO-8859-1")

df = df.dropna()

df = df.drop_duplicates()

if "Quantity" in df.columns and "Price per Unit" in df.columns:
    df["TotalPrice"] = df["Quantity"] * df["Price per Unit"]
else:
    df["TotalPrice"] = df["Quantity"] * 10  


df.to_csv(r"E:\SkillRankHackathon\backend\db\ecommerce_clean.csv", index=False)