=================================
Compiling and modifying bootstrap
=================================

Building a simple web page these days is fraught with hidden traps for
the unwary.  A long time ago, I sat wearing a padded jacket in a cold
office, hand-typing out webpages for multi-national companies.  (That
got old quick so we pretty soon fixed the heating and the production
workflow).

But the point was, one person used to be able to write an entire web
site, suitable for the Fortune 500, in a text editor.

These days, not so much.  Obviously we still use text editors, but
they produce programs that produce programs that produce web sites.
And they are not one-person jobs.

However one person can still pull together all the right pieces, and
with Twitter Bootstrap, its even easier to get "good enough" design
and look, whilst still keeping everything manageable.

I intend to create the following page template, for an open source
project I am working on and promoting - it takes a DataWarehouse ETL
tool (Oracle ODI) and allows it to work bi-directionally with modern
source control tools (http://github.com/pmsoftware/odietamo)

.. figure todo


Installation
============

We shall

* git clone the Bootstrap repo,
* install the (mostly javascript) dependancies and tool chains
* run a simple compile
* celebrate.

::

  ## Some variables for later
  rootdir=/opt/bootstrap


.. code:: bash

   cd $rootdir
   git clone https://github.com/twbs/bootstrap.git

Right, now a bit of tricky javascript.  Install `node` and `npm` with
your distribution's preferred method.  For example that would be ports
on FreeBSD - you are using BSD no?  If not try ::


   $ apt-get install -y node npm

If you have node and npm installed then::

   $ cd $rootdir/bootstrap/bootstrap
   $ sudo npm install

This will download all the dependancies and

NB - FreeBSD is not well supported for PhantomJS - which only matters
for the self-tests.  I ignore this on my local machine and blip over
to a VM when I need.

If that did not make sense, do not worry.


How to compile
--------------

Its simple, in the bootstrap dir, where we can see the `Gruntfile.js`
run::

  $ grunt dist

This will start a javascript task runner (sort of make for js) that
simply builds a `/dist/` directory containing the compiled js, css and
font files.  This `/dist/` dir is what gets served to the browser in
production.  The rest of the files are supporting acts.


OK, we should have seen something like this::

    Running "copy:fonts" (copy) task
    Copied 4 files

    Running "concat:bootstrap" (concat) task
    File "dist/js/bootstrap.js" created.

    Running "uglify:bootstrap" (uglify) task
    File "dist/js/bootstrap.min.js" created.

    Done, without errors.

Serving
=======

As this is all very local, we want to see the web browser deal with it ::

  $ cd $rootdir
  $ python -m SimpleHTTPServer
  Serving HTTP on 0.0.0.0 port 8000 ...

Now a webbrowser can ask for `http://localhost:8000/example-page.html`
and it should see

.. figure::  https://raw.github.com/mikadosoftware/screengrab/master/screenshots/customfree-examplepage.png
    :width: 50 %

Moving things around
--------------------

You can skip this bit and come back later - it will make more sense
then.

We don't want to directly change the files provided for us by the
bootstrap team.  We do however need to change *something*




Our first Bootstrap File
========================

We are now using Bootstrap 3.  This is a new, updated version, that is
*mobile first*.  Which means its designed to be really sensible on
most devices.  Hooray - that means we can deploy applications to a
mobile, without going through the various appstores.  Well sort of.

HTML5
-----

We need a solid HTML5 template file.  The best one to use is HTML5 boilerplate.

Make sure this is in the template file ``<head>``::

  <meta name="viewport" content="width=device-width, initial-scale=1.0">

Responsive friendly images.  We need to add ``.img-responsive`` class
to each ``img`` tag so that they are treated correctly by Bootstrap.
I need to use a post-process step in the CMS to shoe-horn these in -
whatever gets you through the night.



Containers
----------

Everything in BootStrap is in a container.  A container is defined as
follows. ::

  <div class="container">
  ...
  </div>

The hero units (now seemingly renamed Jumbotrons), the forms, the tables, they

Shims and things
----------------

Shims and polyfills are bits of javascript code that provide HTML5
functionality on older, but still widely deployed, web browsers that
do not support HTML5 natively.  The IE range upto IE 7 is a notable
case, still widely deployed in corporate environments.

An example is the HTML5 element ``canvas`` which allows javascript to
draw on a canvas.  Where there is no HTML5 ``canvas`` element built
into the browser, the polyfill will call up perhaps a Silverlight
plugin and perform the draw action on that.

These shims and polyfills are amazing pieces of work, but (as in
polyfilla) they simply cover over cracks. And they are not perfect.
So I am ignoring them for now in my template code.  In production this
may change but for our purposes they add complexity to understanding.

https://github.com/Modernizr/Modernizr/wiki/HTML5-Cross-browser-Polyfills
http://remysharp.com/2010/10/08/what-is-a-polyfill/




A quick customisation
=====================

Lets start with `variables.less`.  The CSS we use for Bootstrap is not
hand-written - it is compiled into CSS after the original `less` code
is parsed.  The original `less` code is designed to make writing lots
of CSS easier, so it supports things like variables and functions
(called `mixins` but think returning function for ease).

So a quick snippet of `variables.less`::

    @gray-darker:            lighten(#000, 13.5%); // #222
    @gray-dark:              lighten(#000, 20%);   // #333
    @gray:                   lighten(#000, 33.5%); // #555
    @gray-light:             lighten(#000, 60%);   // #999
    @gray-lighter:           lighten(#000, 93.5%); // #eee

    // Scaffolding
    // -------------------------

    @body-bg:               #fff;
    @text-color:            @gray-dark;
   `

Now, lets have some fun.  Firstly our `test.html` page.  This is quite
a bit of code, but it is about the simplest HTML5 + bootstrap page you
can make, and it liberally ripped off from the bootstrap site.

.. code:: html

    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <title>Navbar Template for Bootstrap</title>
        <!-- Bootstrap core CSS -->
        <link href="bootstrap/dist/css/bootstrap.css" rel="stylesheet">
        <!-- Custom styles for this template -->
        <link href="navbar.css" rel="stylesheet">
      </head>

      <body>

        <div class="container">

          <!-- Main component for a primary marketing message or call to action -->
          <div class="jumbotron" id="showcasing" style="background: url('LHC.jpg') repeat-x top center;">>
            <h1>It works !</h1>
            <p>Hooray</p>
            <p>
              <a class="btn btn-primary" href="#">Press me</a>
            </p>
          </div>

        </div> <!-- /container -->

        <!-- Bootstrap core JavaScript
        ================================================== -->
        <!-- Placed at the end of the document so the pages load faster -->
        <script src="bootstrap/assets/js/jquery.js"></script>
        <script src="bootstrap/dist/js/bootstrap.min.js"></script>
      </body>
    </html>






Now the above html, is about the simplest one can get for bootstrap.
And it looks like this:


.. figure:: https://raw.github.com/mikadosoftware/screengrab/master/screenshots/bare-initial-css.png
     :width: 50 %
     :alt: Screenshot showing standard bootstrap themeing.


Firstly let's adjust the simplest things we can - the LESS variables.


.. code:: css


    // added pbrian
    @brand-back: #8a928e;
    @brand-fore:  #8e393f;

    @gray-darker:            lighten(#000, 13.5%); // #222
    @gray-dark:              lighten(#000, 20%);   // #333
    @gray:                   lighten(#000, 33.5%); // #555


    @brand-primary:         @brand-fore;

                            ^^^^^^
                            This will roll out across the site.


And the result is :


.. figure::  https://raw.github.com/mikadosoftware/screengrab/master/screenshots/redgreyexample.png
   :width: 50 %
   :alt: Screenshot showing subtly changed colors using new compiled LESS


Ok, nothing spectacular, but one line change gives us a new colour set
across the board.  What else can we do?


Fonts
=====

TBD

Images
======

TBD


biblio
======

https://raw.github.com/mikadosoftware/screengrab/master/screenshots/colorschemedesigner.png
http://bootstrap.lesscss.ru/less.html
http://copyhackers.com/2012/12/the-3-step-hack-for-startups-bootstrapping-their-design/
http://24ways.org/2012/how-to-make-your-site-look-half-decent/
http://www.sitediscount.ru/verso/index.html


Choose a color scheme: http://colorschemedesigner.com/

::

    #####  Color Palette by Color Scheme Designer
    #####  Palette URL: http://colorschemedesigner.com/#0Q51Rw0w0w0w0
    #####  Color Space: RGB;



    *** Primary Color:

       var. 1 = #FF9F00 = rgb(255,159,0)
       var. 2 = #BF8930 = rgb(191,137,48)
       var. 3 = #A66800 = rgb(166,104,0)
       var. 4 = #FFB740 = rgb(255,183,64)
       var. 5 = #FFCA73 = rgb(255,202,115)

    *** Secondary Color A:

       var. 1 = #FFC700 = rgb(255,199,0)
       var. 2 = #BFA030 = rgb(191,160,48)
       var. 3 = #A68100 = rgb(166,129,0)
       var. 4 = #FFD540 = rgb(255,213,64)
       var. 5 = #FFE073 = rgb(255,224,115)

    *** Secondary Color B:

       var. 1 = #FF6700 = rgb(255,103,0)
       var. 2 = #BF6A30 = rgb(191,106,48)
       var. 3 = #A64300 = rgb(166,67,0)
       var. 4 = #FF8D40 = rgb(255,141,64)
       var. 5 = #FFAB73 = rgb(255,171,115)


    #####  Generated by Color Scheme Designer (c) Petr Stanicek 2002-2010


       @colorA1:  #FF9F00;
       @colorA2:  #BF8930;
       @colorA3:  #A66800;
       @colorA4:  #FFB740;
       @colorA5:  #FFCA73;

       @colorB1:  #FFC700;
       @colorB2:  #BFA030;
       @colorB3:  #A68100;
       @colorB4:  #FFD540;
       @colorB5:  #FFE073;

       @colorC1:  #FF6700;
       @colorC2:  #BF6A30;
       @colorC3:  #A64300;
       @colorC4:  #FF8D40;
       @colorC5:  #FFAB73;


We can also adjust the fonts site wide.

New fonts:
http://www.google.com/fonts/

<link href='http://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>

font-family: 'Roboto', sans-serif;
<link href='http://fonts.googleapis.com/css?family=Press+Start+2P' rel='stylesheet' type='text/css'> (ad nauseum example)



We can see the results (quite horrible) here:

.. figure:: https://raw.github.com/mikadosoftware/screengrab/master/screenshots/horriblecolorandfont.png
    :width: 50 %
    :alt: horrible color scheme






http://coding.smashingmagazine.com/2013/03/12/customizing-bootstrap/


Building my masterpiece
=======================

OK, so I want to transform this

.. figure:: https://raw.github.com/mikadosoftware/screengrab/master/screenshots/original-odi.png
    :width: 50 %

Into this::

   Tada


So lets start with Design basics - cribbed liberally from the folks on
InterWebs


* Step 1 - Make it look good in Black and White first
* Step 2 - Write the right things
* Step 3 - Do less.  No less than that.



Color theory
------------

Well, just colour wheels really.

.. figure:: https://raw.github.com/mikadosoftware/screengrab/master/screenshots/colorpicker-simple.png
    :width: 50 %




Building my own bootstrap classes
=================================

Its pretty obvious what <div class="span6"> means.  But that does not mean its
a good idea.  Yopu want a sidebar, not a span6.

So we define our own classes, and use those in the HTML instead.




This is accounted for in Bootstrap by
http://getbootstrap.com/css/#grid-less

http://ruby.bvision.com/blog/please-stop-embedding-bootstrap-classes-in-your-html


Building our own mobile aware classes
=====================================

Oh fuck it, really.  This is the shit designers are supposed to
obessess over.  Here I stop.  If I cannot make do with a main column
and a sidebar I am going to have to go back to pen and paper.


.. raw::  html

   <a href="http://www.colourlovers.com/palette/3010906/RedBlue" target="_blank"><img src="http://www.colourlovers.com/images/badges/p/3010/3010906_RedBlue.png" style="width: 240px; height: 120px; border: 0 none;" alt="RedBlue" /></a><br /><span style="font-size: 10px; color: #5e5e5e;"><a href="http://www.colourlovers.com/color" target="_blank" style="font-size: 10px; color: #5e5e5e;">Color</a> by <a href="http://www.colourlovers.com/" target="_blank" style="font-size: 10px; color: #5e5e5e;">COLOURlovers</a></span>
