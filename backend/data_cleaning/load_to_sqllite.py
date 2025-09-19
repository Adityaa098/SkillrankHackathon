import pandas as pd
import sqlite3

conn = sqlite3.connect(r"E:\SkillRankHackathon\backend\db\database.db")

pd.read_csv(r"E:\SkillRankHackathon\backend\db\ecommerce_clean.csv", encoding="ISO-8859-1").to_sql("ecommerce", conn, index=False, if_exists="replace")
pd.read_csv(r"E:\SkillRankHackathon\backend\db\retail_clean.csv", encoding="ISO-8859-1").to_sql("retail", conn, index=False, if_exists="replace")
pd.read_csv(r"E:\SkillRankHackathon\backend\db\marketing_clean.csv", encoding="ISO-8859-1").to_sql("marketing", conn, index=False, if_exists="replace")

conn.close()
print("All cleaned datasets merged into SQLite.")
