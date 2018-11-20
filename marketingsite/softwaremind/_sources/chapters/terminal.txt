===============
Using Terminals
===============

Coders live in terminals. So it's really hard to tell someone how to
live.  But here is my, kinda, sorta, ideal setup. Actually its far
from ideal but I have lived with stuff like this for a long time so
it's ok.

Firstly, we want some decent fist of unicode display on the
terminal. Because otehrwise its just embarrassing.

`urxt-unicode` is a terminal emulator that does a decent job of
displaying unicode.

I can install it with this chunk of code from `weaver`


Using Intersphinx
-----------------

Some rules

* inside each package or repo, all the mdoules and methods should be
  documented.

* if we want to copy directly - we really have to copy not reference lines

* so we can rfefer to other packages notes, but each pacakge does its own docs.


We can a given packages objects.inv data to understand what links it
offers externally to intersphinx

I have written that in weaver in :py:mod:`weaver.devtools.sphinx_tools`

my notes :ref:`foo <weaver:xterm>`

my notes :py:mod:`weaver.fabmodules.fab_terminal_setup`

my notes :doc:`foo <weaver:xterm>`

     
