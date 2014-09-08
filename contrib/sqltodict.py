# -*- coding: utf-8 -*-
#!/usr/bin/env python

import psycopg2, mysql
## conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
## conn = mysql.connector.connect(user='dbuser', password='dbpass', host='localhost', database='template1')

class PostgressConnectionError(Exception): pass
class MySqlConnectionError(Exception): pass
class ExecutionError(Exception): pass

class SQLtoDICT(object):
    def __init__(sql, dbname, user, host, password, port):
        self.sql=sql
        self.dbname=dbname
        self.user=user
        self.host=host
        self.password=password
        self.port=post
        self.connection=None
        self.cursor=None
        self.result=None

    def make_postgres_connection(self):
        """ Basicly to build postgres connection by given attributes """
        try:
            self.connection=psycopg2.connect(database=self.dbname,
                                             user=self.user,
                                             password=self.password,
                                             host=self.host,
                                             port=self.port)
        except Exception, e:
            raise PostgressConnectionError, e

    def make_mysql_connection(self):
        """ Basicly to build mysql connection by given attributes """
        try:
            self.connection=mysql.connector.connect(database=self.dbname,
                                                    user=self.user,
                                                    password=self.password,
                                                    host=self.host,
                                                    port=self.port)
        except Exception, e:
            raise MySqlConnectionError, e

    def execute_sql(self):
        """ To execute raw sql """
        try:
            self.cursor=self.connection.cursor()
            self.result=self.cursor.execute(self.sql)
        except Exception, e:
            raise ExecutionError, e
