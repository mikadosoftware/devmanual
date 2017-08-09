class baz(object):
    def __init__(self):
        pass

    def dec2(self, fn):
        def wrappedfn(*args, **kwds):
            #add one to each result
            return fn(*args, **kwds)+1
        return wrappedfn




def dec(fn):
    def wrappedfn(*args, **kwds):
        #add one to each result
        return fn(*args, **kwds)+1
    return wrappedfn

objB = baz()


@objB.dec2
def addone(a):
    return a+1

print addone(2) 
       
