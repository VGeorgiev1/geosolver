import subprocess
import sys

def expression(equations):
    return '{\n' + ',\n'.join(equations) + '}'

def solveReal(equations):
    expr = expression(equations)
    # print(expression)
    p = subprocess.run(['wolframscript', '-f', 'solve.m', expr], stdout=subprocess.PIPE)
    try:
        return float(p.stdout)
    except:
        print(str(p.stdout, 'utf-8'))

def solveBetter(equations, variables):
    expr = expression(equations)
    variables = expression(variables)
    # print(expr, variables)
    p = subprocess.run(['wolframscript', '-f', 'solveBetter.m', expr, variables], stdout=subprocess.PIPE)
    try:
        return float(p.stdout)
    except:
        print(str(p.stdout, 'utf-8'))