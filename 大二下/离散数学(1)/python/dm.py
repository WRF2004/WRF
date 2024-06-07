import pandas as pd
import sympy.logic
from sympy.logic.boolalg import SOPform
from sympy import symbols, Not, And, Or, Equivalent
from sympy.logic.boolalg import to_cnf
import sympy
import sympy.logic.boolalg

def read_truth_table_from_excel(file_path, sheet_name):
    # 读取Excel文件中的真值表
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df

def convert_truth_table_to_dnf(df):
    # 获取变量名
    variables = list(df.columns[:-1])
    result_col = df.columns[-1]

    # 将变量名转换为sympy符号
    sympy_vars = symbols(variables)

    # 提取最小项
    minterms = []
    for row in df.itertuples(index=False):
        if row[-1] == 1:
            minterms.append(tuple(row[:-1]))

    # 使用SOPform生成析取范式
    expr = SOPform(sympy_vars, minterms)

    return expr

def convert_truth_table_to_cnf(df):
    # 获取变量名
    variables = list(df.columns[:-1])
    result_col = df.columns[-1]
    # 将变量名转换为sympy符号
    sympy_vars = symbols(variables)

    # 提取最大项
    maxterms = []
    for row in df.itertuples(index=False):
        if row[-1] == 0:
            maxterms.append(tuple(row[:-1]))

    # 生成每个最大项的否定
    clauses = []
    for maxterm in maxterms:
        clause = []
        for var, val in zip(sympy_vars, maxterm):
            if val == 1:
                clause.append(Not(var))
            else:
                clause.append(var)
        clauses.append(Or(*clause))

    # 将所有最大项的否定合取在一起生成CNF
    cnf_expr = And(*clauses)

    return to_cnf(cnf_expr, force=True, simplify=True)

def format_expression(expr):
    expr_str = str(expr)
    expr_str = expr_str.replace('&', '∧')
    expr_str = expr_str.replace('|', '∨')
    expr_str = expr_str.replace('~', '¬')
    return expr_str

def count(s):
    special_chars = ['∧', '∨', '¬', '→', '↔', '⊕']
    total = 0
    for char in special_chars:
        total += s.count(char)
    return total

def main():
    file_path = 'D:\Desktop\github\大二下\离散数学(1)\python\score\真值表.xlsx' 
    sheet_name = '10-vars'  

    df = read_truth_table_from_excel(file_path, sheet_name)

    expr_dnf = convert_truth_table_to_dnf(df)
    expr_cnf = convert_truth_table_to_cnf(df)

    print(Equivalent(expr_cnf, expr_dnf).simplify())

    # 打印简化后的表达式及其联结词数量
    print("Simplified Boolean DNF Expression:")
    print(format_expression(expr_dnf))
    print(count(format_expression(expr_dnf)))

    print("Simplified Boolean CNF Expression:")
    print(format_expression(expr_cnf))
    print(count(format_expression(expr_cnf)))

if __name__ == "__main__":
    main()
