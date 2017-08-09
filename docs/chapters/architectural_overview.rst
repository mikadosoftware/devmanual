======================================
Architectural overview
======================================

The architecture of a micro-services based eco-system is realtively simple, but
I shall introduce each stage or component one step at a time.

We will start with just running a simple Python web app on its own (a few lines
of code at best) and move to a eco-system that includes enterprise level metric
reporting, Google-level best practises in SRE (sysadmin'y term) and more.

The goal is to go from "I have written my fantastic app" to "I am confident I
can run this without making glaring huge holes."

This is not a process to make you experienced, talented or skilled.  THis is ...
well, there is a phrase "Its easier to avoid stupidity than achieve brilliance."
Its true. Avoiding looking stupid is mostly a question of knowing the layout of
the landscape, taking care to avoid obivous mistakes and moving slowly (as in
slow programmer).

The essential point to remember in software engineering is that software is like
wearing seven-league boots.  As Terry Pratchett said, When wearing boots capable
of putting one foot 21 miles in front of the other, its vitally important to
step carefully.

The take away for me is simple - if you are going to take a giant step, take it
carefully with lots of tests and thinking. If you are not taking a giant step,
why not. You have seven league boots for heavens sake.

You can win by baby steps, if you are wearing seven league boots.


We are going to build a fully functional micro-services architecture *and*
the attendant engineering processes, team, support systems. A complete eco-system
for software enginerring and services.

And we are going to keep it simple.

Why? Because its the only way to understand the decisions at each step.

* source control, repos and searching all repos
* builds
* deployments
* testing - all 3 kinds, all 3 passing.
* features vs simplicity - PEPs, discussion, goals and PM vs RM
* risk management and project management
* ownership, not looking foolish. Avoid the contractor curse. Its not the olympics. There is no race. Its farming, or mining.
* docs and marketing
* reviews and code ownership. Teams are more effective than rockstars
* Analysis, no blame - code analysis, production analysis, business analysis
* tie in other business systems like accounts


Host architecture
=================

Swardley maps may be useful here



    -------------------
    App
    -------------------
    App dependancies
    -------------------
    EcoSystem Services
    -------------------
    Host OS
    -------------------
    Physical Server
    -------------------
    Data Centre
    -------------------

EcoSystem services
- logging
- TLS, auth
- metric gathering

App depednancies
- DBase?

App
.deb files




The first steps
===============

* simplest app possible
* adding a unit test
* adding a performance test
* building it under python / distutils
* running it under systemd
* running dual, behind load balancer, using weaver/ansible/fabric
* building it on a build server, using .deb files
* build assets -> docs, perf results, test results, .deb files
* Security on microservice
* Identity
* host-host services (ntp etc)
* host-app services -> logging, TLS etc 
* central services - DNS, metric names,
* code reviews and code promotion
* metrics gatehrinfg
* log mgmt
* rolling out changes
* incident mgmt (incidents, SLAs, uptime measurements from metrics etc etc)
* adding message queues, backend services, passing back identiy
* adding dependancy services - monitoring everything
* CTO dashboard, mission control centre
* bug tracking, feature development
