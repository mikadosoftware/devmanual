Fractal Management
==================

TBD


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

Span of code control
--------------------
Scripts get better as we re-write then. Code gets better as ewe refactor it.  Two pizza teams are good for a sizing of span of control - and we want the quality of code to keep improving - so is there a number of lines of code that we should compare "editors" to - book editors? 
but even that is not right as it's common to reuse code - not reuse books. perhaps editing regular editions ? 

