from itertools import combinations
import numpy as np

# List

names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
# inefficient
better_list = []
for name in names:
    if len(name) >= 6:
        better_list.append(name)
print(better_list)
# efficient
best_list = [name for name in names if len(name) >= 6]
print(best_list)

# Enumerate()

# inefficient
indexed_names = []
for i, name in enumerate(names):
    index_name = (i, name)
    indexed_names.append(index_name)
print(indexed_names)
# efficient
indexed_names_comp = [(i, name) for i, name in enumerate(names)]
print(indexed_names_comp)
# Unpack an enumerate object (even more efficient)
indexed_names_unpack = [*enumerate(names)]
print(indexed_names_unpack)

# Map()

# Use map to apply str.upper to each element in names
names_map = map(str.upper, names)
# Unpack names_map into a list (efficient)
names_uppercase = [*names_map]
print(names_uppercase)

# Combinations()

poke_types = ['Bug', 'Fire', 'Water', 'Grass', 'Ghost']
# eliminating nested loops
combos = [*combinations(poke_types, 2)]
print(combos)

# NumPy Arrays

poke_stats = np.array([
    [90, 92, 75, 60],
    [91, 85, 90, 70],
    [25, 20, 60, 90]
])
# instead of using for loop to calculate the average,
print(poke_stats.mean(axis=1))



