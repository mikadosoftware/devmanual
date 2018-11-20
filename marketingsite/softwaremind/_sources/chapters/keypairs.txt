==================
Key pairs and GPG
==================

The basics are that all modern security relies on a simple feature of prime numbers - it's really hard to find a factor of a very very large number. Hard as in hundreds of years via brute force.

Edward Snowden said it simply - trust the math

But the math is simple - how is it implemented

My goal is to look at the anatomy of a GPG key (openpgp) and show how the primary key self signs it's user ids and subkeys - that way I can show a calculation in process and show how subkeys can be split up and still have link back to primary key pair


Using larger than 4096 size
http://www.jroller.com/robertburrelldonkin/entry/gnupg_8192bit_rsa_keys

Basdically adjyst 'keygen.c'


Biblio
------
https://davesteele.github.io/gpg/2014/09/20/anatomy-of-a-gpg-key/

https://alexcabal.com/creating-the-perfect-gpg-keypair/
https://wiki.debian.org/GnuPG/AirgappedMasterKey
 
https://wiki.debian.org/Subkeys?action=show&redirect=subkeys
https://security.stackexchange.com/questions/31594/what-is-a-good-general-purpose-gnupg-key-setup
https://security.stackexchange.com/questions/29851/how-many-openpgp-keys-should-i-make/29858#29858
https://futureboy.us/pgp.html


How does SSL/TLS verify a certificate
https://security.stackexchange.com/questions/72077/validating-an-ssl-certificate-chain-according-to-rfc-5280-am-i-understanding-th

https://tools.ietf.org/html/rfc5280#section-6.1

https://tools.ietf.org/html/rfc5246

How does this all fit together and why does it matter?

Encryption underpins *everything*. But just thinking its multiplying primes and then ... secure is fallacious and just leaves that "Gotham city" feeling (lego batman)

I don't like floating on nothing.


 
