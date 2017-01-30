:rm
Best Practises, Open Source
===========================


My best practises Open Source Project

Guest blogs in Rackspace etc
Focus on open stack deployment


So like many others Inhave a sprinkling of Open Source projects,
ranging from fairly full featured to a good idea and two hours typing.
But OSS is not simply the place to practise ones actual coding
skills - but it could be a place to home the skills and approaches
needed around the actual work.
- death of middle management

So this is my *exemplar* project - how I would run a commercial providing-food-for-the-kids project if I had the managerial space - and perhaps with my own company I shall

1. source control
2. tech debt and tech assets - code and tests
3. requirements lifecycle (PEP)
4. automated build and deployment (dogfood)
5. Documentation and Marketing
6. openness and reviews
7. Progress Not Perfection (YouTube clip)
8. static and other analysis
9. performance mgmt and measuring everything (and making reports on everything)
10. Automatic project mgmt
11. Risk management
12. have fun, try new things, don't be afraid

Sustainable Open Source
I am by no means a prolific OSS contributor, and my contributions are sometimes of poorer quality than I wish.  This is the conflict between the inner project manager and the inner software developer.

Let's look at a discussion in clean Coder by uncle Bob - (ref)
Here there is an ideal professional developer and an ideal professional PM who when one says they cannot the other accepts.  My problem is that for a lot of jobs and times, one is expected to act as the projects PM and the lead Dev. In which case you have two personalities inside you - and the PM one is socially seen as the professional correct one (hit this arbitrary deadline) but the Dev is crippled by social pressure we all have inside ourselves - the idea that maybe perhaps we could do that deadline

- need to please


Instead we could have red lines:

Automated testing and coverage
Strategic decisions - well they are strategic (cannot be hedged away by tactical work like automated tests)

Can we see tests as risk hedging.  So is this about risk mgmt?

Software risk mgmt :

Hedging and option pricing

Of course - retainers are option premiums !
So how should they be priced ?


Because the values of option contracts depend on a number of different variables in addition to the value of the underlying asset, they are complex to value. There are many pricing models in use, although all essentially incorporate the concepts of rational pricing, moneyness, option time value and put-call parity.
https://en.m.wikipedia.org/wiki/Binomial_options_pricing_model#Method


Source Control
seriously, just use git but githubfkow
rewrite as much as you like until you publish
commit public ally with a description in the commit, bugid is not enough.  explain why to the reviewer - put the detail in the commit message (see no project management)

tech debt - writing code introduces more complexity and bugs.  it is debt. even well written code is debt.  Responsibly lent mortgage debt but still debt.  badly written poorly tested code is payday lender style debt.

assets are the opposite of debt - tests are the opposite of code.  tests tell you code is like well invested debts, debts you know went on sensible things.

Contract testing - like testing the type of parameters and returns - aka Eiffel

3. Requirements lifecycle.  oh yes. oh yes. seriously the amount of money major enterprises throw into projects with poorly formed, badly if at all written requirements that are promptly not read by anyone involved is - well it's a lot let me tell you sonny Jim.

so part of the no project mama gents process is to actually have requirements, you know, written down, discussed, thought about and tried out.

these are of course miniature projects in themselves.

Trust in people to challenge why others are doing something.


4. automated build and deployment
for an automated build and deployment project this is pretty obvious

5. docs and marketing
docs are vital.  screencasts it seems are just as vital.
however marketing is begun there but not ends there. forums.
being an all round good egg

6. openness and reviews

7. progress not perfection
I have a massive discuss next between what is reasonably possible for a average to good developer (me) to be able to achieve in two or three days at work (with interruptions) and what I *could* do if I had got plenty of rest, drunk my Orange Juice, refactored code on this area just last week and ... well, I think I *could* do more than I have.  but this leads me to think I should have done more - and that tends to lead to outrageously negative defensiveness, including rushing and cutting corners to get it done in the arbitrary self imposed deadline, or perhaps worse, lying about how far I have got and saying "just another day" (often lying to myself first)

https://basildoncoder.com/blog/pg-wodehouse-method-of-refactoring.html

8. static analysis

9. Performance analysis

10. Automatic project mgmt.  not tasks. milestones.  not manually approved milestones, automated tests that validate milestone.  and requirements analysis


11. Waltzing with bears

12. have fun.


On 24 Jun 2015, at 19:48, Paul Brian <paul@mikadosoftware.com> wrote:

Info products:

- PyHolodeck, saltstack and python deployment for the cloud

eBook
eBook and screencast
eBook and 4 hours consultancy

Py2to3 consultancy
work with EMagine
develop own eBook, identify potential python developers


Future of Software
mobi - release in Amazon etc

SaaS products and enterprise products
- MyTestVideo - selenium recordings of new bug fixes
- Standard Operating Procedures - especially for DevOps
- Blockchain : share ownership registration, split out by pension fund holders

knock on head:
kickstarter at kids school? no do that but kill off code club



Sent from my iPhone

On 24 Jun 2015, at 11:20, Paul Brian <paul@mikadosoftware.com> wrote:

useful business services to automate / OSS /  SaaS

project mgmt
Standard Operating Procedures
laptop builds

options:
moonshot - video of selenium
sops
blockchain - licensing options



Sent from my iPhone
