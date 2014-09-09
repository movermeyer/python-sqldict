# -*- coding: utf-8 -*-
#!/usr/bin/env python

## conn = mysql.connector.connect(user='dbuser', password='dbpass', host='localhost', database='template1')

import mysql
from .baseconnection import BaseConnection

class MySqlConnectionError(Exception): pass

class MYSQLConnection(BaseConnection):

    def make_connection(self):
        """ Basicly to build mysql connection by given attributes """
        try:
            self.connection=mysql.connector.connect(database=self.dbname,
                                                    user=self.user,
                                                    password=self.password,
                                                    host=self.host,
                                                    port=self.port)
        except Exception, e:
            raise MySqlConnectionError, e
