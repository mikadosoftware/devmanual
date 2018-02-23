========================
The SimpleCTO Dev Manual
========================

In the software industry a dev manual is a "how we do things around here" document. It details everything from the right way to format code and how to bring up new servers.

This Dev Manual covers such things, but importantly it is focused on how to form and bring up people - the teams themselves that do the every day coding and development.

it is always a delicate balance - teams must have clear rules and common ideas on the right way to test their code - but it is harder to lay out rules on how to treat one another with respect.  We layout ideas on team formation from FBI hostage negotiation to political activists.  



Start reading here
------------------

.. toctree::
   :glob:

   entrypoint_chapters/*


The whole lot
-------------

.. toctree::
   :glob:

   chapters/*   


   
Themes
======

1. source to release

2. tech debt and tech assets - code and tests

3. mise en place (workstation, areas of expertise)
 
4. Security

5. Documentation and Marketing

6. Culture openness and reviews and picking on people and culture
   
7. Progress Not Perfection (YouTube clip)

8. code analysis and performance analusis static (metrics) and other analysis
   linting, opinionated structure, consistency, pre-commit hooks and useful
   things.
   
   
9. Automatic project mgmt Risk management, requirements lifecycle (PEP)
    
10. have fun, try new things, don't be afraid


Vitural Environments
--------------------
* I want a common setup of libraries etc.
  so we need to define that setup, and requirements.txt seems best appracoh
  this way i have common libraries across all projects and try v hard not to vary.

  
    

Workstation 
------------

   

Source control, continuous integration
--------------------------------------


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



