import itertools
import string
print(list(string.ascii_lowercase))
a = ['a', 'b', 'c']
b = [a[:], a[:], a[:]]
for i in itertools.product(*b):
    print(i)