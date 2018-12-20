Plumbing and CI
===============

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