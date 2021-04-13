Fractal Management
==================

TBD

What is management?
--------------------
https://news.ycombinator.com/item?id=16775166

Going to go with my definitions - based on what is bad management we can see good

- build and improve a process (ie dev lead forums)


Historically :

a king plus parliament 
openness

Where we double down on democracy


The two minute guide to growing a dev team 
------------------------
https://allarsblog.com/2018/03/17/confessions-of-an-unreal-engine-4-engineering-firefighter/
"""
If you're reading this as an employer or producer, this is how you should be classifying your team's weaknesses and how you should look at distributing team effort to overcome them. If you find yourself in a situation where your top level engineers are being strapped for time because their too busy helping the people below them, you need more senior level engineers. If you find that productivity is good and that you are underutilizing your senior level engineers, the answer is to bring on mid-level engineers. The seniors will allow the mid levels to grow, which in turn allow the seniors to grow as well either sideways into lead roles or upwards into executive / principle / board member roles.
"""

The essence is you need to start with senior engineers (and in my view senior is 50/50 context and skill - ie you have to know the codebase abs have to have skills.)

But basically you have to monitor burn down (points over time, not tickets) and it should be roughly consistent and *then* you need to find that your engineers have time to answer questions and convey answers abs meaning - ie watch the mailing lists 

public email works because it is as precise or quick as needed and it can be mass publication or individual and it is asynchronous - so not a  interrupt culture like slack 

But 

Start with Senior engineers - when they have surfaced the product or are comfortable then bringin people under them - if seniors become too short on time you have brought on too many mid level so hire senior or reduce mid level


Then abs only then bring on people under them - grow teams from the top - 

Wealth taxes and bill gates
---------------------------
https://keenen.xyz/just-be-rich/


government is bad at spending money so they should not tax the wealthy 

Bill gates is waaay better at spending money than Inam - or almost anyone frankly

So we should not impose a wealth tax and let him spend that money effectively - a good use of money 

kinda - what if we go one better and give home more
on why to spend? Like he can have my salary and make me more cash ? Or at least make
me feel better it is curing malaria or something 

but hang on - why don't we just *elect* billg then he can spend trillions well, not billions

- but no ! that will mean he has to deal with special interests and so on 

hang on - you just said he was better at spending it than governments? if governments would be good if not for all the crap we give then, then why - what?

Ok - let's tax but then be really careful about who we elect and what system they work under - i mean what governments would billg work in - what's wrong with the system such that it cannot work like a business? or what's right (ie disabled rights ) 


sweep
of history
----------
Empires evolved to be nice places to live - better than europe mostly
but unable to take on changes as they fell back from edge of chaos

so we want some means to take on the chaos and valuable improvements - basically a generational rewrite? that's revolution and scary

i don't have a good answer

but rely on democracy and all people making sensible choices 




Many intelligences model of an organisation / country / culture

- am intelligence is any group of people that given a new fact will probably all process it to the next outcome.

impact on fake news etc, consensus

https://www.ribbonfarm.com/2009/10/07/the-gervais-principle-or-the-office-according-to-the-office/

Old hierarchies, the failure of management etc


developer hegemony
https://news.ycombinator.com/edit?id=18840640


Why was AWS more successful than Google Cloud and what does it mean for serverless

Amazon offered IaaS - infrastructure as a service.  Google Cloud offered something subtly different - PaaS plaforn as a service. For amazon you could just lift and shift - take your 3 webservers and 2 database instances that run Application X for a company and copy them over to 5 E3 instances, 
and presto, you are in the cloud, and Amazon is doing the hardware stuff - the company gets savings with no real chnage.
Google cloud however was predicated on "join us and you get the massive scaling ability of google" but that means you don't just "lift and shift" - you need to rewrite quite if lot of the application (basically assuming every request is stateless, which is fine for simple web apps but bet your bottom dollar the devs took shortcuts a few years back and good luck identifying which parts of the code need fixing - and this move to cloud project is to be done in 3 weeks.

So no-one bothered rewriting their whole apllication to suit a new paradigm and amazon buys a lot of servers that do not much.

Now we have "serverless" as a incoming paradigm - and this is Google Cloud Platform again in a hat and dark sunglasses.  It is an attractive idea - don't pay for the servers just pay for the CPU time taken to process each request.  The potential savings are huge and the scaling and load balancing possibilities are ... the same as Google's.

But - firstly it means an new rewrite of any existing applications - which costs waaay more than what can be saved in each individual app.  So to justify this a company needs the top down Board level pressure to "get in the cloud - but properly this time".

And secondly security issues really do raise their heads - if you thought heartbleed was bad enough, imagine what nightmare scenarios we could have when your secure request is sandwiched in the same CPU as any one else's requests separated by a few microseconds.  Intel did not design its layer 1-3 caches and CPU architecture with the idea that an attacker will be processing their code on the same damn CPU either side of you.

And finally - some things, like map reduce search queries scale really well and produce business benefits by scaling. And quite a lot of business applications do not - calculating payroll adds no value to business if it is done in five hundred servers in two seconds on or one server over an hour or two.

Only front end web facing businesses are going to have that hockey stick - and frankly very few of them have been invented.

i may be being overly cynical in that lat one. but if your business model scales to the web then every part of your business will need to do this same thing.


.. quote::
https://news.ycombinator.com/reply?id=19066087&goto=item%3Fid%3D19062042%2319066087
"""Legacy apps asummes a certain degree of reliability from the underlaying infrastructure. This assumption falls flat on its face in the cloud. Netflix wouldn't have needed to develop Chaos Monkey if this wasn't the case.
Secondly leap to cloud native never happens because no one wants to take the pain once it works even barely. Any issues can be pushed onto Infrastructure team. It's pure and simple risk avoidance."""



Google SRE
- seek to cap time on operational work at 50% so they can invent and build capability 
https://www.usenix.org/system/files/login/articles/login_fall16_08_beyer.pdf

This is part of the automate all the things attitude 

Shipped Email list
------------------
Internally publish a shipped email - similar to Stripe - see https://news.ycombinator.com/item?id=19423530

The Toyota way still applies
-----------------------------
https://en.m.wikipedia.org/wiki/Toyota_Production_System

Slow programming
Zero bugs methodology
Automate all the things

It is amazing to see what I slowly have arrived at already being in existence

Hiring the right way
--------------------

https://news.ycombinator.com/item?id=19707543

Calibrate your interview process by having a recruiter identify ten great hires and pay them to do your crappy interview questions. if most of them fail think about it

Embrace the Grind
-----------------
https://jacobian.org/2021/apr/7/embrace-the-grind/


NOSql world view
-----------------
https://highlyscalable.wordpress.com/2012/03/01/nosql-data-modeling-techniques/




Span of code control
--------------------
Scripts get better as we re-write then. Code gets better as ewe refactor it.  Two pizza teams are good for a sizing of span of control - and we want the quality of code to keep improving - so is there a number of lines of code that we should compare "editors" to - book editors? 
but even that is not right as it's common to reuse code - not reuse books. perhaps editing regular editions ? 


Capturing tech debt
-------------------

Tech debt is a vital and costly idea.  (see why can't people with SAP installs upgrade ?)

we can assess costs as follows


- backwards compatible means that a given reference model (ie test suite) passes when a change is made, and that the test suite / ref model adequately matches real world requirements 

(yes that means coding up your requirements)

- Can we accept upstream patches / upgrades with only a single release cycle of testing and no custom coding (ie assume patch has no backward compatible issues) 

- can we make our own upstream changes (ie developmcode) and see the same effect? 
