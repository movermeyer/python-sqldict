# -*- coding: utf-8 -*-
#!/usr/bin/env python

class ExecutionError(Exception): pass
class GenerationDictError(Exception): pass

class BaseConnection(object):
    def __init__(self, sql, dbname=None, user=None, host=None,
                 password=None, port=None, cursor=None):
        self.sql=sql
        self.dbname=dbname
        self.user=user
        self.host=host
        self.password=password
        self.port=port
        self.cursor=cursor
        self.connection=None
        self.result=None

    @classmethod
    def cursorready(cls, sql, cursor):
        """
        Connection can be established already,
        so the class can also be generated
        """
        return cls(sql=sql, cursor=cursor)

    def make_connection(self):
        pass

    def execute_sql(self):
        """ To execute raw sql """
        try:
            if not self.cursor:
                self.make_connection()
                self.cursor=self.connection.cursor()
            self.cursor.execute(self.sql)
            self.result=self.cursor.fetchall()
        except Exception, e:
            raise ExecutionError, e

    def sql_result_as_dict(self):
        """ Generation dictionary from the result """
        self.execute_sql()
        data=self.result
        try:
            columns = map(lambda x: x.name, self.cursor.description)
            data=[dict(zip(columns, row)) for row in self.result]
        except Exception, e:
            raise GenerationDictError, e
        return data
