#! python3
first = lambda a,b: a
last = lambda a,b: b
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

car = lambda f: f(first)
cdr = lambda f: f(last)

print(car(cons(3,4)))
print(cdr(cons(3,4)))