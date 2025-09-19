import React from "react";

export default function ChartFilters({ chartType, setChartType, metric, setMetric, groupBy, setGroupBy }) {
  return (
    <div className="filters">
      <select value={chartType} onChange={(e) => setChartType(e.target.value)}>
        <option value="bar">Bar</option>
        <option value="line">Line</option>
        <option value="pie">Pie</option>
      </select>

      <select value={metric} onChange={(e) => setMetric(e.target.value)}>
        <option value="revenue">Revenue</option>
        <option value="orders">Orders</option>
        <option value="customers">Customers</option>
      </select>

      <select value={groupBy} onChange={(e) => setGroupBy(e.target.value)}>
        <option value="category">Category</option>
        <option value="month">Month</option>
        <option value="country">Country</option>
      </select>
    </div>
  );
}
