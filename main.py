# map(func, seq)
# filter(func, seq)
# reduce(func, seq)
from functools import reduce
a = [1, 2, 3, 4]

product_a = reduce(lambda x,y: x*y, a)
print(product_a)
