# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:34:13 2017

@author: Nyemo
"""

fichier =  open('cmudict.txt' , 'r')
cmudict = fichier.readlines()
fichier1 =  open('lexicon.txt' , 'r')
lexicon = fichier1.readlines()
condo = {}
difference = []
cmudictstrip = []
for mot in cmudict:
    cmudictstrip.append(mot.strip())
    
for line in lexicon:
           
           data = line.split()
           word = data[1]
           #print(word.upper())
           if word.upper() in cmudictstrip:
               condo[data[0]] = word
           else:
               difference.append(word)

print("nombre de mot : {} -- difference : {}".format(len(condo), len(difference) ))
print(difference)