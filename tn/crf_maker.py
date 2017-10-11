# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 23:31:10 2017

@author: Nyemo
"""
import os
import text_normalisation as tn

def crftrainmaker(wofile, wpfile, wsfile, out):
    """
        align word, oov and phoneme for the crf++ input train format
        input : word-oov file, word-phoneme file, output
    """
    l_to_l = tn.l2lalignment(wofile)  
    l_to_p = tn.l2palignment(wpfile)
    word_syllabes = tn.openfiles(wsfile)
    crf =  open(out , 'w') #input
    i = 0
    match = 0
    print(len(l_to_l))
    print(len(l_to_p))
    while i < len(l_to_l):   
          
        if l_to_l[i][0] == l_to_p[i][0]:
            syllabes = getsyllabepos(word_syllabes[i].split(" ")[0].strip(), word_syllabes[i].split(" ")[1].strip()) # word's syllabes alignment
            #print(syllabes)
            match += 1 
            word = l_to_l[i][0]
            oov = l_to_l[i][1]
            phoneme = l_to_p[i][1]
            j = 0
            coov = cword = cphoneme = ""
            while j < len(oov):
                coov = oov[j]
                cword =""
                cphoneme =""
                sypos =""
                if j >= len(word):
                    cword = "-"
                    cphoneme = "-"
                    sypos = "-"
                else:
                    cword = word[j]
                    cphoneme = phoneme[j]
                    sypos = syllabes[j]
                #crf.write(cword + " " + cphoneme + " " + coov + "\n")
                crf.write("{}\t{}\t{}\t{}".format(cword, cphoneme, sypos, coov))
                crf.write('\n')
                
                        
                j += 1
        
        else:   
            print(word + " " + "".join(l_to_p[i][0])+" " +"".join(oov) + " " + "".join(phoneme))
        crf.write("\n")
            
        i += 1
    

def crftestmaker(dirname, hyphfile, crftrainfile):
    """ input l2p .align file 
        output : crf test format
    """
    crftrain = open(dirname+"/"+crftrainfile, "w", encoding='utf-8')
    hyph = tn.openfiles(hyphfile)
    dict_align = []
    for filename in os.listdir(dirname):
        if filename.endswith(".align"):  #l2p files
            print(filename)
            dict_align.extend(tn.l2palignment(dirname+"/"+filename)) #l2p call
    
    print("lines : {}".format(len(dict_align)))
    print("hyphenation : {}".format(len(hyph)))
    #print(dict_align)
    j = 0
    while j < len(dict_align)-1:
        i = 0
        lp = dict_align[j]
        wh = getsyllabepos(hyph[j].split(" ")[0].strip(), hyph[j].split(" ")[1].strip()) 
        if len(wh) == 0:
            print(j)
            print(hyph[j].split(" ")[0].strip())
        while i < len(lp[0]): # assume that len(lp[0] == len(lp[1]))
            #print(lp[0][i]) 
            #print(lp[1][i])
            #print(wh[i])
            crftrain.write(lp[0][i] + "\t" + lp[1][i] + "\t" + wh[i]+ "\n")
            i += 1
        crftrain.write("\n")
        j += 1
        

def getsyllabepos(word, syllabe):
   
    #i = 0
    sypos = []
    for sy in syllabe.split("-"):
        
        if len(sy) == 1:
            sypos.append('b')
        else:
            j = 0
            while j < len(sy):
                if j == 0:
                    #syldict[word[i]]='b'
                    sypos.append('b')
                elif j == len(sy)-1:
                    #syldict[word[i]]='e'
                    sypos.append('e')
                else:
                    #syldict[word[i]]=' '
                    sypos.append('-')
                j += 1
           # i += 1
    if len(sypos) == len(word):
        
        
        return sypos
    else:
        
        return []
         
def checktrainfile(trainfile):
    lines = tn.openfiles(trainfile)
    i = 1
    for line in lines:
        if line != '\n' and len(line.strip().split(" ")) != 4:
            print("{} | {}".format(i, line))
        i += 1
#letter_phoneme_align('cmu/align', 'crfcmutrain.txt')
if __name__ == '__main__':
    #crftrainmaker('../files/newchoice.txt', '../files/newalign.align', '../files/wordsyllabe.txt', '../crf/newcrftrain1.txt')
    #print(getsyllabepos('cigarette', 'cig-a-rette'))
    #checktrainfile('../crf/newcrftrain1.txt')  
    crftestmaker('../hyph/toalign', '../hyph/wordhyphenation.txt', 'hyphtest.txt')
    """
    s = tn.openfiles('../files/wordsyllabe.txt')
    i = 1
    for line in s:
        w, sy = line.split(" ")
        print("{},{}".format(w,sy))
        a = len(getsyllabepos(w.strip(), sy.strip()))
        print(a)
        if a==0:
            print("{} {}".format(i, line))
        i += 1
            
      """                  