=======
Testing
=======

Two kinds
---— — —
There are two kinds of test
Unit tests and integration  tests

Unit tests should be typified by doctrst - explanatory, covering the developers thought processes when building this
And also by hypothesis- attribute based testing (passing in nulls and floats to top end of the ranges and billion character strings)


Then everything else is integration testing - UI level, in through the front door.  Jason just makes this easier but it builds up to become the operational level feedback - you cannot do operational testin gwithout building integration tests up and up.  And integration tests should be runnable from any env 

Se feynmanns description of engine based testing


Nose is the standard for Python testing.


http://stackoverflow.com/questions/8054512/anyone-know-how-nosetests-m-i-and-e-work
https://groups.google.com/forum/?fromgroups=#!topic/nose-users/1IGF0xliWiA


Sphinx and DocTests

https://mitmproxy.org/posts/releases/mitmproxy3/
Basic principles
it's hard 
go with your gut (ref elite handbook)

https://stephenmann.io/post/lessons-learned-writing-unit-tests/#lesson-4-if-you-can-t-make-a-test-smaller-your-code-probably-has-too-many-dependencies

- functional helps
- smaller, pure, smaller than that
- doc tests are great cos you can see the relative sizes

Do lots of integrationnand fitness tests - they help users a lot.  this is why cucumber style testing is crap - 



