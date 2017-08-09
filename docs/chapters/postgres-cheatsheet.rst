======================
PostgreSQL Cheat Sheet
======================

I am sure I stole this from somewhere but I cannot find the source.
Please take this with a degree of plagarism.



Start off::

  CREATE DATABASE dbName;

  CREATE TABLE (with auto numbering integer id)

  CREATE TABLE tableName (
   id serial PRIMARY KEY,
   name varchar(50) UNIQUE NOT NULL,
   dateCreated timestamp DEFAULT current_timestamp
  );

Add a primary key::

  ALTER TABLE tableName ADD PRIMARY KEY (id);

Create an INDEX::

  CREATE UNIQUE INDEX indexName ON tableName (columnNames);

Backup a database (command line)::

  pg_dump dbName > dbName.sql

Backup all databases (command line)::

  pg_dumpall > pgbackup.sql

Run a SQL script (command line)::

  psql -f script.sql databaseName

Search using a regular expression::

  SELECT column FROM table WHERE column ~ 'foo.*';

The first N records::

  SELECT columns FROM table LIMIT 10;

Pagination::

  SELECT cols FROM table LIMIT 10 OFFSET 30;

Prepared Statements::

  PREPARE preparedInsert (int, varchar) AS
    INSERT INTO tableName (intColumn, charColumn) VALUES ($1, $2);
  EXECUTE preparedInsert (1,'a');
  EXECUTE preparedInsert (2,'b');
  DEALLOCATE preparedInsert;

Create a Function::

  CREATE OR REPLACE FUNCTION month (timestamp) RETURNS integer
   AS 'SELECT date_part(''month'', $1)::integer;'
  LANGUAGE 'sql';

Table Maintenance::

  VACUUM ANALYZE table;

Reindex a database, table or index::

  REINDEX DATABASE dbName;

Show query plan::

  EXPLAIN SELECT * FROM table;

Import from a file::

  COPY destTable FROM '/tmp/somefile';

Show all runtime parameters::

  SHOW ALL;

Grant all permissions to a user::

  GRANT ALL PRIVILEGES ON table TO username;

Perform a transaction::

  BEGIN TRANSACTION
   UPDATE accounts SET balance += 50 WHERE id = 1;
  COMMIT;


Basic SQL
---------

Get all columns and rows from a table::

  SELECT * FROM table;

Add a new row::

  INSERT INTO table (column1,column2)
  VALUES (1, 'one');

Update a row::


  UPDATE table SET foo = 'bar' WHERE id = 1;

Delete a row ::

  DELETE FROM table WHERE id = 1;

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
