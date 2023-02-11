How we do things around here
============================

This is The DevManual - a guide to organising, workingnin and growing a software team, usually within a "enterprise" franework

Its partly a survival guide and partly a "just add water" software framework.

It is specifically designes (ecolves) to handle working inside the usually restrictive world of large enterpises

Follow the rules, break the rules, transcend the rules (shuhari)

Why Companiez ?

Since humans discovered agricyktre and so made technology (somethijg that genrally is easier if youndont move location evey month) we have been a texhnology auffised society and organisae around its beenfots

The very idea that the modern limited company with direct hierarchical control is the only or best organisatioalnform is laughable even if we seem to pay homage to it globally.  

More chnages will come as democracy matures 

The rocket equation for enterprises

The more money / political outcome is put onto a project (the more money) then more momey and effort is needed tomlift it - more expectation, means more
money, which means more
momey needed yo lift all the people who like to be on multinmillion dollar project

Also 
- autuer theory for projects and systems linus and linux but extend it out - whomare autoers for facebook ? Google? gmail guy 


india not caring about US culture https://dor.gov.in/sites/default/files/FinalBlackMoney.pdf

Marxism - britain and dutch developed modern capitalism / bourges and wound it uo with empire and industrial revolution - also trade is profitable, empire is costly

The modern world is woukd up with industrial revolution 

But each empire is tied up with a "philosophy" - empire, industry, capitalism, democracy for all (US) and now the indian and chinese philosophies which are ... less clear

but democracy is something it hink wont die - indovodual rofhts make a difference and somdoes agreement in path forward. Its really hard and lots of negotiation and compromise and niance and frnakly we moght not like ot 



discussion on enterprises
-------------------------

The secret : 

in any enterprise no-one knows what fuck is going on and everyone is too scared to admit it.  Most enterprise pathologies stemmfrom this simple fact

Cf naval vessels.  A naval vessel is a highly complex interaction of technology and process - people are trained in a process and follow the same

A few people (chief engineer, captain, others) will have a ujderstnading of how the technology works from stem to stern - but this is beckmingnharder in an age of software complexity

it maybe too much for anyone person but it is needed to "reason" about a system - only when you can teason about a systen can you control it adapt tomit and move on

what you cannot create tou donnot indertand 



Often try to make everyone work same way with same tools - a better approach is to use nokia style report


Tools in the toolkit
Commonly agreed processs and stabdards

- use Blender for 2/3d animations for simple get the point across



https://koptional.com/article/software-start-up-system-essentials



Capabilities etc 
UI design guide
https://anthonyhobday.com/sideprojects/saferules/





What is the new ideal minimum?
===================•=••

Use pyodide and html web components 
https://www.jackfranklin.co.uk/blog/working-with-react-and-the-web-platform/

Use pyodide and wasm and pandas to handle tablular front end

IAM
something like this?
https://news.ycombinator.com/item?id=31258953
ideally client certificates 






Systems and products and software etc.
======================================

We write, maintain andoperate a *software system*.
This could be some giant tech company like FAANG or it could be
a small IT department in a small company, or even just a start up.

A system will have *components*


First things
------------

- publish / surface
- security 
https://news.ycombinator.com/item?id=26838333









Source code repos - a discussion
--------------------------------
(see moxie on why not federated - basically cannot enforce
keeping up.  This is likely to be the major constraint on
all network growth - it may be a regulated issue - it often is
no bank can run on out of support software.)

Monorepo - this is a trick to try and force everyone to upgrade
on a treadmill - your stuff simply stops working.
(other benefits to monrepo - reduces number of dependnacies)

I think the monorepo idea is *minimal* - its quite feaible to have
a mono-working-area - just ensure any rollout follows
scripted set of dependancies and limit the number of choices people can have.
They are paid to work here after all.

* Components
Divide the system into compnents

- audience comms
- reportlib

Each component has a cision/roadmap
interleaved for the systme as a whole


- Rooms and Racking 
- Power and cooling
- Network Hardware and cabling
- CPU Hardware
- OS
Mostly this is answered by "AWS" but we old timers still dream of
heading to B&Q and buying portable air-con units to keep the server room
cool in summer.

- primary development stack (ie Python, pandas, AWS)
I am going to aly down this as python. But the important point here is
Rust , PHP, Go, Elixir perl, whatever these are language decsioons and are
all *fine*. They are mainstream and have hundreds of thousandas to millions of people using the stack.  The main trade off to learn here is ... stick to one
stack as if your life depends on it. Dont try a little bit of everything.

If you realise you need to change the language do it slowly and controlled.

PS Front end does not count as stack - that is more .. flexible. We shall see later.  But even so - dont go hunting off wildly without good reason.
And mostly, go native for a front end on Mobile.

Plumbing
--------

- Audience comms
- database
- config tables
- operator tooling
- metrics

etc


Google's Four Keys
==================

https://github.com/GoogleCloudPlatform/fourkeys

Deployment Frequency
Lead Time for Changes
Time to Restore Services
Change Failure Rate



https://thenewstack.io/googles-formula-for-elite-devops-performance/


Wrong on things like prod and launchdarkly but interesting 

https://paulosman.me/2019/12/30/production-oriented-development.html

better
https://news.ycombinator.com/item?id=25170547

Dev mode and product mode
-------------------------

You need to talk to users but also think like users - and it's hard to do both at same time 


Building the Decking
--------------------
The decking - planks of wood, each simple on its on, together a nice place to stand

plumbing Index
---------------


- Ongoing Incident Management
  An external or internal situation that seems 
  highly 
  A means to gather all known data about incident
  
  
  
Internal to the code is 

plumbing : 
- logging
- metrics

But this all needs a degree of infrastructure - ie carbon or splint

Company telemetry from NaSA
-----------------------
https://news.ycombinator.com/item?id=25951003


Then there is the enterprisey stuff

* Ticketing system
* Git
* CI build system (jenkins and docker)
* Unit testing, functional testing
* code analysis - black, coverage, vulnerability analysis etc
* artifact mgmt
* deployment orchestration (bash is barely ok, scripting and something like salt long before you try kuberbetes).  Build the monolith before the micro services

* Release mgmt - uploading to pypi, release notes, sign off process (build bot), cryptography

* config mgmt
don't make it tempting - everything goes out through same release process even config - else every release is done through config 

(use four keys to measure this - keeps us on straight and narrow)

* metrics
* maturity assessment 
* project and product mgmt
* AB testing 


https://panelbear.com/blog/tech-stack/


Twelve principles
-----------------

Cattle not pets
Metrics in production 
Rollouts are continuous and monitored 
security is job one
Doing it for first time means you cannot plan by time. This infects top to bottom
engineering means ...
politics means everyone wants to be at top - but that means picking winners which almost always fails (see literacy at top) try voting 
Emergent competition is not good way to engineer - no one has lots of roads being built and chooses one - or do they?? 


Organisational design 
----------
https://riverin.substack.com/p/the-canonical-startup-org-structure

Simple : there are 5 main "functions" Product Management / Product Developement (engineering) / Product Marketing / Operations / Sales.

As you grow you fill out those as "functions" - but everyone has an 80/20 association with those - ie have a major and a minor and 3 awaeenesses

Then you can build teams with a major in each five so they can herd a product 

