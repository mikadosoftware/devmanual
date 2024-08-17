
We will list a range of "concepts" like "capacity planning"
which are important parts of the plumning of a software system 
and so you need to understand, and understand how it fits into our
system

Each componwnt shows how theybwork indovidually,
shows the bronze, silver and sometimes gold approaches 
and implements the bronze levels into our "out of the box" 
software team management syatem



- logging, event capturing
- production monitoring and QA in production (spectrum)
- unit tests, mocking and stubbing, 
- teat rigs emvironemts
- config handling and environments
- security authentication authorisation access
FIDO / client certs etc
- queues and queueing theory
- runbooks, prod support 
- trade off between urgency and robustness (promtiong code and FFS) 
- use of dashboards
- business metrics growing out of / related to tech metrics
- 



- Wikidata as sourc eif "truth"? https://stackoverflow.com/questions/55961615/how-to-integrate-wikidata-query-in-python



What to moniotr on servers
https://news.ycombinator.com/item?id=41240379

Queueing Theory
---------------
https://news.ycombinator.com/item?id=29225681

The basics of queueing theory are 

mean rate in / mean rate out / variance distribution

So lets model a simple cars at traffic lights - how 
often at what variance will ot take for there to be a queue of ten cars (whichbwill block the next interaecrion?)

Then using thatbmodel, what donyou meed toncollect frommevery 
connector in your ecosystem to be able tonbuild queue based models?

how to raise red flags, plan for expansion etc? 

(Production monitoring, capacity planning)






plumbing
--------
Four dashboards 

- software in development (new projects
new capital) 
- marketing (funnels) & finance (payjents and churn and costs)
- current operations performance speed v stability
- unmeasured operations 


GPU progrsmmjngcand derp leadnkng

data structures (database structures)

functional data atructires

CSZdZt data struvtures

heaph dara structure 


Coders are the new Managers
---------------------------

Software is becoming central to how many many businesses operate.  

But software grows its own scaffolding - and this essentially replaces the original human (https://en.m.wikipedia.org/wiki/Strangler_fig)

This scaffolding has layers (see meta meta notes) but it grows to the point that it is now providing all data about the performance of the software which is now the performance of the business - and coders are the only ones able to chnage it.  (two rods mag) 

- code solves specific business problem
- write an environment that allows easy testing (test rig) and deployment (release process)
- write code to monitor the code - from is it running at all to its performance speed, is it outputting correct data (log monitoring)
- how to monitor in production (qa to performance monitoring)
- how has this chnaged the problem we had - we need to measure the metric as well
- what if we adjust the orignal code - how does it chnage on the metrics we care about? 
- what about chnage a different metric - are we fixing one thing to break another? 
- where is the model to predict this - it needs to be encoded so it can be tested (backtested) with prediction 
- another environment needs to be built to verify the model / replay production 
- pretty soon we have a model of how the business reacts across many areas and metrics - and we have an env to test validate some of that (pre release verification) and can validate it in production 
- and the orignal tree is gone


Everything texhnical you might want to donin a large orfanisation is as simple as the technical side in a two person startup

- python
- prolog
- haskell
- Sql

Plumbing
- authentication 
- authorisation
- access 



The role of morale in war battle and organisations - this is where leadership excels 

software is engaged (front of battle?) at the point of user interaction - being used - and further back from that development occurs the less effective feedback the worse the decision loop is - individuals decisions make all the difference - we can look at operational aspects (communication, logistics) at the level of general and then strategic issues at financier and politician level but 



politics and organisations
- the role of politics and oN levels - you can hear statements that are supporting an elite 

at each layer we have engineers down and airways and politicians upwards - you must build system to make the next hire workable, provide the purchased service / product upwards - but political is always about representing the people around upwards - not using them - the political is local politician on behalf of the constituency 

politican ipwards means representing on behalf of 
i 

treat it like politics - have decisions made at higher levels and publish them so the org A and B can see what is going on 

politics is the sorting out of common agreements amoung each level - and applying up for changes 

2 columns A and B, 4 levels 


A politician is at the next level up - but just as war is not about tactics and weapons but logistics and supply operations then business is not about polities - it's about building the systems to apply those policies at marginal costs 




the elite trade off - it's like paradox of representation - as long as elected is self aware and going in right direction and making few mistakes (wrong not wrong) it's bearable not breakable

but often the politics is retoric not aligned to reality so much it is the dissonance of totalitarianism- which is of course what a hierarchy of (economic) coercion is 


everyrhing hard is down to the structure of org

one approach os to make relationships - but this only helps you and makes you kore valuable

the right approach is to increase the wealth for all - thats what this bookmis about 

complicated is forst oass - and thats all most entrrprises can ever achieve because simplicity requires constant refinement and expeimentation and its waaay easier to buy that in vendors - who rhneaeoves are enterprises and  conlkicated meeting buyer checklists 

techs talk to texhs is best aolution to most buskness problems - indicating software literacy is a general solution 

All projects are startuos looking for validation in form
of funding - no project is ever new in mind of CeO there is always soneone else whonis closer to engineering having ephiany (phase soace)

so all enterprise work is trying to build something that fits inside current philosophy when outside it 

ventire funding internal

pipelijes of process can be automated and adjusted more easily

a policy manual followed relentlessly 

its all 

worker
coder
financier 
oolitician 

anythingninvetween adds friction ans cost 



democracy lies in the approach to understanding yhe decisions we take not in how we take decisions 

management is "specially privledged people taking decisions" - but generally trying to take decisions based onnsxientific priciple of eliminating the wrong

but they use people they trust, take all important decisions in a rush ten minites before the budget deadline 

a better democracy has more people invocled in deciding what is wrong and then maybe voting on what is right - but its much wasier to stay in org that you have helped prevent do wring than not

thats democracy - can i trust it to do not wring 

also internet is a snapshot ofnhuman metamind 
