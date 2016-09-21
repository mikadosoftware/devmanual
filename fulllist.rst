Introduction 
------------

This book tries to cover a lot of ground.  Ostensibly, we are simply laying out the *best practises* for a modern software team.  I have been working in, leading and hiring such teams for twenty years (and yes I do feel old thank you for asking!).  But the interweb is full of humblebragging lists like  "you should do X, I did, ain't it cool" - but I find them actively unhelpful, for two major reasons 

Firstly, Without knowing *why* a certain practise is "best" then it is hard to resist the siren call of the latest fashion fad (of which the software industry has so many we can laugh at the Milanese fashion houses.  "Oh, you have a new colour to deal with this *season*.  Well apparently this sprint I have to re-implement a ten year testing regieme").

Secondly, they don't cover the whole field. Reading about one startups marvellous new medicine for log management does not give you a sense of how well they are doing with the thirty other vital areas like CI, project management etc.  And it does not give you an idea for how much effort is left over after logging is tied up and ready to be left well alone.

So I wanted to get my own best practises out of my head and onto both scripts and paper.

I have been tempted to make this book a form of literate programming, but it seems a lot simpler to make a literal working small company, with a small product, with the code that produced it available to read.

This is possible because of DevOps - that is there exists a set of scripts that will produce a fully working company - it is not something locked up in the brains of talented people.  (What is locked up is the understanding needed to recreate or adjust the scripts - that is never abstracted away)

I use building a dashboard for a new CTO of a hypothetical company as the core of this book.  The dashboard is a good way for a new CTO to gather the data needed and project it back out.  It is by no means easy to gather the right data by the way.  Which is kind of the point.

There are real working code examples, an actual dashboard you can run in your own organisation or team.

And there is the why. The history of software development is short and yet we forget many of its lessons. Why are some of these practises desirable, how did we get here. 

This book is partly a history lesson then. But one I (sadly) have got a personal view on a large chunk of the history.  I hope we can draw out the right lessons.


Modern Capabilities 
-------------------


Modern trends
-------------


Privacy issues
https://news.ycombinator.com/item?id=12388370

Not so modern people
--------------------

Disfluency
----------
- nee time to learn as well as data.
- need to do it by hand 
- need to learn 

Why is software so diverse ?

Not age, sex or race. That's a whole 'nother problem.  But the practises are diverse. 
The US Presidential election of 1896 was a turning point in US politics. (** Relate to modern elections) But it marked the end of a hugely turbulent period of change in Western world and business practises. Electricity is a great example. Factories were redesigning - took another twenty years. Best practises emerged and final result was ford.

Google is not ford. Ford is the programmable company.

This book is a walk around the software factories of today, and an attempt to understand what the first programmable company will look like.

Ford's not ideal (1937 battle of the overpass). In many ways the battles of UK in 19C were reflected in early 20th, culminating in business coup referenced by Gen Smedley X

The goal here is the programmable company. Like ford it is an inflection point. One. It reached yet.

But it is worth exploring 
Most software teams develop and release software in their own way.  Like factories that have not yet settled on best practise.
Agile is not it. Trust me



Why - because we are re-inventing our factories
We could have industry standard operating procedures for vast majority of companies. We could - but we don't.

But most of problems of software in house I have seen is not developers with timenonntheir hands still unable to meet business needs, mostly it is two things

- inability to articulate what is needed for business to succeed
- the whole other crap that swamps is all 


esprit de corps
---------------
Teams matter waaaay more than individual contributors

No one likes being told what to do.  So let developers contribute their next best step.

Discuss planning carefully, have wide open discussions on next step.  Lieutenants own chunks of code. Use Linux development model 

At the beginning of greenfield almost any code laid down is 10x. Don't believe in 10x myth.  Iceland and Wales versus England.  Esprit de corp

Social organisation, commit bits, licenses and future income and reputation.
-----


Major trends
------------

- distributed by default. This works for data, and processing.  But for organisations too - conways law.

- chips everywhere (inverse mores law), privacy pollution problem

- Agility vs Architecture.
You can't plan out each step in your journey
You can't change your destination in between each step

- Science is measurement. Engineering is applied science. Metrics everywhere.

- the world at large (politics gets everywhere, and as software programs the world, politics and software will meet. New forms of governance (Debian)

Start with the Dashboard
------------------------
This gives us a simple means to always show we have a feedback loop and always remain in control.  It is also the simplest means to show what is provided for the end user.


The New CTO Dashboard
---------------------

Every software team (whether one person or a hundred) has multiple streams of work they must do to keep their software

I am including "operations" as part of this as most software teams do this - either directly ala Facebook / Amazon or indirectly ala third line support.

These streams are 

- producing new features
- maintaining high code quality
- operational performance and metrics
- bug fixing
- tech debt 
- marketing
- servicing users





For every software organisation we can define a set of capabilities, and for each capability we can define best practise and then rate our own organisation against the best practise.  This can give a clear idea where to focus improvement efforts.

Team capabilities
-----------------

- 

- micro-services architecture



Organisation capabilities
-------------------------

- flexible cell structure ?

Business capabilities
---------------------

- programmable corporation


- Deploy
- Develop
- Release 
- monitor
- operations (SOP)
- security
- service levels (SLA)
- ticket requests
- architecture / distributed data
- programmable corporation 
- adjusting business model
- marketing
- disaster recovery / option pricing
- learning and training and teamwork
- stakeholder engagement
- project management: new agile

New agile 
https://medium.com/@gabrielgambetta/how-i-wrote-my-first-novel-during-my-daily-commute-e1d02c9447b9#.248qy79fb

Good description of process - 80 "scenes" - we must must have a storyboard - think the sticky notes
Always have storyboard
Always have interactions between stories
Stories are states??? 

But always always - must be clear must be shared

Technical Capabilities
----------------------

* Measure Lines Spent 
  Edgar Djyskstra quote - tech debt
  The more code written the more there is to understand
  Writing lots of code, writing it quickly, is often the contractor curse - too much too soon. There is no such thing as hitting the ground running.
  
* measure Onboarding times

* measure code quality not feature velocity

* measure effort to deploy

* measure inter dependancy

* measure metrics - is code well
Measured in production


* Deployment can deploy code through promotion of fixed "builds" into production using totally automated means.

* micro services architecture
  This is a major issue. Includes security, service discovery messaging logging and pr nose to only go through front door. See stevey blog post.
  https://news.ycombinator.com/item?id=12133670
  Use fluentd logging 
https://blog.treasuredata.com/blog/2016/08/03/distributed-logging-architecture-in-the-container-era/

* OS installation and Hardening
  Choice of OS, location
  Ansible or similar automation scripts

* Kerberos and Authentication
  Authentication and Authorisation are vital capabilities and federated, distributed security have so many advantages (think uUId as primary key )
  
* Build promotion and use of containers
  PyHolodeck 

* message queues and worker pools
  Messaging
  Job scheduling based on events and then queues
  Is a resource problem always

* performance monitoring
  metrics gathering with graphite

* unit testing, integration testing, perfromance testing

* user acceptanbce tests and UI tests
  Automated testing is vital and we must put huge amounts of effort into it simply to make the next release
  
* continuous integrations and delivery
  There is no point batching up changes to go on a time based schedule. Code is ready as it is written and the decision to release should be based on automated tests. Only marketing or other business decisions should delay - so always push to pre-prod 
  
* pre-prod is live-clone

* replaying actual traffic
  
* Reporting
  Simple reports

* SOPs and checklists

* Measuring metrics

* documentation

* Dev Ops

* statistics

* distributed data and computation
  Use of Apache spark, Hadoop etc

* Javascript

* Angular vs Jquery

* Programmable Corporation

* functional programming and scalability
  Elixr and OTP

* bug tracking, code analysis,

* git and git workflow

* Linux and workstations

* Mobile development

* Big Data

* Maturity and keeping on a single course

* seven league boots

* earthquake-let theory of software development. Building blocks not planned features 

* Work harder on fewer projects and polish them to be CV-worthy shipping working software

* Message Queue

* Business Intelligence reporting

* Software KPIs, buisness KPIs

* Simple Marketing (Twilio approach), SEO

* Debugging tools
  CHarles proxy
  Chrome debugger

* Web technologies (html 5)
  Bootstrap, HTML 5, cimples CSS

* Rekational Databases

* NOSQL databases

* Storage systems

* Backup and recovery
  Business Disaster recovery and assurance
  Multiple data centres

* Time, Unicode, basic data types

* serialisation
  pickle, json etc

* Cacheing

* Configuration basics

* command line is all

* Publishing own work

* contact management

* email management

* Practise on smaller complete projects

* jenkins

* chatbots and IRC. Team comms. Choose one one o said one!! 

* erlang

* rethinkdb
 
* training and just reading and exploring
if you do not explicitly make time to learn but sprint all the time all you will have is people who have learnt what they wrote


Systems Infrastructure
----------------------

Storage
-------

Front end
---------

Middleware
----------

Storage
-------

Disaster Recovery
-----------------

Distributed computing vs redundant
----------------------------------

SOA and API design
------------------

Project management
------------------

Debugging
---------

https://en.m.wikipedia.org/wiki/American_fuzzy_lop_(fuzzer)

KISS
----

Slow Development, manageable infrastructure
-------------------------------------------


NOSQL
-----

Statistics
----------

Seven league Boots
------------------

Statistics
ML
NLP
CV


Why full stack matters, and why you cant do it all
---------------------------------------------------




* Project Management
  history of Agile and scrum
  Critique of Agile / SCrum
     " You dont have to sprint if you are making seven-league boots"
  Essential project management
  Tight co-ordination with team members
  Mostly the same capabilities - but teamwork, transfer of trust.
  Read that book quoted by Clinton Roshenm

* Specfication discovery
  Working with users
  See service lifecycle - whats the User Need?

* build everything as a service
  Gov.uk service manaual
  SOA
  history of SOA in Amazon

* Managing tickets and commits
  Use of source cntrol
  Use of ticketing system

* specifications, design and tickets
  Must do upfront design.
  Design / discussion documents are vital and allow clarification
  Call this Architecture if you like, but dont assume people understand

* Everything is a service
  So services have Interface Points and lifecycles.

* 



Project mgmt
------------

We all work on projects of some form or other.  Tools will help us.
Working for an enterprise, they want different reporting approaches.
So the simplest answer is to have a buffer - write and read to and from

Tickets in a parent child chain
A child can have many parents (?)
Git based bugs?
Functional specs that map easily to tickets (spec2ticket)
Unless you write down explicitly what you are trying to achieve, and discuss it with the developers and business owners, you end up with three things - some people who don't understand most of it and just go along hoping to pick it up later, some people who think they understand it but have forgotten some vital and really hard parts and think this is going to be easy, and some people who think they are building something not quite the same shape as everyone else.

The mark of a high functioning team is how quickly new hires get up to speed - you don't need Einstein to come in if you kept it simple and well tested and well API'd.

Discover, write up and do OSS projects on
Scale up to 1000 cloud instances with full deployment and development and monitoring process

Server to server authentication


"Full on Full Stack"

What does it really take to be a full stack developer?

-


Intelligence gathering :
- economy model etc

Security as a baked in goal

We are aiming for a level of security that is good but not awesome.

This is where the internal threat is minimal  and external threat is high - we protect against threats with high external component and lower internal.

Internal is best to use a lot lot of audit

- server to server authentication
 

Skills required (bold=essential)
·         FreeIPA/LDAP
·         Ubuntu/Redhat/CentOS
·         VMware (candidate does not have to be a specialist, but ability to spin up VMs)
·         Configuration management (Ansible desirable but can demonstrate familiarity with others such puppet and chef)
·         Scripting - shell/php/python
·         mysql
·         apache
·         HA-Proxy / load balancing (both desirable)
·         High availability (Keepalived) (desirable)
·         Change control (exposure/demonstration of working in a controlled environment)
·         Source code control (git)
·         monitoring (solarwinds/nagios)
·         system hardening and security
·         iptables (desirable)
·         open source software
·         DNS/DHCP



the inevitable:
digital hygiene 
tco of digital life

perosnal to business
- less stuff (dvds to cloud)

climate chnage

http://worrydream.com/ClimateChange/


Underpinning philosophy 
- Equality
- Empiricism
- Extrrnalities

Economics is important but it's use of energy for human benefit.

Avoiding the google bubble - digital gated communities


- Airbnb has a race issue - people more likely to refuse a blackmsoundingnname. But the solution to this is simple - renters must offer a room to whomever applies - just as hotels cannot turn people away.  But because these new efficient services are ignoring existing regulation and so will need new (smarter regulating if we can - see below)

AirBNb and other "regulation challenging" unicorns are quite simply breaking the law in almost every country in which they operate.  They are, incidentally, raising matters of public policy that are long overdue 

How is airbnb the same as European Commission - both trying to harmonise regulation across a globalised world.

Car Charing versus taxi : here is my regulatory change - the car sharing service must advertise its start and leave positions and make the subsequent journey of 


What happens when a regulated hotel tries to discriminate (gay bo'nb issue) - they get their ass sued.

- European court tries ban hyoerlinks
http://searchengineland.com/european-court-says-linking-illegal-content-copyright-infringement-258442

- eefragmentation - http://www.paulgraham.com/re.html

The new labour contract: superstars and payment.
http://www.totalsportek.com/money/manchester-united-player-salaries/

So for 2015 Manchester United made 450M, of which it spent 250M on player salaries (holy cow). If we take 20% corporation tax (yeah right) then we see around 80/20 for labour to capital

Does this hold true for other superstar driven areas - finance? Oh yes - here is traders that took all the revenue in a year.

Is Pikkety wrong? Will global remote working make this kind of impact? Not clear. 
