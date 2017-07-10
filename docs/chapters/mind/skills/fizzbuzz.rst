========
Fizzbuzz
========

(lnks to algorithms tests as an antipattern)

The `fizzbuzz test <http://blog.codinghorror.com/why-cant-programmers-program/>`_ is a pretty good determinate of ability to code.

It has a low false negative rate - that is if you can code, its pretty hard to
fail.  It also has a low false positive rate - if you cannot code, you simply
wont pass.  As such it is apparently depressing why it is still a necessary evil
- I can attest to sitting slackjawed as candidates could not understand a SELECT
  query let alone attempt a for loop.

I am not a big fan of programming puzzles like `codility
<http://www.codility.com>`_.  I think they certainly have their place - I
suspect as ongoing development for coders.  Having an hour or two a week just to
work on Project Euler problems would sharpen anyone's saw.

It must be admitted that I have only seen *early* candidates fail so amazingly.
In general there is a pool of people who apply for every programming gig going,
and will have CVs tuned to get through the doors.  But there is a reason they
don't get hired and so are available to interview the first day you post the ad.

This is why recruitment is an ongoing investment.


I however have flamed out over the more complex puzzles.  I remember happily
designing a scalable architecture for some pretend web app, discussing the
benefits and costs of Rabbit MQ, and then being asked to write a routine to
calculate prime numbers, whilst the director of Engineering harangued looking
like the dog with the bone if he saw a missed optimisation.  I have never yet
turned round in an interview and said shut the fuck up and let me write on the
board.  But it was touch and go.


As such, lets look at fizzbuzz, and Python and Tail Call Recursion.

.. todo:: show to AST for this and how elimating tail call could elimnate the stack.





.. literalinclude:: fizzbuzz.py

But if I exceed pythons recursion depth limit

1001
