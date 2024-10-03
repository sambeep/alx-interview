#!/usr/bin/python3
'''
Pascal's Triangle
'''


def pascal_triangle(n):
    '''
    func: pascal_triangle
        returns a list of lists of integers
        representing the Pascal’s triangle of n
    args:
        <int: n> : number of rows (> 0)
    return:
        <list <of list>>
    '''
    if type(n) is not int and n <= 0:
        return ([])
    row = []
    for a in range(n):
        row.append([])
        row[a].append(1)
        if (a > 0):
            for b in range(1, a):
                row[a].append(row[a - 1][b - 1] + row[a - 1][b])
            row[a].append(1)

    return (row)