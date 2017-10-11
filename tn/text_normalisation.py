# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:57:09 2017

@author: Nyemo
ce script permet de créer les alignements pour avoir le fichier input
pour la transformation phonetique
"""
import os
import shutil
import tn.letter_alignment as la


def openfiles(inputfile):
    
    with open(inputfile, 'r',  encoding='utf-8') as fichier:
        return fichier.readlines()
    
"""
cmudict = open(newcmu, 'w', encoding='utf-8')
    cmudir = '../cmu/align/' 
    for fn in os.listdir(cmudir):
        if fn.endswith('.align'):
            src = cmudir+fn
            print(src)
            if shutil.copyfileobj(open(src, 'r'), cmudict):
                print('ok')
"""

#------------------------------------
def l2p(inputfile, outputfile):
    """
    input : fichier cmudic phoneme
    separation des caracteres par un espace pour le traitement par l'algo l2p
    """
    print(inputfile)
    #fichier =  open(inputfile , 'r')
    falign = open(outputfile , 'w', encoding='utf-8')
    lines = openfiles(inputfile)
    for line in lines:
        if ("2" not in line) and ("3" not in line) and ("4" not in line):
            data = line.split("\t")
            word = data[0].lower()
            i = 0
            texte = ""
            while i < len(word)-1:
                texte = texte + word[i] + " "
                i += 1
            texte += word[i]
            falign.write(texte+"\t"+data[1])
    falign.close()
        
#----------------------------------------------------------    

def l2palignment(filetoalign):
    """
    input : latter to phone alignment file
    return list like : list[0] and list[1] phoneme
    """
    #fichier =  open('files/faligncorrect.txt' , 'r')
    #falign = open('falign.txt' , 'w')
    lines = openfiles(filetoalign)
    #fichier.close()
    l2p = []
    for line in lines:
        data = line.split("\t") #split la ligne en 2 le word et sa phonetique
        word = data[0] # word
        phone = data[1] # ponetique
        wordsplit = word.split("|")
        phonesplit = phone.split("|")
        i = 0
        globalword = []
        phoneme = []
        retour = ["", ""]
        while i < len(wordsplit)-1: # assume that len(wordsplit) = len(phonesplit)
            wordchunk = wordsplit[i]
            phonechunk = phonesplit[i]
            for c in wordchunk:
                if c != ":":
                    globalword.append(c)
                    phoneme.append(phonechunk)
                
            i += 1
        
        retour[0] =  "".join(globalword)
        retour[1] = phoneme
        l2p.append(retour)
    
    return l2p
    
    
#----------------------------------------------------        

def l2lalignment(filetoalign):
    """
    input : file of words and oovs 
    return : list of word and oov alignment
    """  
    lines = openfiles(filetoalign)
    retour = ["", ""]
    l2l = []
 
    for line in lines:
        retour = ["", ""]
        data = line.split("|") #data[0]= dictionary word, data[1]= oov
        oovalignment = la.l_to_l_alignment(data[0], data[1].strip())
        retour[0] = data[0].strip()
        retour[1] = oovalignment
        
        l2l.append(retour)
        
        
    
    return l2l
        
        
#---------------------------------------------------------
def trainchoice():
    """
     make train data
     input : data
     output : train data to use for l2p and l2l alignment
    """
    fichier =  open('../filesold/pairs.txt' , 'r') #input
    fwords = open('../files/fword.txt' , 'w') # l2l alignment
    fchoice = open('../files/fchoice.txt' , 'w') #l2p
    oovtest = open('../files/oovtest.txt' , 'w')
    lines = fichier.readlines()
    #dictc = {}
    words = []
    oovs = []
    #choices = {}
    
    for line in lines:
        data1 = line.split("\t")
        data = data1[1].split(" ")
        #print(data)
        
        oovs.append(data[0].strip())
        oovtest.write(data[0].strip()+"\n")
        i = 1
        while i < len(data):    
            if data[i] != "|":
                words.append(data[i].strip())
                fchoice.writelines(data[i].strip() + "-" + data[0].strip() + "\n")
                fwords.write(data[i].strip()+"\n")
            i += 1
    
   # for i in range(100):
    #    j = random.randint(1, len(words)-1)
        #choices[oovs[j]] = words[j]
        #fchoice.writelines(words[j] + "-" + oovs[j]+"\n")
        
       
        
        #fwords.write(words[j]+"\n")
        #oovtest.write(oovs[j]+"\n")
        
    fwords.close()
    fchoice.close()
    oovtest.close()

def slang():
    lines = openfiles("../files/slang")
    slang = open("../files/slang.txt", 'w')
    for line in lines:
        data = line.split("##")
        print(len(data))
        
        if len(data) > 1:
            test = data[1].split("#")
            if len(test) == 1:
                slang.write(data[1].strip() + "-" + data[0].strip()+"\n")
    slang.close()
            

#-----------------------------

def addslang():
    lines = openfiles("../files/slang1.txt")
    fwords = open('../files/fword.txt' , 'a') # l2l alignment
    fchoice = open('../files/fchoice.txt' , 'a') #l2p
    oovtest = open('../files/oovtest.txt' , 'a')
    for line in lines:
        data = line.split("-")
        fchoice.writelines(line)
        fwords.write(data[0].strip()+"\n")
        oovtest.write(data[1].strip()+"\n")
    
def wordsyllabe():
    #words = openfiles("../files/fchoice.txt")
    #align = openfiles("../files/lptoalign.align")
    syllabes = openfiles("../ressources/hyphnation.txt")
    #ws = open('../files/wordsyllabe.txt' , 'w')
    ws = open('../cmu/align/cmusyllabe.txt' , 'w')
    error = open('../cmu/align/errorsyllabe.txt' , 'w')
    #newchoice = open('../files/newchoice.txt' , 'w')
    #newalign = open('../files/newalign.align' , 'w')
    newcmu = '../cmu/dict.txt'
    cmuchoice = open('../cmu/align/cmuchoice.txt' , 'w')
    
        
    
    words = openfiles(newcmu)
        
    i = 0
    for word in words:
        #a = word.split("|")
        #w = a[0]
        print(word)
        match = False
        for syllabe in syllabes:
            syl = syllabe.split(" ")
            if len(syl)==2:
                
                if word.strip().lower() == syl[0].lower():
                    print('ok')
                    ws.write("{} {}".format(word.lower(), syl[1]))
                    #newchoice.write(word)
                    #newalign.write(align[i])
                    cmuchoice.write(word.lower())
                    
                    match = True
                    break
        i += 1
        if match==False:
           #print(w)
           error.write("{}\n".format(word.lower()))
    ws.close()
    error.close()
    #newchoice.close()
    #newalign.close()
    #cmudict.close()
                
                
if __name__ == '__main__':
    """
        1. trainchoice() pour choisir les mots et oov
        2. alignement des mots avec phonemes (site cmudict)
        3. l2p() pour input format de l'alignement l2p
        4. excution de l2p(cf script l2p jiampojarma)
        4. crftrainmaker (script crfmaker)
        5. training crf (crf++)
        6. executer 3 et 4 pour le fichier test (eg: cmudict)
        7. creation de fichier json avec input de 7 (script crfout_to_json)
        8. main script pour prédiction 
        
    """
    print("text normalisation")
    #wordsyllabe()
    
    lines = openfiles('../test/kddcup.data_10_percent_2classes_nominal.arff')
    #with open("../test/kdd2.arff", "w", encoding='utf-8') as test:
    with open("../test/kdd2.arff", "w") as test:
        for line in lines:
           data =  line.split(",")
           if data[len(data)-1] != 'normal.\n':
               data[len(data)-1] = 'attack.\n'
           test.write(",".join(data))
           
           
"""
    lines = openfiles('../test/fchoice.txt')
    with open("../test/oovlist.txt", "w", encoding='utf-8') as test:
        for line in lines:
           
            test.write( line.split("-")[1])
    
    
  
      
    #slang()
    #l2p('../files/2314.dict', '../files/lptoalign.txt')
"""