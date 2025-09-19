import React from "react";

export default function ExportButton({ data }) {
  const handleExport = () => {
    const csv = data.map(d => `${d.label},${d.value}`).join("\n");
    const blob = new Blob([csv], { type: "text/csv" });
    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "chart_data.csv";
    a.click();
  };

  return <button onClick={handleExport}>Export CSV</button>;
}
