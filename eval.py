from lark import Lark
from problem import *
from lark import Tree, Token

def eval(sample):

    p = Problem() 
    methods = {
    'line': p.line,
    'triangle': p.triangle,
    'circle': p.circle,
    'perimeter': p.perimeter,
    'area': p.area,
    'angle': p.angle,
    'circumcircle': p.circumcircle,
    'inscribedcircle': p.inscribedcircle,
    'eq': p.eq,
    'radius':p.radius,
    'center':p.center,
    'dist': p.dist,
    'solve': p.solve,
    'mid': p.midpoint,
    'intersect': p.intersect,
    'altitude': p.altitude,
    'project': p.project,
    'angularbisector': p.angular_bisector,
    'belongs': p.belongs,
    'angularbisector': p.angular_bisector,
    '+': p.add,
    '-': p.sub,
    '*': p.mul,
    '/': p.div,
    '==': p.eq,
    '\\X': p.intersect,
    '\\E': p.belongs,
    }

    def process_expression(root, problem):
        if root.data == 'literal':
            return(float(root.children[0]))
        elif root.data == 'symbol':
            return(str(root.children[0]))
        elif root.data == 'method':
            method = visit_branch(root, problem)
            return(methods.get(method[0], lambda: 'Invalid')(*method[1]))

        #return visit_branch(root)

    def visit_branch(root, problem):
        if isinstance(root, Tree):
            params = [visit_branch(child, problem) for child in root.children]
        # print(params)
            if root.data == 'expr' and len(params) == 1:
                return process_expression(root.children[0], problem)
            elif root.data == 'operation':
                res = [visit_branch(child, problem) for child in root.children]
                idx = 0
                for child in root.children:
                    if isinstance(child, Token) and child.type == 'OPERATOR':
                        op = res.pop(idx)
                    idx += 1
                return (methods.get(op, lambda: 'Invalid')(*res))
            elif root.data == 'solveoperation':
                return (methods.get('solve')(visit_branch(root.children[0], problem)))
            elif root.data == 'decl':
                problem.bind(*params)
            elif root.data == 'literal' or root.data == 'symbol':
                return params[0]
            return params
        if isinstance(root, Token):
            return str(root)

    solver_grammar = r"""
    ?start: _NL? problem
    problem: ([solveoperation | operation | decl | expr] _NL)+
    decl: symbol ":=" expr
    expr: method
        | symbol
        | literal
    method: symbol "(" parameter ")"
    parameter: [expr | operation] ("," [expr | operation])*
    operation: expr (expr)* OPERATOR expr (expr)*
    solveoperation: (operation | expr) "=" "?"
    symbol: SYMBOL
    literal: LITERAL
    
    SYMBOL: /[a-zA-Z][a-zA-Z0-9]*/
    LITERAL: /-?\d*\.?\d+/
    OPERATOR: /([\/*\-+]|==|\\E|\\X)/
    COMMENT: "(*" /(.|\n|\r)+/ "*)"     
           |  "{" /(.|\n|\r)+/ "}"      
           |  "#" /(.)+/
    
    %import common.INT -> NUMBER
    %import common.NEWLINE -> _NL
    %import common.WS_INLINE
    
    %ignore WS_INLINE
    %ignore COMMENT
    """
    parser = Lark(solver_grammar)
    res = visit_branch(parser.parse(sample), p)[-1]
    print(p.equations)
    return res