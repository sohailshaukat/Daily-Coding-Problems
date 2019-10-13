#! python3
def first(a, b): return a


def last(a, b): return b


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f): return f(first)


def cdr(f): return f(last)


print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
