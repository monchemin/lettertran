# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:50:33 2017

@author: Nyemo
"""
"""
input : oovs file; each per line
output : word
"""
import os.path
import sys
import oovtoword as otw
oovfile = "test/oovlist.txt"
outfile = "test/predictedlist.txt"
if len(sys.argv) == 3:
    oovfile = sys.argv[1]
    outfile = sys.argv[2]
if os.path.isfile(oovfile):
    otw.oov_to_word(oovfile, outfile)   
else:
    print("No such file : {}".format(oovfile))
