==================
Using GitHub / ssh
==================

==================


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
