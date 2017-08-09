https://www.microservices.com/talks/dont-build-a-distributed-monolith/

Use public apsi, based on protocols 

Because if you just write one client code to work with one server code slowly they drift together / and worse you just end up sending round the depenancies of that client, installing those 50 libraries everywhere (npm)

That means if you want to install a breaking version of client suddenly you have to install the 50 new libraries in hundreds of places - you have built a distributed monolith

Hunting
https://www.usenix.org/conference/enigma2016/conference-program/presentation/payne
Talk online

https://www.google.co.uk/amp/www.techrepublic.com/google-amp/article/how-to-establish-strong-microservice-security-using-ssl-tls-and-api-gateways/

Obvious but checklist


Basics
TLS pki, using short lived certs internally
Longer pki for external contacts
Maybe use oauth for consumers


Service mesh
https://eng.lyft.com/announcing-envoy-c-l7-proxy-and-communication-bus-92520b6c8191

This evolved into istio now wider supported

An on host network proxy that could transparently just pass through network traffic OR can apply policy on say service discovery, load balancing, circuit breaking, rate limiting etc - a balance between not knowing which network portion the hosts will be on so not being able to use traditional routers, and well this is part of software defined networks but at the application layer

Software defined networks push packets around, thisnoperates on requests??? 


Basic security and architecture

https://stackoverflow.com/questions/549/the-definitive-guide-to-form-based-website-authentication

The basal architecture:

