:manual
Best practise for logging in Python
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
