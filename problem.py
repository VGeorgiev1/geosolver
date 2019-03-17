from solve import solveReal, solveBetter
from figure import Figure
import math

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
        self.name = value
    def __repr__(self):
        return self.value
    @operator
    def __radd__(self, lhs):
        return Expression(f'{lhs.value} + {self.value}')
    @operator
    def __add__(self, rhs):
        return Expression(f'{self.value} + {rhs.value}')
    @operator
    def __sub__(self, rhs):
        return Expression(f'{self.value} - {rhs.value}')
    @operator
    def __rsub__(self, lhs):
        return Expression(f'{lhs.value} - {self.value}')
    @operator
    def __mul__(self, rhs):
        return Expression(f'{self.value} * {rhs.value}')
    @operator
    def __pow__(self, rhs):
        return Expression(f'{self.value} ^ {rhs.value}')
    @operator
    def __truediv__(self, rhs):
        return Expression(f'{self.value} / {rhs.value}')
    @operator
    def __rtruediv__(self, lhs):
        return Expression(f'{lhs.value} / {self.value}')
    @operator
    def __eq__(self, rhs):
        return Expression(f'{self.value} == {rhs.value}')
    @operator
    def __req__(self, lhs):
        return Expression(f'{lhs.value} == {self.value}')
    def invert(self):
        return Expression(f'!{self.value}')
def distance(a, b):
    return Expression(f'Abs[{(a-b).value}]')
def angle(a,b,c):
    return Expression(f'Angle[{a.value}, {b.value}, {c.value}]')
def belongs(n, a, b):
    return Expression(f'Belongs[{n.value}, {a.value}, {b.value}]')

class Line:
    def __init__(self, A, B):
        self.A = A
        self.B = B
    def length(self):
        return dist(self.A, self.B)

class Triangle:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
    def perimeter(self):
        return distance(self.A, self.B) + distance(self.B, self.C) + distance(self.A, self.C)
    def area(self):
        p = self.perimeter() / 2
        a = dist(self.A, self.B)
        b = dist(self.B, self.C)
        c = dist(self.C, self.A)
        return math.sqrt(p*(p-a)*(p-b)*(p-c))

class Circle:
    def __init__(self, O, r):
        self.O = O
        self.r = r
    def perimeter(self):
        return 2 * math.pi * self.r
    def area(self):
        return self.r**2 * math.pi

class Quad:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
    def perimeter(self):
        return distance(self.A, self.B) + distance(self.B, self.C) + distance(self.A, self.C) + distance(self.C, self.D)
    def area(self):
        return 0.5*dist(self.A,self.B)*dist(self.A, self.D)*math.sin(angle(self.D,self.A,self.B))*dist(self.B,self.C)*dist(self.C, self.D)*math.sin(angle(self.D,self.B,self.C))        

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
#         print(arguments)
        return func(self, *arguments)
    return func_wrapper
  
class Problem:
    def __init__(self):
        self.symbols = {}
        self.equations = []
        self.figure = Figure()
        self.dummy_counter = 0
    def dummy(self):
        self.dummy_counter+=1
        name = f'geosolver{self.dummy_counter}'
        self.symbols[name] = Expression(name)
        return self.symbols[name]
    @parse_symbols
    def midpoint(self, a, b, m = None):
        if m != None:
            self.eq(m, (a+b)/2)
        return (a+b)/2
    @parse_symbols
    def line(self, a, b):
        return Line(a, b)
    @parse_symbols
    def triangle(self, a, b, c):
        self.figure.point(a.name)
        self.figure.point(b.name)
        self.figure.point(c.name)
        self.figure.line(a.name, b.name)
        self.figure.line(b.name, c.name)
        self.figure.line(a.name, c.name)
        self.equations.append(belongs(a, b, c).invert())
        return Triangle(a, b, c)
    @parse_symbols
    def circle(self, o, r):
        return Circle(o,r)
    @parse_symbols
    def circumcircle(self, a, b, c, o = None):
        if o is None:
            O = self.dummy()
        else:
            O = o
        r = self.dummy()
        self.eq(distance(O, a), distance(O,b))
        self.eq(distance(O, a), distance(O,c))
        self.eq(distance(O, a), r)
        self.figure.circle(O.name, r.name)
        self.figure.point(O.name)
        self.figure.point(r.name)
        return Circle(O, r)
    @parse_symbols
    def angle(self, a, b, c, value = None):
        if value is None:
            return angle(a,b,c)
        else:
            self.eq(angle(a,b,c), value)
    @parse_symbols
    def area(self, shape, value = None):
        if value is None:
            return shape.area()
        else:
            self.eq(shape.area(), value)
    @parse_symbols
    def perimeter(self, shape, value = None):
        if value is None:
            return shape.perimeter()
        else:
            self.eq(shape.perimeter(), value)
    @parse_symbols
    def altitude(self, origin, line, h = None):
        if isinstance(h, Line):
            self.eq(h.A, origin)
            self.belongs(h.B, line.A, line.B)
            self.eq(angle(h.A, h.B, line.A), 90)
        else:
            return self.project(origin, line, h)
    @parse_symbols
    def project(self, origin, line, h = None):
        if h is None:
            h = self.dummy()
        self.belongs(h, line.A, line.B)
        self.eq(angle(origin, h, line.A), 90)
        return h
            
    @parse_symbols
    def intersect(self, a, b, a1 = None, b1 = None, m = None):
        if m is None:
            m = self.dummy()
        if a1 is None and b1 is None:
            self.belongs(m, a.A, a.B)
            self.belongs(m, b.A, b.B)
        else:
            self.belongs(m, a, b)
            self.belongs(m, a1, b1)
        return m
    @parse_symbols
    def belongs(self, m, a, b):
        self.equations.append(belongs(m, a, b))
    @parse_symbols
    def eq(self, a, b):
        self.equations.append(a == b)
    @parse_symbols
    def radius(self, circle):
        return circle.r
    @parse_symbols
    def dist(self, a, b):
        return distance(a, b)
    @parse_symbols
    def add(self, a, b):
        return a + b
    @parse_symbols
    def sub(self, a, b):
        return a - b
    @parse_symbols
    def mul(self, a, b):
        return a * b
    @parse_symbols
    def div(self, a, b):
        return a / b
    def get_figure(self):
        self.solve(0)
        return self.figure.get_data()
    def bind(self, a, b):
        self.symbols[a] = b
        if isinstance(b, Expression):
            self.equations.append(Expression(a) == b)
        elif isinstance(b, (str, int, float)):
            self.equations.append(Expression(a) == Expression(b))
    def variables(self):
        return list(self.symbols.keys()) + ['answer']
    def solve(self, expression):
        answer = Expression('answer')
        self.equations.append(answer == expression)
        solutions = solveBetter(map(lambda e: e.value, self.equations), self.variables())
        for s in solutions:
            self.figure.set_point(s, *solutions[s])
        return solutions["answer"]