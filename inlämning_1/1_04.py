class Var:
    def __init__(self, key, value=True):
        self.key = key
        self.value = value

    def pull(self):
        return self.value

    def push(self, value):
        self.value = value

class Con:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def value(self, attr):
        print(self.lhs.pull())
        print(self.rhs.pull())

class Dis:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def pull(self):
        return self.lhs.pull() or self.rhs.pull()

class Neg:
    def __init__(self, key):
        self.key = key

    


example = Con(Var('a'), Dis(Var('b'), Var('c')))
example.value({'a': True, 'b': True, 'c': False})
