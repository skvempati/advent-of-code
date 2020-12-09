
def get_row(bd_pass):

    row = range(128)
    length = len(row)

    for i in range(7):
        if bd_pass[i] == 'F':
            length = int(length/2)
            row = row[:length]
        elif bd_pass[i] == 'B':
            length = int(length/2)
            row = row[length:]

    return row[0]



def get_col(bd_pass):

    col = range(8)
    length = len(col)

    for i in range(7, 10):
        if bd_pass[i] == 'L':
            length = int(length/2)
            col = col[:length]
        elif bd_pass[i] == 'R':
            length = int(length/2)
            col = col[length:]

    return col[0]


def get_seat(bd_pass):
    row_num = get_row(bd_pass)
    col_num = get_col(bd_pass)
    seat_id = (row_num*8) + col_num
    return seat_id


with open('input.txt') as f:
    input = f.read()

input = input.split('\n')

### Part 1 ###
seat_list = []
for i in input:
    seat_list.append(get_seat(i))

print(max(seat_list))

### Part 2 ###
max_id = max(seat_list)
min_id = min(seat_list)
print(sorted(set(range(min_id, max_id + 1)).difference(seat_list)))
