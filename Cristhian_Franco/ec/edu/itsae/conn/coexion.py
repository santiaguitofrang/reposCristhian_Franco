'''
Created on 18/2/2015

@author: PC06
'''

from flaskext.mysql import MySQL
from flask import Flask

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'python1'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'ventas1'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


con=mysql.connect().cursor()
con.execute(" select * from personas ")
report=con.fetchall()
print report

