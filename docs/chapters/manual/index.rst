===================
Revolutions
===================

The software development process is like a wheel.  We write some code to solve
a problem, we *automatically* build it, test it, deploy it to one or many servers
and we monitor it and the eco-system in which it lives, and we spot things we
want to improve and go back to writing code.

.. :: draw a better diagram

  Source -> Build -> Test -> Deploy -> Monitor -|
   /\                                           |
   ---------------------------------------------

   The eco system is things like DNS, hosted services like OpenStack and AWS,
   things like PKIs and simpler things like comprehensive logging and metric gathering.

In this Software Manual, a companion piece to the Software Mind, I will walk
through the development of a piece of software - going through many revolutions
each time adding some more to the technology stack, but trying my best to keep
clear the underlying simplicity.




Revolutions
-----------

* Simplest possible
  We shall build a working web app (about three lines, honest).
  Build it, test it, deploy it to a location locally, and log it.
* systemd, well-behaved services
* simplest app possible
* adding a unit test
* adding a performance test
* building it under python / distutils
* running it under systemd
* running dual, behind load balancer, using weaver/ansible/fabric
* building it on a build server, using .deb files
* build assets -> docs, perf results, test results, .deb files
* Security on microservice
* linting and style and code reviews
* Identity
* host-host services (ntp etc)
* host-app services -> logging, TLS etc
* central services - DNS, metric names,
* code reviews and code promotion
* metrics gatehrinfg
* log mgmt
* rolling out changes
* adding message queues, backend services, passing back identiy
* adding dependancy services - monitoring everything
* CTO dashboard, mission control centre
* bug tracking, feature development


Revolutions
===========

.. toctree::
   :maxdepth: 1

   Revolutions01/index.rst
