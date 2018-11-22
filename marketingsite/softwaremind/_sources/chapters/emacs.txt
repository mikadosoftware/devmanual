=====
emacs
=====

Aha - at last, a subject that if I write about it five or more years ago,
the article is still relevant.  Nothing to worry about here... :-)

You gotta love emacs, it never changes...


.emacs file
-----------
this is the "init file"


Setting variables in the init file -

setting modes in the init file.  I like to use 80 char line breaks
so,

::

          (add-hook 'text-mode-hook
            '(lambda () (auto-fill-mode 1)))

    (add-hook 'text-mode-hook 'turn-on-auto-fill)

OK, each mode has a hook that is a variable holding a list of functions
that are called when the hook activates.  in this example when we start
text-mode we shall execute the list of one function, a lambda that
simply sets auto-fill-mode to 1


OK, what is the column after which I should break - well I set it at 75

::

    (setq fill-column 75)


examining variables

C-h v <VARNAME>
