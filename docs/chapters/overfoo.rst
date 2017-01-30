===================
Dev Manual Overview
===================

So place to put all the bitty mind parts






This will become a toctree of the file sin the directory, but for now it is a
list of work or notes on what makes a developers manual for 21C

"How are things developed around here, and why."

* Source control
* prmotoing code up
* having a robot promite code after meeting automatic criteria
* having automatic testing
* build servers
*



1. source control
   5 chars etc.
   but good example of using automated policy enforcement on checkin

2. tech debt and tech assets - code and tests

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
   Look, bash is just *fine*
   pyholodeck

5. Documentation and Marketing
6. openness and reviews
7. Progress Not Perfection (YouTube clip)
8. static and other analysis
9. performance mgmt and measuring everything (and making reports on everything)
10. Automatic project mgmt
11. Risk management
12. have fun, try new things, don't be afraid

* plumbing needed for every project / component
  - error handling
  - config
  - todo
  - docs
  - logging
  - metrics
  - activity reporting
  - governance, style, testing, coverage
  - source code policy
  - physically distinct DEV, [UAT], PREPROD and PROD
    UAT is optional if you have automated testing.
    dont mix preprod and uat cos you will want to release when users are looking
  - dashboards for can I release, and what is governance ?
  


* distributed file systems
  Cephfs, GlusterFS, Lustre, and HDFS

* work queues
  CElery, zeroMQ

* amazon, openstack

package management
http://nvie.com/posts/better-package-management/

Instrumentation
https://honeycomb.io/blog/2017/01/instrumentation-the-first-four-things-you-measure/

Pki
Cloudflare how to build your own
https://en.m.wikipedia.org/wiki/Hardware_security_module
