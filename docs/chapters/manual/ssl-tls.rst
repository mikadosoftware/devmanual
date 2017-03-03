=========================
SSL-TLS and microservices
=========================

.. quote::

    From the HN profile page of security expert T Ptacek:
    
    * Just use bcrypt.

    * Don't build crypto features; use TLS and PGP.


We need to understand the SSL process and so forth to understand the last line

We want to build microservices - we shall do so by using BI-directional TLS certificates under a PKI to allow our services and servers to talk to each other

We shall deploy a simple distributed application and slowly build up its architecture to be modern responsive but also secure. We won't be dealing with much serverless architecture

The road to lambda

- discuss the article by Adam ??



The theory behind TLS
---------------------

http://www.moserware.com/2009/06/first-few-milliseconds-of-https.html

The architecture aimed at
-------------------------

Somthe first approach will be to have one application web server that will 
ask a back end server for some details before returning it to the user in a secure fashion

We shall slowly build on this secure base (always build the security first - features get minus 100) until we have load balanced globally distibut e stack with cdns JavaScript monitoring metrics deployment and more 

We shall get there don't worry



The major problems 
------------------

https://medium.facilelogin.com/securing-microservices-with-oauth-2-0-jwt-and-xacml-d03770a9a838#.z305bkcrl

- CA
- automating handing out cert 
- deploying them securely
- each host can verify each other
- now how does each service on each host verify each other
- now how does a service request action on another service on behalf of end user? 

These are listed at as well:
http://www.grahamlea.com/2015/07/microservices-security-questions/
This is JWt or oauth2.0

And security affects architecture
http://www.grahamlea.com/2015/03/notes-from-yow-2014-scott-shaw-on-avoiding-speedbumps-on-the-road-to-microservices/

But also logging events -> bitemporal business event 
Log aggregation as well as metrics and logging. What is my business domain event (usually money, but maybe stock movement, assets etc etc) 

Can we store bitemproal data efficiently in a UBTree
http://www.scholarpedia.org/article/B-tree_and_UB-tree / https://en.m.wikipedia.org/wiki/Bx-tree

http://www.grahamlea.com/2015/03/notes-from-yow-2014-scott-shaw-on-avoiding-speedbumps-on-the-road-to-microservices/


The other problem - use oauth2.0 as identify proof for customers not employees


JWt
http://nordicapis.com/how-to-control-user-identity-within-microservices/

Adrian Cockcroft 
Netflix CTO guy and microservices evangelist 
Details are https://www.nginx.com/blog/microservices-at-netflix-architectural-best-practices/


