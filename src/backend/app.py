from flask import Flask, request, jsonify
from genetic_algorithm import genetic_algorithm, denoising_1c, denoising_mc, move_1p, move_3p, move_2p_dp, pcopy_1c, move_dp, move_2p, hollow_array, d_scale_dp, padded_fill, pcopy_mc, fill_1d, flipped
from generate import generate_random_array
from generate import apply_rules_to_random_array
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  
@app.route('/')
def home():
    return "Welcome to the Classification API. Use POST /classify to classify data."
@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json()

    # Check if data is provided and has required fields
    if not data or 'Input' not in data or 'Output' not in data:
        return jsonify({'error': 'Invalid data format'}), 400

    # Rules available for genetic algorithm
    rules = [denoising_1c, denoising_mc, move_1p, move_3p, move_2p_dp, pcopy_1c, move_dp, move_2p, hollow_array, d_scale_dp, padded_fill, pcopy_mc, fill_1d, flipped]

    try:
        best_rule = genetic_algorithm(data, rules)
        if best_rule:
            return jsonify({'predicted_class': best_rule.__name__})
        else:
            return jsonify({'predicted_class': 'No suitable rule found'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

from flask import Flask, request, jsonify
import numpy as np  # Assuming numpy is used to generate random arrays and other operations

app = Flask(__name__)
CORS(app)  
def generate_random_array(size):
    return np.random.randint(0, 100, size)  # Generating random integers between 0 and 99

# Dummy rule functions, you need to implement these according to your requirements
def denoising_1c(arr): return arr
def denoising_mc(arr): return arr
def move_1p(arr): return arr
def move_3p(arr): return arr
def move_2p_dp(arr): return arr
def pcopy_1c(arr): return arr
def move_dp(arr): return arr
def move_2p(arr): return arr
def hollow_array(arr): return arr
def d_scale_dp(arr): return arr
def padded_fill(arr): return arr
def pcopy_mc(arr): return arr
def fill_1d(arr): return arr
def flipped(arr): return arr

def apply_rules_to_random_array(random_array):
    # Example function to apply rules and return results, needs real implementations
    return (
        denoising_1c(random_array),
        denoising_mc(random_array),
        len(str(random_array)),  # Example for digits replaced in rule 2
        move_1p(random_array),
        move_3p(random_array),
        move_2p_dp(random_array),
        pcopy_1c(random_array),
        move_dp(random_array),
        move_2p(random_array),
        np.linalg.norm(random_array)  # Example for calculating distance
    )

@app.route('/generate', methods=['GET'])
def generate():
    random_array = generate_random_array(10)  # Generates a random array of size 10

    # Assuming this function call works with your real implementation of rules
    results = apply_rules_to_random_array(random_array)

    return jsonify({
        "random_array": random_array.tolist(),  # Convert numpy array to list for JSON serialization
        "outputs": [result.tolist() if isinstance(result, np.ndarray) else result for result in results]
    })

if __name__ == '__main__':
    app.run(debug=True)



if __name__ == '__main__':
    app.run(debug=True)