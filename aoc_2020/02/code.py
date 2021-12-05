
def load_data(filepath):
    """Loads input expense data and returns a list"""
    with open(filepath, 'r') as f:
        input = f.readlines()
        input = [w.rstrip() for w in input]
    return input

def check_valid_1(row):
    """Check if the password is valid according to the policy in each row - Part 1"""
    policy, password = row.split(': ')
    letter = policy.split(' ')[1]
    min_num, max_num = policy.split(' ')[0].split('-')
    
    return password.count(letter) >= int(min_num) and password.count(letter) <= int(max_num)

def check_valid_2(row):
    """Check if the password is valid according to the policy in Part 2"""
    policy, password = row.split(': ')
    letter = policy.split(' ')[1]
    start, end = policy.split(' ')[0].split('-')
  
    return((password[int(start)-1] == letter) != (password[int(end)-1] == letter))
    

if __name__ == "__main__":

    input = load_data('input.txt')

    print("Part 1: ")
    counter = 0
    for l in input:
        if check_valid_1(l):
            counter = counter+1
    print(counter)

    print("\nPart 2: ")
    counter = 0
    for l in input:
        if check_valid_2(l):
            counter = counter+1
    print(counter)

