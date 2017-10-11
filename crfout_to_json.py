# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:51:12 2017

@author: Nyemo
"""
import re
import json
import tn.text_normalisation as tn


def predicted_base(crfoutputfile, outputjson):
    """
    input : cfr++ output file
    output : word and his variant predicted by crf++ in json format
    """
    lines = tn.openfiles(crfoutputfile)
    word = ""
    oov = ""
    prediction = []
    wo = ["", ""]
    for line in lines:
        if line.startswith("#"): #new word
             wo[0] = word
             wo[1] = oov
             prediction.append(wo)
             wo = ["", ""]
             word = ""
             oov = ""
        else:
            data = line.strip().split("\t")
            word += data[0]
            oov += data[len(data)-1]
    wo[0] = word
    wo[1] = oov
    prediction.append(wo)
    
    
    i = 1
    cmudict = {}
    while i < len(prediction):
        oovlist = []
        word = prediction[i][0]
        j = i
        while j <= i+29: # i + nbest-1       
            if j < len(prediction):
                ov = re.sub('-', '', prediction[j][1])
                oovlist.append(ov)
                
            j += 1
        cmudict[word] = oovlist
        i += 30 # n best
    with open(outputjson, 'w', encoding='utf-8') as f:
        json.dump(cmudict, f, indent=4)
    
if __name__ == '__main__':       
    predicted_base('ressources/hyphoutput.txt', 'ressources/hyphenation.json')       
        
     
     