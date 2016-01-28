List of topics to cover
=======================

Simple to complex roadmaps
--------------------------

One of the important things in software, perhaps the most important, is to keep things simple.
As the needs of an organisation grow, the complexity of the systems it uses increases.
I show here, in each section, a roadmap of complexity.  The base simplicity levels are 
expected to give the fundamental understanding of the problems, but give way fgracefully to 
new, (ope source) solutions that do the same thing as the simple system, but have extra more useful features.

FOr example, in configuration and co-ordination, we start with just a init file style API that reads from a text file
telling us what config data exists for our systems.  This is *fine* but it really quickly hits limits.
SOmething like APache Zookeeper is the next logical step, but that is waay more complicated to set up.
So we start witht he simplest possible, and point to where to take the next steps.


Automated provisioning
----------------------

- Ansible vs salt vs bash
  Look, bash is just *fine*
  We could use fabric for everything if we wanted.
  Now fabric supports parallel execution, there is limited need for other solutions
  I will use salt for basic infrastructure buildouts, its integreation with AWS etc.
  and then use fabirc once we have managed the state of PKI / servers up and pinabgle.
  This may be too complex but it is at least clear.
  
  Use fabric to build basic modules that ansible runs
  http://bsdploy.readthedocs.org/en/latest/usage/ansible-with-fabric.html
  
  in a venv...
  ::
  
     pip install ansible
  
  /etc/ansible/hosts::
  
     # /etc/ansible/hosts
     localhost ansible_connection=local
     
  
- pyholodeck
- holoconfig


Personal Security
-----------------

- QubeOS

- iOS - libimobiledevice

http://2014.zeronights.org/assets/files/slides/belenko.pdf


- Personal Password management

  Use Password Safe, on iOS and on linux.  
  Keep the safe file in sync via dropbox
  I need to : install pwsafe, dropbox on laptop and iOS, configure synching
  https://github.com/ronys/pypwsafe
  
  
- ssh-agent
  how toconfigure
  
- Run own CA

  Use client and server certificates to ensure comms secure.
  
-  eCryptfs


PKIs
----

The oprginasiuation needs to use PKI

It can use SSH public keys to allow comms between a user and servers over SSH
It needs to use SSL client certificates to allow commms between user and web servers (apps)
It can also use SAML to intermediate beween those 
It will need another solution for server-server comms


Server Security
---------------

- unikernels and cloud deployments
  The obvious end point of docker and immutable servers
   http://erlangonxen.org/blog/rediscovering-cloud
   Can we rely on the library is?

- qubeos

- security models and PKI

- saml and single sign on multiple providers 
  A sensible approach is client certs
  That won't happen with passwords so ...

- ssh


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


BOS Projects
------------

Business Operating System Projects - what features / capabilities do I want that are simple, expansiable, unix-like and much more business orientated?

1. Report-setting 
2. Purchase Orider mgtm
3. contact mgmt
4. address book
5. 


Business Administration 
=======================

If you are responsible for a team of one or more (!)
you should do these, even if it's not a legal entity
you are leading.  However if it's your own company - 
You definitely need to do these

*. Data room
   Storage of all legal and administrative contracts
   I have simple email system, drop box also work

*. Monthly Board pack
   You need this - writing is natures way of showing us how poor our thinking is. 

*. Accounts 
