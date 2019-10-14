import timeit

import random
SR = random.SystemRandom()

def run_prng():
    random.seed('wibble')
    #grab a 1000 random numbers
    out = [random.random() for i in range(1000)]

def run_sysrng():
    #grab a 1000 random numbers
    out = [SR.random() for i in range(1000)]


def testit():
    print(min(timeit.Timer(run_prng).repeat(7,100)))
    print(min(timeit.Timer(run_sysrng).repeat(7,100)))

if __name__ == '__main__':
    testit()
