# Discrete Structures (CSCI 220)
# Summer 2023, Session 2
# Assignment 1 - Propositional Logic and Truth Tables
# Justin Espinal

# Acknowledgements:
# I worked with the class
# I used the following sites ... (if applicable)


import inspect
import pandas as pd
from itertools import product


def func_body(f):
    body = inspect.getsource(f)  # gets the code
    idx = body.index("return")  # get the part after the word return
    return '"' + body[7 + idx:].strip() + '"'


def truth_table(f):
    values = [list(x) + [f(*x)] for x in product([False, True], repeat=f.__code__.co_argcount)]
    return pd.DataFrame(values, columns=(list(f.__code__.co_varnames) + [f.__name__]))


def analyze_truth_table(f):
    tt = truth_table(f)
    tt_rows = tt.shape[0]
    tt_cols = tt.shape[1]
    tt_vars = tt_cols - 1
    tt_type = None
    last_col = tt.iloc[:, tt_vars]
    if last_col.all():
        tt_type = "Tautology"
    elif last_col.any():
        tt_type = "Contingency"
    else:
        tt_type = "Contradiction"
    print("Name:", f.__name__, func_body(f))
    print(tt)
    print("Rows:", tt_rows, "Cols:", tt_cols, "Vars:", tt_vars, "Type:", tt_type)
    print()


def impl(p, q):
    return not p or q


def bi_impl(p,q):
    return impl(p,q) and impl(q,p)


def f0(p, q, r):
    return (p or q) and r


def f1(p):
    return p and not p


def f2(p):
    return p or not p


def f3(p, q):
    return not p and impl(p, q)


def f4(p, q):
    return impl(p, q) or impl(q, p)


def f5(p, q):
    return (p or q) or (not p and not q)


def f6(p, q):
    return (p or q) and (not p and not q)


def f7(p, q, r):
    return impl(p, q) and impl(q, r)


# Hypothetical Syllogism
def f8(p, q, r):
    return impl((impl(p, q)) and (impl(q, r)), impl(p, r))


# DeMorgan's First Law
def f9(p,q):
    return bi_impl(not(p or q),(not p and not q))


# DeMorgan's Second Law
def f10(p, q):
    return bi_impl(not (p and q), (not p or not q))


# Commutative Law
def f11(p, q):
    return bi_impl((p or q), (q or p))


# Commutative Law
def f12(p, q):
    return bi_impl((p and q), (q and p))


# Associative Law
def f13(p,q,r):
    return bi_impl((p and q) and r, p and (q and r))


# Associative Law
def f14(p,q,r):
    return bi_impl((p or q) or r, p or (q or r))


# Distributive Law
def f15(p,q,r):
    return bi_impl((p or (q and r)), ((p or q) and (p or r)))


# Distributive Law
def f16(p, q, r):
    return bi_impl((p and (q or r)), ((p and q) or (p and r)))


# Absorption Law
def f17(p, q):
    return bi_impl((p or (p and q)), p)


# Absorption Law
def f18(p, q):
    return bi_impl((p and (p or q)), p)


def main():
    for f in [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18]:
        analyze_truth_table(f)


if __name__ == "__main__":
    main()
