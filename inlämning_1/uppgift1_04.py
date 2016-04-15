import itertools

class Var:
    def __init__(self, key):
        self.key = key

    def get_k(self):
        return self.key

class Neg:
    def __init__(self, rhs):
        self.vars = []
        for v in [lhs, rhs]:
            self.vars.append(v)

    def value(self, attr):
        operator = []
        for v in self.vars:
            if type(v) is Var:
                operator.append(attr[v.get_k()])
            else:
                operator.append(v.value(attr))
        rhs = operator
        return(not rhs)

    def variables(self, attr):
        operators = []
        for v in self.vars:
            if type(v) is Var:
                operators.append(v.get_k())
            else:
                operators.append(v.variables(attr))
        return list(itertools.chain(*operators))

class Con:
    def __init__(self, lhs, rhs):
        self.vars = []
        for v in [lhs, rhs]:
            self.vars.append(v)

    def value(self, attr):
        operator = []
        for v in self.vars:
            if type(v) is Var:
                operator.append(attr[v.get_k()])
            else:
                operator.append(v.value(attr))
        lhs, rhs = operator
        return(lhs and rhs)

    def variables(self):
        operators = []
        for v in self.vars:
            if type(v) is Var:
                operators.append(v.get_k())
            else:
                operators.append(v.variables())
        return list(itertools.chain(*operators))


class Dis:
    def __init__(self, lhs, rhs):
        self.vars = []
        for v in [lhs, rhs]:
            self.vars.append(v)

    def value(self, attr):
        operator = []
        for v in self.vars:
            if type(v) is Var:
                operator.append(attr[v.get_k()])
            else:
                operator.append(v.value(attr))
        lhs, rhs = operator
        return(lhs or rhs)

    def variables(self):
        operators = []
        for v in self.vars:
            if type(v) is Var:
                operators.append(v.get_k())
            else:
                operators.append(v.variables())
        return list(itertools.chain(*operators))

class Imp:
    def __init__(self, lhs, rhs):
        self.vars = []
        for v in [lhs, rhs]:
            self.vars.append(v)

    def value(self, attr):
        operator = []
        for v in self.vars:
            if type(v) is Var:
                operator.append(attr[v.get_k()])
            else:
                operator.append(v.value(attr))
        lhs, rhs = operator
        return(not lhs or rhs)

    def variables(self, attr):
        operators = []
        for v in self.vars:
            if type(v) is Var:
                operators.append(v.get_k())
            else:
                operators.append(v.variables(attr))
        return list(itertools.chain(*operators))

class Equ:
    def __init__(self, lhs, rhs):
        self.vars = []
        for v in [lhs, rhs]:
            self.vars.append(v)

    def value(self, attr):
        operator = []
        for v in self.vars:
            if type(v) is Var:
                operator.append(attr[v.get_k()])
            else:
                operator.append(v.value(attr))
        lhs, rhs = operator
        return(not( lhs and not ( lhs and rhs)) and not (rhs and not (lhs and rhs)))

    def variables(self, attr):
        operators = []
        for v in self.vars:
            if type(v) is Var:
                operators.append(v.get_k())
            else:
                operators.append(v.variables(attr))
        return list(itertools.chain(*operators))
#example = Con(Var('a'), Dis(Var('b'), Var('c')))
#print(example.value({'a': True, 'b': True, 'c': False}))
#print(example.value({'a': True, 'b': False, 'c': False}))
