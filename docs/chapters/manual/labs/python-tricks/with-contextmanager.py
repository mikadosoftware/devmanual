"""
An example of `with` context manager

A good use might be to move to a specific dir, do something in that "context"
then return to orig dir.

"""

class foo(object):
    def __enter__(self):
        print "entered"
        return self
    def __exit__(self, exceptiontype, exceptionvalue, exceptiontb):
        if exceptiontype:
            print exceptiontype, exceptionvalue
        else:
            print "exited"
    def __init__(self, a,b):
        self.a = a
        self.b = b
        

with foo(2,3) as f:
    print f.b

