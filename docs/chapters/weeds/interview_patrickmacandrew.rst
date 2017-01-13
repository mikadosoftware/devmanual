=========================
Patrick MacAndrew - PeerJ
=========================

:date: 6 Feb 2013

Continuous Deployment at Scientific Journal
===========================================

Patrick MacAndrew is the "DevOps guy" for `PeerJ <www.peerj.com>`_.  PeerJ is part of the current exciting movement towards greater open access to the world's scientific publications, which after the tragic death of Aaron Schwartz cannot come soon enough.

Patrick is a 15 year IT veteran and moved to London 9 years ago from the USA ("Oh, whereabouts?", "Errr, all over really").  After a startup he was working at went the way of most startups, Patrick took some time to look around - and liked the look of PeerJ, starting with them about 18 months ago.

After some pleasantries, Patrick took me through the rough architecture of the PeerJ site.  It consists of "about two dozen" AWS servers run under Scalr, working as production MySQL Databases and PHP App servers, along with the all-important Dev/Beta environments.

When Patrick joined a lot of the deployment code was on Scalr, and got pushed by the developers - usually to allow the San Francisco office to review the business logic behind the code.  Adding Jenkins into the mix means that a successful build of the system in Jenkins triggers a Scalr API call that will push the code to the beta environment.  Patrick readily admits that the Continuous Delivery goal is still in front of them.

.. pull-quote:: "We want to get to the point where we can *scale without thinking*.  We are a long way down that road, but there is still plenty to do."


"Less time, greater ease of use - and far less error prone" was Patricks simple description of how the build step has improved developer's lives - however he feels that the number of deployments per week has stayed relatively stable over his improvements - a function determined more other factors in the business than a slavish desire to push 50 times a day just because they can.

Patrick says he divides his time roughly 50/50 between project work and putting out daily fires - still a healthy proportion for the only DevOps guy in a growing young startup.  

The startup culture also may be helping the developers too - running a "loosely modified Scrum :-)" there is sufficient trust in the infrastructure that home working is "flexible", and managed through a combination of just about every form and mix of email, IM, IRC and Skype.  Sounds pretty familiar !

Patrick then wondered if he could have some extra time to deal with the next seamer - "what are the three changes that will make the most difference at PeerJ?". But he rallied well, and focused on three areas that will have a few heads nodding in agreement.

Firstly, more testing, especially at the User Experience end (lots more Selenium-style tests).   Then getting to the point of being able to *scale without thinking* - a phrase so good I hereby steal it ! And finally better monitoring and metrics - Patrick has been investigating redis and graphite to try and give a real-time flavour to the business metrics every startup lives or dies by.

Overall Patrick has painted a picture of a growing startup meeting challenges with a pragmatic mix of high-flying vision and realistic appraisal of the effort and time involved in getting there.

Thank you for taking the time to talk Patrick, and I look forward to seeing PeerJ's success in the future.






