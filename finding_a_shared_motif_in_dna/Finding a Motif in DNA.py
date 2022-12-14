from Bio.Seq import Seq
from Bio import SeqUtils
# works:
pattern = Seq("ATAT")
sequence = Seq("GATATATGCATATACTT")
results = SeqUtils.nt_search(str(sequence), pattern)
print(results)

# print(int(results[i]) + 1)

# method 2
seq = "AGACTAACTAATCCTAACTAGCTAACTAAACTAACTACCTAACTAGCTAACTACGCAGCCTAACTACTAACTAGTCAAGACTAACTACGCCTAACTACTAACTAATTTCTAACTAAGTCCTAACTACTAACTACATCTAACTAAACTAACTACTAACTAACGCTAACTATGACACTAACTAGTCTAACTATCTAACTACCATGCCTAACTAGCTAACTAGGAGGCTAACTATCTAACTACCTAACTAGCTAACTACCTAACTAGCAAATGCTAACTAAAGAGCTTTGCTAACTACGAATCAGCTAACTATCTAACTAGGACTAACTATAGTACTAACTAACGGTACTAACTACTAACTACCTAACTACCTAACTATCTCATCTAACTACACACTAACTAATCGACTAACTACTCGACCTAACTAACATTCTAACTAGTCTAGCTAACTAAACGACTAACTACTAACTAGGAGTAGGCTAACTAAGTGATCTAACTACCGGCTTTTTCTAACTAGCTAACTAATACTCTAACTATTGCTAACTAACTAACTACTAACTACTAACTAGCTAACTACTAACTACTGTACTAACTATTGTTCCAGCATTATTCACCTAACTAAACAATTTACTAACTAAATTCTAACTACTAACTAGCGGATATGCTAACTACTAACTAACTATGTCTAACTACTAACTAATCCTAACTACTAACTATGCTAACTAAATCCCACTAACTAAATCGATCCCTAACTAACTAACTACCTAACTATCCTAACTAACTAACTAGCTAACTACTCTAACTAAGGCCTAACTACTAACTACCTAACTAGATGCTAACTACTAACTAAGCGTAGCCTAACTACTTCTAACTAATCTAACTAGGTGTGAGAGGCTAACTAGGAACTAACTAGACTAACTATGCCCTAACTACTCTAACTA"
motif = "CTAACTACT"


def find_motif(seq, motif):
    start = 0
    count = 0
    """GC content in a DNA/RNA subsequence of default length k=20"""
   # Search through the string till
    # we reach the end of it
    while start < len(seq):

        # Check if a substring is present from
        # 'start' position till the end
        pos = seq.find(motif, start)

        if pos != -1:
            # If a substring is present, move 'start' to
            # the next position from start of the substring
            start = pos + 1

            # Increment the count
            count += 1
        else:
            # If no further substring is present
            break
    # return the value of count
    return count


# Driver Code
print(find_motif(seq, motif))


def find_motif2(seq, motif):
    count = 0
    pos = []
    for x in range(len(seq) - len(motif) + 1):  # how it works?
        if seq[x:x + len(motif)] == motif:  # how it works?
            count += 1
            pos.append(str(x + 1))
    return pos


    # Driver Code
print(find_motif2(seq, motif))
for item in find_motif2(seq, motif):

    print(item, end=" ")

s1 = "AGACTAACTAATCCTAACTAGCTAACTAAACTAACTACCTAACTAGCTAACTACGCAGCCTAACTACTAACTAGTCAAGACTAACTACGCCTAACTACTAACTAATTTCTAACTAAGTCCTAACTACTAACTACATCTAACTAAACTAACTACTAACTAACGCTAACTATGACACTAACTAGTCTAACTATCTAACTACCATGCCTAACTAGCTAACTAGGAGGCTAACTATCTAACTACCTAACTAGCTAACTACCTAACTAGCAAATGCTAACTAAAGAGCTTTGCTAACTACGAATCAGCTAACTATCTAACTAGGACTAACTATAGTACTAACTAACGGTACTAACTACTAACTACCTAACTACCTAACTATCTCATCTAACTACACACTAACTAATCGACTAACTACTCGACCTAACTAACATTCTAACTAGTCTAGCTAACTAAACGACTAACTACTAACTAGGAGTAGGCTAACTAAGTGATCTAACTACCGGCTTTTTCTAACTAGCTAACTAATACTCTAACTATTGCTAACTAACTAACTACTAACTACTAACTAGCTAACTACTAACTACTGTACTAACTATTGTTCCAGCATTATTCACCTAACTAAACAATTTACTAACTAAATTCTAACTACTAACTAGCGGATATGCTAACTACTAACTAACTATGTCTAACTACTAACTAATCCTAACTACTAACTATGCTAACTAAATCCCACTAACTAAATCGATCCCTAACTAACTAACTACCTAACTATCCTAACTAACTAACTAGCTAACTACTCTAACTAAGGCCTAACTACTAACTACCTAACTAGATGCTAACTACTAACTAAGCGTAGCCTAACTACTTCTAACTAATCTAACTAGGTGTGAGAGGCTAACTAGGAACTAACTAGACTAACTATGCCCTAACTACTCTAACTA"
s2 = "CTAACTACT"

#method 4
for i in range(len(s1)):
    if s1[i:].startswith(s2):
        print(i + 1, end=" ")
