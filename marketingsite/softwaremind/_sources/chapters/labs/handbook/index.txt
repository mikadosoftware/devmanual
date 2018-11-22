==================
Show your workings
==================


I spend quite a lot of time working out how to do things in code.
Which tends to make it look like I am not doing much *producing* of code

Which means I want a nice way of "showing my working"

1. I have a story to do
2. If it is not trivial, I need to

   a) experiement with different solutions
   b) measure, collate the results
   c) publish the results.

There is no ground-breaking stuff in here.  Just a nice way of 
saying how to do stuff.

Think ... each experiment should result in a blog post like a web framework
shoot-out.


.. sphinx-report - things like tying in graphviz and graphics


Examples
--------

Link to a Python file
~~~~~~~~~~~~~~~~~~~~~

Here is a :download:`link <demo1.py>` to a python file stored next to this
ReSt text file.



Include a python file
~~~~~~~~~~~~~~~~~~~~~

This is a snippet from a file

.. literalinclude:: demo1.py

This is including just one object

.. literalinclude:: demo1.py
   :pyobject: hello_world

This is including just lines

.. literalinclude:: demo1.py
   :lines: 3-7




We can also use : include : to include a whole file but it is not really meeting
our purpoases
