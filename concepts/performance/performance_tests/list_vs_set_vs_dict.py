from timeit import timeit

# Setup the circumstance
b = ['c' * 100000 + chr(i) for i in range(100)]

a = b[-1]

# Measure
for _ in range(3):
    print(timeit(lambda: a in b,      number=1000))
    print(timeit(lambda: a in set(b), number=1000))
    print(timeit(lambda: a in dict.fromkeys(b), number=1000))
