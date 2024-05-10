import numpy as np
import numpy as np

# Define rules that we have 
def move_dp(arr):
  
    if not arr:
        return arr
    new_arr = [0] * len(arr)
    non_zeros = [x for x in arr if x != 0]
    last_non_zero_idx = len(arr) - 1
    while last_non_zero_idx >= 0 and arr[last_non_zero_idx] == 0:
        last_non_zero_idx -= 1
    start_index = last_non_zero_idx + 1 - len(non_zeros)
    for i in range(start_index, start_index + len(non_zeros)):
        new_arr[i] = non_zeros.pop(0) if non_zeros else 0
    return new_arr
def move_3p(arr):
    if not arr:
        return arr
    n = len(arr)
    new_arr = [0] * n
    for i in range(n):
        if arr[i] != 0:
            new_position = i + 3  # Changed from +2 to +3
            if new_position < n:
                new_arr[new_position] = arr[i]
    return new_arr
def denoising_1c(input_array):
    output_array = input_array[:]
    for i in range(len(input_array)):
        if input_array[i] != 0 and (i == 0 or input_array[i - 1] == 0) and (i == len(input_array) - 1 or input_array[i + 1] == 0):
            output_array[i] = 0
    return output_array

def denoising_mc(input_array):
    non_zero_digits = [digit for digit in input_array if digit != 0]
    if not non_zero_digits:
        return input_array
    digit_counts = {digit: non_zero_digits.count(digit) for digit in set(non_zero_digits)}
    majority_digit = max(digit_counts, key=digit_counts.get)
    output_array = [majority_digit if digit != 0 and digit != majority_digit else digit for digit in input_array]
    return output_array
def move_2p(arr):
   
    if not arr:
        return arr
    n = len(arr)
    new_arr = [0] * n
    for i in range(n):
        if arr[i] != 0:  
            new_position = i + 2  
            if new_position < n:  
                new_arr[new_position] = arr[i]
    return new_arr
def move_2p_dp(arr):
    if not arr:
        return arr
    # Step 1: Move all non-zero elements two positions to the right
    n = len(arr)
    temp_arr = [0] * n
    for i in range(n):
        if arr[i] != 0:
            new_position = i + 2
            if new_position < n:
                temp_arr[new_position] = arr[i]

    # Step 2: Adjust the last isolated non-zero element towards the left group
    new_arr = [0] * n
    last_index = -1  # Track the last index of non-zero group
    i = 0
    while i < n:
        if temp_arr[i] != 0:
            if last_index != -1 and i - last_index > 1:  # Gap found
                # Move the non-zero value at 'i' next to the last group
                new_arr[last_index + 1] = temp_arr[i]
                temp_arr[i] = 0
            start = i
            # Process current block of non-zeros
            while i < n and temp_arr[i] != 0:
                new_arr[i] = temp_arr[i]
                last_index = i
                i += 1
        else:
            i += 1

    return new_arr
def move_1p(arr):
    if not arr:
        return arr
    
    new_arr = [0] * len(arr)
    
    for i in range(len(arr) - 1, 0, -1):
        if arr[i - 1] != 0:
            new_arr[i] = arr[i - 1]
    
    if len(arr) > 1 and arr[0] != 0:
        new_arr[1] = arr[0]
    
    return new_arr
def  d_scale_dp(arr):
    """
    Shifts each non-zero element in the array one position to the right and fills the next pixels with the non-zero number encountered until another non-zero number is found. Then stops filling until another non-zero pixel is encountered.
    """
    if not arr:
        return arr
    
    new_arr = [0] * len(arr)
    prev_non_zero = None
    
    for i in range(len(arr)):
        if arr[i] != 0:
            prev_non_zero = arr[i]
            new_arr[i] = arr[i]
        elif prev_non_zero is not None:
            # If there are no more non-zero values after the last non-zero value encountered,
            # stop filling and leave the pixel values as they are
            if all(val == 0 for val in arr[i:]):
                break
            new_arr[i] = prev_non_zero
    
    return new_arr
def hollow_array(input_array):
    # Initialize the output array with the same elements as the input array
    output_array = input_array[:]
    
    # Get the first non-zero element index
    first_non_zero_index = next((i for i, x in enumerate(input_array) if x != 0), None)
    
    # Get the last non-zero element index
    last_non_zero_index = len(input_array) - next((i for i, x in enumerate(input_array[::-1]) if x != 0), None) - 1
    
    # Set all elements to 0 except for the first and last non-zero elements
    for i in range(first_non_zero_index + 1, last_non_zero_index):
        output_array[i] = 0
    
    return output_array
def padded_fill(input_list):
    output_list = input_list.copy()
    start_index = None
    end_index = None
    for i, num in enumerate(input_list):
        if num != 0:
            
            if start_index is not None:
                for j in range(start_index + 1, i):
                    output_list[j] = input_list[start_index]
                start_index = None
            else:
                start_index = i
    return output_list

def pcopy_mc(input_sequence):
    output_sequence = input_sequence.copy()
    for i in range(len(input_sequence)):
        if input_sequence[i] != 0:
            # Check if the current number is part of a sequence
            if input_sequence[i] == input_sequence[i-1] and input_sequence[i] == input_sequence[i+1]:
                pass
            elif input_sequence[i+1] == 0 and input_sequence[i-1] == 0:
                output_sequence[i-1]=input_sequence[i]
                output_sequence[i+1]=input_sequence[i]
    return output_sequence
def move_2p_dp(arr):
    if not arr:
        return arr
    # Step 1: Move all non-zero elements two positions to the right
    n = len(arr)
    temp_arr = [0] * n
    for i in range(n):
        if arr[i] != 0:
            new_position = i + 2
            if new_position < n:
                temp_arr[new_position] = arr[i]

    # Step 2: Adjust the last isolated non-zero element towards the left group
    new_arr = [0] * n
    last_index = -1  # Track the last index of non-zero group
    i = 0
    while i < n:
        if temp_arr[i] != 0:
            if last_index != -1 and i - last_index > 1:  # Gap found
                # Move the non-zero value at 'i' next to the last group
                new_arr[last_index + 1] = temp_arr[i]
                temp_arr[i] = 0
            start = i
            # Process current block of non-zeros
            while i < n and temp_arr[i] != 0:
                new_arr[i] = temp_arr[i]
                last_index = i
                i += 1
        else:
            i += 1

    return new_arr
def pcopy_1c(input_sequence):
    output_sequence = input_sequence.copy()
    index = None  # Initialize index to None
    for i in range(1, len(input_sequence) - 1):  # Start from 1 and end at len - 1 to safely access i-1 and i+1
        if input_sequence[i] != 0:
            # Check if the current number is part of a sequence
            if input_sequence[i] == input_sequence[i - 1] and input_sequence[i] == input_sequence[i + 1]:
                index = i  # Only update index if current number is part of a sequence
            elif input_sequence[i + 1] == 0 and input_sequence[i - 1] == 0 and index is not None:
                # Only modify neighbors if index has been assigned a valid number
                output_sequence[i - 1] = input_sequence[index]
                output_sequence[i + 1] = input_sequence[index]
    return output_sequence
def fill_1d(arr):
    if not arr:
        return arr
    output = arr.copy()  # Copy the array to avoid mutating the original data

    # Initialize variables to track the start and end indices of the fill operation
    start = None

    for i in range(len(arr)):
        if arr[i] != 0:
            if start is not None:
                # If start is set and we encounter a non-zero, fill up to the current position
                for j in range(start + 1, i):
                    output[j] = arr[start]
            start = i  # Update start to current non-zero position

    return output
def flipped(input_array):
    # Extract non-zero elements from input array
    input_nonzero = [val for val in input_array if val != 0]

    # Reverse the list of non-zero elements
    flipped_nonzero = input_nonzero[::-1]

    # Replace non-zero elements in the original input array with flipped values
    flipped_output = input_array[:]  # Create a copy to avoid modifying the original array
    j = 0  # Index for flipped_nonzero list
    for i in range(len(flipped_output)):
        if flipped_output[i] != 0:
            flipped_output[i] = flipped_nonzero[j]
            j += 1

    return flipped_output

# Define the fitness function
def fitness_function(rule, data):
    input_array = data['Input']
    expected_output_array = data['Output']

    output_array = rule(input_array)

    correct_predictions = sum(1 for pred, expected in zip(output_array, expected_output_array) if pred == expected)

    return correct_predictions

# Genetic Algorithm
def genetic_algorithm(data, rules, population_size=100, num_generations=100, mutation_rate=0.1):
    population = np.random.randint(len(rules), size=(population_size,))
    best_rule = None

    for generation in range(num_generations):
        fitness_scores = [fitness_function(rules[chromosome], data) for chromosome in population]

        if np.all(np.array(fitness_scores) == 0):
            print("No rule found for the given data.")
            return None

        selected_indices = np.random.choice(population_size, size=population_size, replace=True, p=fitness_scores/np.sum(fitness_scores))

        for i in range(len(selected_indices)):
            if np.random.random() < mutation_rate:
                population[selected_indices[i]] = np.random.randint(len(rules))

        best_rule_index = population[np.argmax(fitness_scores)]
        best_rule = rules[best_rule_index]

    # Check if the best rule produces the expected output
    output_array = best_rule(data['Input'])
    if output_array != data['Output']:
        print("No suitable rule found.")
        return None
    return best_rule
if __name__ == "__main__":
    sample_data = {
        'Input': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]	,
        'Output':[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    }

    rules = [denoising_1c, denoising_mc, move_1p,move_3p,move_2p_dp,pcopy_1c,move_dp,move_2p,hollow_array,d_scale_dp,padded_fill,pcopy_mc,fill_1d,flipped]

    best_rule = genetic_algorithm(sample_data, rules)
    if best_rule:
        print("Best rule:", best_rule.__name__)
