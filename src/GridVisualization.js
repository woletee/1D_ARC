import React from "react";
import "./gridVisualization.css";

function GridVisualization({ data }) {
  // Define a function to map cell values to colors
  const getColor = (value) => {
    switch (value) {
      case 0:
        return "#000000"; // Black
      case 1:
        return "#0074D9"; // Blue
      case 2:
        return "#FF4136"; // Red
      case 3:
        return "#2ECC40"; // Green
      case 4:
        return "#FFDC00"; // Yellow
      case 5:
        return "#AAAAAA"; // Gray
      case 6:
        return "#F012BE"; // Pink
      case 7:
        return "#FF851B"; // Orange
      case 8:
        return "#7FDBFF"; // Sky Blue
      case 9:
        return "#870C25"; // Maroon
      default:
        return "#FFFFFF"; // White for unknown values
    }
  };

  return (
    <div className="grid-container">
      {data.map((row, rowIndex) => (
        <div className="grid-row" key={rowIndex}>
          {row.map((cell, colIndex) => (
            <div
              className="grid-cell"
              key={colIndex}
              style={{ backgroundColor: getColor(cell) }}
            ></div>
          ))}
        </div>
      ))}
    </div>
  );
}

export default GridVisualization;
