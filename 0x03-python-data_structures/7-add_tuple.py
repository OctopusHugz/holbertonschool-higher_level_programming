#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = 0, 0
    if len(tuple_a) >= 2:
        tuple_c = tuple_c[0] + tuple_a[0], tuple_c[1] + tuple_a[1]
    elif len(tuple_a) == 1:
        tuple_c = tuple_c[0] + tuple_a[0], tuple_c[1]
    if len(tuple_b) >= 2:
        tuple_c = tuple_c[0] + tuple_b[0], tuple_c[1] + tuple_b[1]
    elif len(tuple_b) == 1:
        tuple_c = tuple_c[0] + tuple_b[0], tuple_c[1]
    return tuple_c
