==========
Burp Suite
==========

==========

A java based, advanced proxy / intercept / wiretapping tool for watching your
REST API talk and debug.

Its less user-friendly than charles, but it runs on FreeBSD...

It is also recommended by tpatcek

Options are stored in ``.java/.userPrefs/burp/prefs.xml``


Installing a CA
---------------

We force Chrome to visit a site where a CA error will throw a User Warning.
Basically this means almost any https site. The browser shows a warning- we click through to details of the certificate (it is the one sent by burp, and not the one recieved by burp from https://google

Then export the certificate, and now visit the "update cert" in the browser and import what we just saved.
