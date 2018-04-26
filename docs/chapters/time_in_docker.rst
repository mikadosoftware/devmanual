Time and Docker
===============

(ref my previous ntp article)

When a docker instance runs on a host, it will not have the
permissions needed to alter the host time (unless running --privileged
which is a bad idea and not avaialable from most cloud providers
anyway)

So our containers rely and depend on the host for an accurate time
keeping.  But we would be sensible to not just trust it, and check,
especially if it means keeping several instances in sync




Biblio
------
ivankrizsan.se
