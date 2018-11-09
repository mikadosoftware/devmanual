============
SoftwareMind
============

Introduction
============

I have twenty years experience "in the trenches" of software
development - writing commercial and open source software for cutting
edge ISPs, major financial houses and not-for-profit organisations, in
big offices, tiny offices or on globally distributed teams.

And I have learnt a lot about what works, and what does not, when it
comes to getting software out of the door.

This book is my attempt to distill those two decades of lessons, into
one book.  Well, maybe two books.  And a website. OK, so there is a
lot to distill ...

How this book is organised
==========================

Mostly what needs to be distilled is not *how* to create software and
software teams, a lot of this book is about ... why.  Why is software
eating the world, why do certain practises work well and why do
certain pathologies still run in our organisations.

I call this *why*, The Software Mind.  The *how* is The Dev Manual.

So there are two kinds of chapter - one trying to explain the why, the
context for the more detailed, how-to chapters. Both are useful to
read, and you can think of this as two interleaved books.

=================
Software Literacy
=================

I'm standing in a cavernous room underneath a bustling, noisy pub in
London's Covent Garden.  It was a fine Summers day and the evening is
sharply cooking.

I look around at the 90-odd developers, graduates and entrepreneurs in
the room, and, as I have been persuaded to sponsor this meeting, now
all I have to do is give a quick speech.

I never quite know what to do for these sort of speeches - so I decide
to give a history lesson. Yes. A history lesson. Gripping stuff, some
were even rolling their eyes in excitement.

It's a good one though. You see, in 1454, Johannes Gutenberg printed
the first of his Bibles using movable type - and ushered in a new era
of literacy and communication. Printing books was now orders of
magnitude cheaper, and there was an explosion of publishing. The
number of published books leapt from an estimated 30,000 books *in all
of Europe in 1450* to 12 million books by 1500.  Think about that. A
decent sized library today, in many large towns in England will have
30,000 books.  More than were in the whole of Europe before the
printing press. [#]_

Within a generation literacy in Western Europe had leapt from under 2%
to well over 20% - and it changed everything. Martin Luther was able
to nail a piece of paper to a church door and expect most members of
the middle-class congregation to simply read it, not have it read to
them by clergy. Books on mathematics and navigation enabled the
training of middle-class merchantmen who would then dare, only 40
years later, to cross the Atlantic.

Literacy en mass changed the course of human history and gave a tiny
corner EurAsia some huge advantages the effects of which are only just
wearing off five centuries later.

Before people wandered off to the bar I decided to let them know why
they were getting my best Simon Scharma impression.

Because, in my view, and remember they were eating my sausage rolls,
so that counts, in my view we are entering the age of a new form of
literacy - *software literacy.*

Even in the 15th century, nations, companies and guilds and churches
competed, and ran international concerns. But somewhere between
Gutenberg's Bible and Luther's 95 Theses these companies changed. Not
with business process reengineering, or total quality circles - but
changed like leaving the water and walking on land changed. I have no
idea how to quantify the advantages a company whose staff can all read
and write will have over a company whose staff are illiterate. It's
not one of lower labour cost, or better marketing, it's something
else...Deep in our bones we *know* that literacy changes everything.
Its so built into us and into everyone we know that we cannot imagine
a world where we cannot read or write.

Anyway, you, like the poor people wanting to get to the bar, can see
where I am taking this. The ability to marshall knowledge, to code and
compile and compute, the natural inclination to arrange the world so
it can be iterated over, the ability to turn a business from a
medieval scriptorium into an operating system is software literacy.

The final shape of a software literate company is probably unguessable
to us, in the same way that an airports departures board was
unguessable to Pope Pius II, or that a major newspaper run by
illiterate editors will look and work nothing like the Washington
Post. But we can be sure they are coming. And we can make sensible
predictions about what they will and won't be.

And so, as the Meetup wanders back to the bar slightly shocked, we
wander back to our theme.

The software literate company, and the programmable company
-----------------------------------------------------------

Software literacy for a company does not mean that it just hires a lot
of programmers, and calls the job done.  Thats been happening for a
long time and yet few companies manage to evolve.  I am hoping to
describe in this book a vision of a company *that does not exist yet*.
A truly literate company, in a world of other softwre literate
companies.  We cannot know for sure the shape such companies will
take - they will jostle and change in a complex dance of evolution,
but we can look at both positive and negative data we have today - how
companies have failed to act in a sane / literate manner, and how some
fundamentals of software literacy are shining thorugh and will be
unavoidable in the future.



.. figure:: /_static/all-the-presidents-men.png
   :width: 75%

   When I speak of a literate company, please keep this film in mind.

'All the President's Men' is one of my favourite films, engrossing and
suspenseful.  And it also portrays life in a deeply literate company.

I will take a leap and argue that the Washington Post under Ben
Bradlee was the epitome of a (non-software) literate company.  It had
well trained professionals, clear ethical standards, clear business
processes and clear processes for ensuring that its literate output
met their standards. Editors and copy-sub-editors and so on.  Oh, and
cashflow. That helped a lot.

I suggest that even companies like tech-behemoth Google are not really
software literate ... yet. But the clues are there. In the excellent
SRE book (link) author (link) the "founder" of SRE in Google, defines
SRE as "SRE is what happens when you ask a software engineer to design
an operations team".  As we go forward we shall find the software
literate companies are what happens when software engineers design
(found, run, populate and evolve) companies.  The flush of unicorns
today in Silicon Valley are nearly software literate - the effort of
founding a company is so huge that it's hard to believe that what
results is what a software engineer would design. Things get missed.
But each generation of companies will steal from previous until the
majority of a company is what would be designed.

Does it make a difference - well let's compare the old "knowledge
company" and the new. In 2012 `Google` had a revenue of $50bn and a
workforce of 40,000 - whereas the finance house `Barclays
International` also had a revenue of $50bn, but a far larger workforce
of 120,000.  Fast-forward to 2016 and `Google` has grown to $89bn and
70,000 people.  In the same year of 2016, `Bank Of America` posted
revenues of $89bn, and a workforce of over 200,000 people.  There are
many caveats comparing these numbers, but all the firms involved are
resolutely "knowledge-based" - the core processes of the firms do not
involve smelting iron ore or manufacturing cars.  And yet `Google`
carries 2/3 less humans for same revenue at each stage.  One of them
has used software in a markedly different manner.


Just what is a programmable company?
------------------------------------

(image of dutch 16th century trader pointing at his accounts books)

My conjecture is that we are hitting a limit on what tracking company
processes through accounting can do to limit wasteful (coase)
growth. That by forcing more reproducible processes into

And this is my definition of a programmable company - where all
processes are visible in the virtual world

The brilliant mid-twentieth century Economist `Roald Coase` gave us a fascinating
way to model why companies and organisations are the size they are - a Theory of the Firm.
We shall dive deeper into this later on but as more and more processes become visible in
the virtual, as we practise 'topless computing', then we shall see dramatic shifts in
the size and shape of our organisations.

We are already seeing calls for the software industry to regulate
itself, on privacy, on deals with repressive regiemes.  The answer is
not as simple as coders all being nice people.  But society needs to
regulate and also accept change.  We shall see that in section 2.

But companies, governments and organisations of every stripe, will need to adapt
to a new set of technologies that have a grain, a direction of travel, ... a tidal force.
Those techologies are here now, and our old organisational structures are no longer
sufficent.  

Lets look at it this way - Facebook, if it took all 1.5 BILLION users
and moved to a new land mass would be the worlds largest
country. Ever.

And it would be the least democratic. Ever. A one man dictatorship. No
law courts, no police, no constitution.  Nada.  And yet every Facebook
app-using citizen would have more daily contact (what 3 hours a day?)
with its "government" than they ever had with their proper governments.

Each day we see some new controversy, YouTube failing to police its
comments section against paedophiles, (find more examples).  This is not because
Facebook is inherently evil, but because we are moving our lives online - and
some people moving online are inherently evil. [#]_

So companies, governments, organisations, the structures we all spend
so much of our lives wirking within, need to change to get the best
out of the new technologial opportunity we face.

Because it could be a golden future for humanity.  Honest.




.. [#]:: OK, you might need to know a tiny bit about my political
      stance, which can be described as nice fluffy Euro-liberal until
      we look at Child Protection and I take a stance that makes
      Gengis Khan look forgiving.  Anyway.
================================
From literacy to programmability
================================

.. pull-quote::

  "Writing is nature’s way of showing us how sloppy our thinking is."
  Leslie Lamport


I very happily recounted my "Literacy started with the printing press,
software literacy starts with the Internet" meme in the last chapter.
I was rather proud of my little self, right up until I attended `Sprint 16`
the UK Government's annual conference on tech and software and government.
And the Minister for the Cabinet Office stood up and gave a keynote that
was basically the speech I gave so many years prior in a London pub basement.

Nothing stops you feeling smug like national politicians spouting the same ideas as you.

But the thing is, we are both right.  Although his suit was better. 

The first mass-literacy revolution ran roughly in parallel with the
Commercial and Industrial Revolutions in Europe.  But apart from the
usual things we associate with literacy, things like sharing ideas
widely, democratic access to knowledge and so on, the one that is
often *missed* is that ideas have to be much more precisely expressed
when you write them down.  If you go around making speeches, each
person can walk off with different ideas as to what you said but
writing it down means it is waaay harder to mistake what you meant.

WIth software this applies to the n'th degree. There is no longer any
forgiving human mind in the way of your writing to work out what you
really meant. Software is unforgiving. The compiler will do what you
tell it.  And this means we shall have to write down what we really
mean.

This is going to be a problem.

- self driving car issue
- access to agorithms
- gorillas AI

Some computer vision AI software failed to see black women as human
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




When it goes wrong
==================


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

Sweden Mistry Transport
-----------------------
So just as we thought OPM was bad, the Swedish Government stood up, looked the US Feds in the eye and said, "Hold my beer"

https://www.privateinternetaccess.com/blog/2017/07/swedish-transport-agency-worst-known-governmental-leak-ever-is-slowly-coming-to-light/


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

Equifax
--------
Equifax is worse - waaaay worse because in this mucked up world of mothers maidennname 
they alga every away all the answers. God knows what the effect will be but unless the swedes shoot the manager and Equifax goes out of business then we will never fix these security issues


You want security in your company - fire the head of the CIA if he can't keep his affairs secret. Fire people who breach secrets. Otherwise stop worrying about it 


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


Not agile - use rfc based development

Not agile - North Korea - turns out that for most engineering problems, if you kill middle mangers frequently enough everyone else stops talking to spies and works hard

========================================
What I cannot create I do not understand
========================================



.. figure:: http://static.duartes.org/img/blogPosts/feynmanLastBoard.gif

When Richard Feynman died in 1988, his chalkboard at CalTech contained
several notes, including the one that has struck such a cord with me

::

  What I cannot create I do not understand

This says *everything* I want to say about why Open Source Software is
important, why re-creating the existing work is important, why open
and transparent - ness works, why things need to be evovled not designed
and why, we cannot understand everything.

It takes a genius to put all that in 8 words.


So, what can be extracted from eight words.

* Build from scratch
* Open Source keeps re-inventing the wheel
* software is evolved
* relax.

Build from scratch
------------------

One of my software development tenets is you should be able to *build
your whole systems from scratch*.  That is given bare metal hardware,
get up and running, not from a few lucky backups and _dd_ but from
controlled scripted installs.

I have always thought this vital - without being able to (re)create
your systems, how do you know if you can in a disaster, or more
importantly that you can when it is not a disaster.  ITs impossible to
believe that the first time you installed your webserver you got it
perfect, first time, but if you cannot rebuild it with confidence, you
just will put off rebuilding it again and again until it is a mess of
libraries, patches and symlinks that you could never hope to remmeberm
nor worse, simplifiy.  Now expand that to your DNS, file server, your
database.

But being able to run a simple script, and the system is configured,
that makes life so much simpler.  I can read the script and see what it
will do.  I can change it, experiment, confident that I can just rerun
the original and get back to where I started.  And I can run the script
and go do something more interesting.

And no, I do not believe in _dd_, _ghost_ or other image based
methods.  Yes, they are very nice for Virtualisation, but always there
is a flaw - to get to an image, one has to build the original.  If you
build the original by hand, how do you know what steps you took - how
sure can you be? The Sysadmin was very careful?  Was he? Thats nice.
Oh look a new patch is out, and we no longer want to use version 5.2.2
of php and can we put the incompatible library onto only half of the
hosts.  Can you rebuild all of the images to do that, by tomorrow?
Still going to be careful are you?


Build from scripts, from scratch.

And you know what, I finally worked out why I was so insistent on this,
in the face of others desire to take the easy route.  Quite simply because
I did not understand a system till I had wrestled it enough to automate it.

You find out where all the gaps are when you try and automate a system.


Re-inventing the wheel
----------------------
I am (re)writing a ER diagramming tool, for about the third time. This time no
funny copyright issues with my employers, I swear.

But there are many ER tools out there. And there are many languages, databases,
games and more.  This does not stop us from writing another, just as
the existence of a Haynes car manual does not stop people from taking their
car engine apart.  We do it because we do not understand, and we want to learn.

Sometimes, there is an itch to scratch.  But often the itch is for knowledge,
and the desire to know if we *can*.  Benefiting the rest of the world is what we
do to share our knowledge.


Evolution
---------

Because we have to re-invent the wheel to teach the next generation,
we tend to incrementally improve.  And that is a slow evolutionary process.

Software *evolves* to fit its niche.

Relax
-----

I am sometimes troubled by comparing myself to some of life's winners.  But
looking at Feynman makes those comparisons silly.  A genius that other genius'
thought a genius, he still tried to understand this strange world we live in,
and had no more a grasp on *why* than the rest of us poor schmucks.

So, we do what we can.  And move the world on a little bit.  Some more than
others, I must admit, but I am happy to be pushing it in the right direction.
==============================
Price of gold is fairly stable
==============================

------------------------------

I do love me a bit of Ancient Rome.  And I love the term Solid - it came from the solidus, a gold coin minted by Constantine 315AD

Domain have done some amateur digging and will try the following: in Neros day 2 denarii would buy a Modius, which was sufficent grain for ten days for one average male (two one pound loaves a day, there is a diet to make wheat intolerant weep)

Now the aureus was replaced by the solidus, but it was about 25 denarii.  So we can say that one gold coin bought you about 100 -120 days worth of basic food.

A kuggerand is about four times the weight of gold as a aureus, and it's about £1,000 to buy today. And at £3 per day I could carefully feed myself.  Certainly in bread alone.

So over nearly 2000 years, a gold coin is roughly enough to feed one man for three months.

Fascinating

Biblio
------
- http://www.forumancientcoins.com/dougsmith/worth.html
- https://en.m.wikipedia.org/wiki/Aureus
==============
What a foul up
==============

==============
(this is posted here because I can't post over 2000 characters to HN and I wanted a bit more space)

So, I made a dick move yesterday. I misunderstood someone's comment (or I misunderstood their intention) and ... well @dang accused me of racewar and something about stone tablets and science.

I was of course outraged and reacted. Then a minute later I took a deep breath and reacted better.

We all value our reputation and having a judgement so clearly divergent from my own self perception has caused some internal reflection.

You see, there is an old joke about the definition of a liberal - a conservative who just got arrested.

Looking at my self in the mirror, I still see a sensible well balanced person, with strong liberal tendencies (who has worked at the UK version of ACLU, organised anti-intimidation watchdogs at voting booths in racially charge elections in London, and so on - things which while true when repeated here they still sound hollowly like "some of my best friends are")

I am sure dang and the other hard working moderators see a lot of crap in their job.  I am of course *certain* that that was not what I meant - who me?

Except that one thing middle age teaches you is that, quite often, it is you.

So yes, when someone arrives with a Vote Trump T shirt they probably do not find HN an easy place to discuss things in the terms they usually use.  And they will I am sure always protest "but it was not me, but what I said was perfectly sensible debate / free speech, how dare you accuse me like that, gosh you should treat people better around here, I am off to Breightbart"

But just like the recently arrested conservative I want to say just that (well not the breightbart bit obviously, but I certainly felt ill-used. Especially the bit about "other breaches of the guidelines in my previous history". Yeah gulp. I have asked for a list - in my case because I want to analyse and improve. Clearly those other cases where people ask they are just indignant)

But no matter what, I have been sorted into the basket of deplorables.

- Did I make a mistake and step down the slippery slope thinking I had good grips on my shoes?

- Did I not notice the slope?

- Am I actually deplorable?

- Or is it all the fault of those evil moderators ?

Actually this last point is not fair. I have reread the post and - I really failed to convey my thoughts. What is posted there is ... a horrific comment. (I can remember what I meant. I can see where I missed out indicative punctuation. But thats not the point is it.) Totally not what I meant and hopefully would never ever think. But someone I respect has come back with "well thats not actually out of character for you Paul.  We were thinking of banning your account for some of the stuff you have said".  That has shaken me deeply and I would like to know what has lead them there.  And how can I adjust my public statements to better reflect me.

So I herewith apologise to everyone on HN or elsewhere for posting text that reads so horrifically. Even if I did not mean it, I still wrote it.

I also need to think about why I post stuff too quickly, why I chose such am inflammatory subject to post on anyway, and why I did not review.

Fewer words. More thought.

I am going to take a bit of a break.

I have spent many years on HN (and am probably a little too anxious to be this close to 10,000).

Apart from satirical news shows on radio 4, it's my main source of information on the world. (This may of course not be a great thing.)

So a break is called for - I check too often, and while Facebook is often criticised by us for its addictive-like properties, I still obsessively check HN morning and night and am sooo close to 10k and my last couple of submissions did feel more like testing the reactions for points, not sharing something.


(Actually re-re-re-reading my offending post I can see I meant to put a question mark (or more ??!!) at the end of the first paragraph - so a challenge to the poster looks a lot like a statement of .. oh fuck me what a disaster.  I was remembering what I meant, not reading what I actually wrote.  It really does read like a trolling post - I can quite see what happened there.  But the "other posts violating our guidelines" indicates its a good time to take a break till I have processed things.)

Start here: https://news.ycombinator.com/reply?id=13010342&goto=threads%3Fid%3Dlifeisstillgood%2313010342

I am sure cold turkey will last a day, maybe a couple of weeks.  Please don't discover working fusion power while I am away.  I really want to comment on that.
=================
Tendency to guess
=================

Sat scores and scoring penalty
Katherine Kauffman Harvard business chill

Code reviews should be based on performance metrics

Engineers do not judge bridge changes based on style guides

Choose based on metrics - means we need metrics


https://www.theguardian.com/books/2003/oct/18/features.weekend
Braben and bell wrote elite. And their life stories are the prototypical coder life goals - build a business of coders or withdraw and focus on family. I want both - and that day's a lot ==============================
The Journey of Mikado Software
==============================

==============================

The journey to freedom
----------------------

I was made redundant in 2008, from a nice CTO job in London's City, at the
height of the financial crisis.

Now, I have worked in the "Internet Industry" since 1995.  Yes I am that old.
And I have done most jobs, from CTO to consultant, Developer to DBA.  I ran some
of the UK's first ADSL trials back when 14.4 modem was a big deal, have written
software for the FTSE100 and the footie club.  And so I decided not to take
it lying down.

Two weeks later, I walked into a new contracting job, and I hustled, and hunted,
worked my way up the salary ladder, started my own consultancy and landed the
*big gig*.

It was the worst move I ever made.

I sat in a car for between 2 and 4 hours a day (and I never knew how long the
trip would be).  And I was not curing cancer so I could hardly claim my work was
worth the sacrifice.

.. figure:: /assets/images/m25.jpg

I saw my children only when they were asleep, or at weekends, when I was
exhausted. My wife saw me for about ten minutes before we climbed into bed and
slept shattered.  It put strains on my marriage and our kids.

And I put on nearly two stone.

So, as that contract ended, I swore to stop.  I did not need to actually be in an office, watched to see if I was slacking off.  I could work remotely, from
anywhere, for anyone.

And things turned a corner.  I was able to walk into
work, able to make breakfast for my kids, let my wife have a lie in and a cuppa.[#]_

It is not heaven, bills still need to be paid, relationships repaired, the office is tiny.

But like nearly 3 out of 4 workers, my job does not need to involve me
travelling to the same office as everyone else.  Nearly 75% of us could do the
same job from *anywhere*.  And we could do it minutes from our families, our
lives.

The more of us who make that break, who escape, the more our societies will
shift.  Till raising a family stops being a struggle that tears us from being
productive in work.


The journey for freedom
-----------------------

One of the defining characteristics of the next decade of the Internet is
the vast, vast amount of data that will be available, and the new insights
that data will afford us.  But it is too much data for any one company to
own it and use it.  All the pharamceutical companies will need to share their results to find the next break throughs, all the financial companies will need to
share their trades to avoid the next crash.

Data will have to be *open* to be *big* and with that will come the open software to handle the data, and the open forms of working (like above) that will
be used to write the software.

And this is my second journey - I am a `passionate believer
<http://www.oss4gov.org/manifesto>`_ in the role of open source in public sector
software.  Mikado Software is driven to put high quality, open software into
government and public sector hands.  We are not a lone voice, the new NHS Spine2 will be built on the open source Python language (a speciality of Mikado) and the Government Digital Service is not just revamping websites, but pushing the
very defintion of Open and Agile into the heart of UK government.

Journey's End
-------------

I care passionately about my family, which makes me not unique.  I also care
passionately that governments, councils and citizens all have the right to read
the software that more and more runs our lives.  The right to read it, critique
it, and one day remove the offending code.  Just as we do with our written laws
today.

Software matters now, and will matter more in the future.  It need to be kept
free and open so the laws that run our lives are as accessible as the laws that
govern us.

Mikado Software is the end of two journeys, a company that treats work that can
be done anywhere as an opportunity to work anywhere, and a company that creates
the future of public services.



.. [#]   (I am pretty sure I am supposed to get the occassional lie-in too, but she says it's in the marriage contract.  Subsection B, paragraph ii. I'm scared to look just in case.)
=================
Topless computing
=================

(June 2007)

Not nearly as much fun as it sounds
===================================

The other day I was asked by a member of staff if it would be possible to tie
the holiday spreadsheet into the master workplanner application.

Now *possible* is a horrible word for IT people, because it is *always*
possible.  Its really a question of is it a good idea.

I said, well, not until the holiday recording was taken out of spreadsheet form
and put into something that was less ... topless.

Yes, I got the eyebrow reaction.

However it does make sense.  We do not know what the future is going to hold, so
it is always sensible to put our data and code into a form that makes it easy /
simple / feasible to build another system on top of it.

In other words we should build our systems to be **top-less**.

Of course, like in the real world, there are varying degrees of topless.  A
spreadsheet is possible to extract data from.  Perhaps I could write a
Python-server that looked at Excel at one end and spat out HTML / JSON the
other. But then I need to map employeeIDs between excel and this other thing,
and write some interpreter for the weird way the spreadsheet deals with time,
and it would probably be a good idea to cache the dates for speed, which means a
storage engine, and by this time I have written yet another half-assed
application, that still does not handle half-days sick, nor talk to the payroll,
nor know anything about regulations.

But to get rid of it will mean *me* going off finding a list of decent payroll
applications, and asking if they are topless.

Which always makes for a fun phone call.


To me **topless computing** is really, truly **user-friendly** software.  But by
that I assume there are computer literate users being considered.  Because
user-friendly does not mean it has a nice UI, it does not mean it has predictive
text.  It means that when I want to extend it, it does not get in the way.
(Some describe this as difference between *plumbing* and *porcelain*).

If all users could write source code, all programs would be topless. Or at least
have easy to remove bikinis. [#]_ And that is ultimately why I go around talking
about topless computing.

Because it sounds naughty.


European topless computing directive - the idea that this accessibility needs to be enforced as a competitive need. Owning up banking like PSD2
Making personal data geneuninely owned by the person and making the computing substrate accessible and open - thinknautomatic cars



.. [#] OK, yes this is a bit sexist.


Software as capital 
Capex
Software as infrastructure 
Now it is capital each should look to standards to enable not mere reuse but composability - look to stripe and Patrick m 

A Useful theory of software engineering
(Adolph / Kruchten) - a good over view - basically it's a social process over the whole of the developer community - making the community of developers an important thing to manage - an implication not merely for large open source projects but indeed internal engineering teams.


================================
Why Am I writing these articles?
================================

================================

Something about tech needing to be for the 100% not the majority only - http://www.cracked.com/article_24934_5-ways-technology-can-unintentionally-become-racist.html

Whilst my daughter usually asks "Why are you singing like that?" (the answer to
which is "I am tone deaf darling") there is a simpler reason for writing a site
like this - I have reached the age where Homer Simpson is becoming a model of
clarity and reason.


.. raw:: html

   <iframe width="420" height="315" src="//www.youtube.com/embed/8dbDJzDV1CM" frameborder="0" allowfullscreen></iframe>


Basically, I need to get the old stuff out of my brain and down onto paper, or at least blogroll, so I can go and
have fun learning some new stuff.

I hope you enjoy what is getting pushed out of my brain.  I also hope it helps you.

I am trying to guess what
they will look like, in the same way a scribe in a Medieval
Scriptoreum could try and guess what Woodward and Bernstein's
Washington Post would look like.


- :doc:`conceptchapters/dm_plumbing_ci`
- :doc:`conceptchapters/sm_firms_coase_democracy`
- :doc:`conceptchapters/dm_projects_tickets_todoinator`
- :doc:`conceptchapters/dm_townplanning_goverance`
- :doc:`conceptchapters/dm_fractal_management`
- :doc:`conceptchapters/sm_pikkety_social_regulation`
- :doc:`conceptchapters/dm_team_morale_trust`
- :doc:`conceptchapters/sm_futuresoftwaretrends`
- :doc:`conceptchapters/dm_culture_people_process`
- :doc:`conceptchapters/conclusions`
- :doc:`conceptchapters/landscapestrategy`




A point about Company Size
--------------------------

OK, this is meandering a bit but, company size matters. A mid-20C
econmist named Roald Coase had a great theory of the firm - basically
wondering why a firm would have say, an internal depratmetn for, I
dunno, say, market research, when it could go to the outside markte
and buy it in.  Why hire employees basically.  And the answer is its
easier to tell an employee what to do, and then change your mind as
circumstances change, than it is to find, source, and contract for
similar in open market.

A lot is changing about this.  From Virtual assisitants to others.

But downward sizer pressure exists.  (see note on Google / Barlcays)

A point about Software Literacy
-------------------------------

* Software Literacy is an important concept - it is hard for us to
  recongise how literacy has shaped us and our society. Look at road
  signs. And it is hard to recognise how much software literacy will
  change companies, socieites and opportunities.  This is the
  underlying message of "Software is eating the world" - we have made
  a world that only works because everyone in it can read and write.
  We are making a new world, where everyone will be expected to code.

* Software is subject to politics, but the importance of software is
  leaving development of softre to be driven by people who do not
  "understand" software (see literacy), and it is also leading to
  substandard software being allowed.  Regulation and
  professinalisation is likely to affect that.

* Almost all software development is about exploring.  And two things
  we can say about exploration - you never know how long it is going
  to take and it often is risky.  Guess what the vast majority of
  project planning and management try and do They demand time
  estimates and plan other items around that, and they do not schedule
  resources to mitigate risk.  In my experience, software takes as
  long as it takes.  All the running around and shouting, the pressure
  and the politics are just ways of selling the inevitable time /
  money / scope trade offs.

* Software literate company The value of building good software as a
  company
  tps://www.ben-evans.com/benedictevans/2018/8/29/tesla-software-and-disruption


A point about the Google Peace Dividend
---------------------------------------

* The Google Peace Dividend - three / four major areas of computing
  beig transformed by OSS - ML/AI, data processing pipelines, virtual machine management,

A point about Pikety
--------------------

* Pikety redux

  - Labour lost, capital won (the reaosn wages not  subject to suply demand)
  - the great hollowing out
  - literacy and automation
  - Snowden was also right - data and pollution 
  - snowden
https://en.m.wikipedia.org/wiki/NSA_ANT_catalog
http://www.nsaplayset.org
- Whats happening in the world - a sense of perspective
* http://www.digitalattackmap.com/faq/
* also want, wars, trade, shipping, energy, employment, poverty, investment etc.* 
some kind of model / mapp for the whole world. where is the money flowing / going?


  That the record of software coming in to disrupt industry is good -
  it's hard to learn software.  As a company this book is about having
  software in your company DNA

A point about project management and democratic companies
---------------------------------------------------------

I am going to stick my neck out and go for it - companies will become
more democratic - we shall see more voting and consensus in the
workplace.  We will also see the end of deadlines as companies become
*event driven* - that is, instead of shouting "get to this point"
there will be more "we need to get here" and monitoring and
encouragement.


The problem is *always* at the top
----------------------------------

Most technical problems can be solved by changing the business environment.
If the security of a company is challenged because a top level executive refuses to follow
the security restrictions, then there is a clear choice betwene firing the Sales Director
or having security.  Only the Board can decide that, and once they do it must be clear.

Google is currently experiencing a similar issue over sexual harrassment.

Data publication




Fractal Management
------------------

How individuals and teams need to model, monitor, mentor.


- CI and repeatability
- reporting on functionality of running processes
- analysis of inputs, running, outputs
- reporting upwards and outwards
- marketing your code





security (secrets management & auth)
------------------------------------
-- user management / aithentication authorisation
-- FIDO


security (deployment / repeatability)
-------------------------------------


prod parallel
-------------
Modelling



-- plumbing






The Metaphor of Building Software
=================================

Discuss "The code is the design", and the DevOps idea of code for
everything.  Look at building site in City of London

The office building metahpr is a good one because it also includes a
clear idea of just how much is ocvered in software build chains these
days - from Steel girders and foundations to Glass UIs and bathroom
and waste services in conduits no one sees, to building security and
power outlets.  These things are beasts, and software at even mid size
enterprise scale is a beast too.  Hence my focus on *governance* as
well.

Technical Architecture
----------------------

There are lot of "Technical Architects" around these days.  (One of
the problems with not having a software profession the same way we do
in actual architecture is its hard to stop people calling themselves a
Technical Architect. (I mean, just look at *my* business card ...)

A stereotype of TAs is of isolated geniuses (at least they hope to
give that impression) announcing the correct way to build software to
a large team or organisation.

The problem is that if no-one is following yourq architectureal rules,
then you arent an architect.  Architecture is a human function,
persuading others that your way is better.  SOmetimes, we *enforce*
that - through Software Governance (an important idea we will return
to) In the same way that an Architects design for a building is
followed by the builders, or a City Planners rules for a City are
followed by all agents involved.

With a metaphor of building cities, we can see why the idea of Architecture is
an attractive one, but it is really at the scale of the biggest software houses
in the world (Major Banks and financial instituions) that you can see the incredilbe
value of ... City Planning.  We shall call this Software Governance.

A point about Software Governance
=================================

There is a software rule of thumb - that code-bases pass through
'complexity horizons' every couple of orders of magnitude. That is a
project that was easy to manage at 1,000 LOC cannot be maintained with
the same approach when its a 10,000 or 100,000 LOC cadebase.

Pieter Levels is a entrpreneur and coder, who found a certain
noteriety in 2017 by announcing that he was making sales of over
$2,000 a day, using a single php file with 4000 LOC, with no
frameworks and libraries.  The Twitter-sphere exploded, quite
amusingly, by criticising his coding approach and insisting he needed
some architecture and frameworks.

.. pull-quote::

   "What about the frameworks. Think of the frameworks"

Pieter seems to be doing fine his way, but yes, at some point the 'one
guy opens up one file' approach is of course going to fail as
complexity rises.  But managing it with the latest technical framework is
not the right answer - a technical framework is one response to the problem
of increasing complexity, one means of *governing* the codebase.

How we manage that is *software governance*.  The goal of software
governance is to raise the floor everywhere.

We can write code, we can write code that gets us to a basic level of
feature complete-ness.  And then the next fire alarm arrives, the next
email from the boss, and ... the polish disappears, the extra bit of
effort to make something long term useful just does not get done.

But that extra piece of effort can pay dividends just for one
developer.  For a team or a whole community, the dividends are
endless, just by raising the floor of quality.

In `todo-inator` I have a concept of self-rating each module or
function with a modern form of P.G. Wodehouse's re-writing of
chapters.  This simple mark::

  pgw: **

While this is a subjective measure from the developer, it is a guide
to where improvements can be made.  And importantly resides in the
codebase.

Other measures of code quality can be autoated and should be part of
every commit cycle.

:doc:`chapters/best_approach_to_software_quality`

Code base governance
--------------------

Style,
coverage
ast based syntax checking use of non-standard plumbing
`Code as a crime scene`
Static Analysis and raising all boats.
ast
and how to do syntax checking like pyflake - how to build own rules



- :doc:`chapters/application-performance-management`
- :doc:`chapters/systemd`
- :doc:`chapters/technical_capabilities`
- :doc:`chapters/terminal`
- :doc:`chapters/testing`
- :doc:`chapters/text_mining`
- :doc:`chapters/sphinx`


.. toctree::

   chapters/sphinx

A point about Systems governance
--------------------------------

SRE / building for failure (Erlang and OTP)
this is monitoring running systems.  Things like approvals, security etc.


Managing the lifecycle
-----------------------

Application Lifecycle Management
Gov Service Design Manual




A point about Simplicity
========================


Our golden goal is to keep things simple.

Simple breaks in simple ways, simple is simple to extend and improve.

Its not that simple is *easy* - often it is the opposite of easy, or quick.

But simple wins out over time. Simple gives great ROI.

I throughly recommend listening to Rich Hickey on this subject (Link)

So please keep in mind - we aim for simple.  Even if our day to day
work pushes us to quick and easy and complicated.  We need to push
back.


Data Mangement  Philosophy
==========================

Data Publishing needs to be a business level function, providing
consistent accurate and timely data to the rest of the organisation is
a vital task.

Like Bezos, can only consume data that is published - and people only
publishbsokething they willing to support

"but i cannot get my job done if "... that's not the problem ... the
problem is clean data

it's like security - it's a priority or it is not.


Workstation
===========

The project mikadosoftware/workstation is the best point to discuss a
develoeprs workstation.  A while back I realised I was spending waaay
too much time altering my worksttion - as an itinerant developer /
contractor I would effectivety be a bum on a seat (in many senses of
the word!).

So I have taken some time to define a repeatable workstation process.
Its not ever going to be perfect but at least it is a valuable start


Workstations are part of overall plumbing.





Plumbing
========

Every software project of any size needs some basic plumbing, things
like a good config approach, a means of linting and testing.  These
things pay dividends throughout the lifetime of a project, making the
simple easy and the hard doable.  WIthout it, you are in trouble.

  
  - :doc:`chapters/errors`
  - :doc:`chapters/config`
  - :doc:`chapters/sphinx`
  - :doc:`chapters/metrics`
  - :doc:`chapters/backup_strategy`
  - :doc:`chapters/logging`
  - :doc:`chapters/metricsAndTracing`
  - :doc:`chapters/network_monitor`

- Runbooks and monitoring


Plumbing
-----------------

The goal here is not best practise, but good enough practise that can
scale enough for you not to panic while replacing it.
Our golden goal is to keep things simple.

Simple breaks in simple ways, simple is simple to extend and improve.

Its not that simple is *easy* - often it is the opposite of easy, or quick.

But simple wins out over time. Simple gives great ROI.

I throughly recommend listening to Rich Hickey on this subject (Link)

chaos engineering 
http://principlesofchaos.org

KISS
http://widgetsandshit.com/teddziuba/2010/10/taco-bell-programming.html
there is simple, and there is too simple to easily manage and monitor. 

pentesting and adversarial security
https://www.trailofbits.com
black hat python
the simple ones still work
AES based oracle 


- microservices
- CI / CD
-- metric capture and operations management 
testing
linting and commuting and pre commit hooks
governance
simple worker queues
simple load balancer
simple kubernetes / DNS etc
simple js client 
simple web server 
simple user management 

    
    
Continuous Integration (CI)
===========================

.. pull-quote::
   
   Re-create your company from scratch, every single day.

   
Continuous Integration / Delivery is probably the biggest boon to developer produtivity
since the rise of memory managed languages in the 90's.

Languages like C expected the developer to write code that assigned a
certain amount of memory for a certain data structure - which meant at
the point of writing your code, you had to know *how big the data was
going to be, in say two years time*.

People would get this wrong.  The biggest security risk for many years
was your program accepting a piece of data larger than expected and
simply overwriting its own memory.  With luck your program just
crashed.  Otherwise the hacker was very good, and the piece of data
sent just put their evil code on top of the stack ready to be run.

Nowadays, the business logic we grind out does not need to worry about
such things.  Instead we have the fun of not being entirely sure if
the version of the code we think of is going to run on the server with
the code we think of, using the password we meant and thats if no one
else changed anything.

Lets call these build services.



- :doc:`chapters/environments`
- :doc:`chapters/continuous_integration`
- :doc:`chapters/using_docker`
- :doc:`chapters/sharing_secrets`
- :doc:`chapters/packaging`
- :doc:`chapters/pep8`
- :doc:`chapters/writing_docs`
- :doc:`chapters/random`
- :doc:`chapters/reporting`


 

  
Security
========

Security is principles that are applied across the system. PKI, etc.

Basically trust the maths, and trust nonces.

* :doc:`chapters/ch1 security`
- :doc:`chapters/cookie_testing` #security
- :doc:`chapters/network-testing`
- :doc:`chapters/personal_security`
- :doc:`chapters/pki`
- :doc:`chapters/pkis`


Pki
Cloudflare how to build your own
https://en.m.wikipedia.org/wiki/Hardware_security_module


* GPG and keypairs
* host based security, networks of trust between hosts,  and DMZs
* Kubernetes / Rancher as a host / VM world 

Configuration management and secrets
====================================

Use etcd / kubernetes.
How to build own Docker based co-ordination service - or why kUbernetes is nice.
My USB Secrets

(also Google Peace Dividend)

Testing - a heresy
==================

Rick Hickey on simple vs easy
  How does a bug get into production? It is written
  And it passes the tests.  So if you have tests, and you refactor, how
  do you prevent that bug?
  Need to be able to *reason* about code. Which is why 900 npm packages worry me.

  Tests are *regression* tests. They are written so that having written some code to
  do a thing, you dont later on screw it up and it stops doing that thing.  Tests are
  almost by defintion, backwards looking.

- :doc:`chapters/unittests`
- :doc:`chapters/browser-automation`
  

DevOps
======

Falls naturally out of Microservices owned by Small Teams, with Strong Interfaces
SRE and SRE book.
Start small, keep whole thing in overview
Use graphite, and just report out, graph 10 important things
to your team *today*.

* :doc:`chapters/graphite_docker`



Basic Management Reporting
==========================

* reportlib
* SLAs and KPIs - keeping ourselves honest
* focusing upwards to higher levels of leverage
* avoiding the drumbeat of deadlines, and panic, and agreeing goals based on
  data / 20% most effective things to fix.
* Make one weekly report *today*


The scope
=========

How much software is there

https://news.ycombinator.com/reply?id=17994976&goto=item%3Fid%3D17994600%2317994976
https://www.theatlantic.com/technology/archive/2017/09/saving-the-world-from-code/540393/

the google peace dividend
https://news.ycombinator.com/reply?id=17996693&goto=item%3Fid%3D17995053%2317996693

Data schedulaers /  Processors / BigIsh Data
Apache Beam
https://stackoverflow.com/questions/43581127/what-are-the-benefits-of-apache-beam-over-spark-flink-for-batch-processing




Soft Skills
===========

Skills for individual developer
===============================

Software Governance as a force multiplier implies a number of things
One is that each individual contributor should have the same minimal
set of skills, and perform those common skills in a similar fashion.

An obvious example might be making good source code commits, and so there
would need to be an internal "standard" for commits. 

This of course implies ... training. Training your staff to be better
at their jobs, something that the commitment-less culture these days
seems to mitigate against.  Things will change - our "principle" of a
change to Roald Coase's equilibrium point means smaller companies, and
greater need to standard interfaces and so more need to train your
people to do it the right way.


You are not a programmer
product engineers not software engineers 
https://blog.intercom.com/run-less-software/
Three circles of leverage


Profesional Stuff you should know 
---------------------------------


- :doc:`chapters/jupyter`
- :doc:`chapters/kernel_and_world`
- :doc:`chapters/misc`
- :doc:`chapters/statistics`
* :doc:`chapters/sourcecontrol`
* :doc:`chapters/keypairs`
- :doc:`chapters/databases`
- :doc:`chapters/DNS`
- :doc:`chapters/email`??
- :doc:`chapters/source-control`    
- :doc:`chapters/using_burpsuite`

Actually personal stuff

* :doc:`chapters/careermanagement`
* :doc:`chapters/interviewQuestions`
- :doc:`chapters/interviews_algorithms`
- :doc:`chapters/basic_seo`

Misc
- :doc:`chapters/generative`


Esprit d'corp and Team honesty
==============================

Hiring practises - be part of the team
Entry hurdles. 
start with feedback - sprints and retrospectives
Be aware of your priviledge
Begin the difficult conversations publically 
be aware of the likely problems - metoo is just one.

then aim for the culture you want - 

then hire good people


* Culture, and hostile cultures
* trust, safe space, I dont know
* learning
* lunch
* Keep on in good faith
* Google HR managemenet
* management fixes are the middle ground - 


* serverless is cheaper. Please rewrite everything now.
* Overtime is bad
* remote working is more productive
* Risk management beats project Management
  
- :doc:`chapters/software-capital`
- :doc:`chapters/software-estimation`
- :doc:`chapters/project_mgmt`

Project and Programme management
================================

So there is a well known story in the Agile world about `why estimates
are always wrong
<https://www.quora.com/Engineering-Management/Why-are-software-development-task-estimations-regularly-off-by-a-factor-of-2-3/answer/Michael-Wolfe?srid=24b&share=1>`_

Basically we cannot do it.  So why do people ask for estimates? They
dont want estimates - they want evenly spaced landmarks. They want
confidence that progress is being made.


It if ain't got a ticket dont work on it If it ain't possible to
rollup tickets you dont know where you are going A backlog out of
context is just a horror There is nothing wrong with top-down design
(see Linux) Backlog for the whole company - agile for the whole
company just see progress on a map.  If its not going fast wnough for
the board they can fix things at their level.


We need to track our work so we can provide an audit trail
THese are useful


Event driven Project Management
-------------------------------

How companies need to reactively plan, with exception / assert monitoring.
How this replaces "managment judgement" with clear budgeting.?


** Project Management
The Chairman's tricky Question
==============================

Some time ago I was asked by the Chairman of the Board what one thing
he could do to make sure all these damn software projects were under
control.

What he meant by under-control, was *on-time* and *as expected*. Which
is not what I meant.

So I had two answers.   One was under control from a development perspective.
This is pretty simple and  boils  down to 

* Require *every* project to automatically deploy to at least a prod-parallel
  environment, *every* day, their most recent approved, tested code
  and post their test results.

These seemed radical, but achievable.  A lot of the *technical* side
of this Dev Manual is focused on achieving this.

But the *real* point was about *on-time* and *as expected*.  And that
is where I gave an answer he did not like.

* Stop having deadlines.  That way nothing is late.

Yes.  You can see why it was not a popular suggestion.

We will expand on that, but I am going to stick to it.  I hate
deadlines.  They infect everything with panic and poor quality.  And
the deadlines are almost always derived from poor information about
reality, and where the deadline should be, and rarely if ever updated,
as if reality and poor estimation are irrelevant.

Its much better to have regular, reality-grounded views on where one
really is, and alter plans based on that.  Automatically.

Deadlines sometimes help. Mostly they do not.

If it ain't ready, setting the deadline to today won't make it ready.


- :doc:`chapters/agile_estimation`
- :doc:`chapters/SoHo1`
- :doc:`chapters/themes`
- :doc:`chapters/urljoin`
- :doc:`chapters/veryquickMBA`


CTO dashboards and Business Process Dashboards
==============================================

Dashboards matter
The basics of code quality can be in dashboard.
The basics of production health can be in dashboard
Putting a business process into dashboard is powerful - use Graphite and "light beam trackers"


- :doc:`chapters/aspell`
- :doc:`chapters/mikado-doc-manager`
- :doc:https://github.com/getredash/redash/blob/master/README.md




AWS and old school
------------------
- :doc:`chapters/aws_dns`
- :doc:`chapters/cabling_hardware`
- :doc:`chapters/filesharing`
- :doc:`chapters/freewifi`
- :doc:`chapters/highAvailability`
- :doc:`chapters/laptop`
- :doc:`chapters/loadbalancing`
- :doc:`chapters/mail-handling`


  
UI for idiots
=============


- :doc:`chapters/UIDesign`
- :doc:`chapters/ajax`
- :doc:`chapters/bootstrap_index`
- :doc:`chapters/building_bootstrap`
- :doc:`chapters/coloursfortheweb`
- :doc:`chapters/lessrest`

  

The dev manual - a proof of concept
===================================


Example Micro-Service eco-system


I want to have a detailed exmaple - so here is a functioning, internal and external
web based, docker based complete setup.

Docker AWS
----------

We shall build a complete enterprise service in the cloud - because we can

- :doc:`chapters/time_in_docker`
- :doc:`chapters/time`


This is a "business in a box" - it kind of does not matter what the
buisness is, its just that all the software engineering goodness
that I describe here needs to be ... dmeonstrable - so I have built a
example business (and launching a real product) with it.

Its WIP

* simplest app possible
* adding a unit test
* adding a performance test
* building it under python / distutils
* running it under systemd
* running dual, behind load balancer, using weaver/ansible/fabric
* building it on a build server, using .deb files
* build assets -> docs, perf results, test results, .deb files
* Security on microservice
* Identity
* host-host services (ntp etc)
* host-app services -> logging, TLS etc 
* central services - DNS, metric names,
* code reviews and code promotion
* metrics gatehrinfg
* log mgmt
* rolling out changes
* incident mgmt (incidents, SLAs, uptime measurements from metrics etc etc)
* adding message queues, backend services, passing back identiy
* adding dependancy services - monitoring everything
* CTO dashboard, mission control centre
* bug tracking, feature development

  
Putting it all together
=======================

* Simplest possible
  We shall build a working web app (about three lines, honest).
  Build it, test it, deploy it to a location locally, and log it.
* systemd, well-behaved services
* simplest app possible
* adding a unit test
* adding a performance test
* building it under python / distutils
* running it under systemd
* running dual, behind load balancer, using weaver/ansible/fabric
* building it on a build server, using .deb files
* build assets -> docs, perf results, test results, .deb files
* Security on microservice
* linting and style and code reviews
* Identity
* host-host services (ntp etc)
* host-app services -> logging, TLS etc
* central services - DNS, metric names,
* code reviews and code promotion
* metrics gatehrinfg
* log mgmt
* rolling out changes
* adding message queues, backend services, passing back identiy
* adding dependancy services - monitoring everything
* CTO dashboard, mission control centre
* bug tracking, feature development
* distributed file systems
  Cephfs, GlusterFS, Lustre, and HDFS
* work queues
  CElery, zeroMQ
* amazon, openstack



  
Micro-HowTos
============
(Misc)

- :doc:`chapters/corefile_debugging`
- :doc:`chapters/futuretech`
- :doc:`chapters/bothPythons`
- :doc:`chapters/emacs`
- :doc:`chapters/nginx`

- :doc:`chapters/gh-pages`
- :doc:`chapters/nonblockwsgi`
- :doc:`chapters/wsgi_simple_app`
- :doc:`chapters/wsgi_test`
- :doc:`chapters/wifi`
- :doc:`chapters/ssl-tls`
- :doc:`chapters/workstation-install`
- :doc:`chapters/workstation`
- :doc:`chapters/webdev`
- :doc:`chapters/webtest`
- :doc:`chapters/well-behaved-services`
- :doc:`chapters/using_github__ssh`
- :doc:`chapters/podcast`
- :doc:`chapters/postgres-cheatsheet`
- :doc:`chapters/pxeboot`
- :doc:`chapters/python_warts`
- :doc:`chapters/routes`
- :doc:`chapters/rssso`
- :doc:`chapters/samba`
- :doc:`chapters/securityoverview`
- :doc:`chapters/sed_sort`
- :doc:`chapters/seo-case-study`
- :doc:`chapters/Managing time in docker containers </chapters/time_in_docker>`










The top 12 practices - a summary
--------------------------------

Like Joel's checklist, this is a checklist for things you need
Its trying to get ot barebones


1. source control
   5 chars etc.
   but good example of using automated policy enforcement on checkin

2. tech debt and tech assets - code and tests
   "Lines of code spent"
   
3. requirements lifecycle (PEP)
   the wrongest part of the agile manifesto
   """ The most efficient and effective method of
conveying information to and within a development
team is face-to-face conversation.
   """
   
   Ya do need to write down the discussion.
   written Proof overcomes authority problems
    it is also way to get everyone discussing
    this only works with really co-locateed and mission focused teams

4. automated build and deployment (dogfood)
   Look, bash is just *fine*
   pyholodeck

5. Documentation and Marketing
6. openness and reviews
7. Progress Not Perfection (YouTube clip)
8. static and other analysis
9. performance mgmt and measuring everything (and making reports on everything)
10. Automatic project mgmt
11. Risk management
12. have fun, try new things, don't be afraid


Google Peace dividend and Distributed computing
===============================================

THe new capabilities

Kebernetes (the micro services as cattle)
Beam / spark - distributed parallelised computing - the new scheduler
Tensorflow - AI
(Serverless)

But underneath this we have basics of plumbing, philoshphy and so on




Software development methodologies
https://zwischenzugs.com/2017/10/15/my-20-year-experience-of-software-development-methodologies/


Future
======

the great cyber security rewrite(hospital and pumping stations)
the great project management model - tube of water at real time scale
the great company shrinkage - coase


https://allarsblog.com/2018/03/16/confessions-of-an-unreal-engine-4-engineering-firefighter/

Club
defence at scale
https://brandur.org/idempotency-keys


being better developer
https://news.ycombinator.com/item?id=16863591

i don't agree really - there is two kinds - being a master of anything
is mastery over self (miyazoko tea master) or specialisation is for
insects.  or rather you need experience of all the tools

i suspect he is just complaining that someone is hammering in a nail
with a hammer, then a screwdriver, then a wrench ...


One New Skill Evening Club
--------------------------

Functional Reactive programming and DAGs
-----------------------------------------

"out of the tar pit" marks/moseley - over simplified it says complexity is the problem in software, and there are two types of complexity - state and control.

A third type is information failures or shooting ourselves in the foot.  

There are then three fixes for the world

- functional programming for managing state (immutable data)

- but data does chnage - so how to handle it? datomic?? bi or tri temporality 

- functional reactive programming and dag - and what about SAC

apache spark is fundamentally one of these. which will win?? hard to say but my money is one language-data tie ups (erlang mnesia, clojure datomic)

https://blog.janestreet.com/introducing-incremental/
https://blog.janestreet.com/breaking-down-frp/

Basically don't waste time on recomputing
Which is why Vitrual don can be a dag


Why graphs matter. And who cares


Scope and coverage

- NoSQL and scale and distribution versus consistency 
- rise of functional languages
- the declarative language we all know - SQL
- datomic and clojure
- out of the tar pit (mosley and marks) - two problems are state and control - functional solves some of state but state of data changes.  how to handle changing data ? 
- bitemproarilty and tritemoorality - date we wrote it down, date fact was true, date we are querying about.

- Information management

- systems analysis 

- domain analysis

- leave me alone i am thinking

- stop micro managing 

- no you cannot have an estimate only a direction.  deadline? maybe. try a business solution

- do it smaller first 

- mission and process wins more often 

- ownership of small area wins as well.


Have a incident response book

Have a run book
- basic principle is automate the shit out of it



Software Mind
Moop and IOT
moop

My data collected on my behalf and analysed for my benefit - shared and communal benefit


iot fridge 
will allow my slow thinking to order for me this allowing me to win back control from the bio-hacking of large corps

Ethical Open Source

https://librarianshipwreck.wordpress.com/2018/08/24/striving-to-minimize-technical-and-reputational-risks-ethical-os-and-silicon-valleys-guilty-conscience/


Privacy - telcos / ISPs are worse

https://www.techdirt.com/articles/20180320/10281539457/if-youre-pissed-about-facebooks-privacy-abuses-you-should-be-four-times-as-angry-broadband-industry.shtml


#https://docs.typo3.org/typo3cms/extensions/sphinx/AdvancedUsersManual/RenderingPdf/CustomizingRendering.html




Articles
========

This is the articles linked above.

.. toctree::

    chapters/microservices
    chapters/serverless
    chapters/architectural_overview
    chapters/best_approach_to_software_quality
    chapters/application-performance-management
    chapters/systemd
    chapters/technical_capabilities
    chapters/terminal
    chapters/testing
    chapters/text_mining
    chapters/sphinx
    chapters/errors
    chapters/config
    chapters/sphinx
    chapters/metrics
    chapters/backup_strategy
    chapters/logging
    chapters/metricsAndTracing
    chapters/network_monitor
    chapters/environments
    chapters/continuous_integration
    chapters/using_docker
    chapters/sharing_secrets
    chapters/packaging
    chapters/pep8
    chapters/writing_docs
    chapters/random
    chapters/reporting
    chapters/jupyter
    chapters/kernel_and_world
    chapters/misc
    chapters/statistics
    chapters/sourcecontrol
    chapters/keypairs
    chapters/databases
    chapters/DNS
    chapters/email
    chapters/source-control    
    chapters/using_burpsuite
    chapters/careermanagement
    chapters/interviewQuestions
    chapters/interviews_algorithms
    chapters/basic_seo
    chapters/generative
    chapters/ch1 security
    chapters/cookie_testing #security
    chapters/network-testing
    chapters/personal_security
    chapters/pki
    chapters/pkis
    chapters/unittests
    chapters/browser-automation
    chapters/graphite_docker
    chapters/time_in_docker
    chapters/time
    chapters/software-capital
    chapters/software-estimation
    chapters/project_mgmt
    chapters/agile_estimation
    chapters/SoHo1
    chapters/themes
    chapters/urljoin
    chapters/veryquickMBA
    chapters/aspell
    chapters/mikado-doc-manager
    chapters/aws_dns
    chapters/cabling_hardware
    chapters/filesharing
    chapters/freewifi
    chapters/highAvailability
    chapters/laptop
    chapters/loadbalancing
    chapters/mail-handling
    chapters/virtualbox

    chapters/usbdisk
    chapters/UIDesign
    chapters/ajax
    chapters/bootstrap_index
    chapters/building_bootstrap
    chapters/coloursfortheweb
    chapters/lessrest
    chapters/corefile_debugging
    chapters/futuretech
    chapters/bothPythons
    chapters/emacs
    chapters/nginx
    chapters/gh-pages
    chapters/nonblockwsgi
    chapters/wsgi_simple_app
    chapters/wsgi_test
    chapters/wifi
    chapters/ssl-tls
    chapters/workstation-install
    chapters/workstation
    chapters/webdev
    chapters/webtest
    chapters/well-behaved-services
    chapters/using_github__ssh
    chapters/podcast
    chapters/postgres-cheatsheet
    chapters/pxeboot
    chapters/python_warts
    chapters/routes
    chapters/rssso
    chapters/samba
    chapters/securityoverview
    chapters/sed_sort
    chapters/seo-case-study
    chapters/Managing time in docker containers </chapters/time_in_docker>


Out of date already
===================

chapters/virtualisation
chapters/virtualbox`
chapters/usbdisk`


https://en.wikipedia.org/wiki/Fractal_tree_index


.. rubric:: Footnotes

.. [#f1] The linked essay is by Eric S Raymond and is almost two
   decades old, and lays out an important philosophical difference
   between how open source software gets developed (in a mad press of new
   things being tried out) and how cathedrals are built.  The cathedral
   builders have tried to learn from the bazaar, and concepts like Agile
   are helping (a bit) but building software in our modern day
   institutions is still frustrating.  As software eats the world, it
   will find politics and push back.

