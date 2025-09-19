import React, { useEffect, useState } from "react";
import axios from "axios";

export default function KPIboard() {
  const [kpis, setKpis] = useState({ revenue: 0, orders: 0, customers: 0 });

  useEffect(() => {
    axios.get("http://localhost:8000/kpi").then((res) => {
      setKpis(res.data);
    });
  }, []);

  return (
    <div className="kpi-board">
      <div className="kpi-card">
        <h3>Revenue</h3>
        <p>₹{kpis.revenue.toLocaleString()}</p>
      </div>
      <div className="kpi-card">
        <h3>Orders</h3>
        <p>{kpis.orders.toLocaleString()}</p>
      </div>
      <div className="kpi-card">
        <h3>Customers</h3>
        <p>{kpis.customers.toLocaleString()}</p>
      </div>
    </div>
  );
}
