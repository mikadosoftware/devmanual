FLAG=False
#FLAG=True

def genA():
    if FLAG:
        for word in ("good", "better", "best"):
            yield word
    else:
#       return iter([])
#	yield
        raise StopIteration

def test(val):
    if val not in ("good", "better", "best"):
        raise Exception("Die")
	

def run():
    #: Here is the gotcha -> I am using the empty iterable ([]) to control
    # the flow and not enter the loop.  If I enter the loop with y bad generator I die
    # 
    print "->",
    for i in genA():
        print "in test for %s" % str(i) 
        test(i)
    print "//"

if __name__ == '__main__':
    run()


"""
This is about iterators and itrables
"""
