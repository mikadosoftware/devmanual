Ask a Software Engineer to design Project Management
====================================================

<Name>, an influential Googler who helped popularise the idea of
Software Reliability Engineer (SRE) said "SRE is what you get when you ask a
developer to design an Operations process."

To be honest, this entire book can be boiled down to "Software Literate companies is what you get when you ask a developer to design a company".

But lets just look at one (important) aspect of a company - *Project
Management*.  Fundamentally, work inside a company can be divided into
two parts - *running the company* and *changing (improving hopefully) the
company*.

Running the company is just the day-to-day
business-as-usual processes.  Opening up the store, stocking the
shelves etc.  (and yes, very amenable to automation).  This is the programmable
company - it's hard to do - good solid processes that are repeatable and scalable and respect your values and reflect them externally - it's hard to do.  Harder even to automate, to link the physical to the virtual.  I heard recently that the restaurant chain Wahaca recycled all of its waste - using upto six bins outside the kitchen.  And how much harder is it then to weigh those bins as they grow over the night, to put rfid scanner in them.   it that is how we need to link the virtual and the physical, that is how processes get audited and chained and checked.  It's going to be a lot of work - yes.



Changing the company is usually harder.  It is a search process usually, looking for product-market fit for early stage companies, or later stage companies loking for efficencies etc.

And CHanging the company is almost always coralled into *projects*.  As such automating project management will be very very helpful.

And as we are designgin a softweare literate company, we dhall desing a compny that is mostly automated, and driven by software - a programmable company with software mediated processes - and will need programming ...

Lets repeat that - changing the codebase, means changing a company. And if changing the codebase is now project management, then project management should flow *from* gthe codebase.

So that's my big take away here - if project management takes you away from the codebase it is flat out no question *wrong*

Which means almost all project management in the world today is *wrong*.

So no biggie.


Software Literate Project Management.
-------------------------------------

I am embarrassingly bad at traditional Project management.
Co-ordination, keeping an eye on the most important parts.  Basically
I assume that if i know something, then everyone else knows it too.
So there would be no point in telling other people about
it. 
Co-ordinating. for example.  Also my timekeeping sucks which tends
to piss everyone off eventually. (Such as the woman I left waiting at
the Cinema so long, the film actually finished before I got
there. There wasn't a second date.  Not sure why I am sharing, but you
get the idea. 

What I am saying is that Manual project management is a skill I really want to
automate away.)

So what can a codebase do that is *better* than manual project managers?
Better than teams of "change specialists"?

Well, lets start with lying.  People lie. Everyone lies. If your
husband asks if this sweater makes him look fat round the middle, you
say "no darling".  If your boss' boss asks if the project is going to
be ready on time, you are *optimistic*.  You don't for example,
recommend a regieme of salads, beans and cutting out the chocolate
biscuits while running 2 miles a day just because someone wants an opinion about knitwear.

Similarly You dont say the code base is
crap, the test coverage laughable and the specifications so vague we
still dont know what the goal is.

The question was not designed to find out real problems.

No, you lie. So your boss does not have to be disturbed from his comfort zone and your husband does not have to give up their lofestyle.

And meerily everyone trundles along
kind of hoping everything will work out all right.

Whcih brings us to project management and risk management


Most projects are planned *optimistically*.  When we plan a journey we can only plan the landscape we can see, or imagine.

We tend to underestimate the difficulty of the unknown.

So most projects are risky - they have risks that may or may not come to pass.  And most times when a project manager successfully steers a project home what really happened was that they just got lucky.

Luck is not a strategy
-----------------------

Dancing with bears and risk management 
(cf rudolf reporting)

- code can track wjeee we have been and what remains todo?

Risks and tests
- what don't we know - what tests can we run that show we don't have something fixed but we just call it a risk? a test that is supposed to gail's because we are accepting the risk?

Then we can define every risk in code
- we can even model riskmlikelihood in test runs? 

Risk: we don't account for null values
Risks : the ApI we depend on goes away / rate limits us
Risks: the 



https://github.com/risk-first/website/wiki/Risk-Landscape
(review)

Which brings us to Backlogs and True State of project

WHich brings us to tests, and velocity.


* everybody lies
* Capex and Opex, hidden Capex, slow code movement, spikes and inches.
* Software Option pricing
* Capturng cost data. Infrastructure as code.
* ticketing, scrum and agile, co-ordination, risk management.

Everyone hates agile
https://www.allankellyassociates.co.uk/archives/388/why-do-devs-hate-agile/

Software CapEx

- anecdotally loads of time money thrown away as people decide to rewrite or chnage minds
- this will be more carefully managed if it was clear from capex how much this costs

Software - intangible fixed assets 
https://www.quora.com/What-are-the-rules-and-rationale-behind-treating-software-development-as-capex-vs-an-operating-expense


Project and Programme management
================================

So there is a well known story in the Agile world about `why estimates
are always wrong
<https://www.quora.com/Engineering-Management/Why-are-software-development-task-estimations-regularly-off-by-a-factor-of-2-3/answer/Michael-Wolfe?srid=24b&share=1>`_

Basically we cannot do it.  So why do people ask for estimates? They
dont want estimates - they want evenly spaced landmarks. They want
confidence that progress is being made.


It if ain't got a ticket dont work on it If it ain't possible to
rollup tickets you dont know where you are going A backlog out of
context is just a horror There is nothing wrong with top-down design
(see Linux) Backlog for the whole company - agile for the whole
company just see progress on a map.  If its not going fast wnough for
the board they can fix things at their level.


We need to track our work so we can provide an audit trail
THese are useful


Event driven Project Management
-------------------------------

How companies need to reactively plan, with exception / assert monitoring.
How this replaces "managment judgement" with clear budgeting.?


** Project Management
The Chairman's tricky Question
==============================

Some time ago I was asked by the Chairman of the Board what one thing
he could do to make sure all these damn software projects were under
control.

What he meant by under-control, was *on-time* and *as expected*. Which
is not what I meant.

So I had two answers.   One was under control from a development perspective.
This is pretty simple and  boils  down to 

* Require *every* project to automatically deploy to at least a prod-parallel
  environment, *every* day, their most recent approved, tested code
  and post their test results.

These seemed radical, but achievable.  A lot of the *technical* side
of this Dev Manual is focused on achieving this.

But the *real* point was about *on-time* and *as expected*.  And that
is where I gave an answer he did not like.

* Stop having deadlines.  That way nothing is late.

Yes.  You can see why it was not a popular suggestion.

We will expand on that, but I am going to stick to it.  I hate
deadlines.  They infect everything with panic and poor quality.  And
the deadlines are almost always derived from poor information about
reality, and where the deadline should be, and rarely if ever updated,
as if reality and poor estimation are irrelevant.

Its much better to have regular, reality-grounded views on where one
really is, and alter plans based on that.  Automatically.

Deadlines sometimes help. Mostly they do not.

If it ain't ready, setting the deadline to today won't make it ready.


- :doc:`chapters/agile_estimation`
- :doc:`chapters/SoHo1`
- :doc:`chapters/themes`
- :doc:`chapters/urljoin`
- :doc:`chapters/veryquickMBA`


CTO dashboards and Business Process Dashboards
==============================================

Dashboards matter
The basics of code quality can be in dashboard.
The basics of production health can be in dashboard
Putting a business process into dashboard is powerful - use Graphite and "light beam trackers"


- :doc:`chapters/aspell`
- :doc:`chapters/mikado-doc-manager`
- :doc:https://github.com/getredash/redash/blob/master/README.md


Examples and solutions
----------------------
https://blog.plover.com/tech/prudential.html

Quote for payment upto milestones and delays incur penalties 
> "But," they said, "how do we collect the referral fees?"
This is why you need to understand what problem a client wants solved and not just build what their suggested solution is



Improving Ticket Tracking in Path
=================================

It does not matter what tracking system you use, as long as everyone uses it 
consistently.  The silver bullet is not the tool, its the discipline.

Paul's Personal Principles for Ticket Tracking
----------------------------------------------

Everything is either a *feature*, a *bug* or an *admin task*.

*feature*
  An improvement (hopefully!) to an existing system.  It might be 
  tweaking the logo size, it might be rewriting the accounts system.
  Whatever it is, there is some business value that will be added to 
  the whole.  It is *analogous* to a capital investment.

*bug*
  A bug occurs when we find out what we meant to do, is not actually 
  what happened.  It might be a typo in code that subtracts 20% VAT from
  every till sale instead of adding it on top, or it might be a receiver
  on a wall, with smoke pouring out of the power supply.  Either way, 
  it was working as intended, or we thought it was and did not know.

*admin*
  Admin tasks are at best, things we have not automated yet. Filling in 
  expenses forms, posting a letter, updating the web site news feed.
  There are a million and one things we can put under "admin" but if it's
  something we repeat with only small changes, its admin.  If its a one off,
  it might be more like a feature.

Bugs and Admin tasks are simple - they appear in a queue, you can deal with them
in order of arrival, or triage and apply some importance to them, but they 
are just one queue.

Features are a little more complex - they have hierarchies associated with them.
The usual one in Scrum is Theme -> Epic -> Story -> Task.  Sometimes it is
easier to have explicit hierarchies, sometimes it is easier to use tagging.

However this goal is to manage the backlog of work - to allow everyone to see
the forest of themes and epics, whilst still working on trees of stories.

 



Important and Urgent
--------------------

.. figure:: workstreams.png
   :scale: 50 %

Departments / and teams
-----------------------

however there needs to be someone sweeping the floors.

so we have a compromise - three strands of work - feature, bug, admin.
and they are prioritised across the board (admin is very rately at
the top)

but admin does need to get done - so we time slice and pick off top of
the admin queue

this also works for bugs (such as devops) and features

each time has it's 80% focus.  for a developer like seun it's 80% on features

for devops like Ryan it's 80% bugs (where bugs can also be  the
receiver is not working)

for reporting team the 80% is admin - doing the same report but
slightly different


all of it ends up in us getting paid, so it's all "important",
and it's all "urgent" - our job is to differentiate between very very
important and very very very very important

ordering within groups :

each "team" is responsible for a subset of all features, bugs, admin
work. by dividing up in owner we can then prioritise within owner and
within parent owner. that way while remains ordered


Status transitions

I want to change them. WHo is using them for what
WHy have we got resolved, closed 




Cheat sheet
-----------

TEST and Hashin Kanri


Features and Bugs are in the sprint
Support tickets are done on the "admin day".  However we count the
support tickets done, and display them.  Also [ADMIN] is *exactly* the same as saying "support" tracker.  We shall merge this eventually

Burndown is just burndown.


Release Mangement
-----------------


