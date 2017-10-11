# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 22:48:57 2017

@author: Nyemo
"""

import pymysql
import os

connection = pymysql.connect(host="localhost",user="root",password="", database="coca")

nombre_fichier = 0
file_error = {}
for nom_fichier in os.listdir("database"):
    if nom_fichier.endswith(".txt"):
       fichier =  open("database/" + nom_fichier , 'r')
       nombre_fichier += 1
       nb = 0
       corpus = fichier.readlines()
       
       with connection.cursor() as cursor:
               for line in corpus:
                   data = line.split()
                   if len(data) == 3:
                       sql = "INSERT INTO corpus (textId, Id, wordId) VALUES(%s, %s, %s)"
                       cursor.execute(sql, (data[0], data[1], data[2]))
                   else:
                       nb += 1
       connection.commit()
       file_error[nom_fichier] = nb
       
print("nombre de fichier : {}".format(nombre_fichier))
print(file_error)
connection.close()
