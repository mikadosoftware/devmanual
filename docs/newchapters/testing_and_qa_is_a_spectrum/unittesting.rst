unittesting
===========

JBRAINS.CA - J B Rainsburger argued (https://blog.thecodewhisperer.com/permalink/integrated-tests-are-a-scam)
that if you hide the problems of bad design at the unit level with a sticking plaster of a higher level test.

I really dislike mocking in tests.  I prefer *stubs* at the IO boundaries. But anything else should have unit tests, and if the part you are testing is  runner or a organiser, well that is much harder to test.

But I really like testable code, that forces decoupling on us.  

COupling - if you need to read the caller and the callee to understand what is going on, you are coupled.
