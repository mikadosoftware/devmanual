=========================
Writing code is designing
=========================

(February 2010)

The code is the design.
-----------------------

This is a deceptively simple sentence.  Within it is held the secrets of our
profession, the ultimate explanation of why programming is hard and getting the
results you want never as simple as it looks.

Its not my idea of course.

I am nearly two decades behind the times, but better late than never.  Jack
Reeves in 1992 published an essay [#]_ and followed up 13 years later with a
commentary. [#]_

Go read them.

I'm waiting...

Ok,  I'll give you the precis then.

All the things that are usually thought of as "the design" of a piece of
software are not.  The *specification* is not it, the *screenshots*, the
carefully *word-processed documents* are **not the design**.  Reeves defines
*the* design as the set of documents from which one can mechanistically produce
the final product.  For software, this is the **source code**.  It is easier to
see in manufacturing than elsewhere, because until someone gives the factory
boss an exact set of instructions he cannot tool up the factory or produce it.
There is no creativity on an assembly line.

All the diagrams on backs of napkins, the screenshots and discussion, they are
the *process* of designing.  But the actual, final design, that is
mechanistically followed by the compiler, is source code.

So if the source code is the final design, then writing the source code is
*designing*.  Apparently lots of people get upset at this.  Non-programmers
think that they are designing a piece of software by drawing a screenshot, or
writing down what they want it to do (telling people what they want).  Being
told that is, at best, an "artists impression" people seem to find is taking
away control from them. [#]_

How does this compare to *real* architecture?
---------------------------------------------

People often compare the "building" of software to the "building" of houses and
bridges and architecture.  It's close, but there are some important differences.

Where is the actual final design for a house?  It clearly is not the artists
impression drawing, but the architect draws up detailed plans including weights
and material specifications.  But can the house be built mechanistically from
those plans.  Well frankly no.

Imagine we build a robot that can squirt concrete or lay bricks. [#]_ For this
robot, unlike Bob the Builder, the phrase, "build the south wall where the marks
are laid out", is not going to work.  There will be a thousand IF statements,
about weather, about leaving a hole for a window, all of which need to be
catered for *before* the first concrete is squirted.

So where is the final, full design for a house.  The dirty secret is it never
existed.  No-one ever wrote down precisely how to build a house.  Not in a
mechanistic sense.  A house is built through an amazing ecosystem of
inter-dependant professions and expertise.  But there is no written final
design - the architects blueprints are close, but they are changed on the
ground, to meet local conditions (within certain constraints) and the bill of
materials, well that is working backwards...

These are not things that Architects usually have to worry about.  The preserve
of an architect is usually holding the clients hand (while they sign cheques)
and checking that the infrastructure has enough strength.

In fact that is a fairly good defintion of the role of an Enterprise Architect.
This much maligned (and deserverdly so) role is quite often handed out to some
guy who we cannot fire but do not want near the real code.  What it should be is
a role handed out to the most senior, informed person on the project or in the
company.  Which is another way of saying the IT manager.  The top IT guy must be
holding hands with the CEO as much as possible, and must be confident that the
strengths of the system will hold up.  To do that the system must fit into one
persons head.  How else can you be sure that the system will hold up if you only
understand half of it.

So, after all that I have three rules of thumb.  The role of Software Architect
is a real one, but it is supposed to sit with the CIO, and follows downwards
through the real power hierarchy.  A real-world architect who is not "in charge"
on site would not be able to impose his vision on the building.  He either gets
the power or he leaves.  This is not happening in software, and we have very
messy building sites.  (one area where it is more common is top-flight OSS
projects.  Checking in rights make some people Architects, and they can and do
prevent work they do not want in their design.)

Secondly, the source code is the design, writing code is designing.  Other
things may be designing too, screenshots, thinking hard etc, but the final
design is the cource code.  And if you cannot program, you cannot read,
understand or approve the design.  If you cannot read the source code, you are a
client.  Or in the way.

two-and-a-halfly ...

Thirdly, I happily predict that the architects will have to become
programmers. It will be harder and harder to design a house, but cheaper to
build. The world is becoming software.


.. sidebar::  specifications

   It may be useful to consider the opinions of other software
   professionals on "specifications" ::

     "we still talk about the seven layers model, because it's a
     convenient model for _discussion_, but that has absolutely zero to
     do with any real-life software engineering. In other words, it's a
     way to _talk_ about things, not to implement them. And that's
     important. Specs are a basis for _talking_about_ things. But they
     are _not_ a basis for implementing software."

     Linus Torvalds
     <http://kerneltrap.org/node/5725>

   We should see specifications not as directions given to developers,
   but as shared discussion documents to help everyone understand
   what, together, we are going to build.  During development we want
   to fine tune our directions, but we should rarely shout "Oh no !
   We've been trying to do the wrong thing for weeks".  Volte-face is
   for specifications, not code.






.. [#] http://www.bleading-edge.com/Publications/C++Journal/Cpjour2.htm
.. [#] http://www.developerdotstar.com/printable/mag/articles/reeves_13yearslater.html

.. [#] A quick story might help here.  Working for a large ISP we were
  re-launching our ADSL service, and there were problems - the workflow was a
  mess, and it would take days for a service to be setup by us, minutes for our
  competitors.  As a corporate guerilla act I wrote a simple workflow that
  solved a number of problems (for the best part of a year the multi-million
  pound service ran through an old PC sitting on my desk. Unofficially.)  Then I
  found out we were planning to replace the whole workflow with a 1/4 million
  pound third party system, (that would not replace the core systems, just
  transfer work messages) and being a naive boy back then, I pointed out that
  extending the workflow that existed to meet the new needs would barely cost
  thousands and even hiring two programmers full time would save money.  It
  seemed a cut and dry case - but there is an issue of control and trust.  The
  system was sold on the ability for the non-programming head of the ADSL
  department to be able to alter the workflow graphically.  Even to get his PA
  to do it.  Without this capability he did not feel he had control.  Despite
  the idea that he would be telling the programmers what to do (ie controlling
  them) we went ahead and bought the system.  It worked I think (I left shortly
  afterwards, guerillas of any stripe become unwelcome eventually).  Anyway,
  imagine how many "control issues" the head of a Monastery Scriptorium would
  have if he was illiterate and he was in charge of a bunch of youngsters who
  were writing out the Bible.  No, this is not complaining about *that* guy in
  the ISP, I am over it now, thanks for asking.  This is just another pointer
  towards my thesis that everyone is going to need to be able to program, just
  as everyone needs to be literate.  There is only one way for the head of a
  scriptorium to make good decisions regularly - thats to be able to read and
  write the output of his charges.

.. [#] (OK, these actually exist http://www.timesonline.co.uk/newspaper/0,,176-2546574,00.html - "inkjet" printing of concrete.)
