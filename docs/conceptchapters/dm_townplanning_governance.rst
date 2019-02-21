Town Planning and Governance
============================


A point about Software Governance
=================================

There is a software rule of thumb - that code-bases pass through
'complexity horizons' every couple of orders of magnitude. That is a
project that was easy to manage at 1,000 LOC cannot be maintained with
the same approach when its a 10,000 or 100,000 LOC cadebase.

Pieter Levels is a entrpreneur and coder, who found a certain
noteriety in 2017 by announcing that he was making sales of over
$2,000 a day, using a single php file with 4000 LOC, with no
frameworks and libraries.  The Twitter-sphere exploded, quite
amusingly, by criticising his coding approach and insisting he needed
some architecture and frameworks.

.. pull-quote::

   "What about the frameworks. Think of the frameworks"

Pieter seems to be doing fine his way, but yes, at some point the 'one
guy opens up one file' approach is of course going to fail as
complexity rises.  But managing it with the latest technical framework is
not the right answer - a technical framework is one response to the problem
of increasing complexity, one means of *governing* the codebase.

How we manage that is *software governance*.  The goal of software
governance is to raise the floor everywhere.

We can write code, we can write code that gets us to a basic level of
feature complete-ness.  And then the next fire alarm arrives, the next
email from the boss, and ... the polish disappears, the extra bit of
effort to make something long term useful just does not get done.

But that extra piece of effort can pay dividends just for one
developer.  For a team or a whole community, the dividends are
endless, just by raising the floor of quality.

In `todo-inator` I have a concept of self-rating each module or
function with a modern form of P.G. Wodehouse's re-writing of
chapters.  This simple mark::

  pgw: **

While this is a subjective measure from the developer, it is a guide
to where improvements can be made.  And importantly resides in the
codebase.

Other measures of code quality can be autoated and should be part of
every commit cycle.

:doc:`chapters/best_approach_to_software_quality`

Code base governance
--------------------

Style,
coverage
ast based syntax checking use of non-standard plumbing
`Code as a crime scene`
Static Analysis and raising all boats.
ast
and how to do syntax checking like pyflake - how to build own rules



- :doc:`chapters/application-performance-management`
- :doc:`chapters/systemd`
- :doc:`chapters/technical_capabilities`
- :doc:`chapters/terminal`
- :doc:`chapters/testing`
- :doc:`chapters/text_mining`
- :doc:`chapters/sphinx`


.. toctree::

   chapters/sphinx

A point about Systems governance
--------------------------------

SRE / building for failure (Erlang and OTP)
this is monitoring running systems.  Things like approvals, security etc.


Managing the lifecycle
-----------------------

Application Lifecycle Management
Gov Service Design Manual


TBD


Documenting architecture 
https://news.ycombinator.com/item?id=18508284

the killer post is 

https://news.ycombinator.com/reply?id=18508336&goto=item%3Fid%3D18508284%2318508336

Markets vs governance
- Curation vs eyeball capture
- thinknof the bill walking police officers. the end of blackadder 
No one has time to do those things now - it's all jump cuts
but we make better decisions slowly

so governance 

Python governance 
https://lwn.net/SubscriberLink/775105/5db16cfe82e78dc3/

we are searching for many different suitable approaches.

onencommonality is first past post votes are mostly rejected


Capturing co-created value
- socialising risk privvitisjng profits
- but cryto can easily transform this - if funding comes from government then can apply a form of copyleft

Professor Mariana Mazzucato


Do I need a procedure to deal with governance matters?

Yes - look at this from CISA 
https://cyber.dhs.gov/ed/19-01/#required-actions ::

Within 10 business days, for all .gov or other agency-managed domains, audit public DNS records on all authoritative and secondary DNS servers to verify they 

suddenly you have to do something - and record it and it needs to be done by a deadline and you need to not look like it's your first rodeo


