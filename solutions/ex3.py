import random

bases = ["A", "C", "T", "G"]

dna = "".join([ random.choice(bases) for i in range(20) ])

def paired(dna):
    pdna = ""
    for base in dna:
        if base == "A":
            pdna += "T"
        if base == "T":
            pdna += "A"
        if base == "C":
            pdna += "G"
        if base == "G":
            pdna += "C"
    return pdna[::-1]
    
print dna
print paired(dna)