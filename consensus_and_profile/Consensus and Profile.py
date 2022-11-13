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
