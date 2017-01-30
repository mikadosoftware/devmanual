:rm
=======================
Example ReST directives
=======================

A Subtitle
==========

Bullet lists

* One
* Two
* Three

Footnotes here [#]_ and another here [#]_

.. [#] Footnote First
.. [#] Footnote Second

Sidebar
~~~~~~~

.. sidebar:: A sidebar

   Body of a SideBar

Topic
~~~~~

.. topic:: a Topic

   Body of a Topic

Code
~~~~

.. code:: python

  def my_function():
      "just a test"
      print 8/2

Math
~~~~

.. math::

   α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)

Rubric
~~~~~~

.. rubric::  Its like a pull quote but not


Epigraph
~~~~~~~~

.. epigraph::  And You ma'am are ugly.

   But madam, in the morning I shall be sober
   -- Winston


Highlight
~~~~~~~~~

.. highlights:: Highlight

   Just highlighting this


Pull-Quote
~~~~~~~~~~

.. pull-quote:: Quote me

   Its a quote from the body but bigger.


.. compound::

   The 'rm' command is very dangerous.  If you are logged
   in as root and enter ::

       cd /
       rm -rf *

   you will erase the entire contents of your file system.


.. container:: custom

   This paragraph might be rendered in a custom way.
