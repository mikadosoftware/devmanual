#!

'''There is a story I like about PG Wodehouse, author of the Jeeves
and Wooster novels.  He had an unusual method of editing his own work.
He would write (long hand) a page of his new book.  And read it, and
place the page on the wall of his study, and start on the next page.
But the page stuck to the wall was not at some random location - it
was, perhaps obviously, in order going horizontally around the room,
but it was also vertically where he thought it should be relative to 
the *quality* he expected of himself.::

   "Pages would start near the floor and slowly work their way up 
    until they touched the picture rail, when they were good enough 
    for publication"

This jibes marvellously with how I think of software development.  It
is focused on the code itself - the rating system is not in a
notebook, spreadsheet or bug tracker, it is a natural extension of where
and how the code is stored.

So I intend to update and release my todo-inator idea. 

There are two parts - the rating of the code, by the author.  this will be a simple
five star system ::

   # rate: * * * * *
   # lifecycle: <prototype/PoC>, <pre-release>, maturing, mature, retiring 
   # TODO: 

And we can then see this rating in a specialised `ls`. 

specialised ls - walk over a package source and tell me ::

   star rating
   todos
   new features

I think I will have a second system that correlates to a map of my todos and 
some external systems
And some way of recording success / failures

Design
------

walk a source tree, and build a dict of file: {markers...}
return that 


TODO: build a test framework / runner
TODO: build a lifecycle todo listing
TODO: build a ticketing system??? at least a list of todos
TODO: linting etc - a pre-commit check system ala phabricator

'''

# rate: **
# life: prototype
# TODO: build basic walk and parse and report features

import os


def walk_tree(rootpath):
    ignoredirs = ['.git',]
    for dirpath, dirs, files in os.walk(rootpath):
        #change dirs to remove unwanted dirs to descend into
        #rememer we need to use .remove as dirs seems to just point at
        #underlying implementation, so substitution has no effect
        for d in ignoredirs:
            if d in dirs:
                dirs.remove(d)
                            
        for file in files:
            thisfile = os.path.join(dirpath, file)
            yield thisfile

def parse_file(txt):
    res = {}
    for line in txt.split('\n'):
        if line.strip().startswith('#'):
            #valid possible
            for token in ['rate:', 'todo:', 'life:']:
                if line.lower().find(token) >-1:
                    res[token] = line
    return res
            
if __name__ == '__main__':
    for filepath in walk_tree('/root/projects/devmanual'):
        print filepath, parse_file(open(filepath).read())




