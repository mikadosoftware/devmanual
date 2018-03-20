
import timeit

def run():
    
    #: put code here incidental to timed part, but needed
    #: so I don't want to know how long it takes python to
    #: import a module.  If there is disk stutter that might throw
    # off the measure 
    setup = """import random
SR=random.SystemRandom()
"""

    repeated_code_a = '''
random.seed('wibble')
#grab a 1000 random numbers
out = [random.random() for i in range(1000)]
    '''
    repeated_code_b = '''
#grab a 1000 random numbers
out = [SR.random() for i in range(1000)]
    '''

    
    print min(timeit.Timer(repeated_code_a, setup=setup).repeat(7,100))
    print min(timeit.Timer(repeated_code_b, setup=setup).repeat(7,100))

if __name__ == '__main__':
    run()
