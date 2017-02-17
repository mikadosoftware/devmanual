=============================
Cookies, Testing and security
=============================

=============================

I wish to use a cookie to store a random UUID that represents a server-side
session.  This will then be looked-up server side and the server can trust the
user info gathered (reasonably so)

This works as a useful cut-off point between the authentication system and
everything else.  We can test by sending in a fake session cookie.

Example
-------

If we create a simple wsgi app that just says hello, and returns its environ.

.. literalinclude:: simpleapp.py
   :lines: 93-109


Now we shall write a simple lookup (development only but it will do for now)


.. literalinclude:: simpleapp.py
   :lines: 45-90


Now lets test this.

.. literalinclude:: webtestthis.py

Here we see we are passing a header of the format desired into the test case.
And the output from the webtest shows that the environ held a cookie of the
right form:

::

  Response: 200 OK
  Content-Type: text/html
  You are user PaulHTTP_COOKIE::cnxsessionid=00000


We should use a 2x2 grid to determine responses etc
(TBC)


Basics
~~~~~~

We do not store sensitive information in a cookie.  Thats not what they are for,
it is totally out of our control and we can never know that the encryption loop
has not been broken [#]_

This leaves us with only one option for session cookies - a random number that
is the key to looking up the session details on the server somehow.  Even this
number will need to be in a suiffiociently large space that guessing is
impractical.  And we will need to ensure https traffic end to end to prevent
traffic-sniffing.

So, we shall use a tiered-lookup-cache.  I would expect it to go like this


1. User GET request to restricted page /secret
2. User receives 401 auth request, and by some means authenticates
3. Once authentication is completed, we fire server-side "after-auth"
4. after-auth generates a session

   * user_uri, session_starttime, sesssion_endtime, randomUUID
   * store that in local session cache
   * set response header for cookie with randomUUID

5. next request includes sessioncookie

   * lookup randomUUID in local session cache
   * set REMOTE_USER in environ,

6. scaling - I would only recommend moving to a network local redis style lookup and dropping the local cache - dual cache invalidation for such likely small speed up is foolish

7. logout

   * delete the session details from cache
   * unset the
   * add previosu randomUUID to the users *already ised list*
     (this is where the bloom filter may help)



Onwards work
~~~~~~~~~~~~

The use of sensible cookie handling for sessions is a good thing, however,
there are many many other aspects to a secure system, ranging from acls on the server,


Philosophy
~~~~~~~~~~

I want to digress just a little here.  I am not a security researcher and so I
have no special expertese in this area.  However I am trying to minimise the
errors made in a security system, maximise the likelihood that developers (as
opposed to security researchers) will find bugs, and make plain the trade offs
being made.

So, encryption is very very hard to get right even from basic building blocks
like OpenSSH (basically keyczar and nacl are wrappers around such functionality
to prepackage choices of how to put the building blocks together)

I would prefer to thus avoid relying on encryption for a simple reason - I can
easily get it wrong, rely on it being right and never spot my flaws.  In many
other areas I am likely to spot a flaw (oh, look a SQL stmt using string
formatting)

I am making a trade off here - that the cache lookups will not become impossible to manage




Bibliography
~~~~~~~~~~~~

Never build unnecessary crypto into your design
  https://news.ycombinator.com/item?id=4680444

OWASP top 10
  https://www.owasp.org/index.php/Top_10_2013-T10

AES Oracle attacks
  https://news.ycombinator.com/item?id=1687770


.. [#] Encryption loop is my own term. It is *very* unlikely that the OpenSSH implementation of AES is flawed or explotable.  It is really quite likely that the methods of using AES and setting headers and managing requests and decrypting using a salt stored in a ini file and all the other stuff *is* flawed, mostly because I wrote it.
