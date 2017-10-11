# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:44:11 2017

@author: Nyemo
"""

"""
word : standard word
oov : his variant
line, col : len(oov), len(word)
colIndex : used to have next iteration
digraphs : english common digraph
input : word and his oov
return : oov alignment
"""
def l_to_l_alignment(word, oov):
    digraphs = ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 
                'gl', 'gr', 'ng', 'ph', 'pl', 'pr', 'qu', 'sc', 'sh', 'sk', 
                'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr']
    line = col_index = 0
    aligned_letters = ""
    sequence = ["-" for c in word]  #list of -
    # aligment of the longest common sequence
    while line < len(oov):
        col = col_index
        while col < len(word):
            if oov[line] == word[col]:  #break iteration if matched
                sequence[col] = word[col]
                aligned_letters += word[col]
                col_index = col + 1  #next iteration after loop
                break
            col += 1
        line += 1
    #print(sequence)
    #letter transformation
    sequence[0] =  oov[0]
    p_l_i = 0  #previousLetterIndex
    letter_index = i = 1
    while letter_index < len(sequence):
        if sequence[letter_index] == "-":  #not aligned, need transformation
            if (i < len(oov) and oov[i] not in aligned_letters):
                sequence[letter_index] = oov[i] 
                i += 1
        else:
            if sequence[letter_index-1] == '-':  #sequence[letterIdex-1] not alligned
                 previousLatter = sequence[p_l_i]
                 digraph = previousLatter + sequence[letter_index]
                 if (digraph in digraphs):
                    sequence[p_l_i+1] = sequence[letter_index]
                    sequence[letter_index] = "-"
            i += 1
            p_l_i += 1
        letter_index += 1
    #print(sequence)
    #positioning oov's remaining letters        
    used_letters = [c for c in sequence if (c != "-")]  #used letters
    pos = len(used_letters)
    len_s = len(sequence)    
    while pos < len(oov):
        if pos >= len(sequence):
                sequence.append(oov[pos])
        else:
            moov_index = len_s-2
            while moov_index >= pos:
                if sequence[moov_index] == "-":  #mooving letters
                    sequence[moov_index] = sequence[moov_index+1]
                    sequence[moov_index+1] =  "-"      
                moov_index -= 1
            if sequence[pos] == "-":  #positioning letters after perfomed mooving
                sequence[pos] = oov[pos]
            else:
                if pos == len(sequence) -1:
                    sequence.append(oov[pos])
                else:
                    sequence[pos+1] = oov[pos]  #next position is neccessary - 
        pos += 1
    #checking letter alignment between oov and sequence. 
    #this section is for managing letter repetition inside oov
    used_letters = [c for c in sequence if (c != "-")]  #new used letters
    i = 0
    #print(oov)
    #print(sequence)
    #print(used_letters)
    while i < len(used_letters) and i < len(oov):
        used_letters = [c for c in sequence if (c != "-")]
        #print(i)
        if oov[i] != used_letters[i]:  #mooving to correct position
            #print(oov[i])
            #print(used_letters[i])
            #print(i)
            sequence[i] = oov[i]
        i += 1
    

    #output
    #print(word)
    #print(oov)
    #print("".join(sequence))
    return sequence
                
            
if __name__ == '__main__':            
    print(l_to_l_alignment("ok", "okiiiiiiiiii"))
    """
      #  input : file of words and oovs 
       # return : list of word and oov alignment
"""       
  
                
            
            