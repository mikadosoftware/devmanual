==============================
The Good, the Bad and the Ugly
==============================

::

  Writing is nature’s way of showing us how sloppy our thinking is.

Leslie Lamport


I very happily recounted my "Literacy started with the printing press,
software literacy starts with the Internet" meme in the last chapter.
I was rather proud of my little self, right up until I attended `Sprint 16`
the UK government's annual conference on tech and software and government.
And the Minister for the Cabinet Office stood up and gave a keynote that
was basically the speech I gave so many years prior in a London pub basement.

Nothing stops you feeling smug like politicians having ideas as good as yours.

But the thing is, we are both right.  His suit was better. 

The first mass-literacy revolution ran roughly in parallel with the
commercial and industrial revolutions in Europe.  But apart from the
usual things we associate with literacy, things like sharing ideas
widely, democratic access to knowledge and so on, the one that is
often *missed* is that ideas have to be much more precisely expressed
when you write them down.  If you go around making speeches, each
person can walk off with different ideas as to what you said (cf the
law chapter) but writing it down and they have to disagree with what
you meant.

WIth software this applies to the n'th degree. There is no longer any
forgiving human mind in the way of your writing to work out what you
really meant. Software is unforgiving. And this means we shall have to
write down what we really mean.


Some computer vision AI software failed to see balck women as human
faces - accurately reflecting the cultural make up of the AI
laboratory it sprang from.  And we shall have to solve the multiutude
of robotic actions in the real world that were previosuly left to
chance.  See the chapter on self-driving cars for example.

So software literacty is not just a nice fluffy teach the world to
code idea.  It is going to be a fundamental questioning of every
aspect of our society and assumptions.  And we will need much much
better at resolving those conflicts - large scale democratic politics
does not seem to be good at this. Although, as per Churchill, it is a
*lot* better than all the others.

I do not see this as some portent of doom. More that we are *already*
in a world too sophisticated for any one mind to understand.  We rely
utterly on the expertese, and indeed munificence of others.  Its just
that the procedures for all these are still hidden and opaque. Partly
because it is commercailly beneficial, but the vast majority of the
time it is just the processes have not been made into software, and so
are not accessible.

Let's walk through a few examples.

Knight Capital
--------------

Knight Capital should have been software literate.  It was a new
company, built to operate in the high-frequency trading world of US
equities, and had invested heavily in programmers and computers

Their business model was *market making* - buying shares from someone
who wanted to sell, waiting a bit, and selling them to someone who
wanted to buy. Market making is a valued part of all exchanges, and
way back, when the Exchange gave a priviledged few the right to be
market makers (for a fee of course) it was a very profitable exercise.
However as new market makers were granted access, such as Knight
Capital, the profits dropped (good for buyers and sellers, such as our
pension funds) and the competition sped up - slow market makers did
not get to trade with anyone.

On August 1, 2012, Knight Capital released a new version of their
software. And did so in a partly-manual manner.  Those words, 'not
automated' make those who are software literate shudder.  Imagine
having a book as a loose sheaf of papers, unbound.  You know its just
missing something.  Surely things will eventually get all muddled up.
And sure enough, at Knight Capital, they had left an old, debug
version of the code on one of their servers. Which now merrily started
placing *test* orders onto the *real* market.

Test orders, such as Buy high and Sell at a loss, and repeat 10,000
times in a few fractions of a second.

Knight Capital tried to turn off their mistakes, but 45 minutes later (an age in
HFT) they had mistakenly executed 4 million orders for 100+ stocks, and lost 440
million dollars, effectively bankrupting the company.  Other players in the
market had of course realised something was wrong, and initially expected the
orders to be turned off within seconds. When it was not, they merrily took the
winning side on all Knight Capitals traded and pocketed the cash. No point
turning down free money is there?

Knight Capital's process of getting software that had been written correctly out
and into the hands of users (ie the equivalent of publishing) was broken.  A
newspaper that could write brilliant articles but struggled with the whole
delivering bundles to street vendors would not last long.

In software, this publishing is called a release, but its as vital as the
process of publishing and delivering paper was to the Post.  Companies I have worked in
have had ranges of automated releases done a few times a day, or
manually a few times a year.  Guess who felt more ... literate.

Office Of Personnel Management
------------------------------

In June 2015, the US government agency "Office of Personnel Management"
announced it had suffered a data breach.  Starting in March 2014, external
hackers had breached the firewalls around the agency and were able to access the
personnel records of millions of current and former government workers.  The
agency collected many things, like pay records, but also, held background checks
on employees who needed higher levels of security clearance - in short they had
the records that said you used to be a drug addict or depressed. All the stuff
they want to know about you in case it is used to balckmail you.

This was it seems all stored on mainframes running COBOL.  And the thing about
storing data is that you must at minimum, encrypt it at rest on disk.  This is
like, using ink or folders or filing cabinets. Its something you don't even think
about.  Not for stuff that foreign governments can use to blackmail your Embassy
staff with.

So lets get this clear.  Vital security information and pay records, stored
unencrypted on mainframes that are so old they cannot spell encryption, and then
the Chinese hackers get in.

This breach, discovered seemingly by accident when a computer forensics firm was
asked to preapre a demo, is not something solvable by replacing credit cards.
It is probably America's deepest national security problem for the next few
decades.  Well, one of them.

This is a defining moment in software professionalism.  The right move for a
professional and so the right move for a software literate organisation, was to
shutdown the impossible-to-secure mainframes and announce a budget request and a
migration plan.

Things like intrusion detection programs would have been good, but thats just
"normal best practise" not "professional ethics".

Now, why did the woman at the top (not likely a
malicious actor) why did she not take this action? Because of the degree of
obfuscation? Possibly. But the one thing that leaps out of OPM is the inabiliy
to enmcrypt on COBOL mainframes.

Perhasp Everything else is justifiable in the hindsight race.  But when you
simply cannot do the job ethics dictates you dont pretend and carry on.

OPM shows us that one defining quality of software literacy will be professional
ethics. to quote Spiderman, "with great power comes great responsibility".  For
the next generation at least, software literacy will be unevenly spread
throughout the world.  And the importance of software to the world at large is
so great that we should ensure those who wield that importance are not just
expected to be trustworthy, but are monitored by their peers.

Professional Ethics still matters


Target and Yahoo
----------------

Target and Yahoo make interesting case studies. Target in 2014 had given a
Air conditioning contractor access *into* their internal network, from the
A/C contractor's own network.  So when the A/C contractor was breached, the
Target internal network was just a hop away.

Target lost millions of credit card details, and, probably more importantly
lost their CEO because of the public reaction.

Yahoo, had attackers copy 1 Billion (image) email addresses and passwords.
They only admitted it because they had to for SEC rulings. (check)

Target is probably when software security failings first took a major scalp.
Yahoo is probably the last.

 
Healthcare.gov
--------------

?

What have we learnt
-------------------

A software literate company will not necessarily have these issues fixed and
working perfectly, but they will be top of mind, and everyone in the company
will know, not "something is wrong" but "this thing right here is not happening"

Look at the famous "New Relic Punch".  There was not "we do not know what is
going on" but a clear "if I do this I will know what is going on".

OPM shows us the new scope of ethics, and Healthcare.gov shows us "normal best
pracise"


There is hope
-------------

Government Digital Services


However, these are not normal, or default, or even expected. They are high profile
and positive. But legal frameworks (from privacy laws to the defintion of a company)
have not changed.  We need to go further in changing the structure of a company.


The programmable company
------------------------

One theme I shall return to is the idea that companies and organisations
are simply means to organise humans - and that has lower cost and friction
than it used to with software intermediation.

To put it simply, almost everything that is done in a normal company now
can be automated, and the co-ordination of functions is an email away.

For almost everything a company or organisation does a second time, that can be automated
or co-ordinated via software.  A company will become a programmable entity.


The rare, right way
-------------------

The failures above are all very varied. Amount them no obvious solutions.
This is the point - we simply do not know what the Washington post of often years
Hence will look and behave like.  But like the team at healthcare, we don't need to
We need to follow "best practise".  Sadly there is no written how to on that - it is more
the gross difference between a Washington post set up and run by a literate editor and that setup and run by an illiterate - charlelemn



* software poliktics and snowden and Cathy
  gatekeepers of new news.
  Not news but models

* conway and coase - structure of organisations and markets
* Who owns you? devices, data, profit from data, externalities compensation
* professionalism - growing up - Cracked, its what you can do for others
  reliability. Its like an API for a software dev - and same for a software team
  See the API
* culture and software
  literate companies, esp those with literate output, had a new culture.
  a more open culture in europe. It just came with reading.
  I cannot imagine working on a code base I cannot roam around in
  Add in pixar and candour, and its a new culture.
*



Software is politics now
========================

http://blog.memespring.co.uk/2015/09/14/product-land-part-3/
::

    """Politics in the 21st century will, in part, be about control over the
    digital services we now rely on, and which hold an ever         growing
    concentration of our personal and household data, from how often we move
    (fitbit, jawbone), where to (Google Play             Services), what we tell
    people (WhatsApp, Facebook) and to how often we burn our toast (Nest)."""

The types of organisations that *can* exist are likelyt to have ot expand
We need a software literate civil service as urgently as we need more start ups.
GDS is a marvellous step in the right direction

Weapons of math destruction and the hidden hand
- Asimov ?


The revolution has not happened yet
-----------------------------------

https://medium.com/absurdist/the-computer-revolution-has-yet-to-happen-f1dbf983d477#.a9n5t8be6

Devices are curated not owned by us
The APIs do not exist because vast majority of users could not use them - would need to buy another app

Pen and paper ?



Notes misc
===========

None of these are purely technical foul-ups.  Where humans are involved thats never
the case - it is always tinged with plitics.

It's how would an illiterate person run the Washington Post.  Ben
bradlee


Healthcare.gov - one of the team responsible for the clean up of
healthcare.gov tells a story (YouTube). He explains. But mostly he
says they did nothing clever, they invented nothing new. They just ran
best practises (the famous new relic punch).

But why did they run best practises and not others. There are many
explanations, multiple gov contractors, sclerotic practises etc. but
ultimately the people at the top looked at a newspaper that was run as
it would be run by an illiterate and said "well I can't see how else
it should run", because they were illiterate too.


.. #: http://www.hrc.utexas.edu/educator/modules/gutenberg/books/legacy/


The incremental improvement - constant little bit better till it is out of sight
This is a fundamental part - daily, hourly improvements just sent out.

A Mea Culpa - from me and Uncle Bob
http://blog.paul-brian.com/2015/06/05/being-professional/

::

Conclusion The trick to handling pressure is to avoid it when you can, and weather it when you can’t. You avoid it by managing commitments, following your disciplines, and keeping clean. You weather it by staying calm, communicating, following your disciplines, and getting help

So as we know what is wrong, it is useful to dive into why, and what to do about it.
Uncle bob recommends managing pressure - and Inwoukd like to suggest that professionalism is an API we present to our stake holders - like "keeping a promise"

The APIs -

    source control
    Keeping it readable

    tech debt and tech assets - code and tests
    Debt and assets

    requirements lifecycle (PEP)
    Theory of the firm vs professionalism

    automated build and deployment (dogfood)
    Staying clean

    Documentation and Marketing
    Again a cost of independence in market place

    openness and reviews
    Non n

    Progress Not Perfection (YouTube clip)

    static and other analysis

    performance mgmt and measuring everything (and making reports on everything)

    Automatic project mgmt

    Risk management

    have fun, try new things, don't be afraid

    Requirements Lifecycle (PEPs)

Maintaining a distance, is anathema to Agile hugs.
But look at IR35 SDC - Supervised, Directed and Controlled.
(The theory of the firm, transaction costs, Fonald Coase and IR35. Why requirements management is and is not good for you)

Why is it a good idea
Why is it a bad idea
Is it in my ideal project?

Can I craft a set of ideals for my Open Source Project and how do they touch upon the wider world of professionalism and crafts-person-ship.

A multi layered API for software engineers.
I keep stuffing it up. I am a fairly good coder - and have survived almost 20 years as developer, CTO and consultant. So I occasionally get it right.

Remote pair programming

After the fact ticketd

https://itunes.apple.com/gb/podcast/tedtalks-audio/id160904630?mt=2&i=346210793

Teams not super chickens

    there are no rock stars - we need everyone
    there is only one standard of quality - the best. It is not the enemy of the good. Prioritisation is the enemy
    theory of the team is same as theory of the firm. Let the market decide

Candour

The three goals of software engineering
Reliability
Stability
Progress

As the joker says, "no one panics if everything is going according to plan"
Reliability, even if that means having to reboot every 24 hours, is still reliable
Stability is better - not having to reboot every 24 hours
Progress is the best - not having a joker in the pack
Chaos monkey as a white hat joker.

Release Management

    window of pain
    why it is complex
    Apple style checklists

    automate the build

    privacy
    It's the new pollution- it has enormous benefits to society and its productive capability (ie medical research) but like industrial pollution it has downside and we have not managed to cope with the downside in 150 years. The U.S. Democratic model seems to lead the world in dealing best with pollution (not worried about German vs US standards of chicken handling - look at Russian radiation handling or the Middle East approach to spills.

We're global remember.



Why write a book?
-----------------

  Writing is nature’s way of showing us how sloppy our thinking is.


 Leslie Lam-port


http://blog.fogus.me/2015/11/04/the-100101-method-my-approach-to-open-source/
Keep lots on the go and see what pops
Antithesis of project planning
Psychological
Creative


Do you know what James Watt's second most famous invention was? The
carbon copy paper < http://cnx.org/content/m32173/latest/>_ used to
keep the various parts of an multinational steam engine company
synchronised - Watt had to invent a new technology to cope with the
vast growth his first invention had spawned


Shakespeare and Company
Left bank of seine
What does a software bookshop look like? What events does it engender?

When does data become proprietary
--------------------////////------


Google encrypts the referrer header
But that is what a person types in as search term

Why is that private not public?

European courts missing the point
https://itunes.apple.com/gb/podcast/the-economist-radio-all-audio/id151230264?mt=2&i=361720969

Possible free trade battle
But the battle is over the wrong thing
Data is public - it just is on vastly larger scales than we realise (pea souper fallacy)

Not only that but free trade areas in data will be needed to avoid
Balkanisation of the Internet

It's not unavoidable - it should be a free vs unfree world
The new capitalism - free data

Private data is private, unless published
There was a huge backlash against this for the first and other amendments
See the uk government under fox / Pitt

But the principal has held well
And we need to refresh it - and redefine publish in light of pea souper

http://uk.businessinsider.com/jobs-that-are-quickly-disappearing-thanks-to-robots-2016-2?r=US&IR=T



Open vs closed not right
Oppressive vs liberating is closer

Public data about us can be oppressive, can be limiting
But finding the balance is key
And the default should be open just as default was open for amweica



Exporting democracy

Where does half the world look to for inspiration?
Western democracy or Chinese capitalism without representation?

Democracy is exported - nation to nation, generation to generation
We need to define the new society with new parameters

European democracy is under threat, even building a wall around Mexico

Who wants that ?

Solutions

- remove financial spikes through removing tax relief on loan interest
- allow the natural state of software literacy to be enshrined in the societies norms laws codes and markets
- what is the natural state of software literacy

- best example is open source:

Open
Totally open
Candour
Democracy ?
Meritocracy
Evidence led



The shape of companies and countries to come
--------------------------------------------

So my hypothesis is that software literacy is a real thing,
that it will create programmable companies, and that companies that
have a nervous system, that can be controlled with smaller numbers of humans
instead of having to have humans in place of automation, we shall see
smaller companies due to Ronald Coase theory of the firm

As such these smaller firms can negotiate better deals but what will be the environment
in which they do that

- free trade areas - a perfect market
- common market
- federal system

Discuss European referendum


What’s more, as software eats the world, one side effect is that rewards accrue nonlinearly to those with the best software


Politics and software
---------------------

One thing worth noting is that if he is right, and Facebook (and lesser extent Google and Twitter) represent the new gatekeeper / aggregator for political news, then there is a crying need for their algorithms to be public, and there is a whole industry of political SEO

https://stratechery.com/2016/the-voters-decide/


CIA and job protection
----------------------

America is 50x richer than the rest of the world, but
Let's face it, that's historical accident and some luck of
Democratic capitalism culture

Now the world is consensus - we all know democratic capitalism of some form is the way to go
So will the USA stay fifty times richer? No

Will they get poorer in absolute terms or just wait
in stagnation while everyone else catches up (pretty much what middle class wages have done relative to China)

Either way, USA is likely to fight - hence the CIA and the hegemonic back doors - the use of intelligence gathering against Brazilian companies.

It is Canute turning the tide back.  By throwing stones.

It's not going to be pretty

Redefining privacy
------------------

There is a new round of crypto-wars going on (see Obama speech "absolutist")
But this is part of wider discussion around meaning of privacy

It's a privative

It's based in secure in ones home - constitution

But let's look at ambient computing.
Intelligent context aware programming

Scenario: I walk from my kitchen to the living room, and the music I had playing dims in kitchen
And starts up in living room speakers.  I say "house! Something more dinner jazz please, and dim the lights"

Now to do this I must have computer monitoring me and my voice
It must stream music, electric usage will dip.


How can I defend my privacy?
Do I really care ?
Prevention of annoyance?
My music tastes probably say only a little politically
but what films I watch, what documentaries? Fox News or CNN ?


Social organisation and software
- software as it needs precision highlights a lot
For example conways law - social organisation of contributors reflects the software produced

http://hintjens.com/blog:112

More clearly is need for individual rights
This is a politically accepted thing in real world - but as we move to situation where whole world is a contributor what happens? Much more planning and modelling?


Productivity :

The second biggest issue of our time
Basically the low hanging fruit of mechanisation has gone.

Productivity as measure of energy used to output

The future is more complex solutions to drive smaller increments in productivity until energy becomes orders magnitude cheaper or our usage orders more sophisticated

This should be the big win for electronics

What we are missing is organisational change to cope with it.

Most organisations hold back productivity- and fixing that will be hard

- also remote working and competition across the globe

Privacy:

The biggest issue of our time
The modern day pollution
The issue is who sets the laws
The issue is we must be regulated (murder)
The issue is we shall see Google become a utility in need of regulation - but under whose jurisdiction?

How in Europe do we set this? How in USA? What about China (monitoring all )

Privacy shield - max schremms

Audio visual media services directive - tv regulation. Country of origin country of destination

Unregulated is impossible
Light regulation means skills and information to deal with

The less regulation, the more transparency and individual tools to compensate

My view: it is harmful to insist on country of destination style solutions to regulation as these allow dictatorships to censor

We should have global agreements on base regulation (child pornogrpahy, hate speech etc) and enforce transparency - and it is upto destinations to educate and provide tools to support their choices.


The emerging politics
---------------------
An understanding of politics of technology
Icelands pirate party
http://uk.mobile.reuters.com/article/idUKKCN11Z1RV
Tom Watson
Calling out footballer


The emerging secure computing platform
--------------------------------------


tmzt 32 minutes ago | parent | on: South Korea military cyber command was hacked

RiscV, TCP+crypto offload, hardware switchports with luajit or nf rules. Reactive UI with hardware rendering and compositing.
Hardware keystore with physical switch to generate and enroll keys, user/owner controlled secrets, one-time programmable as an option, hardwired SAK and OS personality switching key.
Real-time security isolation kernel, hardware-enforced containerization with MMU-protected GPU passthrough.

https://news.ycombinator.com/reply?id=12623911&goto=threads%3Fid%3Dlifeisstillgood%2312623911






.. 

Company
-------
* Software literacy
* walked examples
* so what is a company, why does it exits?
  victorian company, modern tech stoneage mind <- problem
  solow / coase / economic theory on markets <- theory
     modern_tech,_victorian_companies_and_stone_age_minds
  solutions:
    new company
    programmable
    smaller coaseian coefficient
    democractic / transparnet decision making
    regulatable
    
* Elements of new company
* programmable company
* coase curve breaking point
* remote working / physical location / 
* comparison with film making not relevant
* fixed elements of company -> manufacturing. But this is light indutrial
* democracy / coase / understanding the mission vs doing as told
  plus expains why MBAs never talk straight -
  A hierarchy is hard to be open in
  democracy breeds right ansers and openness.
  Even if it is hard
  hiring_ringers.rst
  
* swardley mapping - landscape-strategy, simple_to_complex_roadmaps
* technical limitations on future - tape/disks, parallelism, privacy
  futureshifts.rst
* marketingbenefits
