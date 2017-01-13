================================
How is the future going to look?
================================

What is about to make my life harder?
=====================================

Part of the challenge for a simple IT manager is to keep abreast of an ever changing landscape without falling into the twin tarpits of hype and cool.

No-one can be in this business for long without seeing the next big thing whizz past us like a dead bunny with a jetpack.  But inured as we maybe to the sort of hype that got me buying textbooks on marimba and push technology in '98, it takes many years to notice the plausibly disguised tarpits and not spotting them can waste time money and effort vanishing down dead ends.

Oh, by the way, as I am talking about future trends, I am officially sanctioned not to use the phrase 'paradigm shift', a crime for which the gulags beckon.

For IT managers there are four major changes coming

- Disks are becoming tapes
- Parallel programming
- Information security is as busted as DRM
- Everything else, probably involving privacy.

Disks are becoming tapes
------------------------

How big can a hard disk get?  I have got several 500GB disks, and can now buy 1TB disks, which considering I remember saving up for a 16*Kilobyte* expansion pack for my ZX80 [#]_ is quite terrifying.  However, the bods from Seagate believe that, just like light waves put a limit on how small a transistor can be photo-etched onto silicon, similar electro-magnetic theories limit the size of a 5 1/4" hard disk - but we shall reach 20TB before that becomes a manufacturing restraint.

Now for a randomly fragmented hard disk of 20TB the access time for any piece of data is quite slow compared to the total size of the disk.  This ratio has been increasing for a while, and it has some serious implications.

The amount of data a disk can output depends on 2 things, the *transfer rate* or how quickly it can pull data from under the head and out to the rest of the PC, and how quickly it can find the data on the disk. This last one is important. 
Disks can now hold 1TB and will grow to 20TB. They can sustain transfer rates of about 50MegaBytes/s, but even high end disks take 5 milliseconds to find a particular location on the disk [#]_

Lets say we want to pull off mp3 files, snippets of conversation from my life. At a seek time of 5ms, I can get to 200 *locations* a second.  This is not the same as 200 files a second - it will be snippets of files, chunks that have to be pulled off and reassembled.  Today this does not matter much, but with a 20TB disk, and we choose a file fragment size of say 5KB that is retrieved each access, I have a throughput not of 50MB/s but 1MB/s.  That is 20TB / 1MB or 20 million seconds to retrieve the whole disk. That's 231 days by the way.

This is obviously a worst case style example, but if we continue to use hard disks as we have been in my career, then it will take that long to read a disk.  Obviously madness, so when we write to the disk we will have to think about the use of the the data later on.  Thats unheard of today.  Its back to magnetic tapes.
 
We will fill these disks. Not just with cute otters on youtube, but with our lives; emails, phone conversations, videos from our camera equiped eyeglasses (and if you think that is unlikely look at urban cyclists, there is a growth in cameras recording the daily commute ready to send in for that all important insurance claim against the driver who just hit you).  We shall go back to a time when the application developer had to think where on a tape the data was stored.

So disks will stop becoming random access and more than likely be time sequential storage.  Which is fine when I am looking for my phone conversation from the 22nd of August.  But it has a problem when I want all the phone calls I made to my wife, in which I mentioned taking the cats to the vets.  The implications for this are quite huge, programmers today live in a world of random access (this is one half of the reason for dominance of the relational database model).  To end that will require massive mindset changes, and we programmers are by and large a conservative lot.

Parallel programming
--------------------
With one massive change to the way programmers think already coming down the line, the next one is a doozie.

Moore's law is, for its kind, a famous dictum.  It basically states that the processing power of a chip doubles every 18mths.  Understanding this law is widely held to be one reason Microsoft defeated Lotus in the speadsheet market [#]_ - Bill Gates decided to go for the best new features even if it ran slowly, gambling that in time the chips would be twice as fast.  Lotus meantime tried to speed up their spreadsheet in the code, and the market chose the new features of Excel now running at acceptable speeds.

Moore's law has traditionally been implemented by chip manufacturers like Intel making transistors on silicon smaller each generation so squeezing more into a chip.

As mentioned earlier, the wavelength of light is making it difficult to do this any more, so chip manufacturers are basically cheating, keeping the size of the transistors the same but putting twice as many on there.  To get twice as many transistors to work really means two CPUs.  The problem with this is that a single CPU is in essence linear, one instruction at a time.  Programs were written with this in mind, and now,  what worked for Microsoft in the late eighties stops.  If I write my clever new, slow program, in 18 months it will still be just as slow  - it works in a linear fashion, is designed in a linear fashion and so will only run on one CPU.  That power doubling stops.

Intel have already announced a 32 core chip.  Now if I take the Lotus approach and optimise my slow code for multile CPUs, I will run my applications upto 32 times faster than the guy down the road.  I do not know what competitive advantage I can get from that, but it must exist.  In short, what worked for Bill Gates 20 years ago, seems to be stopping now.  There will be no free speed up in 18 mths.  

There are new languages designed to handle these parallel programming worlds, they are a odd and hither too little trodden world of *functional programming*, with Lisp as the poster child.  However two new languages best represent the choices ahead - Erlang, which passes messages between nodes and essentially shares nothing between these cores, and Haskell which does something clever with shared memory which frankly I do not understand. And there in lies the rub, as these are new languages, new *paradigms* (there I said it), and they need massive shifts in how people think and work - and again programmers are slow to pick up new things.  Really new things that is.

Either way, to tackle the parallel programming world, programmers will need to learn a completely new class of languages. And look how long it took to go from C to C++ to Java, which basically was objects, then garbage collection. (about 30 years. Can we wait another 30?  Or perhaps there is competitive advantage in Erlang?)

Tarpits
-------
Here we can see tarpits forming, and it is worth commenting on their likely shape too.

There are already rumblings about Intel and others developing compilers that will parallelise your program for you, meaning the programmer does not have to think about the problems of running his app on 300 CPUs in different time zones, it just happenns. Yeah, and the crack Royal Air Force Porcine Display team is putting on a show at an airfield near you.  So much effort is being expended to stop us from having to learn a new thing.  That's not in line with the idea that computers are tools, not gadgets and we need to learn to use them.
 
Both the above lead to the much heralded Grid computing - we will treat computing like we treat electricity - ubiquitous and commoditised. 

I just do not beleive it.

I can see how already commoditised services will be gridified - but lets face it the reason organisations use IT is two-fold: to not lose cost advantages from not doing what everyone else does (the move from letters and memos to email) and to gain competitive advantage by doing something better than others.

The first one will be gridified - if your email system works like everyone else's, you do not lose out.  But most of the driving force for new IT is to gain a competitive advantage - to be able to do what others cannot.  And that can, by definition, not be commodity.


Information security is as busted as DRM
----------------------------------------
I have an important database in the office, with lots of important data. If the competition finds this data we could lose sales, if the tax authorities find it we could lose the CFO, and if the press find it we could lose the CEO.  So it is important not to let anyone copy it, or take it out of the building.

That is suddenly not so easy anymore.  Mobile phones, PDAs, remote working, on the road, laptops and home offices all mean that the data needs to go to where the people are.  I can encrypt the data as it travels over the network, but the only way someone can work on it is if it is decrypted at their end.  This is the same as a DRM protected song can be as encrypted as you or EMI like, but at some point it needs to be played through my earphones.  At that point someone can copy it, both the songs and the tax data.  And lets face it if it can be copied and has a value, it *will* be copied. [#]_

There is an attempt to control this - Microsoft is trying the '''Trusted Computing''' approach - where the hardware is locked and prevented from running anything Microsoft (and by extension the IP owner) does not want run. However it has been a damp squid so far, and even Apple the most successful hardware-controlled-by-someone-not-the-owner approach is trying to persuade the music business to stop mucking around.
And what is failing in the consumer market will fail harder in the business market - the question to be framed is '''You want me to buy a laptop that can stop the MD from viewing his own sales data if Microsoft decides he is breaching copyright ? This being a man who cannot print from Word every other week?  Yeah, let me get my cheque-book.'''

My data is not secure when it leaves my little data-castle.  And yet everyone wants to work away from the office, on their iphone, in the park.  

Privacy
-------
It is vanishing, or rather, the assumptions we used to have about privacy no longer match reality.  Most of my conversations were assumed to be private and *ephemeral* [#]_, and because they were between two or three people they were.  But when the conversations are on email, or recorded by someone's iphone or life-corder in their glasses, that stops.  Am I to be held to my every whittered word (even the ones on this site I would be happy to stay a bit more ephemeral.)


Conclusion
----------
Hype and the Next Big Thing are always around us, and spotting the difference between real faultlines and over-hyped faultlines is a difficulty, but one we must all learn.  The business world (and real world too) do not change that fast, the signs are all around if we care to look.  Like someone said, 'the future is already here, just not evenly distributed yet.'





.. [#] if you are a british geek and of a certain age the ZX80 will hold a special place in your heart, alongside 'manic miner' and sherbert dipping lollies

.. [#] http://en.wikipedia.org/wiki/Hard_disk#Capacity_and_access_speed
 
.. [#] http://www.joelonsoftware.com/items/2007/09/18.html. The eagle-eyed amoung you may note that while Joel supports my argument on moores law helping microsoft, this article flat out contradicts my idea that this time round betting on Moores law is going to lose.  

.. [#] (The head of Deutsche Post was forced to resign as details of tax avoiders / evaders where handed over to European authorities (and he was on the list).  Basically Germany offered a reward for any (Lichenstein) banker able to prove that Germans were dodging taxes.  An electronic file was duly copied and sent in)

.. [#] Bruce Schneier is good on this subject.

bibliography
------------
http://www.acmqueue.org/modules.php?name=Content&pa=showpage&pid=43


