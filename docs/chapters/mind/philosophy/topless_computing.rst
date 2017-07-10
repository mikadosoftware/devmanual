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
