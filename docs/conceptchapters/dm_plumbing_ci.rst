What is "the plumbing" in the DevManual?
========================================



Principles
-----------

Software is literacy
Software is capital
"let it fail" - dont test in production, but learn from it quickly.
"tech is not a cost centre - dont centralise it", depends on literacy
How can I run this comapny with code and commits
The CEO should merge to master
Automate all the things
Data schemas and ownership
rewrite and refactor are first class learning, so how do we rely on it if its
going to change? This is the depreciation cost - as the factory rots, it must be
maintained, but also improved, the edges smoothed out. The difference between 
putting back to original state and improving used to be hard to see and was
hidden in BAU.  Now BAU is a config file.  What is missing in depreciation is 
we built the (slightly) wrong thing and need to improve it slightly in thousand
ways.

It is highly unlikely and top down project based appraoch will manage a thousand
tiny improvements.  UAT testing wont.  So users need to become scounts -
embedded with developers (and later on developers) and just churn out
improvements all the time.  Eventually the big wins will be small releases.

But what about the vast huge migration project. Yeash tht fine you go do that
too.


Software as capital, capital depreciation is major business expense,
EBITDA is a lie (see Warren Buffet). So software that is just built is a
tech debt but so is not building it.  Software is capital if there is a 
virtual-real connection.  So a wrench that bluetooth records how much it was tightened on which bolt.


devtool

I want a command line tool that gives me

* open a project, and build / open the venv at the project level
* run various lint and other checks for me - precommit but not on the hook
* can do `hub` things
* can reach out to build server
* have a build server - Jenkins





Try to extract all as bullet points here

- logging, event capturing
- production monitoring and QA in production (spectrum)
- unit tests, mocking and stubbing, 
- teat rigs emvironemts
- config handling and environments
- security authentication authorisation access
FIDO / client certs etc
- queues and queueing theory
- runbooks, prod support 
- trade off between urgency and robustness (promtiong code and FFS) 
- use of dashboards
- business metrics growing out of / related to tech metrics
- 


The DevManual is a detailed users guide to setting up
and running software team(s).  And the plumbing are the tools and proccesses (and tools that enforce processes -its turtles all the way down ...), and that can be carried from one organisation to another with minimal changes.  In short we all use the same plumbing, even if the bathroom layout changes.

This is the essence - how to take a working team environment from one company to another, how to have productive teams from day one, or rather how to ensure the lack of productivity comes from the hard people problems not the failure to auto-generate release notes.

Plumbing Features
-----------------

Networking
----------
Wirefuard based VPN
ie netbird to connect all machines at overlay network
Just assume it works. Part if zero-trust networking. Each machine identifies itself coa mTLS




Security
--------
* ssh and client certificates, mutual TLS (mTLS)
* LDAP to client certs
* 

Simple architecture
-------------------

Cloud vs colocation 
Serverless
Pets Then Cattle 
DevTeamMachine 
DataLake and similar storage in office


Release Management
------------------
 
* base OS install
* upgrading OS 
* Release train
* git / github 
* 

RunTime Management
------------------

logging
exceptions
observaility

Front Line support

Moniotring and reporting
------------------------
OpenTelemetry

SDLC
-----
coverage 

testing 
------

project mgmt
-------------

audience mgmt 
--------------




Fundamental principles
----------------------
Simplicity (fits in one brain) and coherent (avoids lots of cases)

High reliability (matches and exceeds (80%) needs if business in normal running and extreme scenarios)

psychological safety

Automation for everything

structured and rational decision making



Team work 
---------
	

Importance of training and certification for systems support



- Logging
- metrics
- observability

https://sre.google/sre-book/table-of-contents/

Chapter 3 - Embracing Risk
Chapter 4 - Service Level Objectives
Chapter 5 - Eliminating Toil
Chapter 6 - Monitoring Distributed Systems
Chapter 7 - The Evolution of Automation at Google
Chapter 8 - Release Engineering
Chapter 9 - Simplicity
Part III - Practices
Chapter 10 - Practical Alerting
Chapter 11 - Being On-Call
Chapter 12 - Effective Troubleshooting
Chapter 13 - Emergency Response
Chapter 14 - Managing Incidents
Chapter 15 - Postmortem Culture: Learning from Failure
Chapter 16 - Tracking Outages
Chapter 17 - Testing for Reliability
Chapter 18 - Software Engineering in SRE
Chapter 19 - Load Balancing at the Frontend
Chapter 20 - Load Balancing in the Datacenter
Chapter 21 - Handling Overload
Chapter 22 - Addressing Cascading Failures
Chapter 23 - Managing Critical State: Distributed Consensus for Reliability
Chapter 24 - Distributed Periodic Scheduling with Cron
Chapter 25 - Data Processing Pipelines
Chapter 26 - Data Integrity: What You Read Is What You Wrote
Chapter 27 - Reliable Product Launches at Scale




Basic plumbing
--------------

Run multiple distributed 
https://www.ray.io/ray-core





144 factor development
----------------------

Imagine you where going to build your web app system.  You have nothing - so you hire - someone who cannot code.  Will 12 factors help? no.  Hire an experienced coder - they are being ong with them some ideas (will need logging) but not the integrated setup

what we want is a full set of tools that act as a platform for development and management - logging and metrics and reporting and time series and audience comma

All the stuff that goes into a full professional .. enterprise .. application

before the actual business rules


law does not have 12 simple rules - that's kind of point of professional  so devmanual is that large body - imagine you have no develope and start from scratch 


- keeping it simple - should fit in one persons head

- Metrics help you keep on the road and there are very few you really need. 
Speed and Stability (google four keys).

Deployment Frequency
Lead Time for Changes

Time to Restore Services
Change Failure Rate
(https://github.com/GoogleCloudPlatform/fourkeys)


We can apply similar four key metrics to the business funnel 

- marketing (lead generation)
- sales (lead conversion)
- onboarding (lead to early customer)
- customer lifecycle (early to ex)

Each of these should also have four keys (or maybe just two) in speed stability terms

Speed:
Percentage loss through funnel (lead quality) - relates heavily to acquisition cost (ie of you spend acquistionnonlymon the exact lead who will convert you can pay almost any acquisition cost)

?ZFeature uptake - how long after release does a feature get used ? 




Stability:

Churn rate as % of MRR 
acquisition cost (total customer cost)

usage % ? that's similar to churn ? 


Upgrade treadmill
-----------------
https://www.cracked.com/article_23108_6-ancient-technologies-u.s.-government-still-relies-on.html

NASA buys 8086 chips off ebay

We have to regularly upgrade our deoendnacies 

RAID project mgmt - risks, assumptions, issues, deoendnacie (issue is a risk / dep / assum that went bad) 


Plumbing and CI
===============

I really wish I had a better term for this next chapter than "plumbing".

The difference between a pile of rocks and a castle is how the rocks interact to strengthen each other.

Whatever that term is, is the term I want to use for this chapter.  But plumbing will do.

Here we describe the various rocks in the modern software world, and try to show how they interact.





build a deploy for (cms) using
spinnaker docker etc 

Front end client trade offs
https://journal.plausible.io/you-probably-dont-need-a-single-page-app

K8s and meshes
--------------
Mutual AUthentication in TLS - ww.nginx.com/blog/do-i-need-a-service-mesh/


The Metaphor of Building Software
=================================

Discuss "The code is the design", and the DevOps idea of code for
everything.  Look at building site in City of London

The office building metahpr is a good one because it also includes a
clear idea of just how much is ocvered in software build chains these
days - from Steel girders and foundations to Glass UIs and bathroom
and waste services in conduits no one sees, to building security and
power outlets.  These things are beasts, and software at even mid size
enterprise scale is a beast too.  Hence my focus on *governance* as
well.

Why does this matter - why try to be full stack? why not specialise?

There are a few, not many, but a few people in companies like Boeing who understand the *entire* airframe - from bernoulli's principle over the wings to the feedback pressure on the pilots control stick - they can reason through the trade offs and keep it all in their heads

A full stack developer is not just a cheaper replacement for hiring 3 specialised ones, (certainly not if I am invoicing you) but is someone who can rationalise the trade offs across the whole stack.

Similarly for a business you need working models for all the interactions - sales, marketing manufacturing etc. And as those models are surfaced and captured in concrete code they can be shared and manipulated - the more the trade offs do not just appear on one person head but are explicitly modelled and tested the closer we get to a programmable company.

So having a full stack is one thing - being able to recreate that stack in a wind tunnel environment and see it respond to new changes is vital for understanding the trade offs across the stack.


As an example the trade offs start to matter at those "order of magnitude" barriers - going from 10x lines of code to 100x, or 10x servers to 100x servers or people.


Stuff Metaphors, what do we do?
===============================

We break almost everything down into services,
run using code-based *products* that generally are
kept in a code repository.

In other words, we run services from code. Together those services
work together to make our offering to the world.

Each repo as a product
----------------------

The organisation, built from scratch every moment
-------------------------------------------------

THis involves test-as-a-spectrum
Pre-prod or no pre-prod?
Generally if you can rebuild all form scratch, and have awesome in prod monitoring you can get away with no pre-prod.  Just its really really hard to pretend.
So I think its much much better to have a pre-prod env where a portion
of prod is fired at the service (replay attacks)

For each *repo* have a product owner
------------------------------------

Yes you heard. If its a repo, its a service, its something someone cares about.
It will have tests and builds and it will matter. Maybe the only users are
three sysadmins - but it still matters that they are customers.

So

* Have a product *vision* (Design the box)
* Have a product *roadmap* (Milestones, and order. DOnt do deadlines)
* Track the metrics 


Business Metrics

- customer account churn %
- Monthly mrr revenue churn %
- net mrr churn 
(check out startups for rest of us) 

Company telemetry from NaSA
-----------------------
https://news.ycombinator.com/item?id=25951003





Is systemd really that bad?
----------------------
comment from archlinux sys init maintainer
https://www.reddit.com/r/archlinux/comments/4lzxs3/comment/d3rhxlc

https://lwn.net/Articles/698822/


Infrastructure matters most
---------------------------
culture is infrastructure 


Submit Queue and any submit queue
---------------------------------

http://delivery.acm.org/10.1145/3310000/3303970/a29-ananthanarayanan.pdf

Uber has SubmitQueue to scale queued commits - but you don't need regression analysis in most cases - you just need to build and test and do so automatically with a queue - a mono repo or a distributed set of repos eventually becomes a mono repo at integration stage

Everything is eventually a monorepo
At integration testing stage everything is a monorepo - so you need a submit queue to manage the process


Testing

TDD is dead
- testing is a roadway not a map - we cannot diacover new things with testing 

We can plan testing upfront if we understand the domain well - this is why (someone) quotes that software is just how much coders understand the problem

sometimes that is why fitnesses testing is excellent - it allows a sme to define the tests not the developer

but mostly the developer need to understand the domain to program it 



Technical Architecture
----------------------

There are lot of "Technical Architects" around these days.  (One of
the problems with not having a software profession the same way we do
in actual architecture is its hard to stop people calling themselves a
Technical Architect. (I mean, just look at *my* business card ...)

A stereotype of TAs is of isolated geniuses (at least they hope to
give that impression) announcing the correct way to build software to
a large team or organisation.

The problem is that if no-one is following yourq architectureal rules,
then you arent an architect.  Architecture is a human function,
persuading others that your way is better.  SOmetimes, we *enforce*
that - through Software Governance (an important idea we will return
to) In the same way that an Architects design for a building is
followed by the builders, or a City Planners rules for a City are
followed by all agents involved.

With a metaphor of building cities, we can see why the idea of Architecture is
an attractive one, but it is really at the scale of the biggest software houses
in the world (Major Banks and financial instituions) that you can see the incredilbe
value of ... City Planning.  We shall call this Software Governance.


real technical architecture 
so, modern functional languages are better because they have better dev friendly features - a good example is pattern matching v if statements- it's just easier to read

but

that's from a standing start - that's sssiminf the code all sits on one place cos if your biz logic is spread out in different suesyens if statements are a unicorn dream

nexus of business logic

in my view technical architecture is about going out and finding the places in the business that need the logic, finding the code, persuading the business of the business case and then right at the end, writing nice code

the inverted pyramid of technical excellent 

opinionated software
--------------------

It has strong views on how it should be used in its domain. This is seen everywhere and it makes software easier to use once you understand its philosophy.  So have an  opinion on how your users should donthings - some users will agree wildly others not so much - but at least they know what you stand for - it's marketing as well as a philosophy 

Workstation
===========

The project mikadosoftware/workstation is the best point to discuss a
develoeprs workstation.  A while back I realised I was spending waaay
too much time altering my worksttion - as an itinerant developer /
contractor I would effectivety be a bum on a seat (in many senses of
the word!).

So I have taken some time to define a repeatable workstation process.
Its not ever going to be perfect but at least it is a valuable start


Workstations are part of overall plumbing.





Plumbing
========

Every software project of any size needs some basic plumbing, things
like a good config approach, a means of linting and testing.  These
things pay dividends throughout the lifetime of a project, making the
simple easy and the hard doable.  WIthout it, you are in trouble.

  
  - :doc:`chapters/errors`
  - :doc:`chapters/config`
  - :doc:`chapters/sphinx`
  - :doc:`chapters/metrics`
  - :doc:`chapters/backup_strategy`
  - :doc:`chapters/logging`
  - :doc:`chapters/metricsAndTracing`
  - :doc:`chapters/network_monitor`

- Runbooks and monitoring


RabbitMQ
- erlang
- erlang
- friendly


Plumbing
-----------------

The goal here is not best practise, but good enough practise that can
scale enough for you not to panic while replacing it.
Our golden goal is to keep things simple.

Simple breaks in simple ways, simple is simple to extend and improve.

Its not that simple is *easy* - often it is the opposite of easy, or quick.

But simple wins out over time. Simple gives great ROI.

I throughly recommend listening to Rich Hickey on this subject (Link)

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


- microservices
- CI / CD
-- metric capture and operations management 
testing
linting and commuting and pre commit hooks
governance
simple worker queues
simple load balancer
simple kubernetes / DNS etc
simple js client 
simple web server 
simple user management 

    
    
Continuous Integration (CI)
===========================

.. pull-quote::
   
   Re-create your company from scratch, every single day.

   
Continuous Integration / Delivery is probably the biggest boon to developer produtivity
since the rise of memory managed languages in the 90's.

Languages like C expected the developer to write code that assigned a
certain amount of memory for a certain data structure - which meant at
the point of writing your code, you had to know *how big the data was
going to be, in say two years time*.

People would get this wrong.  The biggest security risk for many years
was your program accepting a piece of data larger than expected and
simply overwriting its own memory.  With luck your program just
crashed.  Otherwise the hacker was very good, and the piece of data
sent just put their evil code on top of the stack ready to be run.

Nowadays, the business logic we grind out does not need to worry about
such things.  Instead we have the fun of not being entirely sure if
the version of the code we think of is going to run on the server with
the code we think of, using the password we meant and thats if no one
else changed anything.

Lets call these build services.



- :doc:`chapters/environments`
- :doc:`chapters/continuous_integration`
- :doc:`chapters/using_docker`
- :doc:`chapters/sharing_secrets`
- :doc:`chapters/packaging`
- :doc:`chapters/pep8`
- :doc:`chapters/writing_docs`
- :doc:`chapters/random`
- :doc:`chapters/reporting`


 

  
Security
========

Security is principles that are applied across the system. PKI, etc.

Basically trust the maths, and trust nonces.

* :doc:`chapters/ch1 security`
- :doc:`chapters/cookie_testing` #security
- :doc:`chapters/network-testing`
- :doc:`chapters/personal_security`
- :doc:`chapters/pki`
- :doc:`chapters/pkis`


Pki
Cloudflare how to build your own
https://en.m.wikipedia.org/wiki/Hardware_security_module


* GPG and keypairs
* host based security, networks of trust between hosts,  and DMZs
* Kubernetes / Rancher as a host / VM world 

Configuration management and secrets
====================================

Use etcd / kubernetes.
How to build own Docker based co-ordination service - or why kUbernetes is nice.
My USB Secrets

(also Google Peace Dividend)


DataLakes
=========
https://techcrunch.com/2019/04/24/databricks-open-sources-delta-lake-to-make-data-lakes-more-reliable/



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
  

DevOps
======

Falls naturally out of Microservices owned by Small Teams, with Strong Interfaces
SRE and SRE book.
Start small, keep whole thing in overview
Use graphite, and just report out, graph 10 important things
to your team *today*.

* :doc:`chapters/graphite_docker`



Basic Management Reporting
==========================

* reportlib
* SLAs and KPIs - keeping ourselves honest
* focusing upwards to higher levels of leverage
* avoiding the drumbeat of deadlines, and panic, and agreeing goals based on
  data / 20% most effective things to fix.
* Make one weekly report *today*


Style guide
----------
https://medium.com/deepnote/building-a-design-system-at-a-startup-7b352d9875b3

Breach disclosure
-----------------
https://www.troyhunt.com/data-breach-disclosure-101-how-to-succeed-after-youve-failed/

Audience comms
--------------
- release announcements
- feature launches
- breach disclosure
- password reset (don't use passwords)
- user manual 
- 


Cool diagramming
-----------------
https://pikchr.org/home/doc/trunk/homepage.md


The scope
=========

How much software is there

https://news.ycombinator.com/reply?id=17994976&goto=item%3Fid%3D17994600%2317994976
https://www.theatlantic.com/technology/archive/2017/09/saving-the-world-from-code/540393/

the google peace dividend
https://news.ycombinator.com/reply?id=17996693&goto=item%3Fid%3D17995053%2317996693

Data schedulaers /  Processors / BigIsh Data
Apache Beam
https://stackoverflow.com/questions/43581127/what-are-the-benefits-of-apache-beam-over-spark-flink-for-batch-processing




Soft Skills
===========

Skills for individual developer
===============================

Software Governance as a force multiplier implies a number of things
One is that each individual contributor should have the same minimal
set of skills, and perform those common skills in a similar fashion.

An obvious example might be making good source code commits, and so there
would need to be an internal "standard" for commits. 

This of course implies ... training. Training your staff to be better
at their jobs, something that the commitment-less culture these days
seems to mitigate against.  Things will change - our "principle" of a
change to Roald Coase's equilibrium point means smaller companies, and
greater need to standard interfaces and so more need to train your
people to do it the right way.


You are not a programmer
product engineers not software engineers 
https://blog.intercom.com/run-less-software/
Three circles of leverage


Profesional Stuff you should know 
---------------------------------


- :doc:`chapters/jupyter`
- :doc:`chapters/kernel_and_world`
- :doc:`chapters/misc`
- :doc:`chapters/statistics`
* :doc:`chapters/sourcecontrol`
* :doc:`chapters/keypairs`
- :doc:`chapters/databases`
- :doc:`chapters/DNS`
- :doc:`chapters/email`??
- :doc:`chapters/source-control`    
- :doc:`chapters/using_burpsuite`

Actually personal stuff

* :doc:`chapters/careermanagement`
* :doc:`chapters/interviewQuestions`
- :doc:`chapters/interviews_algorithms`
- :doc:`chapters/basic_seo`

Misc
- :doc:`chapters/generative`


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


* Culture, and hostile cultures
* trust, safe space, I dont know
* learning
* lunch
* Keep on in good faith
* Google HR managemenet
* management fixes are the middle ground - 


* serverless is cheaper. Please rewrite everything now.
* Overtime is bad
* remote working is more productive
* Risk management beats project Management
  
- :doc:`chapters/software-capital`
- :doc:`chapters/software-estimation`
- :doc:`chapters/project_mgmt`



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


Visualisation
-------------
D3.js is good
https://github.com/apache/incubator-superset/blob/master/README.md

Typography and Design
---------------------
https://practicaltypography.com/font-basics.html

Really most of what I am going to say on this will be in lib-report


Logging
-------

How to log 
Capturing metrics not logs
Logging as part of governance and security
Logging as governance - everyone uses logging to same centralised monitored logging
Monitor for logging governance - ie Confiedntial / personal data vs proprietary data 


Don't use exceptions as flow control
Don't bury exceptions in logs

The right way to do this is to write log.error(msg) and then have logs grepped for ERROR flag and then log that out to graphite so it is clear what errrors exist

Place that in the project / repo weekly operational report


Business Worst Case "Stop Loss"
-------------------------------

These are the business rules that prevent disaster - that sort of things you would expect a human to say "WTF" about and start calling for help

One thing it is vital to agree with the business is not just what are our SLAs but what are our stop losses - what are the business boundaries that if they are crossed an emergency should be sounded - and what is the emergence safe state to take ?


Lessons from KightFrank

- have a common error raising system - that is not email

- Debug / Info / Warn / Error / Critical / StopLoss

- These are measured at the level of integration tests etc


- invest in preproduction environments 

- advocate for risk mitigation costs in your industry - cf knight frank and Goldman 


https://www.kitchensoap.com/2013/10/29/counterfactuals-knight-capital/

Don't use counterfactuals for post mortems
----------------

What they did not do, what they should have done is not the point - the point is "what did they do" and "why did that make sense to them at the time" - we are trying to work out why the organisations model of reality was at odds with reality, and how to better align the two 

That is basically post mittens

  
UI for idiots
=============


- :doc:`chapters/UIDesign`
- :doc:`chapters/ajax`
- :doc:`chapters/bootstrap_index`
- :doc:`chapters/building_bootstrap`
- :doc:`chapters/coloursfortheweb`
- :doc:`chapters/lessrest`

  

The dev manual - a proof of concept
===================================


Example Micro-Service eco-system


I want to have a detailed exmaple - so here is a functioning, internal and external
web based, docker based complete setup.

Docker AWS
----------

We shall build a complete enterprise service in the cloud - because we can

- :doc:`chapters/time_in_docker`
- :doc:`chapters/time`


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
  need automated error trapping and user bug reporting
* distributed file systems
  Cephfs, GlusterFS, Lustre, and HDFS
* work queues
  CElery, zeroMQ
* amazon, openstack



  
Micro-HowTos
============
(Misc)

- :doc:`chapters/corefile_debugging`
- :doc:`chapters/futuretech`
- :doc:`chapters/bothPythons`
- :doc:`chapters/emacs`
- :doc:`chapters/nginx`

- :doc:`chapters/gh-pages`
- :doc:`chapters/nonblockwsgi`
- :doc:`chapters/wsgi_simple_app`
- :doc:`chapters/wsgi_test`
- :doc:`chapters/wifi`
- :doc:`chapters/ssl-tls`
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
   "Lines of code spent"
   
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


Google Peace dividend and Distributed computing
===============================================

THe new capabilities

Kebernetes (the micro services as cattle)
Beam / spark - distributed parallelised computing - the new scheduler
Tensorflow - AI
(Serverless)

But underneath this we have basics of plumbing, philoshphy and so on




Software development methodologies
https://zwischenzugs.com/2017/10/15/my-20-year-experience-of-software-development-methodologies/

Future
======

the great cyber security rewrite(hospital and pumping stations)
the great project management model - tube of water at real time scale
the great company shrinkage - coase


https://allarsblog.com/2018/03/16/confessions-of-an-unreal-engine-4-engineering-firefighter/

Club
defence at scale
https://brandur.org/idempotency-keys


being better developer
https://news.ycombinator.com/item?id=16863591

i don't agree really - there is two kinds - being a master of anything
is mastery over self (miyazoko tea master) or specialisation is for
insects.  or rather you need experience of all the tools

i suspect he is just complaining that someone is hammering in a nail
with a hammer, then a screwdriver, then a wrench ...


One New Skill Evening Club
--------------------------

Functional Reactive programming and DAGs
-----------------------------------------

"out of the tar pit" marks/moseley - over simplified it says complexity is the problem in software, and there are two types of complexity - state and control.

A third type is information failures or shooting ourselves in the foot.  

There are then three fixes for the world

- functional programming for managing state (immutable data)

- but data does chnage - so how to handle it? datomic?? bi or tri temporality 

- functional reactive programming and dag - and what about SAC

apache spark is fundamentally one of these. which will win?? hard to say but my money is one language-data tie ups (erlang mnesia, clojure datomic)

https://blog.janestreet.com/introducing-incremental/
https://blog.janestreet.com/breaking-down-frp/

Basically don't waste time on recomputing
Which is why Vitrual don can be a dag


Why graphs matter. And who cares


Scope and coverage

- NoSQL and scale and distribution versus consistency 
- rise of functional languages
- the declarative language we all know - SQL
- datomic and clojure
- out of the tar pit (mosley and marks) - two problems are state and control - functional solves some of state but state of data changes.  how to handle changing data ? 
- bitemproarilty and tritemoorality - date we wrote it down, date fact was true, date we are querying about.

- Information management

- systems analysis 

- domain analysis

- leave me alone i am thinking

- stop micro managing 

- no you cannot have an estimate only a direction.  deadline? maybe. try a business solution

- do it smaller first 

- mission and process wins more often 

- ownership of small area wins as well.


Have a incident response book

Have a run book
- basic principle is automate the shit out of it



Software Mind
Moop and IOT
moop

My data collected on my behalf and analysed for my benefit - shared and communal benefit


iot fridge 
will allow my slow thinking to order for me this allowing me to win back control from the bio-hacking of large corps

Ethical Open Source

https://librarianshipwreck.wordpress.com/2018/08/24/striving-to-minimize-technical-and-reputational-risks-ethical-os-and-silicon-valleys-guilty-conscience/


Privacy - telcos / ISPs are worse

https://www.techdirt.com/articles/20180320/10281539457/if-youre-pissed-about-facebooks-privacy-abuses-you-should-be-four-times-as-angry-broadband-industry.shtml


#https://docs.typo3.org/typo3cms/extensions/sphinx/AdvancedUsersManual/RenderingPdf/CustomizingRendering.html




Articles
========

This is the articles linked above.

.. toctree::

    chapters/microservices
    chapters/serverless
    chapters/architectural_overview
    chapters/best_approach_to_software_quality
    chapters/application-performance-management
    chapters/systemd
    chapters/technical_capabilities
    chapters/terminal
    chapters/testing
    chapters/text_mining
    chapters/sphinx
    chapters/errors
    chapters/config
    chapters/sphinx
    chapters/metrics
    chapters/backup_strategy
    chapters/logging
    chapters/metricsAndTracing
    chapters/network_monitor
    chapters/environments
    chapters/continuous_integration
    chapters/using_docker
    chapters/sharing_secrets
    chapters/packaging
    chapters/pep8
    chapters/writing_docs
    chapters/random
    chapters/reporting
    chapters/jupyter
    chapters/kernel_and_world
    chapters/misc
    chapters/statistics
    chapters/sourcecontrol
    chapters/keypairs
    chapters/databases
    chapters/DNS
    chapters/email
    chapters/source-control    
    chapters/using_burpsuite
    chapters/careermanagement
    chapters/interviewQuestions
    chapters/interviews_algorithms
    chapters/basic_seo
    chapters/generative
    chapters/ch1 security
    chapters/cookie_testing #security
    chapters/network-testing
    chapters/personal_security
    chapters/pki
    chapters/pkis
    chapters/unittests
    chapters/browser-automation
    chapters/graphite_docker
    chapters/time_in_docker
    chapters/time
    chapters/software-capital
    chapters/software-estimation
    chapters/project_mgmt
    chapters/agile_estimation
    chapters/SoHo1
    chapters/themes
    chapters/urljoin
    chapters/veryquickMBA
    chapters/aspell
    chapters/mikado-doc-manager
    chapters/aws_dns
    chapters/cabling_hardware
    chapters/filesharing
    chapters/freewifi
    chapters/highAvailability
    chapters/laptop
    chapters/loadbalancing
    chapters/mail-handling
    chapters/virtualbox

    chapters/usbdisk
    chapters/UIDesign
    chapters/ajax
    chapters/bootstrap_index
    chapters/building_bootstrap
    chapters/coloursfortheweb
    chapters/lessrest
    chapters/corefile_debugging
    chapters/futuretech
    chapters/bothPythons
    chapters/emacs
    chapters/nginx
    chapters/gh-pages
    chapters/nonblockwsgi
    chapters/wsgi_simple_app
    chapters/wsgi_test
    chapters/wifi
    chapters/ssl-tls
    chapters/workstation-install
    chapters/workstation
    chapters/webdev
    chapters/webtest
    chapters/well-behaved-services
    chapters/using_github__ssh
    chapters/podcast
    chapters/postgres-cheatsheet
    chapters/pxeboot
    chapters/python_warts
    chapters/routes
    chapters/rssso
    chapters/samba
    chapters/securityoverview
    chapters/sed_sort
    chapters/seo-case-study
    chapters/Managing time in docker containers </chapters/time_in_docker>

Google Plumbing pdf
https://arxiv.org/ftp/arxiv/papers/1702/1702.01715.pdf#page10

Incident response
-----------------
https://response.pagerduty.com/resources/anti_patterns/

SEO and funnels
---------------
https://www.wordstream.com/quality-score
https://www.indiehackers.com/@AntonElfimov/we-wasted-50k-on-google-ads-so-you-don-t-have-to-af688095de

Important concepts:
Sales funnel - 
Awareness ladder - you need to attract people to the site with keywords - either organic search keywords or paid for keywords - but their keywords "betray" how aware of the problem space you are working in - "log all the time all my team spends automatically" to "punchclock " - PR / blog is very good at the bottom of the awareness ladder and targeted keywords at the top
- irrespective of the funnel


AWS Virtual Procate cloud

https://grahamlyons.com/article/everything-you-need-to-know-about-networking-on-aws
https://news.ycombinator.com/item?id=18925350




Out of date already
===================

chapters/virtualisation
chapters/virtualbox`
chapters/usbdisk`


https://en.wikipedia.org/wiki/Fractal_tree_index

Amazon AWS examples / Vendor lock-in
=====================================

I have migrated all of the code here "to the cloud".  This tries to include avoiding the lift and shift paradigm and using the cloud providers own proprietary versions of oss services - see discussion on google paas vs aws iaas

I am even going so far as to try serverless 

but this is because there is value in cloud native approaches vs cloud lift and shift - and more value (or less cost) in serverless

but lock-in is real - but is a trade off if the cost of lockin 

User experience and page loading
--------------------------------

https://www.johnwdefeo.com/articles/seo-for-engineers


Distributed Batch Programming
------------------------------

EC2 docker and mesos
http://mesos.apache.org
Example app is a friday night batch that produces the TPS report (!)

Just run something ok !

Then micro services deployed into cloud with kubernetes (different to mesos)

And a data lake ... ??? 

SRE Software Reliability Engineering
-------------------------

http://rachelbythebay.com/w/2020/08/09/lib/

This is important but it is not about Google Scale.  Google scale is where the one in a million failure happens this week. Twice.  But that is trying to fix the bugs that happen say outside the 2nd standard deviation (98%) 

We are interested in fixing bugs where it affects reliability.  I think this is something like std dev spread - 68% 

example is writing a file or a dot file that might end up getting used in diff threads

just write with normal io - probably won't get used in threads probably won't collide

but if it does collide then do something like write copy as temp and mv file over afterwards in a quick little library (fileio-lib)

that will get us to the 98% level - after that real seriousness takes over

So I am going to try and build devmanual as series of structured points - the basic teaching the simple stuff - then hand off to libraries for second std dev and the rest is up to you 
