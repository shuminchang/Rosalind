# Can 'for index, dna in enumerate(dnas):' solve this?

a = 'ATCTCTCCTACATGTTGATATACCGGAATTATGGAGCTAACTCGAGACAAGCAATTTGTTGAACAACGACCGGCAGCTGAGAGCCTGTTAATGCGGCGTCTCGAAAGCAGGCGGACCCGCCTAGAGGGACGTGGGAACGGGCACTGAATCACGACAGACCCCTGTGATCCGTCATGTTCTTGCTGAAATATGATTAAGCGCCTTGTACTCGTTACCGTATGGATTACGAAGTATGCTTAAGTCTCGAGCCTGCCCATACGCTCGTTAGTAAAATTTTAGCCTGAAAGTTTTCCTCTCAGTAAACAAGGCGTAACCGAAGGAGTGCCGCGTAGTAAACGTGTTGACATCGGCGTCCGGTGATGCCTCCTTTAGCTTTATTAAAAATCGAAACGCGTAATAGAGGTCGGTTCCAGACACGCTTGTTTGTGGGCCGTACTCGCATGATGAACTGCATGCCATTACGTCTGTCGCAGATGCCCGAGTCCTGGTGTTTTTGAGAAACTGTGCCCCACATAGACCTACGTTTCTCATTGCTTTGATCAATGTCCAAGAAAAGGCTTACAACCAGCAATAGCATCAACCTGCTCGACAATGCTGTGCTGTAAGACCAACTCTTCCCAGTCAGTAATACTGGAACTGAGACCATCTACGGCCCCTCTCTCCGCCCTAAATCGGAATCGCCGGCACGATTGCCACTCGCCCGGGCCCCAGACAGTAAGGCCCCATAGACAGCAGAATATAATCTATGTCTCTGCTGCAAGCTCAGTGCGGTCAATTACTTCCATTATATCATAGTGACATTCCCAACCCTTCCGACCCGAGAATACGTAATCCGCCTGGGTTAGCGATTCAGTGTAGTGGTCCAGCCGATGACTCATTGGCAAGGCCACAGAAAGTCCGTGATACTACAGGAAGTTTAGGGCGTGAGTCTTAGCCGAGTATCGAAGCGAAAGGGGTTCTTCGTGCCGTACGTACCTATTTACCTGTTTGGATTACAACC'
b = 'ATCTCAAGCACGGATCAGGTAACCGCTATGATCGGGGCCATTCTTGAACAGGATTTCCAGGAATAACGGCCGTCAGCTGTTTGCCTGTTTCAACCTCGCTACGAAAACAGGCATTTTATCCAGGTGAGGGGTAGCATCTGACCGTCGTATGCGGCTGAGCCCCCTTGTCCTGCATGCTCTACCTGGTAGTAGATTGACCCACATGAGTAGGCACGAGGTTTTATTACAACGAGTGCTTAAGTAGCCAGCCTGTGCTATCGATGTATCGTCACATATGAGACATGGCATTCAAGTAGCTGTAAACATGGCACGGGGGATTGTGTGGGGCCTTAGAAAAGGGTCGATGCCTCAGGACGTCAAATAGGCGTATCCCCCTAGTTAAAAGGGCCTCCCGTGATCTCGCTCCTTTACAGAAGCGGTTGATTGTAAGCGGTAATCGCCCGAAAAACAAATTGCTATTGTGTCATACGCAGCCGCCCCAATCCCTTGGTGTTGGCGACACTTGCACCATCCAGGACTTAGGTGAATACTAGCAATGTTAAATAAAGTGTAAACGGCCTGGTACTAGCAATACGTGCACGGTTCACAGCTGCGAAGCGGTGTTATCCCTCCTCCCTCAGGCCCGGTATACTGCACCGTGGACCCTCCAGAGCTCATTCCACCGACATACATTACTATCCCGTATACCAGGGCGAGTGGGTAAGGCCCGGCAACGAGTGCCAGCAGTGATTGAGGAAGTGAGGTTATGATATTACGTCAAGTGCGGTGGAGTCAGTTACGCCCATAATATCCTAGTGCCATAAATGTAGCGTACTACGCTAAGATAGCAGCGACGCCCGAGTTAATGGTCCCGGAAATAGGTCCTGCCTTGCCGGGGCAAGTTAGGTGACAGTAAATCCGCGATGATTCCCATCGATAAGGGCTGGTATGCTATCGGGGCCTCGGAGCGTCAGGGTACATAATCCTGGGACTTACTAGTTTGCTGGTTTGAATTACGGGC'

n = 0
mut = 0

while n != len(a):
    if a[n] != b[n]:
        n = n + 1
        mut = mut + 1
    else:
        n = n + 1

print(mut)
