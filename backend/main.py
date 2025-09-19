from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from llm_utils import generate_sql
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/query")
async def query(request: Request):
    data = await request.json()
    question = data.get("question", "")
    sql = generate_sql(question)
    print("Generated SQL:", sql)

    conn = sqlite3.connect(r"E:\SkillRankHackathon\backend\db\database.db")
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        result = cursor.fetchall() or []
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
    except Exception as e:
        result = []
        columns = []
        sql = f"Error: {str(e)}"

    conn.close()
    return {"sql": sql, "columns": columns, "results": result}

@app.get("/chart")
def get_chart(chart_type: str, metric: str, group_by: str):
    conn = sqlite3.connect(r"E:\SkillRankHackathon\backend\db\database.db")
    cursor = conn.cursor()

    
    metric_map = {
        "revenue": "TotalPrice",
        "orders": "Quantity",
        "customers": "CustomerID"
    }

    group_map = {
        "category": '"Product Category"',
        "country": "Country",
        "customer": "CustomerID"
    }

    metric_col = metric_map.get(metric, "TotalPrice")
    group_col = group_map.get(group_by, group_by)

    try:
        query = f"""
            SELECT {group_col} AS label, SUM({metric_col}) AS value
            FROM ecommerce
            GROUP BY {group_col}
            ORDER BY value DESC
            LIMIT 10;
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        data = [{"label": row[0], "value": row[1]} for row in rows if row[0] is not None]
    except Exception as e:
        print("Chart error:", e)
        data = []

    conn.close()
    return data



@app.get("/kpi")
def get_kpis():
    conn = sqlite3.connect(r"E:\SkillRankHackathon\backend\db\database.db")
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT SUM("TotalPrice") FROM ecommerce')
        revenue = cursor.fetchone()[0] or 0

        cursor.execute('SELECT COUNT(*) FROM ecommerce')
        orders = cursor.fetchone()[0] or 0

        cursor.execute('SELECT COUNT(DISTINCT "Customer ID") FROM retail')
        customers = cursor.fetchone()[0] or 0
    except Exception as e:
        revenue, orders, customers = 0, 0, 0
        print("KPI error:", e)

    conn.close()
    return {"revenue": revenue, "orders": orders, "customers": customers}
