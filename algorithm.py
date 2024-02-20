from itertools import permutations

def find_permutation(input_string):
    permuted_list = list(permutations(input_string))

    permuted_string = [''.join(perm) for perm in permuted_list]

    return permuted_string




input_str = 'SERIOUS'
results = find_permutation(input_str)
print(results)