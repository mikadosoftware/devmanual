========
closures
========

--------

Lexical closures are a really useful trick.

Basically, we can create a function at run-time, and the complete call-stack
that exists *at the time it was created* gets wrapped up and kept neatly
until the next time it is called.  So its a way of capturing a variable at
a frozen point in time.  (This is to me useful, but has no value in say a functional language).

.. literalinclude:: closures.py

resulting in ::

    $ python closures.py
    The variable avar was                 this value when I was created 0
    The variable avar was                 this value when I was created 1
    The variable avar was                 this value when I was created 2
    The variable avar was                 this value when I was created 3
    The variable avar was                 this value when I was created 4
    The variable avar was                 this value when I was created 5
    The variable avar was                 this value when I was created 6
    The variable avar was                 this value when I was created 7
    The variable avar was                 this value when I was created 8
    The variable avar was                 this value when I was created 9
