from Bio.Seq import Seq
from Bio import SeqIO
import collections


try:
    f=open("C:\Users\Shelly\Python with genomics\dna2.fasta")
except IOError:
    print("File does not exist!!")
seqs={}
for seq in SeqIO.parse("C:\Users\Shelly\Python with genomics\dna2.fasta","fasta"):
    seqs[seq.id]=seq.seq
allSeq=seqs.values()#list of all seqences

totalRepeats=[]
repeatOf12=[]
for seq in allSeq:
    if len(seq)<12:#disregard any sequence less than 12
        continue
    repeats=[]
    
    for i in range(len(seq)):
        repeats.append(seq[i:i+12])
    repeatOf12=repeatOf12+(repeats[:-11])#leave the last 11 items less than 12
    totalRepeats=totalRepeats+repeatOf12
#print repeatOf12            

counter=collections.Counter(repeatOf12)#counts of each repeats of length 12

listVal=counter.values()#list of frequence of repeats all the 12-base sequence
maxN=max(listVal)#the most frequent number
fre=listVal.count(maxN)#count the frequency of the most frequent number
print fre
