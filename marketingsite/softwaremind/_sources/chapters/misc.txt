========================================
misc stuff I will find another place for
========================================

Using sudo and not root
-----------------------

I am a very bad boy and have a tendancy to just use root to get things done
quick.  This very nicely phrased page on why you should `never login as root
<https://help.ubuntu.com/community/RootSudo>`_ tells me off.

in short

1. sudoers is there for audit purposes and audit is half of security.
2. use sudo sh -c "echo foo >> /etc/bar"

this gets around the problem that sudo echo foo >> /etc/bar is two commands

passwords
---------
/etc/passwd is a bit long in the tooth.
/etc/master.passwd is where the action is now kept.
if you look at that and need to, for example, change the login shell
you need to run pwd_mkdb /etc/master.passwd afterwords


Setting Bash prompt
-------------------

You need to set the environment variable PS1.
The simplest approach is the best here I feel.::

  PS1="\[\033[0;36m\][\$(date +%H:%M)][\u@\h:\w]$\[\033[0m\] ";export PS1

We set the PS1 variable.  If we had used ::

  PS1="$ "

Then our prompts would be a boring but functional ::

  $ ls -l

But instead we are being hopefully a little cleaner.  OK ::

  \[\033[0;36m\]
  ^^^^^^^     ^^
  always needed to *wrap* any thing we want to pass to terminal, but not print.  In this case, the command 0;36m which sets the terminal colour to be magenta (not bold).   Later on we set the terminal colour to be 0m, or back to defaults.





.. PROMPT_COMMAND=?if [ ${#PWD} -gt 30 ]; then myPWD=${PWD:0:12}?${PWD:${#PWD}-15}; else myPWD=$PWD; fi?

:biblio: http://www.linuxdoc.org/HOWTO/Bash-Prompt-HOWTO/x329.html




Colours under Bash
------------------

Oh yes, please.  Just type ls -G (or like above, alias it.)  This is
great, right up to the point that the cool green on black screen you
have tries to show you all your directories in a dark blue.  I know I
am getting old but taht is unreadable.

So ...

in ~/.bash_profile::


  CLICOLOR=1; export CLICOLOR
  LSCOLORS='gxfxcxdxbxegedabagacad'; export LSCOLORS

CLICOLOR is the equivalent of ls -G but always set.
LSCOLORS is a
string of 11 pairs, so gx is foreground-magenta, background-default,
and the first pair is how to display a directory in ls (hence
LSCOLORS).  See the man page for details, but suffice to say gx gives
me readble directory names now.

Note that in Linux, the environment variable is LS_COLORS, and its 'ls --colors'.  However this is BSD world (mac included!).

Escape sequences etc etc

Here is a PS1 setting::

 export PS1="\[\033[0;36m\][\u@\h:\W]$\[\033[0m\] "

ESC is ANSI 27
\033 is the octal representation of ESC
\0x1B is HEX
\e is whatever

We want this *not* to be interpreted by shell so ::

  echo "\033[H\033[2J"

will not work.  But::

  printf "\033[H\033[2J"

will (its clear screen btw).::

  tput cl

  tput cl | less

tput is the command to execute escape sequences. DOnt worry.


So we can look up escape sequences in tables (wikiepdia) and build our own

::

  "\[\033[0;36m\][\u@\h:\W]$\[\033[0m\] "

  leftsquarebracket, Escape code (^[), blue colour, username@host:pwd$ reset to defaults/

  gives:

  [pbrian@hadrian:pbrian]$





:biblio: http://www.bigsoft.co.uk/blog/index.php/2008/04/11/configuring-ls_colors  http://unix.stackexchange.com/questions/2897/clicolor-and-ls-colors-in-bash

Temperature
-----------
$  sysctl hw.acpi.thermal.tz0.temperature
hw.acpi.thermal.tz0.temperature: 54.0C


scp
---

Very useful in all respects but wildcards are a bugger ::

  $ scp *.txt myremotesvr:/tmp/misc

will copy all txt file in local dir to remote server.  Thats because the shell
*expands* the commands you give it *before* it passes the commands to the
program (scp).  Normally thats good (in other words the shell took *.txt and
actually sent the scp program ::

    $ scp a.txt b.txt c.txt myremotesvr:/tmp/misc



however::

  $ scp myremotesvr:/tmp/misc/*.txt ./

fails.  It is trying to send ::

   $ scp myremotesvr:/tmp/misc/a.txt  b.txt c.txt ./

and it is invalid.


So to solve the problem, escape the wildcard, the shell will not expand it but
will 'unescape' and pass it to the program as we want::

  $ scp myremotesvr:/tmp/misc/\*.txt ./


`More reading <http://books.google.co.uk/books?id=3XzIFG3w8-YC&pg=PA316&lpg=PA316&dq=scp+wildcard+match&source=bl&ots=oEjO3_aptE&sig=-YFh37YI4hLdFX8hWasA9N0NEOs&hl=en&ei=E5bnSe74CpG1-Qb02LjoBQ&sa=X&oi=book_result&ct=result&resnum=3http://books.google.co.uk/books?id=3XzIFG3w8-YC&pg=PA316&lpg=PA316&dq=scp+wildcard+match&source=bl&ots=oEjO3_aptE&sig=-YFh37YI4hLdFX8hWasA9N0NEOs&hl=en&ei=E5bnSe74CpG1-Qb02LjoBQ&sa=X&oi=book_result&ct=result&resnum=3>`_


mirroring with wget
-------------------
::

  wget -m -k -K -E http://url/of/web/site



emacs and sudo
--------------

Annoyingly, if I run ::

  sudo emacs /etc/rc.conf

sudo runs emacs, but the permissions granted by sudo do not carry over to my
emacs session, making it not possible to edit the locked down file.

## tramp opens a subshell and then usually allows editing over ssh. it is useful
##  for sudo too.  C-c C-f /sudo::/my/path/file (require 'tramp)

emacs and annoying cut paste issues
-----------------------------------

http://www.jwz.org/doc/x-cut-and-paste.html



sort and sed and uniq
---------------------

An interesting one from Dru Lavigne's little nuggets of wisdom

::


 pbrian@delli7 Desktop$ pkg_info | sort | sed -e 's/-[0-9].*$//' | uniq -c | egrep -v '\ *1'
   2 autoconf
   3 automake
   2 font-adobe
   2 font-adobe-utopia
   2 font-bh
   2 font-bh-lucidatypewriter
   2 font-bitstream
   2 glib
   2 gtk
   3 xorg-fonts
 pbrian@delli7 Desktop$ pkg_info | sort | sed -e 's/-[0-9].*$//' | uniq -c | grep -v '^[[:space:]]*1'
   2 autoconf
   3 automake
   2 font-adobe
   2 font-adobe-utopia
   2 font-bh
   2 font-bh-lucidatypewriter
   2 font-bitstream
   2 glib
   2 gtk
   3 xorg-fonts

Quick discussion - we get pkg_info sending us things like ::

  zip-3.0             Create/update ZIP files compatible with pkzip

* We use sed to remove everything from the first -Numeral
* sed -e "s for substitute / this / for that /"
* Then uniq -c gives each word and a count of the occurances
* then grep -v to weed out anything that only occurs once.

Nice example showing a lot of the standard goodies on the command line.

Also interesting is the grep [[:space:]] - but I find '\ ' more readable


Restart networking in FreeBSD
-----------------------------
::

 $ /etc/rc.d/netif restart && /etc/rc.d/routing restart

:biblio: href="http://www.cyberciti.biz/tips/freebsd-how-to-start-restart-stop-network-service.html"



* More emacs

::

    find /usr/local/share/emacs/ -iname '*.el'

  Where the 'builtin' files are kept - but cannot see rst.el Thats because rst
  is now 'builtin' to the emacs, so its supplied compiled, and need search for
  .elc


* Rest mode in emacs

  It has a really horrible highlight the text of each header.  With a dark
  background its distracting and unreadable.  SO we get rid of it.

  in .emacs file ::

     '(rst-level-face-base-light 0)




Red output on StdErr on terminal
================================

http://superuser.com/questions/28869/immediately-tell-which-output-was-sent-to-stderr
put this in .basdh_profile::

 # Red STDERR
 # rse <command string>
 function rse()
 {
    # We need to wrap each phrase of the command in quotes to preserve arguments that contain whitespace
    # Execute the command, swap STDOUT and STDERR, colour STDOUT, swap back
    ((eval $(for phrase in "$@"; do echo -n "'$phrase' "; done)) 3>&1 1>&2 2>&3 | sed -e "s/^\(.*\)$/$(echo -en \\033)[31;1m\1$(echo -en \\033)[0m/") 3>&1 1>&2 2>&3
 }

then you can run ::

  rse mycommand.sh

  or

  command.sh | rse

and stderr will print in red.
