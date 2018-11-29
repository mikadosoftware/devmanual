Use this chapter as opportunity to interview well known and get clarification 


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
