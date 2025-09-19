import React, { useState } from "react";
import { Bar, Line, Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  ArcElement,
  Tooltip,
  Legend,
  ArcElement as PieElement,
} from "chart.js";
import ExportButton from "./Exportbutton";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  LineElement,
  PointElement,
  ArcElement,
  Tooltip,
  Legend,
  PieElement
);

export default function ChartView({ chartData }) {
  const [chartType, setChartType] = useState("bar");

  if (!chartData || !chartData.labels || chartData.labels.length === 0) {
    return null;
  }

  const { labels, values } = chartData;

  const formattedData = {
    labels,
    datasets: [{
      label: "Query Result",
      data: values,
      backgroundColor: chartType === "pie"
        ? ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF", "#FF9F40"]
        : "rgba(75,192,192,0.6)"
    }]
  };

  return (
    <div style={{ marginTop: "20px" }}>
      <div style={{ marginBottom: "10px" }}>
        <label>Chart Type: </label>
        <select value={chartType} onChange={(e) => setChartType(e.target.value)}>
          <option value="bar">Bar</option>
          <option value="line">Line</option>
          <option value="pie">Pie</option>
        </select>
      </div>

      {chartType === "bar" && <Bar data={formattedData} />}
      {chartType === "line" && <Line data={formattedData} />}
      {chartType === "pie" && <Pie data={formattedData} />}

      <ExportButton data={labels.map((label, i) => ({
        label,
        value: values[i]
      }))} />
    </div>
  );
}
