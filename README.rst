================
Dev Manual
================

How to build a software stack a software teams and a software literate  company


This is my *attempt* at a How To for a software company.  It focuses a lot on the software stack(s) that I think are reasonable (not best just reasonabl) practise for a cloud native company.  But it also focuses a lot on the processes needed to use those stacks - talking git without talking about continuous integration is a bit silly.

The goal here is to run a small SaaS like business - using the code I write here.  The dashboards, the AWS integration etc.

Each segment has both code that is runnable (and should be what I use to actually run the business) and has a roadmap - so where I am now might be a horrible commercial compromise and I want to at least pretend I know how to do it better.

Another POV
Any business is only as strong as it's weakest link - strong sales with poor support? So the goal here is not to be best - but to be competent across the board, conoetant and automated.  

So - let's get started.



The desktop metaphor
It's powerful  and widely understood - so how does it apply
today? I want a desktop where the applications Inwant to use are linked from  - so we shall have simple naming convention (ui.customers.businesspanda.com, api.customers.businesspanda.com




Cloud Native 

Languages
I make no bones about this, I am going to go Python. It's been my goto language for decades and has paid for my children's food so I will lean on it one more time. I think leaning towards erlang / Elixer in a few years will be a good choice but right now this is fine.  See beating averages Paul Graham

Cloud stack

I am choosing  docker to AWS for now - it's pretty safe, has bearable costs (actually that's a whole other discussion)

My expectation

A SaaS business of around 10-500 clients with around 10-20 users each - so 100-10,000 users.
(you will see me dance naked in the streets if I hit 10,001 users)

So this is clearly a B2B idea, whatever it may be.  And aimed at smaller businesses because who has time and energy to try and get Fortune 500 company to sign a contract? 

Stacks

Docker (so Linux). Stick to basics of RedHat 
Run docker 


Summit: business model simulator
Ops simulator 
Development simulator 

use simpy??
Plan: we have a simulator for our dev process and our application - so we can propose a feature, make assumption about which needle it will move and determine if it is worth moving - it's part of definition of done / ready 

Moving the needles
- does a metric move after a release - what else has been released since? 
One of the good reasons not to do continuous delivery is not having metrics guide you. 

Monitoring and metrics

https://deadmanssnitch.com




Data Stores

- RDBMS
- Tabular 
- Docs
- archives

Authentication

Authorisation

Logging

Metrics

Business Events

Report making / analysis

Blogging

Html templating

Branding

Marketing 
- Speak to customers (automate and records)
- Contacts database
- CRM 
- email review
- utm_source - how to track clicks from emails through to your site

- Interviews around the major themes - CI, testing, security, 
- .org design, coase economics, etc etc 

Find people and validate the chapters and interview for podcast / vlog






Build by :

sh ./mkdocs.sh

Start with simple non-serverless stack : 

python 3, PostgreSQL, and vue.js. 

https://github.com/philips/ghar/blob/master/README.md


A developer mnaual explains to a new developer in a company "how we do
things around here". It is the rules to follow to work well with your
fellow devs.  Mostkly it is how to work with the Continuous
Integration server, but it is also how to treat others with respect,
and how to be involved in decision making etc.

This is my devmanual - 


- Dev Manual : how to build the systems needed to develop software : deep dive "labs" on big subject areas like important data structures / algorithms, build-your-own example databases, erlang chat clients, graph databases (dagobah)





There are two kinds of devmanual

there is the manual *for* developers and there is the manual *about* developer processes

For most businesses - if for example you are going to sell a business, then the manual *about* the processes is what counts.

- release process
- SDM process sdlc
- infrastructure 
- backup recovery disaster recovery

this is stuff that is how do we operate without you, how do we scale without you, how do we change without you 

Audit cloud services for security
https://news.ycombinator.com/item?id=23262873
