import React, { useState } from "react";
import "./classify.css";
import GridVisualization from "./GridVisualization";
import Function from "./rules"; // Import the Function component

function Classify() {
  const [fileData, setFileData] = useState("");
  const [classification, setClassification] = useState("");
  const [jsonData, setJsonData] = useState(null);
  const [fileName, setFileName] = useState("");

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file && file.type === "application/json") {
      const reader = new FileReader();
      reader.onload = (e) => {
        setFileData(e.target.result);
        console.log("File Data Loaded:", e.target.result);
        try {
          const parsedData = JSON.parse(e.target.result);
          setJsonData(parsedData);
          setFileName(file.name);
        } catch (error) {
          console.error("Error parsing JSON:", error);
          setJsonData(null);
          setFileName("");
        }
      };
      reader.readAsText(file);
    } else {
      alert("Please upload a valid JSON file.");
    }
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("File Data Submitted:", fileData);
    if (jsonData) {
      const classificationIsCorrect = Function.checkClassification(jsonData);
      setClassification(classificationIsCorrect ? "correct" : "incorrect");
    } else {
      alert("Please upload a JSON file first.");
    }
  };

  return (
    <div className="classify-container">
      <h1>Classify JSON Data</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="fileInput">Upload JSON File:</label>
        <input
          id="fileInput"
          type="file"
          accept=".json,application/json"
          onChange={handleFileChange}
          aria-label="Upload JSON file for classification"
        />
        {jsonData && (
          <div>
            <h2>{fileName}</h2>
            <GridVisualization data={jsonData.train[0].input} /> {/* Adjust this based on your JSON structure */}
          </div>
        )}
        <button type="submit" className="classify-button">
          Classify
        </button>
      </form>
      <p>Classification: {classification}</p>
    </div>
  );
}

export default Classify;
