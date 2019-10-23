=============
AWS Overview
=============

I am going to use AWS and Cloud interchangeably for the moment.
This is forgiveable, as *most* cloud issues are common across all platforms
and we can discuss specifics later once the basics are down.

Security Basics
===============

IAM

root user:
https://985718997590.signin.aws.amazon.com/console
Turn on MFA - I have used my u2f key (ubikey) 


* Activate CloudTrail

mikado_global_cloudtrail is the name of the trail, and the S3 bucket used to store all this.  There is a pricing component.
THis is activated by the root user in


Compliance and Monitoring
=========================

AWS `Cloudtrail` is the first step - and is a great idea for
everything else we do.  Every AWS "function" - such as teardown an
instance, store a file, update a DNS record, is recorded in a special
log called Cloudtrail - so that every action we perform on AWS is recorded
and auditable.

biblio:: https://www.skyhighnetworks.com/cloud-security-blog/aws-security-best-practices/
