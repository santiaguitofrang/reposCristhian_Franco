#-*- coding:utf-8 -*-
'''
Created on 18/2/2015

@author: PC06
'''
from flaskext.mysql import MySQL
from flask import Flask

class DBcon():
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def conexion(self):
        mysql = MySQL()
        app = Flask(__name__)
        app.config['MYSQL_DATABASE_USER'] = 'python'
        app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
        app.config['MYSQL_DATABASE_DB'] = 'ventas'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)
        return mysql

