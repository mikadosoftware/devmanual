Agile Estimation - Learning from traditional Project Management
===============================================================

I have long wondered why Agile (well, read Scrum) planning is *so* simplistic.

Yes, having the team estimate the tasks and then agree to them is, frankly, a
world away from the handed-down-from-on-high estimation found in most companies,
big and small.  Even where estimation is *initially* done by the teams, I have
found a number of times that the estimates are either massaged, or are part of a
in-all-but-name waterfall approach.

Even a little more sophistication can lead us to estimates that are dramatically
more useful outside the team, and that tends to lead to teams getting left alone with a reputation for hitting thier promises.

So I suggest that all Planning Poker estimates are provided with PERT three-way estimation points, and then thyat is 


Planning poker is based on `Wide-Band Delphi <http://en.wikipedia.org/wiki/Wide_band_delphi>`_ which came out of RAND Corporation via Barry Boehm.


Notes

* http://www.palisade.com/risk/monte_carlo_simulation.asp

* http://sunset.usc.edu/publications/TECHRPTS/1995/usccse95-507/ASP.pdf

  (Boehm: Know why you are building the software, know your architecture is upto it and make sure the initial release carries the promise.)

* http://csse.usc.edu/csse/TECHRPTS/2007/usc-csse-2007-715/usc-csse-2007-715.pdf
  (Incremental commitment - a very Agile approach, basically using risk based analysis to judge if those paying will get what they are paying for - at each stage they can incrmentally commit a little more money.  Or as Ward Cunningham puts it "Can leave with software representing the amount of money committed to date"


* http://tynerblain.com/blog/2006/04/13/foundation-series-basic-pert-estimate-tutorial/ 
 
  E = (O + 4N + P)/6
  stdev = (pessimistic – optimistic) / 6
  Combining estiamtes (chances of EPIC / backlog)

  
    The combined mean is the sum of the two old means. 32.5 + 32.5 = 65 minutes.
    The combined stdev is the square root of the sum of the squares of the two old stdevs. SQRT(7.5^2 + 7.5^2) = 10.6.
    The combined optimistic estimate is the mean minus ( 3 * stdev). Optimistic = 65 – (3 * 10.6) = 33 minutes.
    The combined pessimistic estimate is the mean plus (3 * stdev). Pessimistic = 65 + (3 * 10.6) = 97 minutes.
    Our combined PERT estimate is 33/65/97 with a mean of 65 minutes and a stdev of 10.6 minutes.

   



