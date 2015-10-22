Standard Operating procedures are of course neccessary
They make up a user manula for my company, Mikado software.

Using GitHub / ssh
------------------

::
   
    $ ssh-keygen
    choose no passphrase, 
    save in home/pbrian/.ssh/github

    Your identification has been saved in /home/pbrian/.ssh/github.
    Your public key has been saved in /home/pbrian/.ssh/github.pub.
    The key fingerprint is:
    a8:81:d2:77:ef:5e:36:e0:8d:74:8e:3e:bd:38:33:7d pbrian@HPCube


Lets test to see if we have github access (ie they got our *public* key)

::

    $ ~/projects$ ssh -T -i ~/.ssh/github git@github.com
    Hi lifeisstillgood! You've successfully authenticated, but GitHub does not provide shell access.

But thats a mouthful to run each time



Now we update our .ssh/config

::


    $ cat ~/.ssh/config
    Host github
        HostName github.com
        IdentityFile ~/.ssh/github
        User git

::

    pbrian@HPCube:~/projects$ ssh -T github
Hi lifeisstillgood! You've successfully authenticated, but GitHub does not provide shell access.


We want to upload github.pub to github and then start up and down loading code

::

    $ git clone git@github.com:lifeisstillgood/myhomedir.git
    Cloning into 'myhomedir'...
Meta Projects
=============

I have lots, perhaps too many, ideas. And I hate to let go of any of them.
This means most are unfinished and thus the really high potential ones do not get as much attention as they should.  

I know I will benefit from more focus, but i also benefit from "a change is as good as a rest".  So I want a means to keep my projects in control, without overwhlming my ability to remeber what they are all.

I need a kind of software "Getting Things Done".


My project control will be 

* stored in individual repos remotely (ie on github)
* secure enough 
* lightweight
* easilyexpansible
* easy to publish information about them

