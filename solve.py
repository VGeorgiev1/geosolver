import subprocess
import sys
import json

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
        arr = json.loads(p.stdout)
        solutions = {}
        for rule in arr[1:]:
            if isinstance(rule[2], float):
                solutions[rule[1]] = [rule[2], 0] 
            else:
                solutions[rule[1]] = [rule[2][1], rule[2][2]] 
        return solutions
    except Exception as e:
        print(str(p.stdout, 'utf-8'), e)