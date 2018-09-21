============
SoftwareMind
============

Introduction
============

I have twenty years experience "in the trenches" of software
developmnet - writing commercial and open source software for cutting
edge ISPs, major financial houses and not-for-profit organisations, in
big offices, tiny offices or on globally distributed teams.  Some were
big successes, some ... well, less so.  And in each case the things
that worked well all shared similar cores.

If I found myself on a team missing some of these vital components
(from automated tests to zookeeper like config) I would work to
install or just plain build the tools we needed to succeed.  Each
component part was only worth the effort it if was an essential part of how software
*shoukd* be made - this book is just a walk through all of those
component parts - it is trying to be a "software team in a box".

My ultimate goal is provide a software team with exactly
what is needed to hit the ground running.

Of course successful software cannot ignore people - it obviously
is *partly* a technical endeavour. Get that wrong and nothing else
will go right.  But the hard-technical stuff is say, 50% of good
software - the other 50% shades into softer human skills, good and bad
"management practises" and as we shall see, into national and even
global politics.

In writing this book I tried to create a good structure, consistent
and meaningful, like any good coder, but frankly this has turned into
a much more comfortable and sprawling bazaar of ideas and how-tos.
There is a `lesson here. <http://cathedralandbazaar>`_. [#f1]_ 


The Chairman's tricky Question
==============================

Some time ago I was asked by the Chairman of the Board what one thing
he could do to make sure all these damn software projects were under
control.

I could only boil it down to two

* Require *every* project to automatically deploy to a prod-parallel
  environment, *every* day, their most recent approved, tested code
  and post their test results.

* Reduce every project to small teams, controlling everything from dev
  to production, with strong interfaces to other services they might
  need.

These two seem to capture pretty much everything that seems important
in software.  It is also treating a company much like a code base -
being able to rebuild it from scratch instantly, and having in-depth
resilience so if some small parts fail, everything does not stop.


The Software Mind
=================

It is hard to understand how software engineering fits into the modern
world without a few *philosophical* underpinnings.  I will bounce in and
around some of these ideas but it is worth having a quick riffle through some.

* The size of companies (in terms of employees) is changing. Mostly we shall
  see pressure to have msaller companies, but the success of companies that are essentially
  federations of very small companies is impressive (see Amazon)
  The Economist Roald Coase is important here, for we are seeing a shift in the curve that determines
  how small a company can be

* Software Literacy is an important concept - it is hard for us to recongise how literacy has shaped us and
  our society. Look at road signs. And it is hard to recognise how much software literacy will change
  companies, socieites and opportunities.
  This is the underlying message of "Software is eating the world" - we have made a world that only works because
  everyone in it can read and write.  We are making a new world, where everyone will be expected to code.

* Software is subject to politics, but the importance of software is leaving development of
  softre to be driven by people who do not "understand" software (see literacy), and it is also leading to substandard
  software being allowed.  Regulation and professinalisation is likely to affect that.

* Almost all software development is about exploring.  And two things
  we can say about exploration - you never know how long it is going
  to take and it often is risky.  Guess what the vast majority of project planning and management try and do
  They demand time estimates and plan other items around that, and they do not schedule resources to mitigate risk.
  In my experience, software takes as long as it takes.  All the running around and shouting, the pressure and the politics
  are just ways of selling the inevitable time / money / scope trade offs.

* The Google Peace Dividend - three / four major areas of computing beig transformed by OSS
  
* Pikety redux
  - Labour lost, capital won (the reaosn wages not  subject to suply demand)
  - the great hollowing out
  - literacy and automation
  - Snowden was also right - data and pollution 
- snowden
https://en.m.wikipedia.org/wiki/NSA_ANT_catalog
http://www.nsaplayset.org
- Whats happening in the world - a sense of perspective
* http://www.digitalattackmap.com/faq/
* also want, wars, trade, shipping, energy, employment, poverty, investment etc.* 
some kind of model / mapp for the whole world. where is the money flowing / going?

* Software literate company
  The value of building good software as a company
  tps://www.ben-evans.com/benedictevans/2018/8/29/tesla-software-and-disruption

  That the record of software coming in to disrupt industry is good - it's hard to learn software.  As a company
  this book is about having software in your company DNA









Principles
==========

Simplicity
==========

Our golden goal is to keep things simple.

Simple breaks in simple ways, simple is simple to extend and improve.

Its not that simple is *easy* - often it is the opposite of easy, or quick.

But simple wins out over time. Simple gives great ROI.

I throughly recommend listening to Rich Hickey on this subject (Link)

So please keep in mind - we aim for simple.  Even if our day to day
work pushes us to quick and easy and complicated.  We need to push
back.

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

Software Governance
===================

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

Systems governance
------------------

SRE / building for failure (Erlang and OTP)
this is monitoring running systems.  Things like approvals, security etc.


Managing the lifecycle
-----------------------

Application Lifecycle Management
Gov Service Design Manual


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

Project and Programme management
================================

So there is a well known story in the Agile world about `why estimates
are always wrong
<https://www.quora.com/Engineering-Management/Why-are-software-development-task-estimations-regularly-off-by-a-factor-of-2-3/answer/Michael-Wolfe?srid=24b&share=1>`_

Basically we cannot do it.  So why do people ask for estimates? They
dont want estimates - they want landmarks !!!


It if ain't got a ticket dont work on it
If it ain't possible to rollup tickets you dont know where you are going
A backlog out of context is just a horror
There is nothing wrong with top-down design (see Linux)
Backlog for the whole company - agile for the whole company  just see progress on a map.
If its not going fast wnough for the board they can fix things at their level.


We need to track our work so we can provide an audit trail
THese are useful



Project Management
------------------
- :doc:`chapters/agile_estimation`
- :doc:`chapters/SoHo1`
- :doc:`chapters/themes`
- :doc:`chapters/urljoin`
- :doc:`chapters/veryquickMBA`


CTO dashboards and Business Process Dashboards
==============================================

Dashboards matter
The basics of code quality can be in dashboard.
The basics of production health can be in dashboard
Putting a business process into dashboard is powerful - use Graphite and "light beam trackers"


- :doc:`chapters/aspell`
- :doc:`chapters/mikado-doc-manager`
- :doc:https://github.com/getredash/redash/blob/master/README.md




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


Out of date already
===================

chapters/virtualisation
chapters/virtualbox`
chapters/usbdisk`


https://en.wikipedia.org/wiki/Fractal_tree_index


.. rubric:: Footnotes

.. [#f1] The linked essay is by Eric S Raymond and is almost two
   decades old, and lays out an important philosophical difference
   between how open source software gets developed (in a mad press of new
   things being tried out) and how cathedrals are built.  The cathedral
   builders have tried to learn from the bazaar, and concepts like Agile
   are helping (a bit) but building software in our modern day
   institutions is still frustrating.  As software eats the world, it
   will find politics and push back.

