from Bio import SeqIO

sequences = []
for seq_record in SeqIO.parse("stringstomatrix.txt", "fasta"):
    sequences.append(str(seq_record.seq))
    # print sequence ID
    print(seq_record.id)
    # print sequence
    print(seq_record.seq)


print("Sequences: ", sequences)


print("length sequences:", len(sequences[0]))
n = len(sequences[0])
prof_matrix = {
    "A": [0] * n,
    "C": [0] * n,
    "G": [0] * n,
    "T": [0] * n,

}

for dna in sequences:
    for position, nucleotide in enumerate(dna):
        prof_matrix[nucleotide][position] += 1


result = []  # list to save nuc with max count in each pos

for position in range(n):
    max_count = 0
    max_nucleotide = None
    for nucleotide in ["A", "C", "G", "T"]:
        count = prof_matrix[nucleotide][position]

        if count > max_count:
            max_count = count
            max_nucleotide = nucleotide
    result.append(max_nucleotide)
consensus = "".join(result)
print("Consensus: ", consensus)
print("A:", *prof_matrix["A"], sep=" ", end="\n")
print("C:", *prof_matrix["C"], sep=" ", end="\n")
print("G:", *prof_matrix["G"], sep=" ", end="\n")
print("T:", *prof_matrix["T"], sep=" ", end="\n")
