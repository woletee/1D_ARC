import React, { useState } from "react";
import Navbar from "./Navbar";
import Classify from "./classify";

function App() {
  const [activeTab, setActiveTab] = useState("Classify"); // Default tab

  // Function to update the active tab
  const handleTabClick = (tabName) => {
    setActiveTab(tabName);
  };

  return (
    <div className="App">
      <Navbar onTabClick={handleTabClick} />
      {activeTab === "Classify" && <Classify />}
      {activeTab === "Generate" && <div>Generate tab content here.</div>}
      {activeTab === "Get output" && (
        <div>Output results will be shown here.</div>
      )}
    </div>
  );
}

export default App;
