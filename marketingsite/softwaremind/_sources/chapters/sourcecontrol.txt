=================
Source Control
=================

History
=======

BAML vs Sourcesafe vs SVN vs CVS


Basic practises

* add / commit
* Aliases

Different Flows for diffent folks
---------------------------------
  
* githubflow vs gitflow vs gits own approach
* git rebase and at-risk branches
  
Good Commit Messages
--------------------



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
==============
source control
==============




Biblio
------

Craft each commit message as a problem: xx solution: xx
https://github.com/PumpkinDB/PumpkinDB/commits/masterNo one's perfect with this stuff.
If you don't believe me, clone git itself ($ git clone https://github.com/git/git) and open up the repo in tig(1)
https://github.com/jonas/tig
To be honest, I only in the past 2 years even bothered to view ($ git log --graph). Regardless of --graph getting wide now and then, I always visualize my git history as a straight line.
Also, sometimes having a non-linear history is inevitable. Especially in large open source projects where you're pulling in patches to a branch, and patches on top of that. You're not always going to be merging a branch with a single author straight onto master.
Despite posts like this (http://www.bitsnbites.eu/a-tidy-linear-git-history/) encouraging good git hygiene, I've had multiple open source projects merge in code via GitHub and never had negative consequence for it :P
Maybe there are corner cases where git bisect wouldn't work? Though I never used git bisect even once. Most I do is scroll through tig and view diffs. Also used to play with a cool git plugin in vim (https://github.com/tpope/vim-fugitive).
Also, GitHub has (since that linear git history post) introduced Rebase + Merge https://github.com/blog/2243-rebase-and-merge-pull-requests. I think that'll get you what you want.
I do keep branches ("pull requests" if you're using GH lingo) up to date with ($ git pull --rebase). That does mean a force push ($ git push --force), but it's ok if it's your personal branch. I also use interactive mode ($ git rebase -i <sha>) to edit/blend multiple commits.
Also, when I do merge, if I go through CLI, I'll preserve the history of the branch by not doing fast forwards ($ git merge <branch> --no-ff).