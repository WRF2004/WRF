import pandas as pd
from sympy import  Not, And, Or

import sympy
import sympy.logic

def generate_dnf(result_df, variables):
    expressions = []
    for _, row in result_df.iterrows():
        terms = []
        for var in variables:
            if row[var] == 1:
                terms.append(f'{var}')
            else:
                terms.append(f'¬{var}')
        expressions.append(f'({" ∧ ".join(terms)})')
    return " ∨ ".join(expressions)

def generate_cnf(result_df, variables):
    expressions = []
    for _, row in result_df.iterrows():
        terms = []
        for var in variables:
            if row[var] == 1:
                terms.append(f'¬{var}')
            else:
                terms.append(f'{var}')
        expressions.append(f'({" ∨ ".join(terms)})')
    return " ∧ ".join(expressions)

def count(s):
    special_chars = ['∧', '∨', '¬', '→', '↔', '⊕']
    total = 0
    for char in special_chars:
        total += s.count(char)
    return total

def format_expression(expr):
    expr_str = str(expr)
    expr_str = expr_str.replace('∧', '&')
    expr_str = expr_str.replace('∨', '|')
    expr_str = expr_str.replace('¬', '~')
    return expr_str

file_path = 'D:\Desktop\github\大二下\离散数学(1)\python\score\真值表.xlsx'
file1 = pd.read_excel(file_path, sheet_name='3-vars')
file2 = pd.read_excel(file_path, sheet_name='5-vars')
file3 = pd.read_excel(file_path, sheet_name='10-vars')
result1 = file1[file1['result'] == 1]
result2 = file2[file2['result'] == 1]
result3 = file3[file3['result'] == 1]
print(len(result3))
print(len(result1))
print(len(result2))

result4 = file1[file1['result'] == 0]
result5 = file2[file2['result'] == 0]
result6 = file3[file3['result'] == 0]

variables_3 = list(file1.columns[:-1])
variables_5 = list(file2.columns[:-1])
variables_10 = list(file3.columns[:-1])

dnf_3 = generate_dnf(result1, variables_3)
dnf_5 = generate_dnf(result2, variables_5)
dnf_10 = generate_dnf(result3, variables_10)

cnf_3 = generate_cnf(result4, variables_3)
cnf_5 = generate_cnf(result5, variables_5)
cnf_10 = generate_cnf(result6, variables_10)

print(count(cnf_10))
print(count(dnf_10))
e = str('(a ∧ ¬c ∧ ¬d) ∨ (d ∧ ¬a ∧ ¬e) ∨ (a ∧ b ∧ e ∧ ¬c) ∨ (c ∧ e ∧ ¬a ∧ ¬d) ∨ (a ∧ c ∧ d ∧ e ∧ ¬b)')
print(count(e))


import sympy
from sympy.logic.boolalg import Or, And, Not

# 定义变量
a, b, c, d, e, f, g, h, i, j = sympy.symbols('a b c d e f g h i j')

# 定义表达式 s 和 s1
s = (a & d & e & f & g & h & i) | (c & e & f & h & i & j & ~b) | (a & c & d & f & g & ~b & ~i) | (c & d & f & i & j & ~a & ~g) | (c & e & f & i & j & ~d & ~g) | (e & f & g & h & j & ~d & ~i) | (a & b & c & e & g & h & j & ~f) | (a & b & d & e & f & i & j & ~c) | (b & c & d & f & g & i & j & ~e) | (b & c & d & f & h & i & j & ~a) | (a & c & d & g & ~b & ~e & ~i) | (a & c & e & f & ~b & ~h & ~j) | (b & c & f & i & ~e & ~g & ~h) | (b & e & f & g & ~a & ~d & ~h) | (d & f & g & h & ~b & ~e & ~i) | (a & b & c & e & i & j & ~d & ~h) | (a & b & c & f & g & h & ~d & ~j) | (a & b & d & e & g & h & ~c & ~j) | (a & b & d & e & g & h & ~f & ~i) | (a & b & d & f & h & i & ~g & ~j) | (a & b & e & f & h & i & ~c & ~j) | (a & b & f & g & h & i & ~c & ~d) | (a & c & d & h & i & j & ~f & ~g) | (a & c & e & f & i & j & ~b & ~d) | (a & d & e & g & h & i & ~b & ~c) | (b & c & d & g & i & j & ~a & ~e) | (b & c & g & h & i & j & ~d & ~f) | (b & e & f & h & i & j & ~a & ~g) | (a & b & g & ~c & ~e & ~f & ~h) | (a & b & j & ~c & ~e & ~f & ~i) | (a & d & j & ~b & ~g & ~h & ~i) | (b & f & g & ~a & ~d & ~h & ~j) | (d & h & i & ~b & ~e & ~f & ~g) | (e & f & j & ~a & ~b & ~d & ~i) | (e & h & i & ~a & ~c & ~g & ~j) | (a & b & c & d & j & ~e & ~g & ~h) | (a & b & c & e & f & ~g & ~h & ~i) | (a & b & c & e & i & ~d & ~f & ~j) | (a & b & d & e & f & ~g & ~h & ~i) | (a & b & g & h & i & ~c & ~d & ~j) | (a & c & d & g & j & ~b & ~e & ~f) | (a & c & d & g & j & ~e & ~f & ~i) | (a & c & e & h & j & ~d & ~f & ~i) | (a & c & f & h & j & ~b & ~d & ~e) | (a & d & e & f & g & ~b & ~h & ~j) | (a & d & h & i & j & ~b & ~c & ~e) | (a & e & g & i & j & ~c & ~f & ~h) | (b & c & d & g & i & ~a & ~h & ~j) | (b & c & e & g & i & ~f & ~h & ~j) | (b & d & e & f & h & ~a & ~c & ~i) | (b & d & e & f & i & ~a & ~c & ~g) | (b & e & f & g & j & ~c & ~d & ~i) | (c & d & e & f & g & ~a & ~h & ~j) | (c & d & e & h & j & ~f & ~g & ~i) | (c & d & e & i & j & ~a & ~g & ~h) | (c & d & f & g & i & ~a & ~e & ~j) | (c & d & f & g & i & ~b & ~h & ~j) | (c & d & f & g & j & ~a & ~e & ~i) | (c & d & f & i & j & ~e & ~g & ~h) | (c & e & g & h & i & ~b & ~f & ~j) | (c & e & g & h & j & ~a & ~b & ~d) | (c & g & h & i & j & ~a & ~d & ~e) | (d & e & f & h & i & ~a & ~b & ~g) | (a & b & d & e & h & i & j & ~f & ~g) | (a & c & ~b & ~e & ~g & ~h & ~i) | (c & g & ~a & ~d & ~h & ~i & ~j) | (g & i & ~c & ~d & ~e & ~f & ~h) | (g & j & ~a & ~b & ~c & ~d & ~h) | (i & j & ~b & ~d & ~e & ~f & ~h) | (a & b & c & h & ~e & ~g & ~i & ~j) | (a & b & f & g & ~c & ~h & ~i & ~j) | (a & b & h & j & ~c & ~d & ~e & ~g) | (a & c & e & j & ~b & ~f & ~h & ~i) | (a & c & f & g & ~d & ~e & ~h & ~i) | (a & c & h & j & ~b & ~d & ~f & ~i) | (a & d & e & h & ~b & ~c & ~g & ~j) | (a & d & e & h & ~b & ~f & ~g & ~i) | (a & e & f & h & ~b & ~c & ~d & ~i) | (a & e & g & h & ~b & ~c & ~d & ~i) | (a & e & i & j & ~b & ~c & ~d & ~f) | (a & f & g & i & ~b & ~c & ~d & ~e) | (b & c & e & g & ~d & ~f & ~h & ~j) | (b & d & f & i & ~c & ~e & ~h & ~j) | (b & d & f & j & ~c & ~e & ~g & ~i) | (b & d & f & j & ~c & ~e & ~h & ~i) | (b & e & f & g & ~c & ~d & ~h & ~j) | (b & e & f & h & ~a & ~g & ~i & ~j) | (b & f & g & h & ~a & ~c & ~i & ~j) | (b & f & g & i & ~a & ~c & ~d & ~h) | (b & h & i & j & ~d & ~e & ~f & ~g) | (c & d & h & i & ~b & ~e & ~g & ~j) | (c & e & f & h & ~a & ~d & ~g & ~i) | (c & e & g & h & ~a & ~b & ~f & ~j) | (c & f & g & h & ~b & ~d & ~e & ~j) | (d & e & g & i & ~a & ~c & ~f & ~h) | (d & f & h & j & ~a & ~c & ~g & ~i) | (e & f & g & h & ~a & ~b & ~i & ~j) | (e & g & i & j & ~a & ~b & ~c & ~h) | (e & h & i & j & ~a & ~b & ~f & ~g) | (a & b & c & e & h & i & ~f & ~g & ~j) | (a & b & e & f & i & j & ~c & ~g & ~h) | (a & d & f & g & i & j & ~c & ~e & ~h) | (b & c & d & e & g & j & ~a & ~h & ~i) | (c & ~b & ~e & ~f & ~h & ~i & ~j) | (a & b & i & ~c & ~e & ~g & ~h & ~j) | (a & d & g & ~e & ~f & ~h & ~i & ~j) | (a & e & i & ~b & ~c & ~g & ~h & ~j) | (a & e & j & ~b & ~c & ~g & ~h & ~i) | (a & g & j & ~c & ~d & ~e & ~f & ~h) | (a & h & i & ~b & ~c & ~d & ~e & ~j) | (a & h & i & ~b & ~d & ~e & ~f & ~j) | (a & i & j & ~b & ~c & ~d & ~e & ~h) | (b & c & j & ~a & ~e & ~g & ~h & ~i) | (b & e & i & ~a & ~c & ~d & ~g & ~j) | (b & f & h & ~a & ~c & ~d & ~e & ~i) | (b & h & j & ~a & ~c & ~f & ~g & ~i) | (c & d & e & ~a & ~g & ~h & ~i & ~j) | (c & d & f & ~a & ~b & ~g & ~i & ~j) | (c & e & j & ~d & ~f & ~g & ~h & ~i) | (d & e & f & ~a & ~b & ~g & ~h & ~i) | (d & e & g & ~c & ~f & ~h & ~i & ~j) | (d & e & i & ~b & ~c & ~f & ~g & ~h) | (d & f & g & ~a & ~b & ~c & ~e & ~j) | (d & g & j & ~a & ~b & ~c & ~e & ~f) | (d & g & j & ~a & ~c & ~e & ~f & ~i) | (e & g & i & ~a & ~b & ~d & ~f & ~h) | (a & b & c & g & i & ~d & ~e & ~h & ~j) | (b & e & g & h & i & ~a & ~c & ~d & ~f) | (c & d & e & g & j & ~a & ~f & ~h & ~i) | (c & f & g & i & j & ~a & ~b & ~e & ~h) | (d & e & g & h & j & ~b & ~c & ~f & ~i) | (a & b & c & d & g & h & i & ~e & ~f & ~j) | (a & c & ~b & ~d & ~e & ~f & ~g & ~i) | (a & c & ~b & ~d & ~e & ~g & ~h & ~j) | (b & c & ~a & ~d & ~f & ~g & ~h & ~i) | (b & d & ~c & ~e & ~f & ~g & ~h & ~j) | (b & h & ~c & ~d & ~e & ~f & ~g & ~i) | (c & g & ~a & ~b & ~e & ~f & ~h & ~i) | (c & i & ~a & ~b & ~e & ~f & ~g & ~h) | (d & e & ~a & ~b & ~c & ~h & ~i & ~j) | (d & f & ~b & ~c & ~e & ~g & ~h & ~j) | (d & g & ~b & ~c & ~f & ~h & ~i & ~j) | (e & f & ~a & ~b & ~c & ~d & ~g & ~h) | (e & g & ~a & ~c & ~d & ~f & ~h & ~i) | (g & h & ~b & ~c & ~e & ~f & ~i & ~j) | (a & c & d & i & ~e & ~f & ~g & ~h & ~j) | (a & d & e & h & ~c & ~f & ~g & ~i & ~j) | (b & c & e & h & ~d & ~f & ~g & ~i & ~j) | (b & c & g & h & ~a & ~d & ~e & ~f & ~i) | (b & g & h & i & ~a & ~c & ~e & ~f & ~j) | (c & f & h & i & ~a & ~d & ~e & ~g & ~j) | (c & f & h & j & ~b & ~d & ~e & ~g & ~i) | (c & ~a & ~b & ~d & ~f & ~g & ~h & ~j) | (e & ~a & ~b & ~d & ~f & ~g & ~i & ~j) | (i & ~a & ~b & ~c & ~d & ~e & ~g & ~j) | (j & ~a & ~b & ~c & ~e & ~f & ~h & ~i) | (a & d & f & ~b & ~c & ~e & ~g & ~i & ~j) | (a & h & j & ~b & ~d & ~e & ~f & ~g & ~i) | (b & e & j & ~a & ~c & ~d & ~f & ~g & ~h) | (b & f & j & ~a & ~c & ~d & ~g & ~h & ~i) | (b & i & j & ~a & ~c & ~e & ~f & ~g & ~h) | (f & h & j & ~a & ~b & ~c & ~d & ~e & ~g) | (a & e & ~c & ~d & ~f & ~g & ~h & ~i & ~j) | (d & h & ~a & ~b & ~c & ~e & ~f & ~g & ~j) | (f & ~a & ~c & ~d & ~e & ~g & ~h & ~i & ~j)
s1 = (a & ~c & ~d & e & ~f & ~g & ~h & ~i & ~j) | (~a & ~b & ~c & ~d & g & ~h & j) | (~a & c & d & e & ~g & ~h & i & j) | (a & ~b & ~c & d & ~e & h & i & j) | (b & c & e & ~f & g & ~h & i & ~j) | (a & ~b & d & e & ~f & ~g & h & ~i) | (a & ~b & ~c & ~d & ~e & ~h & i & j) | (c & ~d & e & f & ~g & i & j) | (a & c & ~d & ~e & f & g & ~h & ~i) | (a & b & c & ~e & ~g & h & ~i & ~j) | (a & b & c & d & ~e & ~f & g & h & i & ~j) | (a & b & d & e & ~f & g & h & ~i) | (b & c & ~d & e & ~f & g & ~h & ~j) | (~a & ~c & e & ~g & h & i & ~j) | (~a & ~b & ~c & e & g & ~h & i & j) | (b & ~c & d & ~e & ~f & ~g & ~h & ~j) | (~a & b & ~c & ~e & ~f & g & h & i & ~j) | (a & b & ~c & ~e & ~f & ~i & j) | (~b & ~c & ~e & ~f & g & h & ~i & ~j)

# 将表达式转换为命题逻辑表达式
expr1_simplified = sympy.simplify_logic(s)
expr2_simplified = sympy.simplify_logic(s1)

# 比较简化后的表达式
are_equal = sympy.satisfiable(Not(expr1_simplified == expr2_simplified)) is False
print(f"The expressions are {'equal' if are_equal else 'not equal'}")
