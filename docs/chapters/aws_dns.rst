Using AWS Route53 for my DNS
============================

I would like to be more "developer-y" about my DNS management.  For a
very long time I have used the UK supplier easily.co.uk, and just been
OK with doing my A-Record updates with a web interface.  But I have
good reasons and bad to move to using AWS' route53 to manage all my
DNS / Nameserver needs, so I should use the command line.

http://boto.cloudhackers.com/en/latest/route53_tut.html

    #Assume we have set up access credentials in `~/.aws/credentials`
    >>> import boto3
    >>> client = boto3.client('route53')
    >>> client.list_hosted_zones()
    ...
    {'HostedZones': [{'CallerReference': '81B9609D-A570-FB70-8764-622A299A5E13',
    'Config': {'PrivateZone': False},
    'Id': '/hostedzone/Z37ZH240XSI8D6',
    'Name': 'cleanpython.com.',
    'ResourceRecordSetCount': 6},
    ...


OK, I can see which zones AWS is acting as nameserver for.
Now I need a HostedZone id - thats the CallerReference I think,

Then I can manipulate this domain and add A and mx records.

client = boto3.client('route53')



def add_cname_record(source, target):
	try:
		response = client.change_resource_record_sets(
		HostedZoneId='<hosted zone id>',
		ChangeBatch= {
						'Comment': 'add %s -> %s' % (source, target),
						'Changes': [
							{
							 'Action': 'UPSERT',
							 'ResourceRecordSet': {
								 'Name': source,
								 'Type': 'CNAME',
								 'TTL': 300,
								 'ResourceRecords': [{'Value': target}]
							}
						}]
})

I need to amnipulate Type etc.

How to add a zone in first place???
-----------------------------------
Use the darfn console.  I will find out later.

Then repoint the DNS



Adding a domain
---------------

>>> c = boto3.client('route53domains')
>>> c
<botocore.client.Route53Domains object at 0x7f6ae169f828>
>>> c.list_domains()
{'Domains': [],


So at the moment I have no domains registered with AWS.
No this is domain registration - as you can see my domain I want to transfer in is not avaul. Because easily is my registrar.


>>> c.check_domain_availability(DomainName='paul-brian.com')
{'Availability': 'UNAVAILABLE',


So I have a plan - register the *zones* in AWS, then transfer domains in



