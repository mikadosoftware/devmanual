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


Building the Decking
--------------------
The decking - planks of wood, each simple on its on, together a nice place to stand


Internal to the code is 

plumbing : 
- logging
- metrics
- etc etc

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

