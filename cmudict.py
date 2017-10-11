# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 20:02:29 2017

@author: Nyemo
"""
import os
import shutil
import tn.text_normalisation as tn
def cutlongfile():
    
    fichier =  open('ressources/hyphnation.txt' , 'r', encoding='utf-8')
    ecrire1 =  open('hyph/cmudict1.txt' , 'w', encoding='utf-8')
    ecrire2 =  open('hyph/cmudict2.txt' , 'w', encoding='utf-8')
    ecrire3 =  open('hyph/cmudict3.txt' , 'w', encoding='utf-8')
    ecrire4 =  open('hyph/cmudict4.txt' , 'w', encoding='utf-8')
    ecrire5 =  open('hyph/cmudict5.txt' , 'w', encoding='utf-8')
    ecrire6 =  open('hyph/cmudict6.txt' , 'w', encoding='utf-8')
    ecrire7 =  open('hyph/cmudict7.txt' , 'w', encoding='utf-8')
    ecrire8 =  open('hyph/cmudict8.txt' , 'w', encoding='utf-8')
    ecrire9 =  open('hyph/cmudict9.txt' , 'w', encoding='utf-8')
    #cmudict = fichier.readlines()
    cmudict = tn.openfiles('ressources/hyphnation.txt')
    print(len(cmudict))
    dictc = []
    
     
    i = 0
    for lines in cmudict:
         if ("1" not in lines) and ("2" not in lines) and ("3" not in lines):
             line = lines.split(" ")[0]
             if i <= 20000:
                 ecrire1.writelines(line.strip())
                 ecrire1.write("\n")
             elif i <= 40000:
                 ecrire2.writelines(line.strip())
                 ecrire2.write("\n")
             elif i <= 60000:
                     ecrire3.writelines(line.strip())
                     ecrire3.write("\n")
             elif i <= 80000:
                     ecrire4.writelines(line.strip())
                     ecrire4.write("\n")
             elif i <= 100000:
                     ecrire5.writelines(line.strip())
                     ecrire5.write("\n")
             elif i <= 120000:
                     ecrire6.writelines(line.strip())
                     ecrire6.write("\n")
             elif i <= 140000:
                     ecrire7.writelines(line.strip())
                     ecrire7.write("\n")
             elif i <= 160000:
                     ecrire8.writelines(line.strip())
                     ecrire8.write("\n")
             else:
                ecrire9.writelines(line.strip())
                ecrire9.write("\n")
         i += 1
    
    ecrire1.close()
    ecrire2.close()
    ecrire3.close()
    ecrire4.close()
    ecrire5.close()
    ecrire6.close()
    ecrire7.close()
    ecrire8.close()
    ecrire9.close()

if __name__ == '__main__':
   
    tn.l2p('hyph/1.dict', 'hyph/toalign/1toalign.txt')
    tn.l2p('hyph/2.dict', 'hyph/toalign/2toalign.txt')
    tn.l2p('hyph/3.dict', 'hyph/toalign/3toalign.txt')
    tn.l2p('hyph/4.dict' ,'hyph/toalign/4toalign.txt')
    tn.l2p('hyph/5.dict', 'hyph/toalign/5toalign.txt')
    tn.l2p('hyph/6.dict', 'hyph/toalign/6toalign.txt')
    tn.l2p('hyph/7.dict', 'hyph/toalign/7toalign.txt')
    tn.l2p('hyph/8.dict', 'hyph/toalign/8toalign.txt')
    tn.l2p('hyph/9.dict', 'hyph/toalign/9toalign.txt')
    
    cmudir = 'hyph/toalign/' 
    with open('hyph/hyphenation.txt', 'w', encoding='utf-8') as  hyphenation:
        for fn in os.listdir(cmudir):
            if fn.endswith('toalign.txt'):
                src = cmudir+fn
                print(src)
                if shutil.copyfileobj(open(src, 'r', encoding='utf-8'), hyphenation):
                    print('ok')
        
    
     
    


