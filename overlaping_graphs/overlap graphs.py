from Bio import SeqIO

with open("overlapgraphsdata.txt") as f:
    fasta_sequences = list(SeqIO.parse(f, 'fasta'))
k = 3
# Part that gets K at the sufix s and prefix p of each string and compares to everyone


def get_pr(dna_seq):
    tmpseq = dna_seq
    nuc = tmpseq[0]
    return(len(tmpseq) - len(tmpseq.lstrip(nuc)))


for fasta1 in fasta_sequences:
    for fasta2 in fasta_sequences:
        name1, sequence1 = fasta1.id, str(fasta1.seq)
        name2, sequence2 = fasta2.id, str(fasta2.seq)
        if sequence1 == sequence2:
            continue
        #pr = get_pr(sequence1)

        suffix = sequence1[-k:]
        prefix = sequence2[:k]
        if prefix == suffix:
            print(name1, name2)


seqs = []
tags = []
nucleotides = ["A", "C", "G", "T"]

for s_record in SeqIO.parse("overlapgraphsdata.txt", "fasta"):
    seqs.append(str(s_record.seq))
    tags.append(str(s_record.id))
