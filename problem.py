from solve import solveReal

def operator(func):
    def func_wrapper(self, rhs):
        if not isinstance(rhs, Expression):
            rhs = Expression(rhs)
        return func(self, rhs)
    return func_wrapper

class Expression:
    def __init__(self, value):
        if isinstance(value, Expression):
            self.value = f'({value.value})'
        else:
            self.value = f'({value})'
    def __str__(self):
        return self.value
    @operator
    def __add__(self, rhs):
        return Expression(f'{self.value} + {rhs.value}')
    @operator
    def __sub__(self, rhs):
        return Expression(f'{self.value} - {rhs.value}')
    @operator
    def __mul__(self, rhs):
        return Expression(f'{self.value} * {rhs.value}')
    @operator
    def __truediv__(self, rhs):
        return Expression(f'{self.value} / {rhs.value}')
    @operator
    def __eq__(self, rhs):
        return Expression(f'{self.value} == {rhs.value}')
def distance(a, b):
    return Expression(f'Abs[{(a-b).value}]')
class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def perimeter(self):
        return distance(self.A, self.B) + distance(self.B, self.C) + distance(self.A, self.C)

def parse_symbols(func):
    def func_wrapper(self, *args):
        arguments = []
        for a in args:
            if isinstance(a, str):
                if a in self.symbols:
                    arguments.append(self.symbols[a])
                else:
                    s = Expression(a)
                    self.symbols[a] = s
                    arguments.append(s)
            elif isinstance(a, (int, float)):
                arguments.append(Expression(a))
            else:
                arguments.append(a)
        return func(self, *arguments)
    return func_wrapper

class Problem:
    def __init__(self):
        self.symbols = {}
        self.equations = []
    @parse_symbols
    def triangle(self, a, b, c):
        return Triangle(a, b, c)
    @parse_symbols
    def perimeter(self, shape, value):
        self.equations.append(shape.perimeter() == value)
    @parse_symbols
    def eq(self, a, b):
        self.equations.append(a == b)
    @parse_symbols
    def dist(self, a, b):
        return distance(a, b)
    def bind(self, a, b):
        self.symbols[a] = b
        if isinstance(b, Expression):
            self.equations.append(Expression(a) == b)
        elif isinstance(b, (str, int, float)):
            self.equations.append(Expression(a) == Expression(b))
    def solve(self, expression):
        answer = Expression('answer')
        self.equations.append(answer == expression)
        return solveReal(map(lambda e: e.value, self.equations))