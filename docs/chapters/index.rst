==============
The Dev Manual
==============

This is a dev manual - a "how we do things around here" for a software
development team.

Normally this would be written (quickly, by senior engineers) as teams
scale up to try and get new joiners onboard quickly, so they would not
bother the senior engineers so much.

This one is slightly different - it is trying to be a plan, a
blueprint for how to run a software team, and slowly by extension, a
software company.  It is in fact my plan for my side-project(s).


SRE
- https://news.ycombinator.com/item?id=41300368#41301147
Paying off my Mortgage.
-----------------------

So I am old, and have spent most of my adult life in the "Internet"
industry.  I rolled out some of the first ever ADSL services in the
UK, wrote the first websites for companies you own shares in, I have built
teams from the ground up and basically I have made *other people* rich.

Now it's my turn.

I am too scared and too old and have too many kids to just toss it all
in for a billion dollar start up.  But I do think I can bootstrap a side project
or two into something valuable - this blog will keep me honest as I try to
build out bootstrapped side projects that I intend to drive to
sufficient revenue to pay off my mortgage.

As I plan to do more than one side project over the next five years,
then I want to standardise and re-use as much of the marketing and
technical tools (yes both matter) as I can.

Tools I build along the way SHOULD be released to the public *either*
as open source software, or packaged productised tools.  I do not want
to spend time building a piece of software that gets used only by me -
I will have little enough time, so all of it needs to be put to work.

My plan is to keep going - publishing and promoting - for the next 5
years - to June 2025.

And to include my family in these activities where possible.


So now what?

Designing a sustainable bootstrapped Business
---------------------------------------------

Jason Cphen

* B2B
* niche
* not time critical support
* small enough but part of big enough ecosystem to survive if we are
  8th or 50th biggest player.
* an eye on the exit
* Grind out to the first 150 customers, charging about 500 - 1000 pa
* Recurring revenue
* aim to build to 1M ARR
* Cashflow is king

The building blocks
===================

Plumbing
The fundamental parts of any piece of useful software are almost
always the same. Not the underlying tiny little kernel of a few
thousand lines that is the widget we are supposed to be selling - but
the plumbing around it that means it can do its job.

FOr example - logging, config, feature flags, reporting

The actual code service

Support tool

CRM

Personal networking system

Marketing - inbound
 Where people come to us
 We do this with
 
Marketing - outbound
 Where we reach out to, cold call(!) them

Marketing funnel
 Awareness
 early transaction
 information and updates
 onboarding begins
 customer success
 continuous usage
 upgrades and lifecycle
 ending relationship

Security


SEO and content production

Email list and management

Stripe and payments

Accounting and bookkeeping

management reporting, dashboards

* Code as a crime scene
  Static Analysis and raising all boats.

* Seeing every beat of the corporate body.
  Dashboards, newspapers of the data rich world - making it easy to understand

* Teams and culture
  Awareness, honesty, task focus.

* Workstation builds and 'mis en place'

* Hardware - an effective moat

Exemplar

package management
http://nvie.com/posts/better-package-management/

Instrumentation
https://honeycomb.io/blog/2017/01/instrumentation-the-first-four-things-you-measure/

Pki
Cloudflare how to build your own
https://en.m.wikipedia.org/wiki/Hardware_security_module
- Hardende images / servers
https://www.cisecurity.org/services/hardened-virtual-images/


chaos engineering 
http://principlesofchaos.org



The action plan
---------------

* identify rough niche to attack, with rough solution
* define audience sterotypes
* find them online
* get feedback and find the pain
* landing page style hook with will you buy
* build something that people will pay for (BSTPWPF)
* SOP / automate ways to reach customers / find them etc
* repeat and grow

So this has several components

Ideas
Audience finding
Where does audience hang out online (sparktoro!)
Talk to people


From Jason Cohen Desiging a business







Plumbing 
========


* plumbing needed for every project / component

  - error handling
  - config
  - todo
  - docs
  - logging
  - metrics
  - activity reporting
  - business and technical event hooks
  - governance, style, testing, coverage
  - source code policy
  - physically distinct DEV, [UAT], PREPROD and PROD
    UAT is optional if you have automated testing.
    dont mix preprod and uat cos you will want to release when users are looking
  - dashboards for can I release, and what is governance ?

AQA - automated Qualty Assurance
- ast based syntax checking
- checking integration test
- similar to CI as well

But even past that we need




* A.S.S.K.I.S.S
  Architecture of Software Should Keep It Simple, Stupid

  <discuss tech arch>

  My architecture around here -> serverless if we need to be
  Keep small (micro) services running.
  Have a single simple queue
  Standard tools and environments in all services (we do not beleive in
  having lots of different languages)
  















  
* Source control
* prmotoing code up
* having a robot promite code after meeting automatic criteria
* having automatic testing
* build serv


3. requirements lifecycle (PEP)
   the wrongest part of the agile manifesto
   """ The most efficient and effective method of
conveying information to and within a development
team is face-to-face conversation.
   """
   Ya do need to write down the discussion.
   written Proof overcomes authority problems
    it is also way to get everyone discussing
    this only works with really co-locateed and mission focused teams

4. automated build and deployment (dogfood)
5. Documentation and Marketing
6. openness and reviews
7. Progress Not Perfection (YouTube clip)
8. static and other analysis
9. performance mgmt and measuring everything (and making reports on everything)
10. Automatic project mgmt
11. Risk management
12. have fun, try new things, don't be afraid


  

