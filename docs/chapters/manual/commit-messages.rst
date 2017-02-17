
===================
Git Commit messages
===================

.. epigraph::

   Any software project is a collaborative project. It has at least two
   developers, the original developer and the original developer a few weeks or
   months later

   -- Peter Hutterer <http://www.blogger.com/profile/17204066043271384535>

.. epigraph::

    The difference between a tolerable programmer and a great programmer is
    [...] whether they can communicate their ideas. By persuading other people,
    they get leverage. By writing clear comments and technical specs, they let
    other programmers understand their code, which means other programmers can
    use and work with their code instead of rewriting it. Absent this, their
    code is worthless.

    -- Joel Spolsky <http://www.joelonsoftware.com/articles/CollegeAdvice.html>


What does a good commit message look like?
------------------------------------------


::

    Scope: Subject line in imperative tense and less than 50 chars

    Body text with why we needed to do this,
    how this works at a high level
    and any side-effects we know of or predict.
    Do not exceed 72 chars on these lines, because 4 chars indent, will
    catch you a lot.

    [tags for closing bugs etc.]




The rules for git commit messages
---------------------------------

1. Put a subject line as the first line, followed by a blank line then the body.

   Git grew out of the `Linux Kernel Mailing List <http://lkml.org>`_

2.


The two rules not to break:

Never have two lines of text at the top.  Always have one line then
blank line and body, or one line only.

Never exceed 72 chars per line.


The one rule to rarely break:

Always have 50 chars in the subject line



For your own sanity, make your project history clear, your documentation good.

Business justification: good code practises save time and money.


Commits and User Stories
------------------------

My view is that in an Agile environment, User Stories should be about the
same size as a commit.  That is if there is a User Story::

  2014.32.16 (16th sprint backlog item in 32nd sprint in 2014)

  As the Sales Manager, in order to motivate my team,
  the weekly sales report must be ordered by total revenue
  in USD.

Then I should expect to see a commit history like::

  $ git log --pretty=format:"%s"
  reporting: Order RW23 (weekly sales) by total rev USD
  reporting: Add function to convert sales.revenue to USD
  externalapis: Store daily GBP -> USD conversion rates
  reporting: Clean up code to PEP8 standards

Here I can see that I had to clean up the code in area of reporting,
then store a GBP to USD conversion rate, add in a function to do the
actual conversion and then change report RW23 to be ordered differently.

I would further expect these commit messages to reference `2014.32.16`
such as ::

   fixes: 2014.32.16
   rel: 2014.32.16
   rel: 2014.32.16
   rel: 2014.32.16


Preferred workflow
------------------

* Integration Manager (or pull-requests)




Breaking Changes into different commits
---------------------------------------

The ideal is to use `git add -p`.  This should be done once or twice
by everyone.  Then stop being a masochist and use `git gui` which allows
you to choose line by line which parts go into the next commit and which
wait.

Very very useful.  There are many other tools for doing this but git gui is fone.

(Just be aware to always pick the right `-` and `+` changes in one go.  Unless
you know what you are doing)



Git is not a backup
-------------------

I am guilty of this almost constantly.

I am weening myself off this habit by backing up all my development dirs
via tarsnap.

(Actually I may have to stop this to overcome EU data protection laws, and rsync
to a Dutch backup location)



Biblio
------
http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
https://docs.google.com/a/mikadosoftware.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit
http://www.mediawiki.org/wiki/Gerrit/Commit_message_guidelines
https://wiki.openstack.org/wiki/GitCommitMessages
https://www.kernel.org/doc/Documentation/SubmittingPatches


Other projects:

* time tracking based on git commits.
*
