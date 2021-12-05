 
def count_trees(tree_map, rise = 1, run = 3):
    """Count trees! """
    tree_count = 0
    position = 0
    row = 0

    while row < len(tree_map):
        if tree_map[row][position] == '#':
            tree_count += 1
        row += rise
        position += run

    return tree_count


## read!
with open('input.txt', 'r') as f:
    tree_map = f.read()

tree_map = tree_map.splitlines()

# make the pattern repeat
tree_map = [row*len(tree_map) for row in tree_map]

### Part 1 ###
print('Part 1: ', count_trees(tree_map, 1, 3))


### Part 2 ###
slope_list = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
slope_result = 1
for s in slope_list:
    slope_result *= count_trees(tree_map, s[0], s[1])

print('Part 2: ', slope_result)
