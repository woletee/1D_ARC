import random
import csv
import json

# Rule 1 (hollow_array)
def hollow_array(input_array):
    output_array = input_array[:]
    first_non_zero_index = next((i for i, x in enumerate(input_array) if x != 0), None)
    last_non_zero_index = len(input_array) - next((i for i, x in enumerate(input_array[::-1]) if x != 0), None) - 1
    for i in range(first_non_zero_index + 1, last_non_zero_index):
        output_array[i] = 0
    return output_array

# Rule 2 (denoising)
def denoising(input_array):
    non_zero_digits = [digit for digit in input_array if digit != 0]
    digit_counts = {digit: non_zero_digits.count(digit) for digit in set(non_zero_digits)}
    majority_digit = max(digit_counts, key=digit_counts.get)
    total_replaced = sum([count for digit, count in digit_counts.items() if digit != majority_digit])
    output_array = [majority_digit if digit != 0 and digit != majority_digit else digit for digit in input_array]
    return output_array, total_replaced

# Rule 3 (move_pixels)
def move_pixels(arr, distance):
    new_arr = [0] * len(arr)
    for i in range(len(arr)):
        if arr[i] != 0:
            new_position = i + distance
            if new_position < len(arr):
                new_arr[new_position] = arr[i]
    return new_arr

# Rule 4 (1d_Flip)
def detect_flip(input_array, output_array):
    input_nonzero = [val for val in input_array if val != 0]
    output_nonzero = [val for val in output_array if val != 0]
    return input_nonzero[::-1] == output_nonzero

# Rule 5 (1d_scale_dp)
def move_1p(arr):
    new_arr = [0] * len(arr)
    prev_non_zero = None
    
    for i in range(len(arr)):
        if arr[i] != 0:
            prev_non_zero = arr[i]
            new_arr[i] = arr[i]
        elif prev_non_zero is not None:
            if all(val == 0 for val in arr[i:]):
                break
            new_arr[i] = prev_non_zero
    
    return new_arr

# Rule 6 (1d_padded_fill)
def padded_fill(input_list):
    output_list = input_list.copy()
    start_index = None
    for i, num in enumerate(input_list):
        if num != 0:
            if start_index is not None:
                for j in range(start_index + 1, i):
                    output_list[j] = input_list[start_index]
                start_index = None
            else:
                start_index = i
    return output_list

# Rule 7 (1d_move_dp)
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

# Rule 8 (1d_Fill)
def fill_1d(arr):
    if not arr:
        return arr
    output = arr.copy()  # Copy the array to avoid mutating the original data
    start = None
    for i in range(len(arr)):
        if arr[i] != 0:
            if start is not None:
                for j in range(start + 1, i):
                    output[j] = arr[start]
            start = i  # Update start to current non-zero position
    return output

# Generate a random array
def generate_random_array(length):
    return [random.randint(0, 9) for _ in range(length)]  # Assuming digits range from 0 to 9

# Apply rules to a random array
def apply_rules_to_random_array(random_array):
    # Rule 1: Hollow Array
    output_array_rule1 = hollow_array(random_array)
    
    # Rule 2: Denoising
    output_array_rule2, digits_replaced_rule2 = denoising(random_array)
    
    # Rule 3: Move Pixels
    distance = random.randint(1, len(random_array) - 1)  # Choose a random distance
    output_array_rule3 = move_pixels(random_array, distance)
    
    # Rule 4: 1d_Flip
    output_array_rule4 = random_array[::-1]
    
    # Rule 5: 1d_scale_dp
    output_array_rule5 = move_1p(random_array)
    
    # Rule 6: 1d_padded_fill
    output_array_rule6 = padded_fill(random_array)
    
    # Rule 7: 1d_move_dp
    output_array_rule7 = move_dp(random_array)
    
    # Rule 8: 1d_Fill
    output_array_rule8 = fill_1d(random_array)
    
    return (output_array_rule1, output_array_rule2, digits_replaced_rule2, output_array_rule3, output_array_rule4, 
            output_array_rule5, output_array_rule6, output_array_rule7, output_array_rule8, distance)

# Example usage
random_array = generate_random_array(10)  # Generate a random array of length 10
(output_rule1, output_rule2, digits_replaced_rule2, output_rule3, output_rule4, output_rule5, 
 output_rule6, output_rule7, output_rule8, distance) = apply_rules_to_random_array(random_array)

print("Random Array:", random_array)
print("Output Rule 1 (Hollow Array):", output_rule1)
print("Output Rule 2 (Denoising", digits_replaced_rule2, "digit(s)):", output_rule2)
print("Output Rule 3 (Move", distance, "Pixels):", output_rule3)
print("Output Rule 4 (1d_Flip):", output_rule4)
print("Output Rule 5 (1d_scale_dp):", output_rule5)
print("Output Rule 6 (1d_padded_fill):", output_rule6)
print("Output Rule 7 (1d_move_dp):", output_rule7)
print("Output Rule 8 (1d_Fill):", output_rule8)