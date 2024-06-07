import openpyxl

def read_truth_table(filename, sheetname):
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook[sheetname]
    truth_table = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # Skip the header row
        truth_table.append(list(row))
    return truth_table

def decimal_to_binary(n, num_vars):
    return bin(n)[2:].zfill(num_vars)

def binary_to_decimal(b):
    return int(b, 2)

def get_minterms(truth_table):
    minterms = []
    for row in truth_table:
        if row[-1] == 1:
            minterm = ''.join(map(str, row[:-1]))
            minterms.append(minterm)
    return minterms

def find_prime_implicants(minterms):
    num_vars = len(minterms[0])
    prime_implicants = []
    unchecked = set(minterms)

    while unchecked:
        new_implicants = set()
        checked = set()
        for a in unchecked:
            for b in unchecked:
                if a != b:
                    diff = sum(1 for x, y in zip(a, b) if x != y)
                    if diff == 1:
                        new_implicant = ''.join(x if x == y else '-' for x, y in zip(a, b))
                        new_implicants.add(new_implicant)
                        checked.add(a)
                        checked.add(b)
        prime_implicants.extend(unchecked - checked)
        unchecked = new_implicants

    return prime_implicants

def is_covered(minterm, implicant):
    return all(m == i or i == '-' for m, i in zip(minterm, implicant))

def find_essential_prime_implicants(minterms, prime_implicants):
    essential_prime_implicants = []

    for minterm in minterms:
        covers = [pi for pi in prime_implicants if is_covered(minterm, pi)]
        if len(covers) == 1:
            essential_prime_implicants.append(covers[0])

    return list(set(essential_prime_implicants))

def simplify_boolean_expression(filename, sheetname):
    truth_table = read_truth_table(filename, sheetname)
    minterms = get_minterms(truth_table)
    prime_implicants = find_prime_implicants(minterms)
    essential_prime_implicants = find_essential_prime_implicants(minterms, prime_implicants)

    return essential_prime_implicants

def display_expression(implicants):
    num_vars = len(implicants[0])
    variables = [chr(i) for i in range(97, 97 + num_vars)]  # a, b, c, ...
    
    terms = []
    for implicant in implicants:
        term = []
        for var, bit in zip(variables, implicant):
            if bit == '0':
                term.append(f"¬{var}")
            elif bit == '1':
                term.append(var)
        terms.append(' ∧ '.join(term))
    
    return ' ∨ '.join(f'({term})' for term in terms)

# 使用示例
file_path = 'D:\Desktop\github\大二下\离散数学(1)\python\score\真值表.xlsx' 
sheet_name = '10-vars'  
essential_prime_implicants = simplify_boolean_expression(file_path, sheet_name)
simplified_expression = display_expression(essential_prime_implicants)
print("Simplified Boolean Expression:", simplified_expression)
