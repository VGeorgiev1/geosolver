from subprocess import run, PIPE


def solveReal(equations):
    expression = '{' + ','.join(equations) + '}'
    p = run(['wolframscript', '-f', 'solve.m', expression], stdout=PIPE)
    return float(p.stdout)

print(solveReal([
    'Abs[x1 - x2] + Abs[x1 - x3] + Abs[x2 - x3] == 5', 
    'Abs[x1 - x2] == 2', 
    'Abs[x1 - x3] == 1', 
    'answer == Abs[x2 - x3]']))

