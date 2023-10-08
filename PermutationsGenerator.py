# PermutationsGenerator.py

from itertools import permutations

def generate_permutations(nums):
    # Use itertools.permutations to generate all permutations
    permutations_list = list(permutations(nums))
    
    # Convert tuples to lists
    permutations_list = [list(perm) for perm in permutations_list]
    
    return permutations_list

# Example usage:
nums = [1, 2, 3]
permutations_result = generate_permutations(nums)
for perm in permutations_result:
    print(perm)
