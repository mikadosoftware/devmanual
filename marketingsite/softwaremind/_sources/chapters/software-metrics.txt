Software Metrics
=================

How can we *automatically* measure code quality? There are a few basic options, and a lot more complex options - let's look at a couple


The basics
-----------

Lines of Code Spent

Computer science pioneer Ed Dykstra suggested one that I like - Number of lines of code Spent.

This is just a line count stat, but it reports it in a simple and inverted manner - spent means there is a cost to every extra line of code.  Giving rise to the idea that reducing our code base  is a saving


Errors Raised
Fairly simple to do again - how many and what errors are raised in production. 

Peer code reviews
Someone needs to walk through and attest they have understood the intention of the changes made.


After these two, which are pretty good, things can get more complicated

Test coverage
This is less great, because human written tests are mostly automated requirements documents.  

Test fuzzing 
This is very good

Next level
Static analysis of code base
there are providers out there that do this - worth hunting out - OWASP ASIDE



.. ::

quality: https://en.wikipedia.org/wiki/Software_quality
Software metric: https://en.wikipedia.org/wiki/Software_metric
''' Common software measurements include:
- Balanced scorecard - Bugs per line of code - Code coverage - Cohesion - Comment density[1] - Connascent software components - Constructive Cost Model - Coupling - Cyclomatic complexity (McCabe's complexity) - DSQI (design structure quality index) - Function Points and Automated Function Points, an Object Management Group standard[2] - Halstead Complexity - Instruction path length - Maintainability index - Number of classes and interfaces[citation needed] - Number of lines of code - Number of lines of customer requirements[citation needed] - Program execution time - Program load time - Program size (binary) - Weighted Micro Function Points - CISQ automated quality characteristics measures '''
Category:Software metrics 