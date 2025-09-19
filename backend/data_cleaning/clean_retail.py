import pandas as pd

df = pd.read_csv(r"E:\SkillRankHackathon\backend\datasets\retail_sales_dataset.csv", encoding="ISO-8859-1")

df = df.dropna()
df = df.drop_duplicates()

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

df.to_csv(r"E:\SkillRankHackathon\backend\db\retail_clean.csv", index=False)

