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





  
Common Architectural choices
----------------------------

Discuss and review common architectural choices

* cacheing
* containerisation
* REST API

  

https://www.microservices.com/talks/dont-build-a-distributed-monolith/

Use public apsi, based on protocols 

Because if you just write one client code to work with one server code slowly they drift together / and worse you just end up sending round the depenancies of that client, installing those 50 libraries everywhere (npm)

That means if you want to install a breaking version of client suddenly you have to install the 50 new libraries in hundreds of places - you have built a distributed monolith

Hunting
https://www.usenix.org/conference/enigma2016/conference-program/presentation/payne
Talk online

https://www.google.co.uk/amp/www.techrepublic.com/google-amp/article/how-to-establish-strong-microservice-security-using-ssl-tls-and-api-gateways/

Obvious but checklist


Basics
TLS pki, using short lived certs internally
Longer pki for external contacts
Maybe use oauth for consumers


Service mesh
https://eng.lyft.com/announcing-envoy-c-l7-proxy-and-communication-bus-92520b6c8191

This evolved into istio now wider supported

An on host network proxy that could transparently just pass through network traffic OR can apply policy on say service discovery, load balancing, circuit breaking, rate limiting etc - a balance between not knowing which network portion the hosts will be on so not being able to use traditional routers, and well this is part of software defined networks but at the application layer

Software defined networks push packets around, thisnoperates on requests??? 


Basic security and architecture

https://stackoverflow.com/questions/549/the-definitive-guide-to-form-based-website-authentication

The basal architecture:

