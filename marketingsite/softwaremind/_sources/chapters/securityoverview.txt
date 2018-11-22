Have a demo website with all different methods of auth and how to share across many enterprise apps

ie - one portal for login, via OAuth2, and sets a redis session key
Use SQRL
Use FIDO2
Use client sertificates (see fido2)
Use TOTP

Thats bout ti.


GPG basics
https://lwn.net/SubscriberLink/734767/b8509e00378301f9/


https://developers.google.com/web/fundamentals/security/csp/
https://hackernoon.com/im-harvesting-credit-card-numbers-and-passwords-from-your-site-here-s-how-9a8cb347c5b5


Hardening and golden docker 
https://support.rackspace.com/how-to/linux-server-security-best-practices/



Managing identity and authentication
------------------------------------

So this is a huge one for me. If i have the below fairly simple
micro-services structure, how can I keep Authentication and
Autorisation correct, and simple?

::

  0           ----------          -----------          (-------)
  |      ---  | www    |   ----   | uService|  ------- (  DB   )
  ^           | gateway|          |         |          (       )
              ----------          -----------          (-------)
  User


Lets say this is a really simple service. User logs in and perform
get /mydetails They should be presented with their profile pulled form
the DB.  The uService MUST be sure that the person performing the
request,

We assume that the hosts in the chain remain uncompromised, but we
cannot assume that the network is anything other than hostile.  So no
"send the profile in plain text" and of course no "I got a request for
user xxx on my port so of course it came from the www server that I
trust."

The challenge.  I want a strong, robust and widely supported method of
client authentication.  This fundamentally means X509 client
certificates.  We are going to "Trust the Math".  But once the TLS
terminates at www, how do we go about re-trusting the whole shooting
match.  How do we get the uService to know who the user

How do we do TLS between servers.

How do we trust anything?


Authentication
Authorisation
ROle Management

Use a central service for Authorisation and Role Management - give it a token
and ask if toekn holder is allowed to do X

We can happily use a random token - no need for JWT etc. Just a single token
and a call to a central service.

THis is the simplest and best.  Discussions on JWT.
=======
Attack tools
https://www.schneier.com/blog/archives/2014/05/the_nsa_is_not_.html

art 
http://www.dirk-loss.de/sshvis/drunken_bishop.pdf


Securing AWS / CI flow
The big big big advantage is if it is repeatable automated steps you can add a tiny improvement once a day and  it is locked in free for ever

Not only but also

- Vendor supply chain. How to verify that the code you download as dependnacies is secure

- Physical security - including personal 

- reputational security - defending your repirtstuin 

- ransomware and recovery

- Losing your apple iphone... 

- infrastructure security - certificates etc. How did that guy find zero days in ?

- 

