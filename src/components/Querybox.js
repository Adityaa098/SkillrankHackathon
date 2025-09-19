import React, { useState } from "react";
import axios from "axios";
import ChartView from "./Chartview";

export default function Querybox() {
  const [question, setQuestion] = useState("");
  const [results, setResults] = useState([]);
  const [columns, setColumns] = useState([]);
  const [sql, setSql] = useState("");
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const [chartData, setChartData] = useState(null);

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await axios.post("http://localhost:8000/query", { question });

      const { sql, columns, results } = res.data;

      setSql(sql || "");
      setColumns(Array.isArray(columns) ? columns : []);
      setResults(Array.isArray(results) ? results : []);

      if (sql.startsWith("Error:")) {
        setError(sql);
        setChartData(null);
      } else if (Array.isArray(results) && results.length > 0 && results[0].length >= 2) {
        const labels = results.map(row => row[0]);
        const values = results.map(row => row[1]);
        setChartData({ labels, values });
      } else {
        setChartData(null);
      }
    } catch (err) {
      console.error("Query failed:", err);
      setError("Failed to fetch results. Please try again.");
      setResults([]);
      setColumns([]);
      setSql("");
      setChartData(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Ask a Question</h2>
      <input
        type="text"
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="e.g. Show top 5 customers by revenue"
        style={{ width: "400px", padding: "8px", marginRight: "10px" }}
      />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Running..." : "Run Query"}
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}
      {!error && sql && <p><strong>SQL:</strong> {sql}</p>}

      {Array.isArray(results) && results.length > 0 && columns.length > 0 && (
        <table style={{ marginTop: "20px", borderCollapse: "collapse" }}>
          <thead>
            <tr>
              {columns.map((col) => (
                <th key={col} style={{ border: "1px solid #ccc", padding: "8px" }}>{col}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {results.map((row, i) => (
              <tr key={i}>
                {row.map((val, j) => (
                  <td key={j} style={{ border: "1px solid #ccc", padding: "8px" }}>{val}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      )}

      {chartData && (
        <div style={{ marginTop: "40px" }}>
          <ChartView chartData={chartData} />
        </div>
      )}
    </div>
  );
}
