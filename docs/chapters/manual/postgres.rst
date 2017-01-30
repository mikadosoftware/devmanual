===========================
Using PostgreSQL on FreeBSD
===========================




Find enum types::



  dbtest=> SELECT pg_type.typname AS enumtype, 
  dbtest->      pg_enum.enumlabel AS enumlabel
  dbtest->  FROM pg_type 
  dbtest->  JOIN pg_enum 
  dbtest->      ON pg_enum.enumtypid = pg_type.oid;

     enumtype   | enumlabel  
  --------------+------------
   cnxrole_type | author
   cnxrole_type | maintainer
   cnxrole_type | copyright
  (3 rows)



Setting up postgres on FreeBSD
------------------------------

::

  $ make install clean
  $ /usr/local/bin/postgres -D /usr/local/pgsql/data


for some reason everything gets put into /usr/local/pgsql/data - the config
files and so on.


Configuration and users
-----------------------

* postgresql.conf

For local service::

    listen_addresses = 'localhost'

and in pg_hba.conf::

    host    all             all             127.0.0.1/32            md5

We change ``trust`` to ``md5`` so that it exxpects user/password




$ createuser -sdrP test1
Enter password for new role: 
Enter it again: 


pgsql$ sudo su - pgsql
$ /usr/local/bin/createdb dbtest -O test1 encoding=UNICODE
$ 

$ psql -U test1 -d dbtest
...
dbtest=# CREATE USER repo WITH PASSWORD 'repopass'; 
CREATE ROLE
dbtest=# GRANT ALL PRIVILEGES ON DATABASE dbtest to repo; 
GRANT


pgsql$ psql -h 127.0.0.1 -U repo -d dbtest
Password for user repo: 
psql (9.2.1)
Type "help" for help.

dbtest=> 


(NB localhost will try to use Unix domain sockets so use 127.0.0.1)


For network server::

    listen_addresses = '*'



Logging
-------
Normally we want to ::

  log_destination = 'syslog'
  logging_collector = off

For development purposes we usually want to watch the SQL fly past::

  log_destination = 'stderr'
  logging_collector = on
  log_directory = 'pg_log'
  log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'
 
  log_statement = 'all'
