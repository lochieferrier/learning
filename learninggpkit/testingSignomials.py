from gpkit import Variable, Model
a = Variable('a')
b = Variable('b')
c = Variable('c')
d = Variable('d')

r = a*b + c*d
print r.__dict__