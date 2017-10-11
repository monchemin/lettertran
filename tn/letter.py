# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 19:02:37 2017

@author: Nyemo
"""
import numpy as np
def letter(word, oov):
#word : dictionnary word
#oov : his oov 
  
  myTable = np.zeros(shape=(len(word), len(oov)))
  line = colIndex = 0
  
  while line < len(word):
      col = colIndex
      ok = False
      while col < len(oov):
          if word[line] == oov[col]:
              myTable[line][col] = 1
              ok = True
             
          col+=1
      if ok:
          colIndex += 1
      line+=1
  print(myTable[:,:])
#traitemen de la matrice pour déternimer les positions
  line = 0
  sequence = str()
  
  while line < len(word):
      match = False
      col = 0
      while col < len(oov):
          if myTable[line][col] == 1:
              match = True            
          col+=1
      if match:
          sequence += word[line]
      else:
          sequence += "-"
          
      line+=1                         
  print(word)  
  print(sequence)   
  
  

letter("birthday", "bday")
letter("photos", "fotoz")
letter("someone", "some1")
letter("nothing", "nuthin")
letter("forever", "4eva")
letter("hubby", "hubbie")
letter("tomorow", "2moro")
letter("together", "2gthr")