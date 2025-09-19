import React from "react";
import QueryBox from "./components/Querybox";
import KPIBoard from "./components/KPIboard";
import ChartView from "./components/Chartview";
import "./App.css";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Natural Language to SQL Dashboard</h1>
        <QueryBox />
        <KPIBoard />
        <ChartView />
      </header>
    </div>
  );
}

export default App;
