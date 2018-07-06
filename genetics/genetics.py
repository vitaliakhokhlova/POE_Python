import csv

dna_string = ""

with open("dna.txt") as f:
    for row in csv.reader(f):
        dna_string = row

class Nucleotide:
    symbol = ''
    NAMES = {'A': "Adenine",
             'C': "Cytosine",
             'T': "Thymine",
             'G': "Guanine",
             'U': "Uracil"}
    SYMBOLS = ['A', 'C', 'T', 'G']

    def __init__(self, symbol):
        symbol = symbol.upper()
        if symbol in Nucleotide.NAMES:
            self.symbol = symbol
        else:
            print("Error: no nucleotide with this symbol")

    def __repr__(self):
        return f"{self.symbol}"

    def get_name(self):
        return Nucleotide.NAMES[self.symbol]

    def get_complementary(self, RNA):
        if RNA and self.symbol == 'A':
            return Nucleotide('U')
        if RNA and self.symbol == 'U':
            return Nucleotide('A')
        index = Nucleotide.SYMBOLS.index(self.symbol)
        symbol = Nucleotide.SYMBOLS[(index+2) % 4]
        return Nucleotide(symbol)

class NucleicAcid:
    strand =[]
    RNA = False
    def __init__(self, chain, RNA):
        if chain.find("U") != -1 and not RNA:
            print("Error: 'U' can not be in DNA")
        if chain.find("T") != -1 and RNA:
            print("Error: 'T' can not be in RNA")
        for c in chain:
            self.strand.append(Nucleotide(c))
        self.RNA = RNA

    def __repr__(self):
        return f"{self.strand}"

    def get_complementary(self, RNA):
        compl = []
        for n in self.strand:
            compl.append(n.get_complementary(RNA))
        cdna = NucleicAcid("",RNA)
        cdna.strand = compl
        return cdna

class Ribosome:
    CODONS = {"UUU": 'F',
              "UUC": 'F',
              "UUA": 'L',
              "UUG": 'L',
              "CUU": 'L',
              "CUC": 'L',
              "CUA": 'L',
              "CUG": 'L',
              "AUU": 'I',
              "AUC": 'I',
              "AUA": 'I',
              "AUG": 'M',
              "GUU": 'V',
              "GUC": 'V',
              "GUA": 'V',
              "GUG": 'V',
              "UCU": 'S',
              "UCC": 'S',
              "UCA": 'S',
              "UCG": 'S',
              "CCU": 'P',
              "CCC": 'P',
              "CCA": 'P',
              "CCG": 'P',
              "ACU": 'T',
              "ACC": 'T',
              "ACA": 'T',
              "ACG": 'T',
              "GCU": 'A',
              "GCC": 'A',
              "GCA": 'A',
              "GCG": 'A',
              "UAU": 'Y',
              "UAC": 'Y',
              "UAA": ' ',
              "UAG": ' ',
              "CAU": 'H',
              "CAC": 'H',
              "CAA": 'Q',
              "CAG": 'Q',
              "AAU": 'N',
              "AAC": 'N',
              "AAA": 'K',
              "AAG": 'K',
              "GAU": 'D',
              "GAC": 'D',
              "GAA": 'E',
              "GAG": 'E',
              "UGU": 'C',
              "UGC": 'C',
              "UGA": ' ',
              "UGG": 'W',
              "CGU": 'R',
              "CGC": 'R',
              "CGA": 'R',
              "CGG": 'R',
              "AGU": 'S',
              "AGC": 'S',
              "AGA": 'R',
              "AGG": 'R',
              "GGU": 'G',
              "GGC": 'G',
              "GGA": 'G',
              "GGG": 'G'}
    def read_codons(self, NucleicAcid):
        if not NucleicAcid.RNA:
            print("Can not translate a DNA, need an RNA")
            return 0
        codonList = []
        for i in range(0, len(NucleicAcid.strand)-2, 3):
            codon=""
            for j in  range(i, i+3):
                codon += (NucleicAcid.strand[j].symbol)
            codonList.append(codon)
        return codonList

    def translate(self, NucleicAcid):
        aminoAcidList = []
        codonList = self.read_codons(NucleicAcid)
        for c in codonList:
            aminoAcidList.append(AminoAcid(Ribosome.CODONS[c]))
        return aminoAcidList

    def factory(self, NucleicAcid):
        peptideList = []
        aminoAcidList = self.translate(NucleicAcid)
        peptide = []
        for a in aminoAcidList:
            if a.symbol != ' ':
                peptide.append(a)
            else:
                if len(peptide) > 1:
                    peptideList.append(peptide)
                peptide = []
        return peptideList

class AminoAcid:
    symbol = ''
    name = ""
    trigram = ""

    def __init__(self, symbol):
        self.symbol = symbol

    def __repr__(self):
        return f"{self.symbol}"



dna = NucleicAcid(dna_string[0], False)
print(dna)
rna = dna.get_complementary(True);
print(rna)
codonList = Ribosome().read_codons(rna)
aminoAcidList = Ribosome().translate(rna)
print(aminoAcidList)
#peptideList = Ribosome().factory(rna)
#print(peptideList)
#print(len(peptideList))
