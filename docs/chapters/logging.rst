===================================
Best practise for logging in Python
===================================

===================================


.. testsetup::

   import logging



Replace print stmts with logging.debug
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If all you ever do with logging is ::


    import logging
    ...
    logging.warn("help")

You are 100% better off than ::

    print "help"

By using logging stmts throughout your code, with no more real thought than
sprinkling with print stmts, we do the hard part (sprinkling print stmts in
difficult places) whilst leaving the easy but valuable part (collating and
reviewing logs) for later.


For example, later on we can create in the `run` start up of any module, something like::

   logging.BasicConfig(filename="/var/log/myapp.log",
                       level=logging.DEBUG)

This will log all this app's calls at or above DEBUG to /var/log.  Which is
where it is supposed to.  And something extra like logging to syslog, then using
rsyslog to pull to a central logging server, is just a `salt` call away.


Do not use string formatting in the calling module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


   >>> logging.error("Help %s has gone wrong." % myvar)

If myvar does not exist here, then we shall raise an error


Do not use Python3 style formatting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Obviously Python 3 stuff is in flux, but the logging module
expects %s style formating, and is unlikely to change for
sometime as it will break backwards compatibility.

So stick to {'reason': MyVar} for the moment.


ReRaise errors by default
~~~~~~~~~~~~~~~~~~~~~~~~~

How we handle errors will vary a lot, depending on the app and the error.
But, if we are logging something, its often because an exception has been
thrown.  In most cases in my personal view, we want to log the existence of
the problem, and then rethrow


   >>> import logging
   ... try:
   ...     open("Notmuchchanceofthisexisting.txt")
   ... except IOError, e:
   ...     logging.error("Could not open file")
   ...     raise


http://victorlin.me/posts/2012/08/26/good-logging-practice-in-python
Logging
-------

http://docs.python.org/2/howto/logging-cookbook.html#logging-cookbook
http://css.dzone.com/articles/best-practices-python-logging
http://victorlin.me/2012/08/good-logging-practice-in-python/
http://www.robg3d.com/?p=906

Basics:

At app start up:
   import logging
   name a logger

in every other module
   import logging
   set a module level global with that same logging name
================================
Centralised Logging and metrics
================================

We need to talk about scale.

Mostly we should ignore scale. Simple will always be easier to scale than anything you planned for scale.

Keeping it simple *is* planning for scale.

There are three layers of scale - that roughly co-incide with two orders of magnitude of servers / cores we have to deal with (a not perfect but ok proxy for complexity of the eco system)

=================   ===================
Scaling phase       Number of servers
=================   ===================
Small                1 - 100
Medium               100 - 10,000
Enterprise           10,000 - 1,000,000
=================   ===================


Yes from 1 to a million. No one has to worry about a million servers. Ok Amazon has to - at about 2 million servers in AWS estimated by Bloomberg back in 2014.

But real companies - yes. If we think not of servers so much as virtual machines running on say one core each, much of the Fortune 500 easily manage 1 m each

And as for 10,000. The entry level enterprise here.? How many machines run the millionth Alexa ? 

Now remember I am assuming we are going to be 
running our small company on cloud based micro-services.  A micro-service is fine at just one rebuikdabke, backed up machine, but this is building services that do not wake us up at night or if they do we can wait a while before fixing them.  So we build in (simple) redundancy, and to do so we start adding servers like the clappers. Have a load balancer, two web servers and two master master databases allowing almost anything to fail over (and we can build one with scripts really quick) and we have 5 machines.  100 is not a long way off.  But we only get there is we are serving lots of customers which is a very good metric (but not the best!) 

But sometimes we need to scale much earlier than we thought. In logging that's when you get a second server. Any number more than one is a log management nightmare.

Want to see if the user who hit the web server also got that SQL stmt executed on the DNase server? Well that's two machines to log into and tail /car/log/messages. Add a simple web load balancer to keep uptime running and ... oh dear

There is a wealth of new log services out there, from LinkedIn, Facebook, Elastic search and Elsewhere. And they are very good.  But we want simple

