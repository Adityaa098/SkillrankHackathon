import requests
import re

OLLAMA_URL = "http://localhost:11434/api/generate"

def clean_sql(raw_output):
    cleaned = re.sub(r"```sql|```", "", raw_output).strip()
    cleaned = re.sub(r"\bT\d+\.", "", cleaned)  
    cleaned = cleaned.split(";")[0] + ";" if ";" in cleaned else cleaned
    return cleaned.strip()

def generate_sql(question):
    prompt = (
        "You are a SQL assistant. Convert the following question into a SQL query using only valid SQL syntax. "
        "Do not include explanations, comments, Markdown formatting, or unnecessary table aliases. Use only the columns listed below. "
        "If a column name contains spaces, wrap it in double quotes.\n\n"

        "ecommerce: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country, TotalPrice\n"
        "retail: Transaction, ID, Date,Customer ID, Gender, Age,Product Category, Quantity,Price per Unit,Total Amount\n"
        "marketing: Income, Kidhome, Teenhome, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, "
        "NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, "
        "AcceptedCmp1, AcceptedCmp2, Complain, Z_CostContact, Z_Revenue, Response, Age, Customer_Days, marital_Divorced, marital_Married, marital_Single, "
        "marital_Together, marital_Widow, education_2n Cycle, education_Basic, education_Graduation, education_Master, education_PhD, MntTotal, "
        "MntRegularProds, AcceptedCmpOverall\n\n"

        f"Question: {question}\nSQL:"
    )

    response = requests.post(OLLAMA_URL, json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })

    if response.status_code == 200:
        try:
            raw_output = response.json().get("response", "")
            if not raw_output:
                return "-- Error: Empty response from model"
            return clean_sql(raw_output)
        except Exception as e:
            return f"-- Error parsing response: {str(e)}"
    else:
        return f"-- Error from Ollama: {response.text}"
