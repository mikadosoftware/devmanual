==================
Why random Matters
==================

Edward Snowden, who really ought to know, says you can only trust the
math.  It is only the hard factorisation problem that keeps
crpytography safe.  That and the assumption that a really random
number has been chosen.

Public Key explained
--------------------

Diffie Helman key exchange / SSL
--------------------------------

When Random goes wrong
----------------------
cf Debian




Sources of entropy
------------------


Session Management - Keeping it simple
--------------------------------------

For many applications, a time-limited, shared secret over a secure
channel is quite good enough for proving who the other end is - this
is session management.  And a shared secret is 

SOme views from tpateck?



Timing Python Code
------------------

Python has a useful library for timing small or large functions - `timeit`.

Lets say we want to compare getting system random numbers to PRNG
random numbers.  Lets grab 10,000 random numbers, count how long it
takes to grab them.  That way I can know which is faster PRNG or real.
(I think we can guess)


.. literalinclude:: randomness.py

   

Which gives us as a result::

    $ python randomness.py 
    0.014582695000171952
    0.21012862700013102

PRNG is 20 times faster than system random.  But system random gets us
"real" randomness, whats called CSRNG - Cryptographically secure
Random Number generator.  Running on a normal linux box this will
generate randomness sufficient for most real world security.

Getting estimates of entropy??
------------------------------



RSA explained
https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Example
