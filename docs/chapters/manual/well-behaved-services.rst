==========================================================
Keeping micro-web services alive, supervised and restarted
==========================================================


Waiting around to restart your web server is painful - Steve Huffman, one of the
founders of Reddit talks about literally sleeping with his laptop next to his
bed and constantly waking to restart a process at ungodly hours of the morning.



`Micro-services
<http://yobriefca.se/blog/2013/04/29/micro-service-architecture/>`_ are in my
view a great way to arrange our business applications.  By splitting the work
done into smaller components, and having the work done by seperate webservers
running just a small piece of code, we find several benefits

* our code is better structured, because we cannot rely on the big framework to
  pass bits around for us

* Testing the service is easier

* Things cen be upgrade, downgrade or side-ways-graded with more confidence.  A
  fix to one tiny piece of independantly running code will hardly ever affect
  the others.  In a monolithic application that is rarely true.  Change the font
  size for Page X, ooops that just killed half the CSS on site.

* naturally robust / redundant.



And so...

Now imagine if he had built a micro-service architecture, 50 or more seperate
web servers, and was manully trying to watch them all, Reddit could have failed
and we would have lost millions of LoLCatz. The horror!


Eventually he discovered `supervisord` and got some sleep.  This is a Good
Thing.

We also want something that will monitor them and respawn them when they die.

This will we hope increase our chances of a service that is small, stays up and
if it fails, is automatically brought back up.

We also want to keep things simple.

The simplest way possible to keep a service running
===================================================

It would be lovely to write a web service, set it running and
know that if it fell over, divided by zero, or otherwise went wrong
it would immediately be picked up, dusted down and restarted.

If we can do that so it scales upwards really well when it is working.

Oh and it needs to make the tea too.

Ok, the first part is `process monitoring` - watching a running process,
and if it falls over (or rather exits with non zero) restarting it.

There are a lot of options out there - `supervisord`, `god` are a couple that
spring to mind.  But these are inherently part of a language ecosystem (Pyhton
and Ruby respecitively).  This is not a *bad* thing, they do the job, but
distributions and sysadmins have for a long time faced these problems and come
up with effective solutions already.  I think this is part of the packaging
problem all language eco-systems seem to face - and often well solved by looking
at the distribution tools first and then worrying.

The SysV / init camp of tools is old, and still very effective.  Over the years
new olutions have been proposed, three I shall cover: `rc.d`, `upstart` and
`systemd`.  Upstart was championed by Ubuntu/Canonical and is an attempt to keep
the simple, file driven approach going.  systemd is however winning hearts and
minds, and has even driven upstart out of the debian world, and so ubuntu will
soon follow suit.  I shall however target 12.04 for the moment and that will
remain upstart based.

rc.d comes from NetBSD, and so is a worthwhile investment in the FreeBSD world.


Python and WSGI
---------------

Web micro-services will consist mostly of well, web servers.  And in the Python
world that means WSGI.

Now, a WSGI app is a curious beast, essentially it cares nothing for web servers
and threads and so on, it simply takes an `environment` (like CGI env) and a
`start_response` callable.

A WSGI enabled server will wrap the core application (returns "hello world")
in a chain of python functions, each one taking an env and a callable, each one
modifying the response as we go up the chain.

I will have to write a small WSGI server to demonstrate.


Anyway, lets run a WSGI app on FreeBSD


FreeBSD
=======


Overview
--------

I want to have *the simplest possible way to run a micro web service*.  For me
this is to make use of the well thought out, well tested and well, simple,
`init` services built into all Unix distributions.

I shall create two dummy web services, `hello.py` that is simply a Flask
service returning "hello World", and this shall be started and stopped
with an `rc.d` script.

A second more complex script shall follow, dealing with some config issues etc.

.. literalinclude:: hello.py

This is about as simple as it gets (ripped, liberally, from the frontpage of
flask.org.).  However run in the terminal it will respond correctly to the
various signals thrown at it.

::


    $ python hello.py
     * Running on http://127.0.0.1:5003/
    ^C

    We set the web server running, then can kill it with ctl-C

However we want to *prove* that if the app dies by itself, `rc` will restart it.


.. literalinclude:: hello-with-kill.py

::

   if we run this and then visit localhost:5003/kill,
   the process will exit.

   (errr... really?)


Lets make this "production-ready" [#]_


.. literalinclude:: hellokill.py


THe app factory issue...


Using the BSD rc.d init approach
--------------------------------

The short approach is we put a simple .sh script in `/usr/local/etc/rc.d`. This
is called during system init, and it will run a command - that command will be
a WSGI server (like uwsgi / gunicorn / waitress) which will bring up a wsgi app.

This app will serve HTTP happily, but if it falls over, rc.d will restart it.



notes
(test-rc)supervisor-scripts(master)$ which gunicorn
/usr/home/pbrian/venvs/test-rc/bin/gunicorn



Now deploying a simple WSGI app with Gunicorn but what about a djaongo app



Django deployed standalone WSGI with gunicorn
---------------------------------------------

::

  $ gunicorn --pythonpath readthedocs readthedocs.wsgi:application
  $ /home/pbrian/venvs/docserver/bin/gunicorn  --pythonpath
  /usr/home/pbrian/venvs/docserver/checkouts/readthedocs.org
  readthedocs.wsgi:application


Have to create a wsgi.py in the readthedocs "app dir"
::

    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.sqlite")

    # This application object is used by the development server
    # as well as any WSGI server configured to use this file.
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()


/home/pbrian/venvs/docserver/bin/gunicorn          --pythonpath
/usr/home/pbrian/venvs/docserver/checkouts/readthedocs.org/readthedocs
wsgi:application

::

    rc.d$ cat readthedocs
    #!/bin/sh
    ###
    # PROVIDE: readthedocs
    # REQUIRE: LOGIN
    # KEYWORD: shutdown

    # We always require LOGIN unless we know what we are doing.
    # shutdown is there to kill us off in case of system shutdown.

    . /etc/rc.subr

    name="readthedocs"
    rcvar=readthedocs_enable
    #pidfile=/tmp/${name}.pid

    ###########
    venv_gunicorn=/home/pbrian/venvs/docserver/bin/gunicorn
    django_app_path=/usr/home/pbrian/venvs/docserver/checkouts/readthedocs.org/readthedocs
    django_app_wsgi=wsgi:application

    command="$venv_gunicorn -D \
             --pythonpath $django_app_path \
             $django_app_wsgi"

    #########

    load_rc_config $name
    run_rc_command "$1"


.. todo:: Also need to deal with command_interpreter.



Bibilio
=======

* #pkgng@freenode

* https://www.freebsd.org/doc/en/articles/rc-scripting/article.html



Linux and Debian
----------------

Well, I used to use `upstart`.  That has been replaced with `systemd` now,
and well, we need to `lose graciously <link to ubuntu post on this>`.

Using systemd
-------------

systemd is controversial but it is becoming widespread. It *may* be over complicted.
For our purposes it is sufficient

We place *our* unit file in `/etc/systemd/system`

::

  [Unit]
  Description=PaulsTest

  [Service]
  ExecStart=/home/pbrian/venvs/prodwww/bin/python /home/pbrian/projects/mikadoCMS/mikadocms/cmsapp.py --config=/home/pbrian/projects/mikadoCMS/mikadocms/data/mikadosoftware.com/mikado_dev.ini

  [Install]
  WantedBy=multi-user.target




Further reading
===============

(get sphinx to link these up for me ...)

* Security for micro-web-services
* running your own CA

.. [#] OK so its not actually production ready - monitoring, logging etc. But its a lot more production than the Flask default server.
