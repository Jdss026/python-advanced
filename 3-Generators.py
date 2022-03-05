# seq 1 to 9.000.000

"""

def mygenerator(n):
    for x in range(n):
        yield x**3

values = mygenerator(100)

for x in values:
    print(x)
"""

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()

for x in range(500):
    print(next(values))