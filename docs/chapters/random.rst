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


[pbrian@localhost chapters]$ python randomness.py 

[0.47841713243204875, 0.9106930754528739, 0.10139849285025149]
[0.47841713243204875, 0.9106930754528739, 0.10139849285025149]
[0.00025916099548339844]

[0.6060143833031767, 0.6573259634008972, 0.586415954525388]
[0.38238270018686693, 0.8731295368542729, 0.1982646979928232]
[0.011247873306274414]

By my measures, 
0.00862002372742
0.168267965317

PRNG is 20 times faster than system random.  WHich for getting `real`
randomness, is pretty good.

Getting estimates of entropy??
------------------------------



RSA explained
https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Example
