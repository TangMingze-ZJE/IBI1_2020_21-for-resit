import os
import re

os.chdir("/Users/23511/IBI1_2020-21/Practical8")
a = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
c = ''
#create a temporary string to store text.
Boole = False
#define a Boolean value to partcipate in circulation below.
s = ''
k = 0
#create a temporary to print text.
for line in a:
    if line.startswith('>'):
    #Reads the header line
        if Boole == True:   
            s = s + ('>'+b+' '+str(len(c)-k)+'\n'+c+'\n')
            #export s including '>', new title,' ', the length of gene, line feed, information of gene, line feed and accumulate s.
            c=''
            #reset value 'c'
            k = 0
            Boole == False
            #change the Boolean value, partcipate in next cycle
        if re.findall(r'unknown',line):
        #reads the header line with 'unknown'
            b = re.findall(r'^>.+?_',line)
            #make 'b' equal to the title. 
            b=b[0]
            #read the first string
            b=b[:-1]
            #remove the end of the first string, make b the new title.
            Boole = True
            #change the Boolean value, partcipate in next cycle
    else:
        if Boole == True:
            c = c + line.strip()+'\n'
            k = k+1
            #read the gene information below 'unknown'
a.close()
z = open('unknown_function.fa','w')
#open new files and write s into it.
z.write(s)
z.close()