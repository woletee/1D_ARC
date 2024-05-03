import React from "react";
import "./NavigationTabs.css"; // Adjust the path as needed if the CSS file is not in the same directory

function Navbar({ onTabClick }) {
  return (
    <nav className="navbar" role="navigation">
      <div className="logo">1D ARC</div>
      <ul className="nav-links">
        <li>
          <a
            href="#classify"
            onClick={() => onTabClick("Classify")}
            role="button"
          >
            Classify
          </a>
        </li>
        <li>
          <a
            href="#generate"
            onClick={() => onTabClick("Generate")}
            role="button"
          >
            Generate
          </a>
        </li>
        <li>
          <a
            href="#get_output"
            onClick={() => onTabClick("Get output")}
            role="button"
          >
            Get output
          </a>
        </li>
      </ul>
    </nav>
  );
}

export default Navbar;
