import re


def check_valid(passport):

    required = ['byr', 'iyr', 'eyr', 'hgt',
                'hcl', 'ecl', 'pid', 'cid']
    ecl_required = ['amb', 'blu', 'brn', 'gry', 
                'grn', 'hzl', 'oth']

    p_dict = {p.split(':')[0]: p.split(':')[1] for p in passport}

    valid_fields = [True]
    valid = False

    if 'cid' not in p_dict.keys():
        p_dict['cid'] = 0

    if sorted(required) == sorted(p_dict.keys()):
        valid_fields.append(1920 <= int(p_dict['byr']) <= 2002)
        valid_fields.append(2010 <= int(p_dict['iyr']) <= 2020)
        valid_fields.append(2020 <= int(p_dict['eyr']) <= 2030)

        if p_dict['hgt'].endswith('cm'):
            valid_fields.append(150 <= int(p_dict['hgt'].strip('cm')) <= 193)
        else:
            valid_fields.append(59 <= int(p_dict['hgt'].strip('in')) <= 76)

        valid_fields.append(bool(re.match(r"^#[a-f0-9]{6}$", p_dict['hcl'])))
        valid_fields.append(p_dict['ecl'] in ecl_required)
        valid_fields.append(bool(re.match(r"^[0-9]{9}$", p_dict['pid'])))
        

    if sum(valid_fields) == len(required):
        valid = True

    return valid


with open('input.txt') as f:
    batch = f.read()

# format passports
batch = batch.split('\n\n')
batch = [re.split("[' '|'\n']", b) for b in batch]

### Part 1 ###
count = 0
for p in batch:
    if check_valid(p):
        count += 1
print('Part 1: {} valid passports'.format(count))

### Part 2 ###
count = 0
for p in batch:
    if check_valid(p):
        count += 1
print('Part 1: {} valid passports'.format(count))
