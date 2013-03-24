#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-03-19

@author: Martin H. Bramwell
'''
import openerplib

def connect(wkbk):

    shtCreds = wkbk.worksheet("Creds")
    lstlstCreds = shtCreds.get_all_values()
    
    creds = {t[0]:t[1] for t in lstlstCreds}
    
    connection = openerplib.get_connection(
                                          login = creds['user_id']
                                        , database = creds['db_name']
                                        , hostname = creds['host_name']
                                        , password = creds['user_pwd']
                                        , protocol = 'xmlrpc'
                                        , port = 8069
                                      )
    print 'Connected to OpenERP database "{}" on server "{}".'.format(creds['db_name'], creds['host_name'])
    return connection


