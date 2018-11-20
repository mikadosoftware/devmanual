Serverless Dev Manual
=====================

This is a dev manual - a "how we do things around here" for a software development team.

It is developed in the open to allow or encourage discussion.  If you feel some updates are needed, pull requests are always welcome.

The index is built first as a jumping off point for the longer explanations in the actual chapters. it seemed easier to build this way, and helps keep it straight in my head.

I have written this to be a useful starting point for an imaginary "new CTO", probably a founder with little prior experience.  it is a companion piece to "The Software Mind".

Themes
======

Plumbing 
--------

* plumbing needed for every project / component
  - error handling
  - config
  - todo
  - docs
  - logging
  - metrics
  - activity reporting
  - governance, style, testing, coverage
  - source code policy
  - physically distinct DEV, [UAT], PREPROD and PROD
    UAT is optional if you have automated testing.
    dont mix preprod and uat cos you will want to release when users are looking
  - dashboards for can I release, and what is governance ?
AQA - automated Qualty Assurance
- ast based syntax checking
- checking integration test
- similar to CI as well

Workstation 
-----------
Workstation builds also matter

Hardware production processes
------------------------------
This is kinda sorta linked to workstations- i have worked at startups who depended on software and hardware builds.  these are much harder at proper scale, but it matters

see bunny houng.  


Teams and culture
------------------

it matters it really does

start with feedback - sprints and retrospectives
Be aware of your priviledge
Begin the difficult conversations publically 
be aware of the likely problems - metoo is just one.

then aim for the culture you want - 

then hire good people


Source control, continuous integration
--------------------------------------

mono repo vs multi repo - really is a tool discussion so discuss the tools
- ability to identify all our dependnacies
- fulltest of all (mono is simpler but multi easier to manage)
- project control files - ownership etc

Security 
--------


Mission statements 
https://www.amazon.jobs/principles

* GPG and keypairs


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


===================
The Dev Manual
===================


The manual 
==========

"How are things developed around here, and why."
-------------------------------------------------

This is a developers manual, constructed as a companion
piece to `The Software Mind` book. 


* The code is the design - code first for everything
  Infrastructure as a Service
  Softwre defined networking

* Code as a crime scene
  Static Analysis and raising all boats.

* Seeing every beat of the corporate body.
  Dashboards, newspapers of the data rich world - making it easy to understand

  
* Source control
* prmotoing code up
* having a robot promite code after meeting automatic criteria
* having automatic testing
* build servers
*


Pyholodeck

- source control
- build systems
- automated tests and xml results
- deployment 
- monitoring
- logging
- metrics
- performance testing
- Pre prod and prod
- cloud evolutions (serverless architecture)
- no damn features
- 


python tricks 

python eco system 
- error capture and management - rollbar 
- metrics capture
- event capture (kpi)
- bug tracking and so on 
how it all fits together 

devmanual - ast and how to do syntax checking like pyflake - how to build own rules 


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


  


* distributed file systems
  Cephfs, GlusterFS, Lustre, and HDFS

* work queues
  CElery, zeroMQ

* amazon, openstack

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


