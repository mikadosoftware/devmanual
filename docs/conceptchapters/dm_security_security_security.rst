Use this chapter as opportunity to interview well known and get clarification 

The landscape - and what you can do
===================================

It's a dangerous cyber world out there.

The 90s to Heartbleed
Heartbleed to Huawei
The future

The 90s to Heartbleed 
This was a wild west - slowly value was being put online, and so it was being stolen by criminals
State actors it seems had a whale of a time - the ease of which stack overflow could be exploited 


CarderPlanet became focus of card sales online 

Heartbleed
A shock moment
Snowden had told us - but to be honest I think it was the SSL vulnerability that brought home how little we had been thinking about our dependencies

The future 
Recovering from part mistakes and building secure future - costs will rise, socialism is our best hope 

- two factor auth and passwords
- open source is still a tragedy of commons and still humanity's best hope. (imagine a world where you could not write down words you chose to - but had to select from authorised or proprietary paragraphs to express yourself)

- socialism - software socialist needs re expressing.  Look at western world today - 


The landscape today
https://krebsonsecurity.com/2013/06/the-value-of-a-hacked-email-account/


The legal landscape 
https://arstechnica.com/tech-policy/2019/01/20-legal-cases-across-20-years-these-are-our-favorites/
192 countries in UN - yeah ... we might need the lessons in Brexit and EU harmonisation 

Basically we are all f****d
============================

When respected security writer Bruce Schneier writes a book titled 

But there is light - slowly larger places are learning to lock it all down https://threader.app/thread/1063423110513418240






but hospitals mri scanners??

become our own pentesters 
http://blog.mallardlabs.com/zero-to-oscp-in-292-days-or-how-i-accidentally-the-whole-thing-part-2/



A Skeleton Design for an evolutionary secure eco-system

Security, as you may guess, is hard. And yet there are a few *basic*
approaches that are more likely to lead to success than others

Firstly it's worth pointing out that online security is never a fixed job, but a process, and your approach needs to *evolve*.  Secondly remember the most important rule - "Anyone is capable of designing a security system that they themselves can not break"
I cannot break this design.  Beware.
Thirdly, remember to evolve your design but have the shape of it in from the beginning.  Look at 'libconfig.py' as an example - it can be as simple as a python library to pull config from environment variables - literally a couple of lines.  But having put that in place, developers will just import that library, and when you upgrade the library so that instead of reading from the environment it pulls from a secure vault, you have improved the security situation and the developers have not noticed.


* Common, evolvable libraries
  libconfig, liblog, libsecrets

* use a vault

* service discovery layer

* user identity

* machine identity

* self hosted CA



The lifecycle

A docker instance is built on a "build machine". It is then saved somewhere, with its hash recorder.

The instance is brought up on a host machine (AWS) and given a set of configuration and a set of secrets.  This is the weaker part of the process, but we go with it.  Kubernetes or rancher are good for this process.  

At this point the machine has a known identity and a private client certificate to use to prove it.


Log shipping to central audit
Using security audits

Policy reference
https://developer.conjur.net/reference/policy-markup.html

Ref: 
https://developer.conjur.net/key_concepts/machine_identity.html
Hashicorp - vault


Config and keyrings
Use Linux Secret Service as means to pass complete secure set of secrets over to a container - and make them accessible (ie 'summon' like) 


Pentesterlab.com


Supply chain Security
---------------------
We are all hugely depenandt in other peoples code. In many ways this is good - software reuse.
In others it is terrible 


Solutions - standardised eco systems 

RHEL is basically charging for the cost of managing depenandcy chain - it's why Debian Developers have months of mentoring to actually become part of the web of trust

It's why I suspect "kyretsu" of trusted webs of companies using same or similar stacks will arise simply because it's easier than doing it yourself - and frankly this is what the dev manual is trying to kick start

There can be great value in curating, monitoring for malicious actors, fuzzing and supplying curated bugs upstream, and then funnelling development money upstream as well


A plan for sustainable Open Source? 


Why you need a Purchase Order System
-----------------

https://www.justice.gov/usao-sdny/press-release/file/950556/download

steal 100M from google and facebook 