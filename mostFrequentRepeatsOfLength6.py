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
repeatOf6=[]
for seq in allSeq:
    if len(seq)<6:#disregard any sequence less than 6
        continue
    repeats=[]
    for i in range(len(seq)):
        repeats.append(seq[i:i+6])
    repeatOf6=repeatOf6+(repeats[:-5])#leave the last 5 items less than 6
    totalRepeats=totalRepeats+repeatOf6

counter=collections.Counter(repeatOf6)#counts of each repeats of length 6
print counter.most_common(1)

