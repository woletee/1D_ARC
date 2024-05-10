import React, { useState } from 'react';
import axios from 'axios';

function Generate() {
    const [generatedData, setGeneratedData] = useState(null);
    const [error, setError] = useState('');

    const handleSubmit = async () => {
        try {
            const response = await axios.get('http://localhost:5000/generate');
            const { outputs, random_array } = response.data;
            setGeneratedData({ outputs, random_array });
            setError('');
        } catch (error) {
            console.error('Error during generation:', error.response ? error.response.data : error.message);
            setError(`Error generating data: ${error.response ? error.response.data : error.message}`);
            setGeneratedData(null);
        }
    };

    return (
        <div className="generate-container">
            <h1>Generated 1D</h1>
            <button onClick={handleSubmit}>Generate Output</button>
            {generatedData && (
                <div>
                    <h2>Random Array</h2>
                    <p>{generatedData.random_array.join(', ')}</p>
                    <h2>Output Results</h2>
                    <ul>
                        {generatedData.outputs.map((output, index) => (
                            <li key={index}>{Array.isArray(output) ? `[${output.join(', ')}]` : output}</li>
                        ))}
                    </ul>
                </div>
            )}
            {error && <p className="error-message">{error}</p>}
        </div>
    );
}

export default Generate;
