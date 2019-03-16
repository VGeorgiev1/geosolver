import subprocess
import sys

def solveReal(equations):
    expression = '{\n' + ',\n'.join(equations) + '}'
    # print(expression)
    p = subprocess.run(['wolframscript', '-f', 'solve.m', expression], stdout=subprocess.PIPE)
    try:
        return float(p.stdout)
    except:
        print(str(p.stdout, 'utf-8'))