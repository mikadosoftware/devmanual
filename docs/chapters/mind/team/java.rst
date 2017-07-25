====
Java
====

.. sidebar:: Historical Note

   I need to update the URLs etc, but the same annoying
   install process still exists.


Most awkward
============

Back in the mists of time (or 2006) Sun released its Java spource code (the
compiler / VM etc) as open source.  This Oracle does not license its version of
the Java SDK / VM as open source, except for "personal" use.  This means they
can try and ensure they still get paid for enterprise Java under Installing Java
is not that simple.  I beleive that OpenJDK is pretty simple to install, but
that is not the supported Oracle version of the JVM, and as I want to use Java
for Oracle's ODI I guess I am going to do this the long winded way.

For various license-based reasons (and no I don't know and don't care right now)
several parts of the java source need to be downloaded manually.

::

 Due to licensing restrictions, certain files must be fetched manually.

 Please download the Update 3 Source from
 http://www.java.net/download/jdk6/6u3/promoted/b05/jdk-6u3-fcs-src-b05-jrl-24_sep_2007.jar
 and the Source Binaries from
 http://www.java.net/download/jdk6/6u3/promoted/b05/jdk-6u3-fcs-bin-b05-jrl-24_sep_2007.jar
 and the Mozilla Headers from
 http://www.java.net/download/jdk6/6u3/promoted/b05/jdk-6u3-fcs-mozilla_headers-b05-unix-24_sep_2007.jar
 .

 Please open http://www.oracle.com/technetwork/java/javase/downloads/index.html
 in a web browser and follow the "Download" link for
 "JDK DST Timezone Update Tool - 1_3_45" to obtain the
 time zone update file, tzupdater-1_3_45-2011n.zip.

 Please download the patchset, bsd-jdk16-patches-4.tar.bz2, from
 http://www.eyesbeyond.com/freebsddom/java/jdk16.html.

 Please place the downloaded file(s) in /usr/ports/distfiles
 and restart the build.

 (NB halfway through the compile you will be asked to download diablo-caffe
 manually too.)


So lets do that.  Download the above as needed.  Please note you get the above
instructions from running $make install clean.  Run this yourself on your source
as the page may be out of date.

You will be asked to agree to a (non-free, personal use only) license.

You may want to use OpenJDK instead.  I am not doing so as I am aiming at a
Oracle application build and am guessing it will have less problems.  I shall
compare and contrast the OpenJDK and the Oracle JDK in a few months time.
