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
repeatOf7=[]
for seq in allSeq:
    if len(seq)<7:#disregard any sequence less than 7
        continue
    repeats=[]
    for i in range(len(seq)):
        repeats.append(seq[i:i+7])
    repeatOf7=repeatOf7+(repeats[:-6])#leave the last 6 items less than 7
    totalRepeats=totalRepeats+repeatOf7

counter=collections.Counter(repeatOf7)#counts of each repeats of length 7
print counter.most_common(1)

