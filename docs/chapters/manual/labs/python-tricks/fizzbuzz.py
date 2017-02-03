
def fb(i, n, result):
    if i == n:
        return result
    elif i % 15 == 0:
       result.append("FizzBuzz")
    elif i % 3 == 0:
       result.append("Fizz")
    elif i % 5 == 0:
       result.append("Buzz")
    else:
       result.append(i)
    return fb(i+1, n, result)

#print fb(1,999,[])

def fb2(i, n, result):
    if i == n:
        return result
    elif i % 15 == 0:
       result.append("FizzBuzz")
    elif i % 3 == 0:
       result.append("Fizz")
    elif i % 5 == 0:
       result.append("Buzz")
    else:
       result.append(i)
    return (lambda: fb2(i+1, n, result))

#this now returns a function that when called ( a() )
# returns the next recursion
    
    
# http://paulbutler.org/archives/tail-recursion-in-python/
# basicakky turning the recursion into a whle loop
# I have expanded out the params 
def tail_rec(fun):
   def tail(fun):
      a = fun
      while callable(a):
         a = a()         # here a is a function that returns a function
                         # that returns the next recursive step
                         # essentially we convert the recursion into a while
                         # loop of each step in the recusrion.
                         # instead of the recursive function calling itself
                         # we make a while loop call it.
      return a
   return (lambda *x: tail(fun(*x)))

fbr = tail_rec(fb2)
print fbr(1,2000,[])


"""
if we use fb in tail_rec it still recurses.
SO what is going on?

the inner part of tail_rec takes any callable and calls it in a while loop
till it returns its halt condition.

This block is then returned as an anonymous function.
So we convert any recursive function into a lambda function that
returns a function that unwinds the recursive function

Now we make that recursive function at its tail, not call itself,
but return a lambda that returns its "call myself"

so...

fbr is now a lambda function that given <params> will
repeatedly set a = a() for the 



"""
