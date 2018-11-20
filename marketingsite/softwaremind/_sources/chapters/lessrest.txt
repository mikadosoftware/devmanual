==================================================
Using Less and ReSt to make nice looking documents
==================================================

--------------------------------------------------

Not so long ago the only *right* way to transform markdown style
documents into something decent was via LaTeX and thence into pdf.

These days HTML and CSS are the way to go it seems.  Its just good enough and
the toolchain is far far more likely to be available on your machine right now.

First steps
-----------

Lets see what a simple ReSt document looks like.  We have
`the demo ReSt <rstdemo.txt>`_ for the docutils project.  ::

   .. This is a comment. Note how any initial comments are moved by
      transforms to after the document title, subtitle, and docinfo.

   ================================
    reStructuredText Demonstration
   ================================

   .. Above is the document title, and below is the subtitle.
      They are transformed from section titles after parsing.


   Literal Blocks
   --------------

   Literal blocks are indicated with a double-colon ("::") at the end of
   the preceding paragraph (over there ``-->``).  They can be indented::

       if literal_block:
           text = 'is left as-is'
           spaces_and_linebreaks = 'are preserved'
           markup_processing = None

Now this looks like the page `here <http://docutils.sourceforge.net/docs/user/rst/demo.html>`_ - a bit plain and boring.

But we want to sprinkle magic Bootstrap dust over it.  Now boring people might suggest the correct way to do this is to alter the HTML-formatter in docutils and so get that to output HTML divs that bootstrap expects.  This is actually the right way to do it but I wont for several reasons.

1. This is an article about configuring bootstrap, not docutils
2. docutils is a really dense impenetrable forest of code and I do not understand it nearly well enough to make a quick change.
3. I am pretty sure I can do this with a few lines of less.  If so, result !
