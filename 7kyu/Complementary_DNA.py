def DNA_strand(dna):
    r = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([r[x] for x in dna])
