===============
Test principles
===============

* You *cannot* ever be exhaustive in hand crafting tests.
Tests must be auto generated and hammer the code with things you cannot imagine.
YOur unit tests should cover the golden path - why I like doctests
Your smoke tests ensure things fit toether
Your automated tests hammer everything else

It is waaaay better to write lots of feature tests from outside and few unit tests
than to write lots unittests and few outside tests.  We are user centritc and users
sit outsode the code.

See danluu on bug tracking with analytics I think you cannot hand craft enough
tests  I think tests should be doc tests and then automated Much better to
hammer an api with every possible option and then arrow back down than to try
and imagine all the options

Python version of this???


Then we can simply do diff between metrics I care about (user signnups funnel)
and metrics that allow performsna car and bugbtracking (i.e. Every step or api
call made)

Source code analytics and testing
- given source code what gets called and how often?
- how to generate test data
- python quickcheck for strong types
