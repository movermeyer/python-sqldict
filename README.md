python-sqldict
==============
[![Build Status](https://travis-ci.org/RedXBeard/python-sqldict.svg?branch=master)](https://travis-ci.org/RedXBeard/python-sqldict)

Raw SQL results returns as dictionary.

Developers who has lots of works on databases, sometimes, especially written raw sql result or in other words selects become to much to handle, so to play with the result of that sqls become pain; columns has to be remembered which index of result list refers which column etc. (ORM usage is fix this issue but has consequences so even if you are using ORM sometimes as said writing raw sqls preferred)

To have a key value pair like dictionaries for sql results will be much more useful, and the pain will become less.

Installation
------------
class will be put into pypi soon, after that;
```bash
$ pip install SQLtoDICT
$ pip install psycopg2
$ pip install mysql-connector-repackaged
```

Usage
-----
To play with postgress database, required connection is as following;
```python
: from SQLtoDICT.connections.postgressconnection import PostgressConnection
```

There are two ways to make class one is giving all required attributes for making the connection;
```python
: pc = PostgressConnection(sql="""select id, code
                                  from product
                                  limit 10
                               """,
                           database='template1'
                           user='dbuser'
                           host='localhost'
                           password='dbpass',
                           port='5433')
```

Other one is; cursor will be already generated and it could be enough to making the class;
```python
: import psycopg2
: conn = psycopg2.connect(dbname='template1',
                          user='dbuser',
                          host='localhost',
                          password='dbpass',
                          port='5433')
: cursor = conn.cursor()
: pc = PostgressConnection(sql="""select id, code
                                  from product
                                  limit 10
                               """,
                           cursor=cursor)
```

Execution is simple as it is;
```python
: pc.execute_sql()
```

The result will as following, as default sql select result which is sometimes so hard to continue working.
```python
: pc.result
[(62392, '4YAL61165JW'),
 (41308, 'Y14FCD010394'),
 (61397, '4YAL16490IK'),
 (4396, 'W2WCR0040'),
 (61696, '4YAK71063AA'),
 (57895, '4YAK38077PW'),
 (64853, 'V0400710218'),
 (61870, 'Y14LGD021110'),
 (55054, '4YAM19187LK'),
 (61027, '4YAM19698LK')]
```

Dictionary conversion after executing the sql result will be following understandable list.
```python
: pc.sql_result_as_dict()
[{'code': '4YAL61165JW', 'id': 62392},
 {'code': 'Y14FCD010394', 'id': 41308},
 {'code': '4YAL16490IK', 'id': 61397},
 {'code': 'W2WCR0040', 'id': 4396},
 {'code': '4YAK71063AA', 'id': 61696},
 {'code': '4YAK38077PW', 'id': 57895},
 {'code': 'V0400710218', 'id': 64853},
 {'code': 'Y14LGD021110', 'id': 61870},
 {'code': '4YAM19187LK', 'id': 55054},
 {'code': '4YAM19698LK', 'id': 61027}]
```
