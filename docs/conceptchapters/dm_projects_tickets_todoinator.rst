Ask a Software Engineer to design Project Management
====================================================

<Name>, an influential Googler who helped popularise the idea of
Software Reliability Engineer (SRE) said "SRE is what you get when you ask a
developer to design an Operations process."

To be honest, this entire book can be boiled down to "Software Literate companies is what you get when you ask a developer to design a company".

But lets just look at one (important) aspect of a company - *Project
Management*.  Fundamentally, work inside a company can be divided into
two parts - *running the company* and *changing (improving?) the
company*.

Running the company is just the day-to-day
business-as-usual processes.  Opening up the store, stocking the
shelves etc.  (and yes, very amenable to automation).

Changing the company is usually harder.  It is a search process usually, looking for product-market fit for early stage companies, or later stage companies loking for efficencies etc.

And CHanging the company is almost always coralled into *projects*.  As such automating project management will be very very helpful.

And as we are designgin a softweare literate company, we dhall desing a compny that is mostly automated, and driven by software - and as such changing the software means changing the company.

Lets repeat that - changing the codebase, means changing a company. And if changing the codebase is now project management, then project management should flow *from* gthe codebase.




Software Literate Project Management.
-------------------------------------

I am embarrassingly bad at traditional Project management.
Co-ordination, keeping an eye on the most important parts.  Basically
I assume that if i know something, then everyone else knows it too.
So there would be no point in telling other people about
it. Co-ordinating. for example.  Also my timekeeping sucks which tends
to piss everyone off eventually. (Such as the woman I left waiting at
the Cinema so long, the film actually finished before I got
there. There wasn't a second date.  Not sure why I am sharing, but you
get the idea. Manual project management is a skill I really want to
automate away.)

So what can a codebase do that is *better* than manual project managers?
Better than teams of "change specialists"?

Well, lets start with lying.  People lie. Everyone lies. If your
husband asks if this sweater makes him look fat round the middle, you
say "no darling".  If your boss' boss asks if the project is going to
be ready on time, you are *optimistic*.  You don't for example,
recommend a regieme of salads, beans and cutting out the chocolate
biscuits while running 2 miles a day.  You dont say the code base is
crap, the test coverage laughable and the specifications so vague we
still dont know what the goal is.

No, you lie. So your boss thinks its ok. And meerily everyone trundles along
kind of hoping everything will work out all right.

Whcih brings us to project management and risk management

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


