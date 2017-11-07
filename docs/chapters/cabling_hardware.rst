==========================
Cabling and other hardware
==========================


Like a number of others this is for historical purposes, but yes, I really
did run a real business with a "server room" that was cooled using a aircon unit
we just hauled in from `B&Q <http://www.diy.com>`_.



Power, and Cooling
==================

At some point a small company will move from having a few laptops, to
having a *server*.[#]_  And at some point after that they get another
one, and an IT manager, and soon they have to think hardware.

A Pentium4 CPU can hit 90C, and stay there under heavy load.  The fans
and other noise are designed to throw that heat away from the CPU.
One of the most common causes of computer failure is overheating in
summer. [#]_

So in essence we are running an office full of bar heaters.

How do I cool this all down ?
-----------------------------

Its all down to Watts.  1 watt is a rate of power consumption equal to 1 joule
per second

.. sidebar:: Get off your BTus

    Q.  How do I convert Kilowatts (kW) into British thermal unit (Btu)?

    A.  To convert Kilowatts (kW) into a British thermal unit (Btu) value simply
    multiply the Kilowatts value by 3414

    kW x 3414 = Btu

    OR from wikipedia

    1 watt is approximately 3.41 BTU/h
    (presumably they mean 1 watt hour is about 3.41 BTU hours)



on average a single server will consume 60-120W (yes that is a big varience, but
dual cores and load all make a difference.  Measure it using a `kill-a-watt
meter <http://michaelbluejay.com/electricity/measure.html>`_ for ease) .

so, 120 W = 120*3.41 = 409 BTU for a single server So, 15 servers, all running
at once will pump out about 9000 BTU 9000 BTU is the bottom end rating for a DIY
air conditioner.  Do you see where we are going?

So if I have a 6000 BTU rated air conditioner I can in theory have 30 servers on
at full blast and the temperature will stay the same.



.. [#] Admittedly that point gets further off as years pass - web
based services really do offer a small business a real benefit if they
are willing to risk hosting. [Ha - can you see my bold prediction of the
cloud-computing era.  Well at least I saw it's benefits :-)]


.. [#] Curiously tropical and desert failures due to heat seem to be
less commonly reported.  My assumption is that in the UK most of the
year it is cold enough to get away with no (or insufficient) dedicated
cooling.  When summer hits, the servers pay the price.  In a hot
climate, that is an ever present threat and is factored in from the
start.
