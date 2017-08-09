======
aspell
======

This is an enormously painful setup and generally a painful program.  But its
a limited choice world it seems.

Install aspell is pretty simple.  `/usr/ports/textproc/aspell`

We then want to get dictionaries - which are word lists in specific formats.
The only place to get these and remain sane is http://ftp.gnu.org/gnu/aspell/dict/en

After untarring, we run::


 $ ./configure
 Finding Dictionary file location ... /usr/local/share/aspell
 Finding Data file location ... /usr/local/lib/aspell-0.60
 $ sudo make
 $ sudo make install

Now if we look in /usr/local/share/aspell we have a huge list of english words in aspell formats.

Using it with emacs::

  M-$
  or
  M-x flyspell-mode
