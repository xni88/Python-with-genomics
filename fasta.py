try:
    f=open("C:\Users\Shelly\Python with genomics\dna2.fasta")
except IOError:
    print("File does not exist!!")
seqs={}
for line in f:
    line=line.rstrip()
    if line.startswith('>'):
        words=line.split()
        name=words[0][1:]
        seqs[name]=''
    else:
       seqs[name]=seqs[name]+line
#number of records in the fasta file
print len(seqs.keys())
a=[]
for i in seqs.values():
    a.append(len(i))    
#longest length of the sequence
print max(a)
#shortest length of the sequence
print min(a)
for x, y in seqs.items():
    if len(y)==max(a):
        print x #identifier of the longest length
    elif len(y)==min(a):
        print x #identifier of the shortest length


f.close()      
