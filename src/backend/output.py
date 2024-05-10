import numpy as np
from genetic_algorithm import genetic_algorithm
#Using our previously created rules and the genetic algorrithm
from genetic_algorithm import denoising_1c, denoising_mc, move_1p,move_3p,move_2p_dp,pcopy_1c,move_dp,move_2p,hollow_array,d_scale_dp,padded_fill,pcopy_mc,fill_1d,flipped

rules = [denoising_1c, denoising_mc, move_1p,move_3p,move_2p_dp,pcopy_1c,move_dp,move_2p,hollow_array,d_scale_dp,padded_fill,pcopy_mc,fill_1d,flipped]

# Example data sets
example_data_sets = [
    {
        'Input': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]	,
        'Output':[4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    },
    {
        'Input':[0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0]	,

        'Output':[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Example expected transformation
    },
    {
        'Input':[0, 0, 4, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'Output': [0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]# Example expected transformation
    }		
]
hidden_test_input = {
    'Input': [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# Apply the genetic algorithm to each example dataset
best_rules = []
for data in example_data_sets:
    best_rule = genetic_algorithm(data, rules)
    if best_rule:
        print(f"Best rule for dataset {example_data_sets.index(data)}: {best_rule.__name__}")
        best_rules.append(best_rule)
    else:
        print(f"No suitable rule found for dataset {example_data_sets.index(data)}")
        best_rules.append(None)

overall_best_rule = next((rule for rule in best_rules if rule is not None), None)

if overall_best_rule:
    predicted_output = overall_best_rule(hidden_test_input['Input'])
    print("Predicted output for hidden test input:", predicted_output)
else:
    print("No effective rule was found for any dataset.")