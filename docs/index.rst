=====================
Overview of DevManual
=====================

..

  Every H1 becomes entrypoint chapter, every chapter is included under H1
  Also intersphnx with softwqre mind
  
Software is *hard*.  And it's getting harder.  As Software starts
to eat more of the world, then the stakes get higher - and the cost of
mistakes become more traumatic, and the rewards become sky-high.

This book focuses on the ground level foundations of desigining,
building and running software - from a SoHo office to the vast scales of
Silicon Valley tech giants, all development processes have similar cores.

Successful software is *partly* a technical endeavour. Get that wrong
and nothing else will go right.  But the hard-technical stuff is 20%
of good software - the other 80% shades into softer human skills, good
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

These `why-tos` are an important part of a Dev Manual.

A seperate book, The Software Mind, is an even higher abstract level,
looking at how these things playout on a bigger scale.  But for now
we are looking at how to combine docker, scripts, and servers into a
complete, working engineering team.

The software behind this Dev Manual is available as Free or Open
Source Software, under a permissive license, and all the third-party
software used as building blocks are chosen for similar licenses.

Please note that the examples and frameworks in this book are
specific to the Python Language. This is simply because I am most
familiar with that.  However *all* the lessons drawn can be applied
to any modern language.  

Plumbing
========

Every software project of any size needs some basic plumbing,
things like a good config approach, a means of linting and testing.
These things pay dividends throughout the lifetime of a project,
making the simple easy and the hard doable.  WIthout it, you are in trouble.

  
  - error handling
  - config
  - todo
  - docs
  - logging
  - metrics (graphene)
  - activity reporting
  - performance metrics
  - :doc:`chapters/backup_strategy`
  - :doc:`chapters/centralised_logging`
  - :doc:`chapters/logging`
  - :doc:`chapters/metricsAndTracing`

Architecture and airy-fairy stuff
=================================

Serverless
Abstraction
Rick Hickey on simple vs easy
  How does a bug get into production? It is written
  And it passes the tests.  So if you have tests, and you refactor, how
  do you prevent that bug?
  Need to be able to *reason* about code. Which is why 900 npm packages worry me.

  Tests are *regression* tests. They are written so that having written some code to
  do a thing, you dont later on screw it up and it stops doing that thing.  Tests are
  almost by defintion, backwards looking.

  

Skills for individual developer
===============================

* Source control
* ALgorithm design, interview questions
* Salary negotiation, presenting a interface to business and collegues (dont call yourself a programmer)
* :doc:`chapters/commit-messages`
* :doc:`chapters/keypairs`




* :doc:`chapters/git`
* 
    
    
Security
========

* :doc:`chapters/ch1 security`
  
Testing
=======

- :doc:`chapters/browser-automation`

- :doc:`chapters/cookie_testing` #security
- :doc:`chapters/gh-pages`
- :doc:`chapters/microservices`
- :doc:`chapters/network_monitor`
- :doc:`chapters/network-testing`
- :doc:`chapters/packaging`
- :doc:`chapters/pep8`
- :doc:`chapters/personal_security`
- :doc:`chapters/pki`
- :doc:`chapters/pkis`
- :doc:`chapters/nginx`
- :doc:`chapters/nonblockwsgi`
- :doc:`chapters/wsgi_simple_app`
- :doc:`chapters/wsgi_test`
- :doc:`chapters/wifi`
- :doc:`chapters/workstation-install`
- :doc:`chapters/workstation`
- :doc:`chapters/writing_docs`
- :doc:`chapters/webdev`
- :doc:`chapters/webtest`
- :doc:`chapters/well-behaved-services`
- :doc:`chapters/using_burpsuite`
- :doc:`chapters/using_github__ssh`
- :doc:`chapters/podcast`
- :doc:`chapters/postgres-cheatsheet`
- :doc:`chapters/pxeboot`
- :doc:`chapters/python_warts`
- :doc:`chapters/random`
- :doc:`chapters/reporting`
- :doc:`chapters/routes`
- :doc:`chapters/rssso`
- :doc:`chapters/samba`
- :doc:`chapters/securityoverview`
- :doc:`chapters/sed_sort`
- :doc:`chapters/seo-case-study`


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

- :doc:`chapters/continuous_integration`
- :doc:`chapters/using_docker`
 
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

Common Architectural choices
----------------------------

Discuss and review common architectural choices

* cacheing
* containerisation
* REST API


WSGI Server
===========

WSGI is an amazingly cool ... idea.  It just reminds you that *all* web servers are doing
is passing text strings up and down a request/response cycle.  Remeber CGI? Its still that
simple.

(all WSGI stuff in here)


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


inline :doc:`chapters/Managing time in docker containers </chapters/time_in_docker>`

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







Business and Software
=====================
serverless
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


Project Management
------------------
- :doc:`chapters/agile_estimation`
- :doc:`chapters/SoHo1`
- :doc:`chapters/ssl-tls`
- :doc:`chapters/themes`
- :doc:`chapters/urljoin`
- :doc:`chapters/veryquickMBA`




Foundational dependancies (like 12 factor)
------------------------------------------
- :doc:`chapters/databases`
- :doc:`chapters/DNS`
- :doc:`chapters/email`??

Management / Governance
-----------------------
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


Reporting, todo
---------------
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


Docker AWS
----------
- :doc:`chapters/time_in_docker`
- :doc:`chapters/time`


Tech depths
-----------
- :doc:`chapters/corefile_debugging`
- :doc:`chapters/futuretech`

UI
--
- :doc:`chapters/UIDesign`
- :doc:`chapters/ajax`
- :doc:`chapters/bootstrap_index`
- :doc:`chapters/building_bootstrap`
- :doc:`chapters/coloursfortheweb`
- :doc:`chapters/lessrest`

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


Overview
--------
- :doc:`chapters/manuallayout`







