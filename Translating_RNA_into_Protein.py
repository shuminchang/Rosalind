'''
Problem
http://rosalind.info/problems/prot/
'''
# make a dict of RNA codon table
d = {'UUU': 'F', 'UUC': 'F',
        'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y',
        'UAA': '', 'UAG': '', 'UGA': '',
        'UGU': 'C', 'UGC': 'C',
        'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H',
        'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
        'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N',
        'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S',
        'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D',
        'GAA': 'E', 'GAG': 'E', 
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}

# split RNA strand by 3 letters each and store as a list
def split(RNA, num):
    return [ RNA[start:start+num] for start in range(0, len(RNA), num) ]
RNA = "AUGGGCCAU"
x = split(RNA, 3)

# compare list x and dict d, append the correct value to protein_list

protein_list = [value for string in x for key, value in d.items() if key == string]

''' 
protein_list = []
for string in x:
    for key, value in d.items():
        if i == string:
            protein_list.append(value)  # the order of the list depends on the first 'for' loop
'''

# convert protein_list to string.
protein_str = ''.join(protein_list)
protein_str
