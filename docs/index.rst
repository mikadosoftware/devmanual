=====================
Overview of DevManual
=====================

..  ::

  Every H1 becomes entrypoint chapter, every chapter is included under H1
  Also intersphnx with softwqre mind
  
As Software starts to eat more of the world, the need for good
software practises, and good software teams will only increase.
You see, I view software not as some other industry or sector that has
positive growth prospects in a consultants 2x2 powerpoint presentation.

Software is the new form of literacy.  This is a revilution on the
scale of moving from illiterate to literate societies - this is not
going away soon.  And so we need to find the best ways to build
software - to invent the new Publishing houses, the new scriptoreums,
the new Newsrooms.

This book focuses on the ground level foundations of desigining,
building and running software - because, from a SoHo office to the
vast scales of Silicon Valley tech giants, all development processes
have similar cores.

Successful software is *partly* a technical endeavour. Get that wrong
and nothing else will go right.  But the hard-technical stuff is say 50%
of good software - the other 50% shades into softer human skills, good
and bad "management practises" and as we shall see, into national and
even global politics.

Format
======

This manual is both a long list of `how-to` chapters, covering ntp
servers or SQL connections. These are useful, in-the-trenches guides
to certain necessary software *capabilities*.  Then there are slightly
higher level chapters - like this one, that take a particular theme,
and while they link to the underlying how-tos, these are much more
`why-tos`.

These `why-tos` are an important part of a Dev Manual.  *How* is just a
group of people peforming the same actions next to each other. *Why*, is
a team.

A seperate book, The Software Mind, is an even higher abstract level,
looking at how these things playout on a bigger scale.  But for now
we are looking at how to combine scripts and servers into a
complete, working engineering team.

The software behind this Dev Manual is available as Free or Open
Source Software, under a permissive license, and all the third-party
software used as building blocks are chosen for similar licenses.

Please note that the examples and frameworks in this book are
specific to the Python Language. This is simply because I am most
familiar with that.  However *all* the lessons drawn can be applied
to any modern language.  

Simplicity
==========

Our golden goal is to keep things simple.

Simple breaks in simple ways, simple is simple to extend and improve.

Its not that simple is *easy* - often it is the opposite of easy, or quick.

But simple wins out over time. Simple gives great ROI.

I throughly recommend listening to Rich Hickey on this subject (Link)

So please keep in mind - we aim for simple.  Even if our day to day work pushes us
to quick and easy and complicated.  We need to push back.

Saying No
=========

Which takes us to our next issue. It is tied up with professionalism, with
power structures and personal identity.  It is saying no to writing bad code

Or rather saying yes to writing good enough code.

(expand)


Plumbing
========

Every software project of any size needs some basic plumbing,
things like a good config approach, a means of linting and testing.
These things pay dividends throughout the lifetime of a project,
making the simple easy and the hard doable.  WIthout it, you are in trouble.

  
  - :doc:`chapters/errors`
  - :doc:`chapters/config`
  - :doc:`chapters/sphinx`
  - :doc:`chapters/metrics`
  - :doc:`chapters/backup_strategy`
  - :doc:`chapters/logging`
  - :doc:`chapters/metricsAndTracing`
  - :doc:`chapters/network_monitor`


    
Continuous Integration (CI)
===========================

There is a very rough history of computing which goes like this -
1940s to 1960s, was a time just getting the basics right, hardware was
weak and the first compiled language took until 1957 to appear.  The 60s to 70s
as a time of moving into large niches, like medical devices, corporate accounting systems.
The 80s was the rise of the Relational Database, the 90s the break out of the web,
democratising access to information inside and outside corporations, and 2000s the
rise of new languages.

Just as the spread of Memory managed languages (Java, Python, C#) in
the 90s gave developers a big boost in avoiding productivity traps (ie
spending hours debugging) Continuous Integratgion is providing the
same sort of productivity gain fro developers.  There are many
components to a large build chain across many servers.  I have called
these Build Services

- :doc:`chapters/environments`
- :doc:`chapters/continuous_integration`
- :doc:`chapters/using_docker`
- :doc:`chapters/packaging`
- :doc:`chapters/pep8`
- :doc:`chapters/writing_docs`
- :doc:`chapters/using_burpsuite`
- :doc:`chapters/random`
- :doc:`chapters/reporting`

    
Architecture and airy-fairy stuff
=================================

Serverless
Abstraction

A standard approach to architecture - break this only once you have found
by measuring that its not suitable for your use case

We can see a complete enterprise level solution to pushing out new code.

- :doc:`chapters/microservices`
- :doc:`chapters/serverless`
- :doc:`chapters/nginx`

  
Skills for individual developer
===============================

Profesional Stuff you should know 
---------------------------------
- :doc:`chapters/bothPythons`
- :doc:`chapters/emacs`
- :doc:`chapters/generative`
- bash
- functional programming and coding tests and graph 
- :doc:`chapters/interviews_algorithms`
- :doc:`chapters/jupyter`
- :doc:`chapters/kernel_and_world`
- :doc:`chapters/misc`

* :doc:`chapters/sourcecontrol`
* :doc:`chapters/interviewQuestions`
* :doc:`chapters/careermanagement`
* :doc:`chapters/keypairs`


- :doc:`chapters/databases`
- :doc:`chapters/DNS`
- :doc:`chapters/email`??
    
    
Security
========

* :doc:`chapters/ch1 security`
- :doc:`chapters/cookie_testing` #security
- :doc:`chapters/network-testing`
- :doc:`chapters/personal_security`
- :doc:`chapters/pki`
- :doc:`chapters/pkis`



Mission statements 
https://www.amazon.jobs/principles

* GPG and keypairs
* host based security, networks of trust between hosts,  and DMZs
* Kubernetes / Rancher as a host / VM world 


Testing - a heresy
==================

Rick Hickey on simple vs easy
  How does a bug get into production? It is written
  And it passes the tests.  So if you have tests, and you refactor, how
  do you prevent that bug?
  Need to be able to *reason* about code. Which is why 900 npm packages worry me.

  Tests are *regression* tests. They are written so that having written some code to
  do a thing, you dont later on screw it up and it stops doing that thing.  Tests are
  almost by defintion, backwards looking.

- :doc:`chapters/unittests`
- :doc:`chapters/browser-automation`
  


 
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

   "What about the frameworks. Think of the frameworks"

Yes, at some point the 'one guy opens up one file' approach is of
course going to fail.

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


Code base governance
--------------------

Style, coverage
ast based syntax checking
use of non-standard plumbing
`Code as a crime scene`
Static Analysis and raising all boats.
ast and how to do syntax checking like pyflake - how to build own rules 


- :doc:`chapters/application-performance-management`
- :doc:`chapters/architectural_overview`
- :doc:`chapters/basic_seo`
- :doc:`chapters/statistics`
- :doc:`chapters/systemd`
- :doc:`chapters/technical_capabilities`
- :doc:`chapters/terminal`
- :doc:`chapters/testing`
- :doc:`chapters/text_mining`
- :doc:`chapters/source-control`
- :doc:`chapters/sphinx`


Systems governance
------------------

Governance (dev to prod access etc) (As infrastructure as code
increases, this sort of thing is more possible)


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

DevOps
========

SRE and SRE book.
Start small, keep whole thing in overview
Use graphite, and just report out, graph 10 important things
to your team *today*.


Docker AWS
----------
- :doc:`chapters/time_in_docker`
- :doc:`chapters/time`


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


Soft Skills
-----------

* Culture, and hostile cultures
* trust, safe space, I dont know
* learning
* lunch
* Keep on in good faith
* Google HR managemenet
* management fixes are the middle ground - 



Business and Software
=====================

* serverless is cheaper. Please rewrite everything now.
* Overtime is bad
* remote working is more productive
* Risk management beats project Management
  
- :doc:`chapters/software-capital`
- :doc:`chapters/software-estimation`
- :doc:`chapters/project_mgmt`

Project and Programme management
--------------------------------

It if ain't got a ticket dont work on it
If it ain't possible to rollup tickets you dont know where you are going
A backlog out of context is just a horror
There is nothing wrong with top-down design (side??)
Backlog for the whole company


Project Management
------------------
- :doc:`chapters/agile_estimation`
- :doc:`chapters/SoHo1`
- :doc:`chapters/ssl-tls`
- :doc:`chapters/themes`
- :doc:`chapters/urljoin`
- :doc:`chapters/veryquickMBA`


CTO dashboards and Business Process Dashboards
----------------------------------------------

Dashboards matter
The basics of code quality can be in dashboard.
The basics of production health can be in dashboard
Putting a business process into dashboard is powerful - use Graphite and "light beam trackers"


- :doc:`chapters/aspell`
- :doc:`chapters/mikado-doc-manager`
AWS and old school
------------------
- :doc:`chapters/aws_dns`
- :doc:`chapters/cabling_hardware`
- :doc:`chapters/filesharing`
- :doc:`chapters/freewifi`
- :doc:`chapters/highAvailability`
- :doc:`chapters/laptop`
- :doc:`chapters/loadbalancing`
- :doc:`chapters/mail-handling`
- :doc:`chapters/virtualbox`
- :doc:`chapters/virtualisation`
- :doc:`chapters/usbdisk`

UI for idiots
=============
UI
--
- :doc:`chapters/UIDesign`
- :doc:`chapters/ajax`
- :doc:`chapters/bootstrap_index`
- :doc:`chapters/building_bootstrap`
- :doc:`chapters/coloursfortheweb`
- :doc:`chapters/lessrest`

  

The dev manual - a proof of concept
===================================

This is a "business in a box" - it kind of does not matter what the
buisness is, its just that all the software engineering goodness
that I describe here needs to be ... dmeonstrable - so I have built a
example business (and launching a real product) with it.

Its WIP

* simplest app possible
* adding a unit test
* adding a performance test
* building it under python / distutils
* running it under systemd
* running dual, behind load balancer, using weaver/ansible/fabric
* building it on a build server, using .deb files
* build assets -> docs, perf results, test results, .deb files
* Security on microservice
* Identity
* host-host services (ntp etc)
* host-app services -> logging, TLS etc 
* central services - DNS, metric names,
* code reviews and code promotion
* metrics gatehrinfg
* log mgmt
* rolling out changes
* incident mgmt (incidents, SLAs, uptime measurements from metrics etc etc)
* adding message queues, backend services, passing back identiy
* adding dependancy services - monitoring everything
* CTO dashboard, mission control centre
* bug tracking, feature development

  
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



  
Micro-HowTos
============

- :doc:`chapters/corefile_debugging`
- :doc:`chapters/futuretech`


- :doc:`chapters/gh-pages`
- :doc:`chapters/nonblockwsgi`
- :doc:`chapters/wsgi_simple_app`
- :doc:`chapters/wsgi_test`
- :doc:`chapters/wifi`

- :doc:`chapters/workstation-install`
- :doc:`chapters/workstation`
- :doc:`chapters/webdev`
- :doc:`chapters/webtest`
- :doc:`chapters/well-behaved-services`
- :doc:`chapters/using_github__ssh`
- :doc:`chapters/podcast`
- :doc:`chapters/postgres-cheatsheet`
- :doc:`chapters/pxeboot`
- :doc:`chapters/python_warts`
- :doc:`chapters/routes`
- :doc:`chapters/rssso`
- :doc:`chapters/samba`
- :doc:`chapters/securityoverview`
- :doc:`chapters/sed_sort`
- :doc:`chapters/seo-case-study`
- :doc:`chapters/Managing time in docker containers </chapters/time_in_docker>`










The top 12 practices - a summary
--------------------------------

Like Joel's checklist, this is a checklist for things you need
Its trying to get ot barebones


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


https://allarsblog.com/2018/03/16/confessions-of-an-unreal-engine-4-engineering-firefighter/


defence at scale
https://brandur.org/idempotency-keys


being better developer
https://news.ycombinator.com/item?id=16863591

i don't agree really - there is two kinds - being a master of anything
is mastery over self (miyazoko tea master) or specialisation is for
insects.  or rather you need experience of all the tools

i suspect he is just complaining that someone is hammering in a nail
with a hammer, then a screwdriver, then a wrench ...
