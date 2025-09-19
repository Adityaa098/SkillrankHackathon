import pandas as pd

df = pd.read_csv(r"E:\SkillRankHackathon\backend\datasets\customer_dataset.csv", encoding="ISO-8859-1")

df = df.dropna(subset=[
    "NumWebVisitsMonth", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5", "AcceptedCmp1", "AcceptedCmp2",
    "Complain", "Z_CostContact", "Z_Revenue", "Response", "Age", "Customer_Days",
    "marital_Divorced", "marital_Married", "marital_Single", "marital_Together", "marital_Widow",
    "education_2n Cycle", "education_Basic", "education_Graduation", "education_Master", "education_PhD",
    "MntTotal", "MntRegularProds", "AcceptedCmpOverall"
])

df = df.drop_duplicates()

df["Age"] = df["Age"].astype(int)
df["Customer_Days"] = df["Customer_Days"].astype(int)

df.to_csv(r"E:\SkillRankHackathon\backend\db\marketing_clean.csv", index=False)

