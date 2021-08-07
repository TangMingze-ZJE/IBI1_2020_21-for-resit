import re
import os
dict()
os.chdir("/Users/23511/IBI1_2020-21/Practical8")
f = open(r'/Users/23511/IBI1_2020-21/Practical8/royal.fa')

b = ''
S = ''
c = ''


for line in f:
    if line.startswith('>'):
        b = re.findall(r'^>.+?_',line)
        b = b[0]
        b = b[:-1]
    else:
        c=re.findall(r'.+',line)
        c=c[0]
    
    protein = {
    'TTT':'F','TTC':'F','TTA':'L','TTG':'L','CTT':'L',
    'CTC':'L','CTA':'L','CTG':'L','ATT':'I','ATC':'I',
    'ATA':'J','ATG':'M','GTT':'V','GTC':'V','GTA':'V',
    'GTG':'V','TCT':'S','TCC':'S','TCA':'S','TCG':'S',
    'CCT':'P','CCC':'P','CCA':'P','CCG':'P','ACT':'T',
    'ACC':'T','ACA':'T','ACG':'T','GCT':'A','GCC':'A',
    'GCA':'A','GCG':'A','TAT':'Y','TAC':'Y','TAA':'O',
    'TAG':'U','CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
    'AAT':'N','AAC':'B','AAA':'K','AAG':'K','GAT':'D',
    'GAC':'D','GAA':'E','GAG':'E','TGT':'C','TGC':'C',
    'TGA':'X','TGG':'W','CGT':'R','CGC':'R','CGA':'R',
    'CGG':'R','AGT':'S','AGC':'S','AGA':'R','AGG':'R',
    'GGT':'G','GGC':'G','GGA':'G','GGG':'G'
    }
for i in range(0,len(c),3):
   S = S + protein[c[i:i+3]]
    
a = '>'+b+' '+str(len(S))+'\n'+S
print(a)
z = open('rng.fa','w')
#open new files and write s into it.
z.write(a)
z.close()