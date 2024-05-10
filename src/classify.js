import React, { useState } from 'react';
import './classify.css';
import axios from 'axios';

function Classify() {
    const [inputData, setInputData] = useState(''); // Store input data as a string
    const [outputData, setOutputData] = useState(''); // Store output data as a string
    const [classification, setClassification] = useState(''); // Store the predicted class name

    // Handle changes in the Input textarea
    const handleInputChange = (event) => {
        setInputData(event.target.value);
    };

    // Handle changes in the Output textarea
    const handleOutputChange = (event) => {
        setOutputData(event.target.value);
    };

    const handleSubmit = async (event) => {
      event.preventDefault();
  
      try {
          // Parse the input and output fields to arrays
          const inputArray = JSON.parse(inputData);
          const outputArray = JSON.parse(outputData);
  
          // Prepare data to send to the backend
          const dataToSend = {
              Input: inputArray,
              Output: outputArray
          };
  
          // Send data to the backend for classification
          const response = await axios.post('http://localhost:5000/classify', dataToSend, {
              headers: { 'Content-Type': 'application/json' }
          });
  
          // Display the predicted class from the response
          setClassification(response.data.predicted_class || 'No suitable class found');
      } catch (error) {
          // Log the error and set a more descriptive error message
          console.error('Error during classification:', error.response ? error.response.data : error.message);
          setClassification(`Error predicting class: ${error.response ? error.response.data : error.message}`);
      }
  };
  

    return (
        <div className="classify-container">
            <h1>Classify JSON Data</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="inputData">Input Data (JSON array format):</label>
                <textarea
                    id="inputData"
                    value={inputData}
                    onChange={handleInputChange}
                    placeholder="[5, 5, 5, 5, 5, 5, 0, 0, 0, 0]" // Example placeholder
                    rows="3"
                    cols="50"
                />
                <br />
                <label htmlFor="outputData">Output Data (JSON array format):</label>
                <textarea
                    id="outputData"
                    value={outputData}
                    onChange={handleOutputChange}
                    placeholder="[5, 0, 0, 0, 0, 5, 0, 0, 0, 0]" // Example placeholder
                    rows="3"
                    cols="50"
                />
                <br />
                <button type="submit" className="classify-button">
                    Classify
                </button>
            </form>
            <p>Predicted Class: {classification}</p> {/* Display the predicted class */}
        </div>
    );
}

export default Classify;
