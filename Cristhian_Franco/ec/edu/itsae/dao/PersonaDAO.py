#-*- coding:utf-8 -*-
'''
Created on 18/2/2015

@author: PC06
'''
from ec.edu.itsae.conn import DBcon
import json

class PersonaDao(DBcon.DBcon):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def reportarPersona(self):
        con=self.conexion().connect().cursor()
        con.execute("select * from personas")
        reporte=con.fetchall()
        return reporte
    
    def insertarPersona(self,nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado):
        con=self.conexion().connect()
        sql=""" insert into personas(nombre, apell_paterno, apell_materno, dni, 
                        fecha_nacimiento, sexo, direccion, celular, estado)
                         values('%s','%s','%s','%s','%s','%s','%s','%s', %i)  """ % (nombre, apaterno, amaterno, cedula, fnacimiento, sexo, direccion, celular, estado)
        print sql
        with con:
            cursor=con.cursor()
            cursor.execute(sql)   
    
    def buscarPersonaNombre(self, datobuscado):
        con=self.conexion().connect().cursor()
        con.execute("""select CONCAT(nombre,' ',apell_paterno,' ', apell_materno) as value, idpersona as id from personas where upper(CONCAT(nombre,' ',apell_paterno,' ', apell_materno)) like upper('%s') """ % ("%"+datobuscado+"%") )
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        for row in reporte:
            lista.append(dict(zip(columna,row)))        
        return json.dumps(lista, indent=2)
    
    def buscarPersonaDato(self, datobuscado):
        con=self.conexion().connect().cursor()
        sql="""select * from personas 
        where upper(CONCAT(nombre,' ',apell_paterno,' ', apell_materno)) 
         like upper('%s') """ % ("%"+datobuscado+"%")
        con.execute(sql)
        reporte=con.fetchall()        
        return reporte  
            
    def validarUsuario(self, usuario, clave):
        con=self.conexion().connect().cursor()
        con.execute("""select * from trabajador where usuario='%s' and clave='%s'""" %(usuario,clave))
        reporte=con.fetchall()
        return reporte        
            
            
            
            
            