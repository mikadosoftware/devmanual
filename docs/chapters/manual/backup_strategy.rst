===================================
How to run a simple backup strategy
===================================

.. epigraph::

   You will never be forgiven for losing data when people want it.
   Even if they never looked at it for a year previously.


1. git is not a backup service.  It is a development history.
2.



3 kinds of backup
- code - svn mostly 1GB - 1mb pday max delta
- strutured data - database - 1gb+ 10mb pday
- semi structured - emails - 200gb - 100mb pday
- unstrucutred - files docs etc

I want the first two off site online backups. Use replicaton for database

Samba - daily backup to local, using yesterday, t-2 t-3 approach for 5 days.
Issues:
- verification. THe cheapest way is to mount the yesterday backup as a samba file and people can come and look at it
- off-site - how do we keep yestedays backup off site. Or do we accept that as a potential loss and just keep the rolling backup off site


Rolling Archive - archive to disk a snapshot each 1st month and keep.

Never remove Archive all files > 1yr old, leaving placeholder txt files? These go to Ongoing archiveof ll files with modification date > 1yr

Email backup - ?
I want exchange totally isolated - with all smtp traffic handled by postfix sendmail both in and out.
Then i want all mail to be side tracked to mysql Then how do we backup pst files?

SPec
----

Our Backup strategy

We have 4 types of data to contend with and 4 types of loss to defend against

Data types
----------
1. 'code' - developed Code, config files for servers etc
2. structured data - SQL basically
3. email data - I would prefer it if it was MailDir, but we have got pst files or rather a huge NTBackup file
4. file server documents - ie Samba

Data Loss
---------

1. Disk failure
2. Accidental deletion
3. file corruption
4. site loss


The strategies for all 4 loss scenarios are very different

1. Disk failure - either
   - striping (ie RAID 5, or google-like map-reduce)
   - mirrored backups (ie a copy on big backup machine)

2. accidental deletion
   - mirrored and temporarily preserved backups (Daily snaphot, rotated weekly)
   - mirrored and permanently preserved backups (archive snapshot kept forever)

3. Random file corruption
   - the strategy is same as accidental deletion, however the approach to detection
     is to use something like mtree (hashes file signatures)

4. site loss
   - disaster recovery using replacement hardware, new site, and a full mirrored backup


Extra strategies
----------------
1. archiving unused documents
2. online backups only go to hot swap not to data dump
   By this I mean we only backup over the wire to a hot application, to a location
   where if we suffer site loss is very simple and easy to set up.

   ie replicate MYSQL to a MYSQL server in US/docklands
      mirror samba to another samba server that is sitting in a spare office
We do not want to be in a situation where we have dumped samba to a disk in docklands
And then lose the site, decide to buy new servers and put them in alans house,
have to wait hours/days to download that disk over alans DSL. We should have servers in
Alans house and mirror the backup to that hot server. So if we need to we just move to alans house and hey presto the data is alsready there



Strategy
--------
1. Backup all to large array of disks at far end of office
2. Install tape drive on large array and perform backup
3. online backup of svn, mysql
4. backup tapes are rotated on daily basis out of office and a snapshot kept every
14 days





Bibliography
------------
Disk failure
(quite common - see biblio. Basically google says its more common than you think. So given MTBF of 100,000 hours, thats bascially 1/2 of all disks will fail in 100,000hours
in 10 years. We have close on 100 disks (pcs, latops, raids) so 50 will fail in next 10 years, expect 5 to fail each year ).
Most MTBF is 300,000 - 500,000. So 1 disk a year from MTBF, but google says more. We have lost 4 since I got here, so 1-2% failure rate  is close.




Google results
http://labs.google.com/papers/disk_failures.pdf

Blog on google results
http://storagemojo.com/2007/02/19/googles-disk-failure-experience/

How to calculate RAID MTBF from HDD MTBF
http://answers.google.com/answers/threadview?id=730165

General article
http://www.computerworld.com/action/article.do?command=viewArticleBasic&articleId=9073158&source=rss_topic17



http://www.freebsd.org/doc/en/books/handbook/backup-strategies.html
