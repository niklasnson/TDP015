class Var:
    def __init__(self, value):
        self.value = value

    def get(self):
        print(self.value)

class Con:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def value(self, attr):
        print(attr['c'])

class Dis:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs


# a and ( b or c )
var = Var('test')
var.get()



example = Con(Var('a'), Dis(Var('b'), Var('c')))
example.value({'a': True, 'b': True, 'c': False})
