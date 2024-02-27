Philosophy
----------

Scaling and growing.

There are 2 options for an organisation, to slowly learn how to do what you do,
to hire slowly, let everyone work together and absorb lessons.  You can speed
this up with good management, knowledge sharing, etc, but there are speed
limitations.  THis is growing our own. THink of it as serial growth.

Then there is scaling.

Scaling almost always fails. (story of delivery - swimming not a bridge, car not
plane). But it fails because people dont already know what to do.

If you are scaling, you need to have already done the job, and have a tempalte
for rebuilding it, and train / hire different people for doing the job in
parallel

The Devmanual is a *template* for building a software team or teams, allowing
them the flexibility to adjust to a given companys particular circumstances,
but sufficient skeleton structure that all bases are covered.

The interactive portion will be interviews with people and teams going through
the process.


Managing via repowatch
----------------------

I want to track and keep updated all repos I use. I avoid monorepos becuase ...
immaturity of some not others, eventually we are all managing multiple repos,
a monorepo justhides that. but is v useful at corp level but leads to bifurcations/

ANyhow.

I want to be able to build a venv with all the repos in it.
I would like to use henrek appraoch of building distro level installers (one for each repo)
and then installing into ... docker???
How we change those / develoo those?? we test it out in its own locationa - we need a docker with all repos installed but at -e 



* using ledger and automated CSV gatehring techniques
  https://disjoint.ca/projects/ledger-reconciler/


Produce a latex version aimed at tufte book template

http://www.latextemplates.com/template/tufte-style-book

http://gordonbrander.com/pattern/

project mgmt
- effectiveness of troops in battle 60-90 days to peak, 200 to trough
lindybeige

- so why not use that for team formation? 

Future
- Climate chnage
-- a war footing solution for the globe - like march of dimes

team based performance reviews - more useful more team focused

concepts from literacy's
-----------------------


- hairdryer with 3200 and 200 300 as increasing value
- gold silver bronze
- shared concepts (religion, bible, preachers)


Efficiencies firns
------------------

Way to scale is partnership with other small clients
See guardian of galaxy style approach
See OSS support networks
See gov tech 

It is likely we shall see newspaper like forms appearing - staff editors (who frame the taste of the code base) and staff writers who are both learning trade and being taught taste - and contributing writers who are stand alone for specialised services

still not a mesh but close


The whole thing 
----------------

>>> fix all the bugs that are upsetting customers and causing them to flee.

Well yes.  I am just posting that it is possible to take a top level metric and build a backlog that represents sensible solutions to that metric.

But you first need

- a top level metric (preferably that measures what will make or break your business)
- a way to determine what things *under your control* drive that metric.

But yes, the things you do in the trenches will probably not move the needle far.  That is for two reasons

- at some point the code base is so big that doing "one thing" won't make impact (i think this is around the 100k SLOC) level which is still fairly small

- and even if you can affect the whole code base, the code is at the bottom
of an inverted pyramid of "leverage to affect the business" - the CEO can chnage the business far far more be deciding to triple the price tomorrow than any bugs you fix.

But yes - in the end, if you have a working product right now the best thing to do is to go
find real customers, work out why they are upset (either with clever telemetry analysis or just *fricking ask*) and go fix that bug / missing feature.

If you don't have a working product there is no telemetry so ... *fricking ask*.

But find what's not working and fix it is a good plan.  If what's not working however is "the business model" we are in interesting territory

I think a non working business model
is *exactly* the purview of software.  I think that we shall
replace all non-coding business people
with coders who can business in a generation.  But that this generation will see real opportunities


- There is a business / coding divide
- there is a leverage of impact pyramid (inverted)
- but "business" is a small skill set (politics is not, sales is not - business is) 
- so it's easier to teach business to coders than vice versa

- bad business model is a eric ties style lean question - and searching is what software does well - somprogram the search 

marketers being replaced by software like was for warehouse workers - a modern marketeer is bit like i was picking and packing - just human doing a robots job.












The DevManual - basic rescue principles

We are trying to get complexity out of a system - which is far harder than building simplicity in. It's where a rewrite is desirable.

I just don't want to fight anymore. People come in with opinions and the only way to over come is - persuasion (minimal), authority (reputation or actual) or competition (go off and build competitor) 

- talk to every developer and ensure their incentives align / otherwise guilt them

- cover all the bases - dev support, prod support, monitoring observability, release process, env creation, 


https://cxl.com/blog/ab-testing-statistics/

build our own p-value AB test framework to learn about stats

logging:
https://news.ycombinator.com/item?id=30393683
https://github.com/citusdata/citus


https://www.unite.ai/ten-best-machine-learning-algorithms/


Asterix / PBX / phone 
https://github.com/MatejKovacic/RasPBX-install


https://rosslazer.com/posts/startup-tooling/


SRE
---

PostMortems

https://codeascraft.com/2012/05/22/blameless-postmortems/


Front end
---------
https://jvns.ca/blog/2020/06/19/a-little-bit-of-plain-javascript-can-do-a-lot/

https://news.ycombinator.com/item?id=23578319


javascript
https://news.ycombinator.com/item?id=23590848


We have become our own agents (all that time looking things up on iphones tripadvisor hotels.com) was supposed to have been done by AI


Project management - noestimates too far but need ranged renegotiations on estimates - error bars on estimates and so on 

telemetry (gathering event data)



- automate all the things -> programmable company
- programmable company -> faster iterations and faster market / product fit
- programmable company -> no executive function???
-> entrepreneur mindset??
-> model mentor monitor 
-> if no labour force then ... nonsupervisor force.  then what is executive compensation based on or for?
-> company chnage becomes the main function - but that's programmaing job...

Software literacy


Future work from Acolyer.org
https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/

developing an organisational capability to design, build, and deploy successful machine learned models in user-facing contexts is, in my opinion, as fundamental to an organisation’s competitiveness as all the other characteristics of high-performing organisations highlighted in the State of DevOps reports. (And by the way, wouldn’t it be wonderful to see data confirming or denying that hypothesis in future reports!).



https://cloud.google.com/blog/products/devops-sre/the-2019-accelerate-state-of-devops-elite-performance-productivity-and-scaling



https://blog.acolyer.org/2019/04/03/establishing-software-root-of-trust-unconditionally/
- external verifier asks server to hash its memory in such a way that it can only happen in time t if there is no malware or anything else present...

Metrics
-------
https://news.ycombinator.com/item?id=23361319


Don't do distributed - yet
--------------------------

99 times out of a hundred your problem is not going to be solved with a distributed processing platform - your data is not that big (see vaez) your reliability not that vital

Solve the problems in order 

- who
- what changes their behaviour
- why 
- 

Build a robust *process* for discovering customer needs and meeting those iteratively - watch your metrics, run tests and experiments - focus on writing business software in a sensible manner 

Once you breach that 4th order of magnitude you can worry about Google Scale problem (GANDALF)




https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/


Distributed tracing 
-------------------

https://medium.com/@copyconstruct/distributed-tracing-weve-been-doing-it-wrong-39fc92a857df

https://www.kartar.net/2019/07/intro-to-distributed-tracing/

https://research.google/pubs/pub36356/


Once we do go distributed we hit many more issues - but we know we need to go there someday


More on encryption
------------------
https://news.ycombinator.com/item?id=23390966

https://github.com/hashicorp/vault/blob/45b9f7c1a53506dc97221f0915daeaeb0a6fe894/website/pages/guides/operations/rekeying-and-rotating.mdx#L20

https://latacora.singles/2019/07/16/the-pgp-problem.html


definition of unit test v integration test 
-------------------------
https://news.ycombinator.com/item?id=27731342


Tech stack for one person saas discussion
-------------------------

https://news.ycombinator.com/item?id=25186342


Methodology 
-----------
Agile is fairly simple - it's an *iterative* process.
Barry Boehm had this in 1986 with "spiral model" - where you developed to mitigate the largest known risks at each iteration.

length of iteration up to you

Web components
--------------
why are they good? 
webcomponents.dev - all the ways to make a web component

Overall views
--------------
https://paulosman.me/2019/12/30/production-oriented-development.html



scaffolding 
-----------
Use the cadence to build scaffolding for organisation 

https://medium.com/craft-ventures/the-cadence-how-to-operate-a-saas-startup-436aa8099e8


Colour grading and themes 

https://youtu.be/CYRyaY-9F_g

60/30/10 rule


deployment etc
https://hynek.me/articles/python-app-deployment-with-native-packages/
Security
XSS and SSTI (template injection)
https://nvisium.com/blog/2016/03/09/exploring-ssti-in-flask-jinja2/

https://btc-hijack.ethz.ch
understand BGP 

ssh tunnelling and von
http://sshuttle.readthedocs.io/en/stable/usage.html
https://news.ycombinator.com/item?id=15773466

software professional 
https://www.reuters.com/article/us-volkswagen-emissions-sentencing/vw-engineer-sentenced-to-40-month-prison-term-in-diesel-case-idUSKCN1B51YP?utm_campaign=trueAnthem:+Trending+Content&utm_content=59a05e9b04d301050bce8161&utm_medium=trueAnthem&utm_source=twitter

satellite tracking and data downloading
https://hackaday.com/2017/01/02/junkyard-dish-mount-tracks-weather-satellites/

weather ballon - send up a rpi 

testing - golem, hypothesis doctest
i mean why have 50% of methods being unitteats? 

Haven - https://www.wired.com/story/snowden-haven-app-turns-phone-into-home-security-system/

every device is a recording device - for every police assault or criminal activity. police state
