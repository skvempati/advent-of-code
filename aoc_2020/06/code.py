
def get_unique(group):
    people = group.split('\n')
    unique_char = ''.join(set(''.join(set(people))))
    return len(unique_char)
    
def get_yes(group):
    people = group.split('\n')
    yes_q = set(people[0]).intersection(*people[1:])
    return len(yes_q)

with open('input.txt') as f:
    input = f.read()

input = input.split('\n\n')

count = 0
yes_count = 0
for group in input:
    count += get_unique(group)
    yes_count += get_yes(group)

print('Part 2: {}'.format(count))
print('Part 2: {}'.format(yes_count))


