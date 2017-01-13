What is HTML5 and why does it matter?
=====================================

HTML5 is a new set of standards and an ecosystem, all designed to work 
in the browser.  It is *not* just a markup defintion, but a set of (javascript)
APIs, a new way to work with attributes and define them, improved CSS, 

So its improved HTML *and* javascript APIs that allow a browser to access almost everything on a device, from battery status to peer-to-peer video calls.


What is out there?
------------------

.. figure:: http://en.wikipedia.org/wiki/File:HTML5-APIs-and-related-technologies-by-Sergey-Mavrody.png


Biblio
------

* http://en.wikipedia.org/wiki/HTML5
* http://davidwalsh.name/html5-apis

A few Major APIs
----------------


    Contacts - The HTML5 specification mentions that the Contacts API allows to have a common contacts repository in the browser which can be access by any web application.
    Selection - The selection API supports selecting items in DOM (supports CSS3 type of selectors), to be used along with JQUERY.
    Offline apps - This API allows marking pages to be available in Offline mode. This is useful if a resource requires dynamic processing.
    Indexed database - This API is meant for a database of records holding simple values (including hierarchical objects). Every record has a key and a value. An indexed database is supposed to be implemented using b-trees. Web SQL DB is no longer being pursued as part of HTML5 specification.
    Web workers - This API is meant to be invoked by web application to spawn background workers to execute scripts which run in parallel to UI page. The concept of web works is similar to worker threads which get spawned for tasks which need to invoked separate from the UI thread.
    Web storage - This specification defines an API for persistent data storage of key-value pair data in Web clients.
    Web sockets - This API used for persisting data storage of data in a key-value pair format for Web clients.
    Server-Sent Events - This API is used for opening an HTTP connection to receive push notifications from a server. These events are received as DOM events. This API is supposed to be used with Push SMS.
    XMLHttpRequest2 - This API is used to provide scripted client functionality to transfer data between a server and a client.
    Geolocation - This API is used to provide web applications with scripted access to geographical location information of the hosting device.
    Canvas 2D Context - This API provides objects, methods and properties to draw and manipulate graphics on a canvas drawing surface.
    HTML Microdata - This API is used to annotate content with specific machine-readable labels, e.g. to allow generic scripts to provide services that are customized to a page. Microdata allows nested groups of name-value pairs to be added to documents.
    Media Capture - This API is used to facilitate user access to a device's media capture mechanism (camera, microphone, file upload control, etc.). This only coves a subset of media capture functionality of the web platform.
    Web Messaging - This API is used for communications between browsing contexts in HTML documents.
    Forms - The Forms API can be used with the new data types supported with HTML5.
    File API - The File APIs are used by the browser to provide secure access to the file system.
