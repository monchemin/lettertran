# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:24:41 2017

@author: Nyemo
"""
import json
import tn.text_normalisation as tn


def oov_to_word(oovfile, out):
    """
        script to predict best word giving oov
        input : oov 
        output : word
    """
    dictionary = {}
    corpus = {}
    
    
    outfile = open(out, "w")
    oovs = tn.openfiles(oovfile) # return list of line
    with open('ressources/dictionary.json', 'r') as fj:
        dictionary = json.load(fj)
    with open('ressources/corpus.json', 'r') as cj:
        corpus = json.load(cj)
    count = 0
    
    for oov in oovs:
        oov = oov.strip()
        candidate_word = []  #list of candidate words
        for word, oovlist in dictionary.items():
            if oov in oovlist:
                candidate_word.append(word)
        score = probality(oov, candidate_word)
        for k, v in score.items():
            if k in corpus.keys(): #use corpus probability (word's count in corpus)
                score[k] = v * corpus[k]
        p_word = ""
        p_score = 0
        for k, v in score.items():
            if v > p_score:
                p_word = k
                p_score = v
        outfile.write("{}\t{}\n".format(oov, p_word))
        if len(p_word) != 0:
            count += 1
    outfile.write("\n -----------------------------\n oov : {}\nfound : {}".format(len(oovs), count))
    outfile.close()

        
            
            
        
        #print(oov + "\t" + "|".join(candidate_word))

def probality(oov, candidate):
     """ 
        common letter's number / len(word)
     """
     score = {}
     for word in candidate:
         line = col_index = 0
         letters = 0
         while line < len(oov):
            col = col_index
            while col < len(word):
                if oov[line] == word[col]:
                    letters += 1
                    col_index = col + 1
                    break
                col += 1
            line += 1
         score[word] = letters/len(word)
     return score
            
  
if __name__ == '__main__':   
    oov_to_word('', '')
    
        
        
    
    
    
        
