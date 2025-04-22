monorepo vs microrepo
=====================

there is in the "code-o-sphere", an ongoing debate about which is best - and as
far as I get the discussion, its a non-issue.

the essence of the problem is "dependancy management" Once you are past a
certain size of development team (probably the Dunbar number),
then you have to start treating *other people in your firm* as third party
developers.  People who arent aware of your great plans, and who could at any
moment break your API, or give you a hug-of-death without warning.

Now it is *great* to be able to grep a codebase of millions of lines of code and
look for some usage of just the parts you are working on and use someone else as
a "how to" 

but eventually the problem of a mononrepo will surface - how do you freeze the
code base long emough that you can develop against it?

imagine you have a master brnach - the general isea is 
you branch off master, do a few days work 
and then merge back to master.

thats kind of ok unless master has just had, err, several thousand commits in that time

by the time you compelte the merge it has moved on 

there evetually becomes a speed of other people commotting 
yhat means there is no agreed copy if HEAD - its like relativilty

you *could* require say quarterly releases where one 
version of master (ie Linus') is blessed and people sunmit PRs

this coukd work and will be required for a product-ised 
sofyware - ie something that gets released to others like firmware (but if younare developing formware with 10,000 coders something has gone wrong)

but if your codebase is used by many different indepenandy
business units, then its *fine* to have them take their snapshot of master 
and use that in their unit while another unit
uses a snapshot from the next day

at this point it does not matter if we have one repo 
and different manchines in the org are running slightly different cersions 
of the same master brnach or of we are using hundreds if repos
and have different machiens running dofferent arrifacts

the problem always becomes how to merge into master
while master is chnaging faster than the commit process

this leads us to commit queues

At some point you have a contended commit process - lots of people 
want to chnage the same master branch at the same time 

And you dont want them
to commot and find they have not got all their approvals 

plus you have too many people committing at once - that is at some point 
you cannot rebase your chnages against head fast enough 
before another commit comes in and needs rebasing

now thats a monorepo problem - its pretty easy tomfox with many repos

and monrepos tend to do this by dividing up commit bits into different areas if code base (ie sales, accounts)

thisnis the same as many repos.

research

how does one repo work (it rarely is one repo)
how dors commit queue work - what happens if get meege conflict in the next queue item?
you just remve that and ask them to resubmit - with no slowdowwn on everyone else

Branching Strategies
--------------------

1. branch off master only. Except...
2. 


At some point we will create a single version of the code we want to "release"
This might be the single version of one area of the company, a LOB or just a
department. But as we quickly hit about 100 devs, we find 

So if the time for CI to complete is 20 minutes, you can make 3 commits per
hour.  This can become a problem at some point so you batch up merges.

However before that, we want to minimse dependancy, 
so use unrollable merges upwards, clear gates for approvals, process not trust




* Use of merge queues

