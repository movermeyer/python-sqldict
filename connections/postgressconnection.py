# -*- coding: utf-8 -*-
#!/usr/bin/env python

## conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")

import psycopg2
from .baseconnection import BaseConnection

class PostgressConnectionError(Exception): pass

class PostgressConnection(BaseConnection):

    def connection(self):
        """ Basicly to build postgres connection by given attributes """
        try:
            self.connection=psycopg2.connect(database=self.dbname,
                                             user=self.user,
                                             password=self.password,
                                             host=self.host,
                                             port=self.port)
        except Exception, e:
            raise PostgressConnectionError, e
