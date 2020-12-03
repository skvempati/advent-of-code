"""2020 Advent of Code - Day 1"""

def load_data(filepath):
    """Loads input expense data and returns a list"""
    with open(filepath, 'r') as f:
        input = f.readlines()
        input = [int(w.rstrip()) for w in input]
    return input


def solve1():
    for i in input:
        for j in input:
            if i+j == 2020:
                print(i*j)
                return

def solve2():
   for i in input:
        for j in input:
            for k in input:
                if i+j+k == 2020:
                    print(i*j*k)
                    return

if __name__ == "__main__":
    print('hi!')

    input = load_data('input.txt')
    
    solve1()
    solve2()
