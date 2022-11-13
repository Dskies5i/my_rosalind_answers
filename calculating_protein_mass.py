from Bio import SeqIO
import datetime
# https://www.youtube.com/watch?v=OnDr4J2UXSA&ab_channel=CSDojo
aminoacid_mass = {
    "A":   71.03711,
    "C":   103.00919,
    "D":   115.02694,
    "E":   129.04259,
    "F":  147.06841,
    "G":   57.02146,
    "H":  137.05891,
    "I":   113.08406,
    "K":   128.09496,
    "L":   113.08406,
    "M":  131.04049,
    "N":   114.04293,
    "P":   97.05276,
    "Q":   128.05858,
    "R":   156.10111,
    "S":   87.03203,
    "T":   101.04768,
    "V":   99.06841,
    "W":   186.07931,
    "Y":   163.06333,
}
start_time1 = datetime.datetime.now()
protein = "QQPIQQDHWQYCWDCLEQHLWHAKFHWCGIFRHQGIYHCHPAPPETHVCMKTYAWDSNVEDFMMSFNEHFYGDITYFNFKSFCPGQDRPIGQTHSGVWSSRMNALFYIQTGILWDDNDRTHPTTMTWPWCLPALMLYDTVSFQDWIQYGECWKDPNGPQRCLNIDANFDDAAKCHDPQIYRFYMREPKQIGGCKQHACPSFIGNEKWSTSEIMDECWATTAHVFVLVSPQHGIYHVTCLSKTGEAIAYPLLCTWEWVTMWKRHPKLLVGHFLHMTVLCREALRPMCHDQPDSAKGQFCLYHMKDRYISTEGSIHIFVGSPPPNECERNTPPPIMQEDFRMCPVMLDTKSRFLLGPAFCRRKAQHQPWQSITNFWLITTCTWHSSGADKGLNQVYITYVFDRQILIMKLSRWKCSSFPRRNTGYCIWMVDYTMRYYYYFMHVVSFVCIWATYQTHRYNEVLSKWNICNHPYQPIIGIQVFPVYNKDKHFSMIMRYFFKGINFNMDAHPGMDWLACLAENIMGHSNEASQMCRHCDKVENKSCEHTMFSIMTLCAWPFCYGCPYIVKHCAGGDHERLYMKGRKFLRNDYCTDMTGVPWCETNKYMGPAYTYNVVPHHLLNNLTVRDFTFHHALRTMFAVNSCENCDFAHRHIVRGNMCKTKDACDVRRDMGNTGCNYRLMWGVWMNVTCEGKQMKGIYHVIMCNVYCVTCPVDMILHWAKFMAYQLPGCQKYFAPYWKSWIQVAVYNNKDGPMWCWCIRPNWDQCTGPMTWVIGETLIKFVRSIALFFYNAYDENQNQTPWFRHDEMQLWFEYFYCRYCPTRVDFAGAWDVPHSLVQTEGANNIDTQDWCFCQRFQQHVVACIHFDCCSWLGTVFVEWMLEKMDYWKGMGGKDEPFDNGRTHMPAHDHPMDGWGHSREDWYVAIANKCG"
weight = 0
aminos = []
for i in range(len(protein)):
    if protein[i] in aminoacid_mass:
        weight = weight + aminoacid_mass[protein[i]]
        aminos.append(protein[i])
    else:
        continue
    #print("aminos: ", aminos)
    #print("Peso acumulado: ", weight)
print("SOLUCIÓN 1: Peso total proteina:", weight)
end_time1 = datetime.datetime.now()


class Protein:
    protein = []
    #     # protein_calculating_mass.txt

    def read_protein(self):
        f = open("protein_calculating_mass.txt", "r")
        self.protein = f.read().rstrip()

    def calculate_weight(self, aminoacid_mass):
        w = 0
        aminos = []
        #print("Prot: ", self.protein)
        for i in range(len(self.protein)):
            # print(aminoacid_mass[prot[i]])
            if self.protein[i] in aminoacid_mass:
                w = w + aminoacid_mass[self.protein[i]]
                aminos.append(self.protein[i])
            else:
                continue
        return w


start_time2 = datetime.datetime.now()
protein1 = Protein()
protein1.read_protein()
#print("protein 1", protein1.protein)
weight = protein1.calculate_weight(aminoacid_mass)
print("SOLUCION 2: Total weight", weight)
end_time2 = datetime.datetime.now()

print("Time elapsed SOLUCION 1: ", end_time1 - start_time1)


print("Time elapsed Solucion 2: ", end_time2 - start_time2)
