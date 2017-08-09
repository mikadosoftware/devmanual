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