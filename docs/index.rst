=====================
Overview of DevManual
=====================

This book dives into the nitty-gritty of building and running a
software *team*.  It takes a combination of both the hard technical
skills, and the soft skills of human inter-personal realtionships and
trust to make an effective team.

This book is a guide for how to smooth the path from the realtively
easy hard skills to the squishier and much more impactful soft skills.

It focuses heavily on the technical side, because there is a lot more of that
that can go wrong. Its rather like bootcamp in the army. WIthout the basics of fitness its ahrd to do the rest. 

Middle ground matters - good management skills make a vital difference
Hostile spaces is easy or impossible, but middle ground can be fixed and will see changes as per programmable company

This manual is both a long list of `how-to` chapters, covering ntp
servers or SQL connections. These are useful, in-the-trenches guides
to certain necessary software *capabilities*.  Then there are slightly
higher level chapters - like this one, that take a particular theme,
and while they link to the underlying how-tos, these are much more
`why-tos`.

These `why-tos` are an important part of a Dev Manual.

A seperate book, The Software Mind, is an even higher abstract level,
looking at how these things playout on a bigger scale.  But for now
we are looking at how to combine docker, scripts, and servers into a
complete, working engineering team.


Plumbing
========

Pretty much every software project of any size needs some basic plumbing,
things like a good config approach, a means of linting and testing.

Libraries and protocols for 

  - error handling
  - config
  - todo
  - docs
  - logging
  - metrics (graphene)
  - activity reporting
  - performance metrics

One of the major areas of *plumbing* is Continuous Integration / Delivery


Software Governance
-------------------

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

   "What about the frameworks. THink of the frameworks"

Yes, at some point the 'one guy opens up one file' approach is of course going to fail.

How we manage that is *software governance*.  The goal of software
governance is to raise the floor everywhere.

We can write code, we can write code that gets us to a basic level
of feature complete-ness.  And then the next fire alarm arrives, the
next email from the boss, and ... the polish disappears, the extra bit of
effort to make something long term useful just does not get done.

But that extra piece of effort can pay dividends just for one developer.
For a team or a whole community, the dividends are endless, just by raising
the floor of quality.

In `todo-inator` I have a concept of self-rating each module or function
with a modern form of P.G. Wodehouse's re-writing of chapters.  This simple mark::

  pgw: **

While this is a subjective measure from the developer, it is a guide to where
improvements can be made.  And importantly resides in the codebase.

Other measures of code quality can be autoated and should be part
of every commit cycle.


Code base governance
--------------------

Style, coverage
ast based syntax checking
use of non-standard plumbing
`Code as a crime scene`
Static Analysis and raising all boats.
ast and how to do syntax checking like pyflake - how to build own rules 


Systems governance
------------------

Governance (dev to prod access etc)
(As infrastructure as code increases, this sort of thing is more possible)


The code is the design - code first for everything
--------------------------------------------------

Discuss "The code is the design", and the DevOps idea of code for everything.

When is language optimisation too much?
---------------------------------------

One of the most common tropes in software world is the 'interview question'.
While that is a whole long rant on its own (link), the desire for the industry to
optimise its code is laudable.  However there is often too much of a focus on
what language, what framework when there are otehr levels to explore

There are at least three levels of "providing business value" When we
focus on the lowest level with the least multiplier, we lose
productivity gains.  THis is too often seen as an excuse for pushing
bad code to prod.  It should rather be seen as an excuse to develop
code facing the problems of the higher levels - marketing automation
can be a huge win.

What we should know about COmputer science

Algorithm design
data structures
python innards

Common Architectural choices
----------------------------

Discuss and review common architectural choices

* cacheing
* containerisation
* REST API

Continuous Integration (CI)
===========================

Just as the spread of Memory managed languages (Java, Python, C#) in
the 90s gave developers a big boost in avoiding productivity traps (ie
spending hours debugging) Continuous Integratgion is providing the
same sort of productivity gain fro developers.  There are many
components to a large build chain across many servers.  I have called
these Build Services


- physically distinct DEV, [UAT], PREPROD and PROD
    UAT is optional if you have automated testing.
    dont mix preprod and uat cos you will want to release when users are looking
- dashboards for can I release, and what is governance ?


Testing
=======

This is seperate from source improvemnt
      

* Source control
* prmotoing code up
* having a robot promite code after meeting automatic criteria
* having automatic testing
* build servers

python eco system 
- error capture and management - rollbar 
- metrics capture
- event capture (kpi)
- bug tracking and so on 
how it all fits together 

DevOps
========

SRE and SRE book.
Start small, keep whole thing in overview
Use graphite, and just report out, graph 10 important things
to your team *today*.


inline :doc:`Managing time in docker containers </chapters/time_in_docker>`

Basic Management Reporting
==========================

* reportlib
* SLAs and KPIs - keeping ourselves honest
* focusing upwards to higher levels of leverage
* avoiding the drumbeat of deadlines, and panic, and agreeing goals based on
  data / 20% most effective things to fix.
* Make one weekly report *today*

Esprit d'corp and Team honesty
==============================

Hiring practises - be part of the team
Entry hurdles. 
start with feedback - sprints and retrospectives
Be aware of your priviledge
Begin the difficult conversations publically 
be aware of the likely problems - metoo is just one.

then aim for the culture you want - 

then hire good people


Security 
=========


Mission statements 
https://www.amazon.jobs/principles

* GPG and keypairs
* host based security, networks of trust between hosts,  and DMZs
* Kubernetes / Rancher as a host / VM world 
  
Managing identity and authentication
------------------------------------

So this is a huge one for me. If i have the below fairly simple
micro-services structure, how can I keep Authentication and
Autorisation correct, and simple?

::

  0           ----------          -----------          (-------)
  |      ---  | www    |   ----   | uService|  ------- (  DB   )
  ^           | gateway|          |         |          (       )
              ----------          -----------          (-------)
  User


Lets say this is a really simple service. User logs in and perform
get /mydetails They should be presented with their profile pulled form
the DB.  The uService MUST be sure that the person performing the
request,

We assume that the hosts in the chain remain uncompromised, but we
cannot assume that the network is anything other than hostile.  So no
"send the profile in plain text" and of course no "I got a request for
user xxx on my port so of course it came from the www server that I
trust."

The challenge.  I want a strong, robust and widely supported method of
client authentication.  This fundamentally means X509 client
certificates.  We are going to "Trust the Math".  But once the TLS
terminates at www, how do we go about re-trusting the whole shooting
match.  How do we get the uService to know who the user

How do we do TLS between servers.

How do we trust anything?


Authentication
Authorisation
ROle Management

Use a central service for Authorisation and Role Management - give it a token
and ask if toekn holder is allowed to do X

We can happily use a random token - no need for JWT etc. Just a single token
and a call to a central service.

THis is the simplest and best.  Discussions on JWT.


  
Workstation 
-----------

Workstation builds also matter, but my preference now is local docker


Soft Skills
-----------

* Culture, and hostile cultures
* trust, safe space, I dont know
* learning
* lunch
* Keep on in good faith
* Google HR managemenet
* management fixes are the middle ground - 



Project and Programme management
--------------------------------

It if ain't got a ticket dont work on it
If it ain't possible to rollup tickets you dont know where you are going
A backlog out of context is just a horror
There is nothing wrong with top-down design (side??)
Backlog for the whole company



CTO dashboards and Business Process Dashboards
----------------------------------------------

Dashboards matter
The basics of code quality can be in dashboard.
The basics of production health can be in dashboard
Putting a business process into dashboard is powerful - use Graphite and "light beam trackers"


Cloud, serverless
==================

Discuss


The top 12 practices
--------------------

1. source control
   5 chars etc.
   but good example of using automated policy enforcement on checkin

2. tech debt and tech assets - code and tests

3. requirements lifecycle (PEP)
   the wrongest part of the agile manifesto
   """ The most efficient and effective method of
conveying information to and within a development
team is face-to-face conversation.
   """
   
   Ya do need to write down the discussion.
   written Proof overcomes authority problems
    it is also way to get everyone discussing
    this only works with really co-locateed and mission focused teams

4. automated build and deployment (dogfood)
   Look, bash is just *fine*
   pyholodeck

5. Documentation and Marketing
6. openness and reviews
7. Progress Not Perfection (YouTube clip)
8. static and other analysis
9. performance mgmt and measuring everything (and making reports on everything)
10. Automatic project mgmt
11. Risk management
12. have fun, try new things, don't be afraid


  
Putting it all together
=======================

* Simplest possible
  We shall build a working web app (about three lines, honest).
  Build it, test it, deploy it to a location locally, and log it.
* systemd, well-behaved services
* simplest app possible
* adding a unit test
* adding a performance test
* building it under python / distutils
* running it under systemd
* running dual, behind load balancer, using weaver/ansible/fabric
* building it on a build server, using .deb files
* build assets -> docs, perf results, test results, .deb files
* Security on microservice
* linting and style and code reviews
* Identity
* host-host services (ntp etc)
* host-app services -> logging, TLS etc
* central services - DNS, metric names,
* code reviews and code promotion
* metrics gatehrinfg
* log mgmt
* rolling out changes
* adding message queues, backend services, passing back identiy
* adding dependancy services - monitoring everything
* CTO dashboard, mission control centre
* bug tracking, feature development


* distributed file systems
  Cephfs, GlusterFS, Lustre, and HDFS

* work queues
  CElery, zeroMQ

* amazon, openstack


Hardware production processes
------------------------------

This is kinda sorta linked to workstations- i have worked at startups
who depended on software and hardware builds.  these are much harder
at proper scale, but it matters

see bunny houng.  


Working conditions

Overtime is bad
http://www.phy6.org/stargaze/Lhipprc2.htm

risk management or project management

office space 


Links
=====
package management
http://nvie.com/posts/better-package-management/

Instrumentation
https://honeycomb.io/blog/2017/01/instrumentation-the-first-four-things-you-measure/

Pki
Cloudflare how to build your own
https://en.m.wikipedia.org/wiki/Hardware_security_module
- France enforces open access to scientific publishing
https://www.openaire.eu/france-final-text-of-the-law-for-oa-has-been-adopted

- pikkety redux
https://news.ycombinator.com/item?id=12417855#12418438

- snowden
https://en.m.wikipedia.org/wiki/NSA_ANT_catalog
http://www.nsaplayset.org


- Whats happening in the world - a sense of perspective
* http://www.digitalattackmap.com/faq/
* also want, wars, trade, shipping, energy, employment, poverty, investment etc.
* some kind of model / mapp for the whole world. where is the money flowing / going?


- Hardende images / servers
https://www.cisecurity.org/services/hardened-virtual-images/

how compare to serverless? 

chaos engineering 
http://principlesofchaos.org


KISS
http://widgetsandshit.com/teddziuba/2010/10/taco-bell-programming.html
there is simple, and there is too simple to easily manage and monitor. 


pentesting and adversarial security
https://www.trailofbits.com
black hat python
the simple ones still work
AES based oracle 


Software development methodologies
https://zwischenzugs.com/2017/10/15/my-20-year-experience-of-software-development-methodologies/


You are not a programmer
product engineers not software engineers 
https://blog.intercom.com/run-less-software/
Three circles of leverage

Future

the great cyber security rewrite(hospital and pumping stations)
the great project management model - tube of water at real time scale
the great company shrinkage - coase

