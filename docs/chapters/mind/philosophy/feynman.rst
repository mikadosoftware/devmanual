========================================
What I cannot create I do not understand
========================================



.. figure:: http://static.duartes.org/img/blogPosts/feynmanLastBoard.gif

When Richard Feynman died in 1988, his chalkboard at CalTech contained
several notes, including the one that has struck such a cord with me

::

  What I cannot create I do not understand

This says *everything* I want to say about why Open Source Software is
important, why re-creating the existing work is important, why open
and transparent - ness works, why things need to be evovled not designed
and why, we cannot understand everything.

It takes a genius to put all that in 8 words.


So, what can be extracted from eight words.

* Build from scratch
* Open Source keeps re-inventing the wheel
* software is evolved
* relax.

Build from scratch
------------------

One of my software development tenets is you should be able to *build
your whole systems from scratch*.  That is given bare metal hardware,
get up and running, not from a few lucky backups and _dd_ but from
controlled scripted installs.

I have always thought this vital - without being able to (re)create
your systems, how do you know if you can in a disaster, or more
importantly that you can when it is not a disaster.  ITs impossible to
believe that the first time you installed your webserver you got it
perfect, first time, but if you cannot rebuild it with confidence, you
just will put off rebuilding it again and again until it is a mess of
libraries, patches and symlinks that you could never hope to remmeberm
nor worse, simplifiy.  Now expand that to your DNS, file server, your
database.

But being able to run a simple script, and the system is configured,
that makes life so much simpler.  I can read the script and see what it
will do.  I can change it, experiment, confident that I can just rerun
the original and get back to where I started.  And I can run the script
and go do something more interesting.

And no, I do not believe in _dd_, _ghost_ or other image based
methods.  Yes, they are very nice for Virtualisation, but always there
is a flaw - to get to an image, one has to build the original.  If you
build the original by hand, how do you know what steps you took - how
sure can you be? The Sysadmin was very careful?  Was he? Thats nice.
Oh look a new patch is out, and we no longer want to use version 5.2.2
of php and can we put the incompatible library onto only half of the
hosts.  Can you rebuild all of the images to do that, by tomorrow?
Still going to be careful are you?


Build from scripts, from scratch.

And you know what, I finally worked out why I was so insistent on this,
in the face of others desire to take the easy route.  Quite simply because
I did not understand a system till I had wrestled it enough to automate it.

You find out where all the gaps are when you try and automate a system.


Re-inventing the wheel
----------------------
I am (re)writing a ER diagramming tool, for about the third time. This time no
funny copyright issues with my employers, I swear.

But there are many ER tools out there. And there are many languages, databases,
games and more.  This does not stop us from writing another, just as
the existence of a Haynes car manual does not stop people from taking their
car engine apart.  We do it because we do not understand, and we want to learn.

Sometimes, there is an itch to scratch.  But often the itch is for knowledge,
and the desire to know if we *can*.  Benefiting the rest of the world is what we
do to share our knowledge.


Evolution
---------

Because we have to re-invent the wheel to teach the next generation,
we tend to incrementally improve.  And that is a slow evolutionary process.

Software *evolves* to fit its niche.

Relax
-----

I am sometimes troubled by comparing myself to some of life's winners.  But
looking at Feynman makes those comparisons silly.  A genius that other genius'
thought a genius, he still tried to understand this strange world we live in,
and had no more a grasp on *why* than the rest of us poor schmucks.

So, we do what we can.  And move the world on a little bit.  Some more than
others, I must admit, but I am happy to be pushing it in the right direction.
