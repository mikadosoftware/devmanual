=====================
Interview Questions
=====================

These are called interview questions but really they are ... fundamentals
you have to know but wont use daily. They are things that if you know about you wont go down horribly wrong roads


* Big O notation

  * caches
  * hashes
  * pre-sorting and indexes
  * search problems
  * graphs
  *
  
=================
Coding interviews
=================

It is fairly difficult to sort wheat from chaff when interviewing for any position, and software engineering is no different.

I have been hiring (and being hired!) for at least two decades and the fads and fashions have changed, but very rarely has the experience on either side been effective or good.

Because of this There is a desire for a silver bullet, a way to cut through the hard work of hiring human beings and get the perfect person. This silver bullet fallacy is I suspect a strong reason why diversity in tech is so miserably bad, that without a willingness to put in effort and self-awareness we will always just hire more copies of ourselves.  But we are where we are.

In the 90s to early 2000's the culture was Microsoft driven, with questions like "how many traffic lights are there in London". MS had teams do their own hiring, but tried to set a minimum bar for each interview so that there was some consistency.

This was a test of reasoning and analysis (this was one of my interview questions at the time  - oh yes, I followed fashion in this and made all the mistakes we shall discuss here.  Quite a lot of them twice.)  generally one was looking for the ability to extrapolate from a position of ignorance to get some back-of-the-envelope figures.  I liked the idea of looking at an old A-Z (a paper based book holding streetmap of London which Google Maps has effectively removed from the passenger seat of every mini-cab in Gods Favourite City) - each square on a page had about one road junction, there were 16 squares to a page, and 500 pages covered London giving a rough answer.

I don't think I ever found these questions useful. They were fun puzzles, and people who just stared blankly or hated the idea were people I found it harder to get on with socially (potentially a useful filter) but they had little direct relevance to the pr blend of software engineering 

As the 21 Century grew old and Microsoft was supplanted with Google, trends in tech interviews changed too, and Google has always had a strong engineering culture and hired by having their HR team hire centrally and then when people were in, they could go to various teams.  This again improved consistency - but was it useful? The trend is now for algorithm based questioning - can you reverse a linked list on a whiteboard.

I freaking hate these interviews as a candidate.  Once I tried to implement Erastothenes sieve on a whiteboard, while the ex-CTO of Google (well that's what he said) sat behind me, and I realised that if his interruptions, sarcastic comments and braying snort was something he used on a daily basis if I actually worked for him, then I would soon have to explain to a police officer why I had shoved a whiteboard eraser where it was not going to be any good for cleaning anymore. 

Famously the bloke who wrote Mac "I have written software 90% of your developers use but I can't reverse a linked list on a whiteboard so fuck you"

Asking people to answer second year university algorithm questions can help eliminate people who were not paying attention at university. These are in the end useful things to know, and many are essential.  But there are limits.  Van Rossum implanted hash tables for ducts in the 90s by "grabbing Knuth vol 3, reading it and implementing that".  Curiously he explained that the hash function then was based on primes. Subsequently the optimisation on CPUs (L1 and L2 caches etc) has meant that primes are no longer the fastest - and power of 2 are faster hash functions. He let those core commuters who were keeping up with that area update the hash table (every decade or so you need to rewrite it seems)

FizzBuzz or SQL
My  most useful filters have been very very simple. 

Spolsky theory is that 2% of the first hundred people to respond are new on the market - the remaining 98 are applying to every job going. Anecdotally this is my exerprience - the first interviewee through the door is almost always awful.  I spent a unproductive five minutes asking someone to write a SELect statemt  and they simply repeated "I know SQL". Maybe they were like me but it's supposed to be simple
FizzBuzz does a similar thing - if you cannot actually do a simple five liner, you can't code. That Elon area most of the problem


My most effective filter was almost an accident. 

When I started hiring in the late 90s Python was an out of the way language, but I had started using it on production and I found that people who had discovered the language were not only my kind of people but were passionate and interested in software engineering.

As a CTO I simply used FreeBSD and python (almost) exclusively and that made the filter system upfront in the job ads - and it became an easy filter. Have you used python before? No? Well you clearly did not read the job as.

This value has diminished considerably, and it may well have been accidental.  Plus I don't honestly think I improved diversity 



Spolsky hiring theory
But even so I rejected someone - was that a mistake? 


All the above are negative filters. You cannot do X. Get out.

http://www.primaryobjects.com/2017/03/28/preparing-for-a-technical-interview-algorithms-data-structures-and-computer-science/#linkedlists

Issues with bias and diversity 
Spolsky hiring theory

What does work? 
HN guy on work related tasks

Good software takes ten years
And then you rewrite


When is language optimisation too much?
---------------------------------------

One of the most common tropes in software world is the 'interview question'.
While that is a whole long rant on its own (link), the desire for the industry to
optimise its code is laudable.  However there is often too much of a focus on
what language, what framework when there are otehr levels to explore

There are at least three levels of "providing business value" When we
focus on the lowest level with the least multiplier, we lose
productivity gains.  THis is too often seen as an excuse for pushing
bad code to prod.  It should rather be seen as an excuse to develop
code facing the problems of the higher levels - marketing automation
can be a huge win.

What we should know about COmputer science

Algorithm design
data structures
python innards

