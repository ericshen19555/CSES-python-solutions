from itertools import groupby as g
print(max(len(list(x))for _,x in g(input())))