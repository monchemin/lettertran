# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 20:44:09 2017

@author: Nyemo
"""

import pymysql
import json


def lexico():
    connection = pymysql.connect(host="localhost",user="root",password="", database="coca")
    
    fichier =  open('lexicon.txt' , 'r')
    lexicon = fichier.readlines()
    nb = 0
    try:
        with connection.cursor() as cursor:
            # Create a new record
           # sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
           for line in lexicon:
               
               data = line.split()
              
               #print(len(data))
               #print(data[2])
               if len(data) == 4:
                   sql = "INSERT INTO lexicon (wordId, word, lemma, Pos) VALUES(%s, %s, %s, %s)"
                   cursor.execute(sql, (data[0], data[1], data[2], data[3]))
               else:
                  nb += 1
    
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    
        
    finally:
        connection.close()
    
    print(nb)
    
def corpus():
    connection = pymysql.connect(host="localhost",user="root",password="", database="coca")
    query = """select lexicon.word, count(corpus.wordId) 
                from lexicon, corpus 
                where lexicon.wordId = corpus.wordId group by lexicon.word"""
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
        corpus = dict(data)
        with open('../ressources/corpus.json', 'w', encoding='utf-8') as f:
            json.dump(corpus, f, indent=4)



        
if __name__ == '__main__':
    corpus()        