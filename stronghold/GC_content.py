#Read data from the file and format
#Clean/prepare the data (format to count GC content easily)
#Format data (store it in convenient way)
#Run needed operation on the data (pass the data to our gc_content function)
#Collect result (Rosalind Submission in our case)

#Read data from the file and format
def readFile (filePath):
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

#Calculate GC gc_content
def gc_content(seq):
    return round(((seq.count('C')+seq.count('G'))/len(seq)*100),6)

##stores file content in a list
FASTAFile = readFile("gc_content.txt")

  #Dictionary for labels + Data
FASTADict = {}
#String for holding the current labels
FASTALabel = ""

#Converting Fasta/List file data into a Dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

#format data, run operations and Collect results

RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}
print(RESULTDict)

MaxGCKey = max(RESULTDict, key=RESULTDict.get)
print(f'{MaxGCKey[1:]} \n{RESULTDict[MaxGCKey]}')
