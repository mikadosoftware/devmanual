I did not say Big Data
=======================

Pachyderm.io
docker to make storing versioned data sets

using DAGs 

using apache spark

data pipeline and consistency

Data Dictionary

com.business-panda.data.hr.total_num_employees

.employee.personalrecord.name
.suppliers


Data Structures matter more than almost anything

Clever code on simple / well known data structure 
https://swtch.com/~rsc/regexp/regexp4.html


Simple haka or tests for one self

Graphs and graph theory
- Three vital graph algorithms
https://mlwhiz.com/blog/2018/12/07/connected_components/


Python simple canvas applications
http://fabiensanglard.net/doom_fire_psx/
http://agilerepose.weebly.com/water-ripple.html


Data Pipeline stack
-------------------

https://medium.com/gyroscopesoftware/a-reference-stack-for-modern-data-science-4bd9fddcdc6b

PySpark to take huge data sets down to something small enough to fit in memory and pandas.  then pandas.  then visualisation tools - the simple enough stuff is Altair / Vega - but always have D3.JS as fallback for when you cannot find the right graph pre made

Adjust lib-report to hold visualisation library too


Gettting an overview of data storage and retrieval
---------------------------------------------------


RDBMS still has its place - for anything under a few million rows SQLite is darn useful and postgres is fine for most other things


it's only when we get to silly amounts of incoming data do we need to start worrying

For me the break point is 1,000s of data points per second - that's at the level of 100 million points per day - that's easily beyond what a "dump to sql and do some daily batch processing" is likely to handle

If you aren't there, it's probably not worth worrying about Big Data

Try worrying about data process management - 

- source control
- data doctionary
- repeatability
- reporting
- analysis

etc

But if we are there are several things worth looking at 

firstly storage

https://wiki.apache.org/incubator/IoTDBProposal
Berkeley tree database

Modern industrial plant output hundreds of time series (speed of rotation, temperature etc etc)
Keeping those and keeping on top of predictions etc is a real need, and ML plays a huge role in it - it's not all "user.signin" events

But they are all time series metrics and they are all our telemetry - it's what we want and need.

The Big Data architecture
- store time series data in columnar format
- use Apache Spark / hadoop map reduce to get a subset of data 
- use Sql / pandas to manipulate that subset as needed

The important thing to remember about BIg Data
https://livefreeordichotomize.com/2019/06/04/using_awk_and_r_to_parse_25tb/


More on big data and software literacy
--------------------------------------

Data Management is the other leg of software literacy - those companies that treat data management as a first class C-Suite level citizen will have more opportunities and less cost of opportunity than those that don't - and those opportunities will compound




Biblio
------
https://conf.slac.stanford.edu/xldb2018/sites/xldb2018.conf.slac.stanford.edu/files/Tues_15.50%20Ian%20Willson%20XLDB%202018%20Boeing%20IOT.pdf


Latex layouts
-------------
https://www.latextemplates.com/cat/books

