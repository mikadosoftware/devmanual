======================================================
Setting up python repos to use Sphinx and Github Pages
======================================================

We want to use `Sphinx <http://sphinx-doc.org>`_ to generate our documentation
but then use github to host the documentation (not withstanding the excellent
`readthedocs <http://www.readthedocs.org>`_.)

Github pages are a relatively simple idea - create a branch with a special name
(`gh-pages`) in your repo.  Whatever (html) is in the root of that branch will
be served from http://reponame.github.com as if it was the document root.

So our basic process will be to create an orphan branch in our repo called
"gh-pages", then generate the docs in the normal fashion, and copy over the docs
to the new branch and commit.

Obviously I would like to automate the complete process, of building the docs,
but that will wait till we have greater control and comfort with creating venvs
automatically and running docs within them (Its doable - just ...)


First stage
-----------

We want to create a new orphan branch called gh-pages (orphans carry no history baggage so its neater)

::
        # cd into repo on disk
        $ git checkout --orphan gh-pages
        Switched to a new branch 'gh-pages'
        $ git rm -rf .

        rhaptos2.user$ echo "Initial commit" > index.html
        rhaptos2.user$ git add index.html
        rhaptos2.user$ git commit -m "First cut for gh-pages"

Now that we have on github a gh-pages branch, we want to put something in it.
Create a file like the one below, in the root of say master.

::

        #
        SRCDOCS=/home/pbrian/src/rhaptos2.user/docs/_build/html

        cd $SRCDOCS
        MSG="Adding gh-pages docs for `git log -1 --pretty=short --abbrev-commit`"

        TMPREPO=/tmp/docs/user
        rm -rf $TMPREPO
        mkdir -p -m 0755 $TMPREPO

        git clone git@github.com:Connexions/rhaptos2.user.git $TMPREPO
        cd $TMPREPO
        git checkout gh-pages  ###gh-pages has previously one off been set to be nothing but html
        cp -r $SRCDOCS/ $TMPREPO
        git add -A
        git commit -m "$MSG" && git push origin gh-pages


I am assuming that we have already built the documentation in branch <master> as in::

        $ cd docs
        $ workon vuser
        $ (vuser) make clean && make html

This can all clearly be adjusted to suit each repo, and easily generic-isized.
But it does the job - of creating a temporary clone of gh-pages, and bringing the
pre-built html into the right location in gh-pages.


/usr/pbi/rxvt-unicode-amd64/lib/urxvt/perl/
thats were tabbed brwstring is in urxvt
