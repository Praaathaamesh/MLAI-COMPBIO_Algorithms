def approximate_pattern_matching(pattern, text, d):
    occurrences = []

    for i in range(len(text) - len(pattern) + 1):
        substring = text[i:i + len(pattern)]
        mismatch_count = sum(1 for p, t in zip(pattern, substring) if p != t)

        if mismatch_count <= d:
            occurrences.append(i)

    return occurrences

ANS = approximate_pattern_matching("CGGGAATTGCTG", "AATGCTAGCTAACGAAGGTGGATAGCTATATTATATGTTTTGTGTGAGTCAGGGTGTGCGAGCTTAGTAGGGCTGTAGTTTCTAGACGGCCCTTTGGTTCAATGAAATCGTAGGTGTTGCGTTCACTCCTCACGACCATGACTCACCAACCATATTCATTCAGGCTAGGTTAGGGGATTTGAAGGCAATATCTTGGGGAGGGCACAAACACTAATGGCGACACACGACACTATGGTTTCGGCCGGCTCAAAGGCCGCGTACGCGCTTTTTCGTGCGCGGACGAATATCAGCCTAAATCAAGAAACGAACACAAAGTGTACGGGCAAGCTCGTTAGTCGTACGTTCATACGCTAGCGCCTGGTGGTACTATCCTTGCATAATATGTCAATACCGCTTCACTCTCCTGGGCCGGATTACGGACTTACCGAGTGCTAATCCTAGTGCTACCCATCTTGGCGGGCCATGTTCCCTACCTTCGCATCCTACCTAGCTAAGGGAATAGATTGTACGATCCCTGGATTATTAGACCAGACGTAAATAAACAGATGAATTCTATGCTAAGGCCGTATCAACTGTCCTCACACTGATGCCCAGGTCTTGTAACAAAATAGAACAACCTACGCGTCCGCGGGATGTCTGGGAAATGATCCGTTATCGGCTATACACTGTTCCTTTTGACCTTGGTACCCATTTCTCGCTACGAGCAACTTATCTGGTAAATAGGGTACGGAGTTCGCAGTCGAGTCCCAGAATTTCGAAACCGGTCTCTTCAGGAGGAAGACCACCACATCCTTGCGCGCCCGGAAGGCCACGGATCTTGGCCGATTCAGCGTGAAGACCCCCGGCTCACCATACAATAGGCCTTCAAGTCCATATACTTAGTCTGTACAAGCAGGGTCACAGGCTTTCAGATGACCCTATTAGCCTAGATCGTCAGAGGTAGTAAAACTAGCATATCTGCTACATCATCCCGGCAAGGTGCGAGTCCAGCGCCTCGAAATTCACAGGTTGACGCAACTCAGGATCTGAAGTCAAGTGCTCTTGTTCGTTAGGCAGTATGGAGGCCTGTATTGATCTTGGTGCACGCCAGATTATCTCTTATGAGAACCCACGCCGTGTTATAACAATGCCATCTTCTTTGTCTAAGTCCCCCTCTCTGGCGATCAATTCTAGTACCCTACTACGTGAATCAGTCGTATGCCACCATGGCGCACTCCATGCCTGTGTCGGCACAGTATAAAAGCAGGCTGTGTTCTTCGCTCTATTTGATCCTAGGCGCATCTCACACAATCGTTATGAGATCACGCTGCTAGACTAAGCTAAATCAACTTCACGGGCAGGTAGCACTCCGTACACGTCGACTTCATACACGAAACGCCAATCCCAGGGCGGGGAGTGTAGATGAAACAGGCCGTACCATACTTACGATTGCATTTCCTGCCCATGGATGACCTTCTTAAGGCTGTATAGGAGCCCGCATAAGCTCTACATACTAACTGCTGTGACATTCGGGCAGATACATGCTATTCGGGACCTGCGGAAGAGAAAGTTTCACGTGCTCCTAGTGACAATTCCAGTTAAGTCCTCCCACTGGGCCGGACTTTCAGCATCTCTGTGACGTCTTCTCTGCAAACTCCTGGTCAGGGCATGCACAGAACCAATTCGGGGATCAAAGTCCGGGTTCTGACACCACGATACGAATCAAAACAGTAACCGTACGACTAATGAACCTAAACACCGTAGCGTCTTTCACAGGAAAACACTATAACATCCGGTAGAGTAACGTTGATAACAGGATTCTAACCCAAATAAGGTCACCCTCGGGGATCATAGTTCGATCCGCCCACAGGCACCCTATAAACCGCATACGACTTCACCAAGACCAGTTCTTATCCTGGCAGGCGGGTTGAACGCCGCACGTCCTTGTGTGCACTCGTGTATACTCAATGGGCGTCACAGAGTCAGTATATAAGCATCTGTCTGACTGGCGTAACACGCCTATTGGTTAGGAGTTCTATAGCACCGCCCGGCGCCGGATGGTCTCGAACACGTCACAACCTACAGTTAGATGTACATCTGGCCATGTAAACCCTAGGCGTTTGATTAAGCTACTATCTGTTAACCCGTCGAACAAGAACAGACTAAACGCCGTTTAGTCCGAACAACTCTCTGAGACAGTGTTCTATTATGCTTTTTCGTCCCTGAAAGGACAAGATGATGCCACTTCGAGGGTGCAGCACCCCTTGAGACCGTTCTGAGAAGTGTTCAGCGATATCTTTTCTGGCTCAATCTCTCGATTGCCTCCGCTGAAAACTGTTAAACATAAATTTTAGCGTCTTAGCGACTTCGTTGTCACCATTACGTCTATGCCGGCAAAGGGGCGCTATATTCAAAACCTGCGTATGGTCAAAGCGCGAGAACCCAGTCTCGCCATCAGCCTCAGGCAGCTACCCCCGGGTCTGTGACATGACGCGAATTAATTGTCGGAACTCTCCCGATTACTAATAAATTTGTACAAGGATCACGATGGTCTATGTCAGGTAGTCGTGAGGGCGTGGGGATAGCTAAACGCACTTATGCCCATTAGATGGAGGACTGTATCACAGCGGGACGACGGAGGCATGTTGGCGCGCGAAGATGCTTCCGACAGCCCTATCAACCCATTGAGGACCTAGACCCATAGATACCCGTGGCATACTTTTTATGATACAGGATTAGACGCGCAGAGAATCTGCCAACCAGATCGGTTGCCGACTCGCTCCGGAAAGTATCTGTCTTCCAGATAGGCGGTGGAGCGAAAACTAATAATACCTGCTTGCTCCCGAGAGCTCAACGAGTGGTGAGAGAGCGTTGTCTTTCGTGATCGAGACGCCGTAGAAGTAATGCTGATAACGGTGGGTAGTGGCCTCATAGGCCTATGTCACGATCTAGCCTTAATCCGCCACCCGTGGGCATGAGTTCACTGTATACTTAGTGGTATGCAGCCCTCCCCTAGCTCGACCGAATGTTTAGCGTACCTATCAGCTGCACAGACACTGTGTGCGGTTTGGAAGAAATGCGGCTACGACTGGAATTGTCAATTGCTTCCTGTTATCGTGGCCAACAGTGCAAAAGTGCTGTCTCGGTGCCTCCCCAAGACGGCTACACTGTGAGAGCGCGGTTCAGGACCCACAGAGCTGCGAGTCCTAATCTTTTCGAGCGAGTCATTAGGCGGCTGTAGTATTAAGATTCTCATGAGGAGACGCGCAACCCGCAAATGAGTCACAATCGACTACTACCTTATCGTTTTCGTAGTTCGGGTCGTATCGAGATTGAGTACTGGCCTACAATACTAGACCTAGGCACAACAAAAGGGCCCATTTCGGGAGTTGCCTTACCACGTCCGTATCTTATAGAAGGCAGGCGTCTCATCAGCGGTTTTGTGGTGCAAGTTATTATTTAGAAACTATCCGGGGCGCGAGAGAGAACATGGGACCGCGCAAGCCGCGCCAGGATAAGTGTGTGGTTGGCCTACGGATGCTCCAGGTATTTCATGCGACCTACATTGTCCCCAGTAACTATAAGAAAAGATTAGTTCGGGCACGCCAATATATACCAAGGGTCCATTGACTTTTCGCCATGATCTCGGGACCATTGATGGTAATGAGCGCAGTGGATTAGCGGACCGTGACAAATTGGCCGACATGAACATAATGGGTGCGAACAGGTAAATTCGGACGTCCCGGCGAGTTATATTAACCACAGAGAGTCTACCGAACTGGTCCGAGAGTAGTCTGAAGATTCGGCCACTGCTTTCGATTAGCGTAACAGGGCACTTCTACGCAGTTTACCTCGACCGCTCCTTGGTCGAACCGGAGGGGATTAGAACATCGATGCGCTTGATTCTATACTGAAGGAGCTCGAGACATAGAATCTTACCCACTCATCATGATCAAGCTTGCAATTCAAACCGGTTTCATGCCATGTTGCTACAGCAGCTAGTGCGCTGACGCTACACGGGCGTATATGGGAGGATGTGCTTCAACACCCCATCTACCGGAACCAGTCCACATACAGGATCGGACTCACTAGGAGTGACCACTACTGATCATTTACATATTTCACTCGAACCTACCAAGATGCTTGAGCTAACCCGGATGTGCTTGGAGATAACGGAAGCTCGACAGATCGCAGCTGTGTAGTAGTACGGGTGAAGCGGACCTAGAACTGTCAAGTAGGTGCTATCCGATGTTCGGCACATCGCTATTTAGTAGTTCGCCCAGTTTGCTAGACGTCCCTATGCTCCCTCCACTTGCATTCGTTCATCGATGTCGTATGTATGCTTAACTGGTCGTCTAACCTTGTAATTGACTGCCGAGTGCTGCTGTATTCCGAGGGATCCCCGAGACCGTAGGTTACCGAGCGACCTCGGTGTTAGATGGATTCTAATGAAAGTGTCTCCATGAATTCTAGTTCAGACATTAAGACCCTTGTTCGTGGGCTACGAAACCTGACGAACTATCTGTGTGGGGACTCCGGTGGAATGATTTAGCCAAAGAGTCTGCAGGATCCTCCTTTCGTGCGCTGAAGTTTCAGCTTGTGTATACACGACCAATCACCATGATGGCATAGTGAATACAATGGTTATAGTGCGCTGTCCGCGGGTGCGGTTCCAATGCGACATTGTCCCCTGCGTATCGGCACAACATGATTGATGACGTCATACTGTACCCTCCCGCGAAACACCCACTCCTGGCGGAGATTACATGTAGTCAGGTAGGACGGCCACTCCGATGGCCTCTAGTGGCGTTATATATTCCCCATCGGTCGACTGGCCCCGAGTGAGGGGTTAACTTCCGGTATCCAGTATAAGTCCGACCAAATTTAGCCAGCTAGCATTCCCGAACACCATCTCGGAGTCGCTCAGCGCTAAACTTACGCAAGAGCTTGCTGGCCTACAGATCGAGACGTCTACGCATTTCCCTCGCGTAGCTGCCAGTCGGAGTCCTTTAGTACGAACCGCACAGAATCCCAAGTAAAAGGGCCGTTGCGAAAAGTCATAGCAATTGATTTCGTCCAATCCCGGTCTGTCTTGACCGGCGCATAAATAGGCGTTTCCCTGGCATACTATCCACATCTCCTACGCCCGAAGTTTTCACTCTGGCTATGAACGCCGTCTTCAGCGCGGTAGCTGGATCAACCTTCGCAAGCGCCGGGAAACTGTAATAAAAAACCACTTCCTATATGCCCGCCCCATCTCCCTTCGCAGGTGAGAGTCGAAGATCGAGGTGCTAACGCGATCCTATCGCCTGAAGGTGAGGTCGAATGGATTCTTCACTGTCTCCGCAAACACCGAAACATTAATTTGTAACTGGTACAGTTATCACGAAGTGACAGACCTAATCGCGAGTGGAGTGCGGAATACGGTGCGGTGAGAGTGATAGGCTTTGGTTGCAACAGAGACTTCAGGAGTACTGTTCAAGGGCCCGCAGAGTTAAAATACTTGGTCGAGGCCGAATCATTCGTGGCCAGGGGTGTTATTGGTTGTTATCATTTACCTTTCCCCCTCCTGGAGTCCTGGACCGCACGGTTAGTCCCACATACCCGACCGAGTGGCCGTCTATAAGGACGGTATAGCTCGATTCAGTCCTGTAGCCTAGACCCGGAAAGTGGTGACGAAAAGGGGGATGAGTAAACACTATCTGGCGGAAATAGCGTACTTCAAGTTACCTTTCAGATAATCGGCGACAAGCTTAAAGCTTTTAAAAGTGTGACACGTTAATGTGGCTCTTACGTCCTATCCAGGGCTTAGGAAACTAGGCATTAAGATTTGATCCGAGGTGACGCCCATCCTTGGACTACCGAGTAGATATACTATCTATAGGCACGCGCTCAGAACGCGCATAAGCGCTCATCACTCATACTTACCTGGACCTAGAGGCGCTCTTAAGGTCTTTGTTTACCCTAAAATTGCTCTAGAACGAAGACAGCTGAGTAAGCAGGATTCGGGTTCGCTGTTAGGAGTGGGTATTCGCGCGTTGGGGGGACACTACCGCTTGTGTGGTATCCTGTATCCTTGCGTGTGGGACAACCCGGCCGCTTTACCTTCTAGCTATGGAAAGACCCTGCGCCGCGCCGGGCATCGTGATTAAGCTTCACCGGAGGGTACTGAGTCTACTAACTAGCGCCTGGGGTCCGAAAAGTCTGCGCTTTGGGATTGACGATCTTCATGGCCGAGGAGCTCCATGCCGTCATGTGCCAAAGACCCGAAGACGTATACGCTTTGACACTCAGCCAATAGCTTACGTCCCTCCTGTCGTCATTTCGAACCGGATTGGTTCTTGCGGTTAATACCATCAATATGCGACATGAGGAATTTAATTGAGGCACACTAACTAAGCGGTCTACCTAAGGCGCTTCGAGACTGCCAATCCCATGCGGGATGGATCATGAAGCCCTGACGCTGAGGCTCCTTTGATCGAGCACGGTTGGTCCTGGAACCATGAGCCAACCAAGCTGATGGCGCACGGTTGACGGATACTCGCGCCGATACAGTGACATGATTGTGGGCAAGAGTTAACAACGTACCTGGATCCTAATTGTATTGCTGCGCGCCGTTAATTGGGTAGCCATCTTGGCACCCTGTCGAGAACGAACTCTATTGGAGTAAGGAGACTACATTTTCTCTAATCATAGGGTTACTGTTTCCTAGATATGTTAGCTGATATCCCTTGTGCGGATTAGTTCGTCACGAAGTAATCCAGGATAAACTGCCGCCATAACTGTTTGTTGTTGCTTATACGAGGCAAAGCTTCCAGAACTGAGCTGGAAATGCAACTACGCGGATATCCAGGTTGGGAAGTGTGCGGAGCTAACAACACCTATGGTCTTGTATTGCATGTTTCGATTGCAAAACGCGAATCTGACACCATCGTCAAGCTTTGCGTTAGGAGCGAGACGGCGTCCGACTCGATATCTACACGTATGGTCGGTGACTTGCTTATCAAAACGTCGCAAAAGGACGTCCATGGGTCTTAGAGCAGTTGTGTGTACCGCTCGAAGATATTTGGGCGCAAGAGCTCTTCAACGTCGCCGTGCTTGCCATTCCTCTCGTGAGTGGTTCGTTTTCGCTCGCGCGTTGCAACTTCAATATAACATGCACGAGCATAAATCCGGCTCTAAAACCGTGCAAAGCGGATATTCCCCCCTCTAGGCGCATAGCGACGCGTTTACGCCTGTGCGAATACGAAGCGAATTCCAATATACGTGGCCTCTTTCGCCAACTTTCGTTGTTCTAACGGTTAACCAATGGGTAGCTAAAATGAGTCGGTTTAGCGTAACAACCAATGTACCCTCTTTTAACTTGTGGATCGCTAGCCAATTCATGTTCAGATATTCTCGCCCAAACTTCTCCTAACAACGTGCGACTTGCTCTGAGCTATCGAGACCATCGCTGTGGTTACTTAGTCAAGGTTTAAGCATCGGATATTATCACTGGACTTCTTACACCTAAGGGGCCCTAGCAGCAAAGGCTACGGGGCCGCTCGAGTTGTCGAATCAGCCTCAAACAAGATGCCACGCAAAACTAAACCATGACACTACGTATACGATGCGGACAGTTGGGAAATAATAAAGCCGTGGTCTTGGCCATGGCTCGTGACCCCAGTCGTTGGAATCCGACGGGCGTCAAATTCTGCGTTCCCAAGATGCGTTCTGCGCGATTCTTGAGGGTGCAGCTCTGGTGCCCCACTCTCCTTAGTAGCGGCGACCACTGTATAGCGGAGTTATCAGGCGAAGACAAACCCAATTGTGGACACTTTGATTCATGCTCCATGGAGGGGCGACTCAAGTTATGACGTAGGACCGCGACGCTACTGGTAGCATCATCCCCAGCTCCATCGGCTAAAGGGGGCCTATCTCTCACCGATTCATCCGTAGCCAAATCTCCCGAGCACCCTGTGTGTAGTTTAGATAATTAACATGACTCGACTAAGGGCTTTTTGTTAAACACAGTCAGATCTCCGGCTCCATCTACATAGAAACCCTAAGAGCAAATTGCTCGCAGGGCGTGTATTGTGTGCGCGAGTAAAATTTGAAGGTCCTGGAATTGGCGGAGCGTGTCACCACCGTAAGACGTTGTCTCTCACCAGCATGGCTCTTCCATTGACCTGTAGTAAGCCCAGCCATCCGAATTCTTACCATTATGAATTGCCAGAACTCGAAAGTGTGGACGCCTAATAGGACGACTACTTTACGCTAGACCGGCAGATCTAGAAGATCGGCTAACCTTGCCATCCCCTTTTTCCCCGTCGAACATTAGCTGGGCTACCAAGTAGCTGCCTCACCCGATAATCAACCATTTCGGGGATGTAAGATTCGTCCGCATCCTAACTCTCAAGTTTGCGAAGGATCGTTCGCCAGCAAACGTCCCGCGACCGGAGCTCACTGCGGCGAACGGAATCGCGCGACCACGAACCAGCGAAGCCGGGTCATATCATACAAAGATCTCGCCCCTCTGTCCACCACATCGCTTATGTTTCTAGAGAGCGCTTCGCAGGGTCGTTTGACCACCAATTTTACCAGTATCTTCTGTACTCGTGTATTAAATACACCGGGTTAGTCGTTGCGACCTAGGTGAAAGTGTTCTAGGGGTGGCCGCAGCTAGGTTATCCCAATGCCGCGCTAGAGACCTCTCATCAGAGTAGACTACATCGTATTGCATCCGTACACTTGTCCACATGATAGCTCTGTCTAAACCGATAACTGTGCCCCGTATTTGCATCAACCTTACGCCTTGCTAGACTTGTATGCTGGCGACAATCGGGAGTCAGTAGGATACATACCTGTTCAATCTCGCGCGGAAGCCGTTTCACGAATTAAACATAGGGGCAAGGCGAGCTGCCCATTAGATCTGAGACCTCACCCGGAGGGCGCTTTATCACAAGGGAGCCGGGCTTGCAGACCAGTAACTCTCGTTAGTTCCCCTGACCCATTTGCGGTAGACGTCAAAAGAAAATACCTACCACCAAAAGAGCCTACACCCTTAGTTATAAAAATAGCTCAACTTTCTCGATACCACCCATCATCAGAGGGCTGGGCCTGAGCTCTTTTCCCGTGCAACCGAAATATCCATAGAGCCGTGAGCGTAGGGCATGCACCGCCTACAGTCGACTGGGCGACCGGCGTGATACCCGCCTGTCTCGCCGCGAACGTATATATCCGGCTTGAGCGCCGATCGGCTGATACCGTCCGGTTGCCTTTAATAGGGCAGGAACCGTGTCTCCTTTAACGAGAGGCGTACTACAGTGTCAAGTAGGGGGAGTCTGCGCGGTACTGTCCTGAGGACTGGTCGACGTAGAGGGGCCCGCTCACCATCAGGTCTAGTGTAAGCAACGAAGTGTCTGCTAGGTCACAACTTAGCCCATCCATTTCGAAGCGGAAATTAGGTCTACATAGAGAAGCTGCACGGAATGACAGTTAAACCAAAGGAGCGGAATAAACATGCTGTGGGGAATTGGTGGTCTTTTCCCGATTCAAGTAGGTTTGACTTCGGTTTACGATCTGATCACGGGTAGCGAAAGTGTTGGTAGCCTCCAGGCGGTGCAGCTGAATTCAGTCAACAGGCTCCGTCTCCAAATCCTTGCGTCCGGGAGTACCGAGTCTTTCTGAGCCTAAGTCGTGCCATGTCCCGGGCGATGTATCTCCGCGTATCTAGCGCGCGACTAAATATTGCCGCCCGCCTGAAGGAAGGACATACGTGACAGCTATAGGGGCCTCGTGGAAAACACAGTGAGAGCCTAGCTAATGAGCCGCCTGCTTGGATTACTGAATCCAGATGTTAGTAATGTATCTCATGATGCGCTGGACAATCGCAAAATTATCAAAGACATGCCCGGTGCTGCACACGCTTTAGTTATTGGAGGCATCTTCTCTACGAGGAGCTCTAGCCGGTCGACTCCCTTGCGTGAGTTGTCGTTGGTAATTACGGTATAGGATGCAATGATGGGCGATTTCCGACCTGGTAGTTGCTCGCTTGTGGCGTGTCTTCTCCTGTTGGGACGCACGTTCTACGAAACAGATCTCCCGACAGTTCTCCTCTATGAACCTAATCGGTAGTACACCCCTGTCCTGCATCTCTAGAGGGCTAGAATGTACGGAGTCGTAATCCTCTTCGCCCGATTAGATAGGACAGATGGACCCACTGTTGTGTGCTACAATATGGCTTAAAGAAAAAGTTCTATATTGCCTTTTATGAGCTCCAGCTGTGGTTTCCCCAAAGCAAGTTTCTAGATAGGGGTACCTGCTCGTGCACCATAGGGGCAATCGTAATTGGTGGTAGTCACATGTCCGGGGATTCCCCAGGCCCCGGCCATTGGTGGGGGGGAAGCATCCTTAACCTCTTATGGACTACATGGCTCGAGATAAAGAAGCTATTGATCTTTCAAATGACGCAAGAGTCACGAAACGCTAGGTCCAGTCAGGTAGTTTGGGAAATTTGCGTAATTCCGGTATCGCTCTAATTTCGTAGCGGGGGGGATAACTGCCTCGTTCCACCCCCGTCGGCACTTTACAGATAGTAACTTATCTGTTTGCGATCTAGGCGTTTGGAATGAACGCAACTGAGGGCCGACGTAGGATCTTGAGAAAACCCCCTGAACATAGAGACCTCCAACCTTGGACTGTTGATTCCAATTTAACTCTATCTGCTGGGCGGGAGGGACAAAACACAAGACTCACTAGGTCAGATTCTAAACTGCGGGCTGCTAAACTGTTAGCCCAGAAGGTGATCCACATGTACTGACAGACTGCTGATCGGAAGGACCTATTCTTCAGCAGCGTAGGCACAAGCGATCTGCACAGACTCCCTTGGTTTCTGCCGTGAAAAAGTAAGCACGGCCGTTTCGGAGCATGCTACACACGAAGAGTGCTAGGTCGAGGTCTTGGCATGTGATAATTTGCCGAGAAGACCAGAGATGCTGCCACGCGTTGTGGGTACACTTAAGTCCTCCTATGCACCGCCGCGGTGATGGCCGATATACAATGATTTTAGCGAGTTTGTGACCTAGGTTATTTCTCCCCTATTTCAGTGCACGCCCTGGTACGGCTCGATCCGCGGGAGTTGCCACAACGCCGGAATGGTCCGCGAAGCATCGACGAATGCCCCGTCACCAGATCTTGGCCTCAGGGAGGGGCCGCGCACTCCCCACTTGGATCAGGCGAGTCTGATGGATATAATAGCAGGACACTTGTCTTCCGTGCAGGCTCGGGATCGATCAATCAGTTCCGCGTTAGAGGGCTGTTTGCGCGCTATCGATTGGGCCGATTCTTATACTAATGGATTAGTTTCGTGGAGTACCTGGTTAGGCTGCTACCTGTCGTCAGTATTGGTTTAGGCGAGAGTCGCAGAAGAGGGTCCTGATCCGGAGCGCGTAAGTTGGCCTTCATTCGCATCTCATAGGACTTGACAGTATGCTATAAAATCTGCACGCTCTAACCATGCTAGTCACCTTGCCTCAAGTGTTGCGTCCTTCGAGTTCCGCAATAGCAAGTCTATTCTTAGCTTCTTATGCTTACATCGCATAGGCCCTGACCCCTTCATGGACAGTCGGCCCAAAAAACGCCAGTTTTGCGCCTCGCCACGAAGATGGTCGACCCGCGTCGTAGCGAGATCCCGGGAACCAACTTGGCGTTAAACTGCGCCGTGCACGAAAGCGTACCTTTGTAAGAATCATTCTCGCGTGAGTCTTTTGGCCCCCAACCAGATGGTCGTCGGGCTCATGACTGTAAACTGTAGGTCGCCGGCGCTGTCGTTGCCAGTATAAACATCCACAAGGATCGCACCTCCGGGGGTATTCCTTAATGGGAAAGGTTTCGGAGCGCATGCTGAGAGACTCCATAGATCAAGAATAAAGTTTTCATCTCGACACTGATTTATCTCTGGAGTAAAATCAAGTGCCTACTGACACGTCCCTGGTTAATGTATCGGTCGTGCGATTGAGCGCCTCCTAATTGTTACTCGTCAGTTAATGTAAGAGTTCCCGGTGAGAGGTACCCTATCTCCCTGATCATACCGCGTCCGATGAATCACTCGAACAGCAAACGCACTACAGCCCTCCATACGCATGTTATCCCGCCGAAATATTCTGGTTTCTCACCACCACCTGGGCGGTGTCCCCGCGGGCCTCGGAGAATAATGACAACCAACGGTTGGCGACCGGCCTCAAACAATGCCCCTACATATCCAATATGTCTTTGTACCCTCGTCTCTAATTTATGGTAAGGGTGAGGCCTACCGTACGTGTCCGATCAGCTATCGACGTCGAAATACACATTGTTCTGAGTTCTTAATCCTTGATAGCTCGAAACATTACCTCGTTAACGACCGGTTAGAGTTTTTTGTTTCCTCCTCGTCCGCGCTTTGTGGTCCAGCGTAAAGGCATGAATGTACAACCGAATCACCATTTGAATAGGTCTGTACATCCACCGCGCAGTACGGGTGCCCCTCGAGCCCGCGCAATGCTCTCGGACGAGACCGGCGTGTCCACGTGGTGACGGGAATTGTAATAAATGGACATAGTCTTGTGTTACTCGTTGATCAAGAGTGTTTAATGTCGGGGGGTGAGGAGGTCCCGAGGTTTGCACAAAGGGTTACATGCGTGCCACTCGCGACTGCGGCGACTTCCTACATTTTGATCTGGACTGGGAGCGACTGTCGTTAGCCCGGACACCTCGGTGGCAGGCGAAACACAATGACAGTATGGCGTTGAAGGGCGCTTTTGCAATGGTGGTGTACTTTACCGCCTTGTTTCCAGGAAGATATCCTATACTACTTATCGCATTTCGTGCCCGGTCGCTTAGCAATAGTACCAGCAGGTTTTAATAGGAAACGAGGGGGAAGGTTGCACTGTCATCGGATGCCCTATTTATGTATTTACCTGCTTCGTTGTCCCTCGCACCGGGGTTGAAATCATGTCCCGGCCAATGTATGCCGCAAATATGGCTCGCCTGCCCCATGGAATTCTTACCCTACATAGTTGATTAAGTGAGGAGCGCTGTTAGAATCTAACTGTTCGAACGGATTGACGTGTGAACCCGCCCCTTATTTACGATCGCGCTTGGAGCCTGCCTACTACTCGTCTTTAGGTAGGTTGCAACCGACCGACGCCTAGGAACAGCCGTCGGTACATGACCTTCTCTACGTGTCCAACTAGCAGAAGAGGAAGAGGGATGCCGTCACGATACCGCCGTATAACCCGAATAGCCCCTGGAAACACCCGCAGGAGACTATCCACTCAGGATTACATGGGGCTGGAACGCTTTGGATACAGATCCACGAGCAATCGATTGTCGGTCAATAATGGACTAATTGCAAGAAGCTCACGGATACTTCAGTCTTGTGTATATGTACTCAAGTTTTAGCTCACTTAGACAAACTGTCTATAAATCCGCATCGCTTTGGAAGTACTAATTGGATGGTCGTCTCGATGAGGTATTGACGTTTTTCTTGAATGGAGTGCCGAACAAGGCTAATAATTCTCGTGTGTCTCGGGTATTGGCTTCTGTACTCGCGCCTAGGAGAGCTAGTGCTCGGCGCGTAACATAACGCCAATCAAACTCAGCATGAAGGGTCTATGCGTGTCTAATCCCGGGTTATAATGACCACGTCCGCTACTTGAGGTAGTTGTCAGGACTACCGGAGTGTGGTACTTGGAAAACTTCTAACGCGGTAGATCTGCAGCAGGTCGCGACTAAAAGTAACGGGTGAACCTGAGTACAGAGATTGAGGAGAACCATAAAGACAATCACTGACCCTCTCTCCGAACCTTCACATACCTGGGTGGAACGTCGGACGAGTAGAAGTACGAGTCTACAGGACGGTACATGAATGTAGAGGCGGTATATTGGCGCTCGGCTCTGGGATAATACTGCCTGCATCAAATCGGCGTGGCTCCGACTTATCGCACGATAATGTGCCTGTCATTAATGGTAGGGGGTAACCTGGAATTGCGGACCGTTACGCCCGCGGACCTGAGGAATGCATAGGTGGTCTCCAAATACTTCTGTTAGTCAGCGGGTAAGTCAAAGGGTTCTTATGACGATAGTAGCATCTCTGCCCTATCTGGGCTACACCCCATCATTTAAATAGGTTCGGACCACACAGGGCGCCCGAGTCCTACTGGAATTGAATGTAACACAGAGGGGCTTACCCCGGAGTGGAAACCTCGTATTAAAATAGTCTAAGACTGGGGTAGGACAGCGGCCAGGCCGGTCCGCGTACAGCAGCTGGACCTTGCCATTGTCAAATCCGTGTAATATCGCACGAAGTAGCAGGTCCTTTATACATCTCAACTGGCACGAGGTTCACTGGGCATTGGGTACTCTTTCCACTATGACATGTTGGAAAGACCGCATCGGGATGTTGCGGCTGTTTATGTGCAGCAGACGATTAACTAGCGGGTCGCGAGGCCCACAGAAGACGGAACCGCCCATGGAGTCACTGACTTGGCTCAGACTTTCGTGTACATCGAATAGGTATTCAGGCTCGAGAATTTACATCTCTCACTCTGGCGCTAAGTTCGTACGCCGTGGAACGGTATCGTGGGGCTTTGACATAGTTACCGTAGAACCGCCTCTCTTTGCGTACGTACCAACATATACAGACTTCGAACGCCATCCGGCGAAACGCGTCGTTCCAATAAAGTGCAAGCGCGAGCACGTTCTCCTGTACGACAAGCAGGTGTACGGAACCTGATGACGATCATAGTAGGATTTAACCTCCCCTGTTCCATTGGGTCTTGATTGGGCGTAACCATTCCCCGACGTAAGACCCTGTAAGGTAAGGGCAATGTCATGGAGGTACGTAGTCCATCACTGAATTGTCCTGTCGGGTTAATTAATAGCATCGACCGATCTATTAATCATACAATGCGTCAGACCTACCCCGTGGTACATCAATCAATAAGCCTGTGCCAACTTCAACGGTCCAGCAGCTATAGGTCTAACAAACATGGTGGGTCTTCATAGGCGGCTTTCCTATGACTACATCCACATGAGTTCGGAATGTTCAGATTTACAACGTTAGTCTAAGGAAGGCTTCTTTCGGCCGCAGGCTACAGAGAGAAACTCCCTTATGCGCGGACCCATATCTGTCCAATCCAGGTCAGGTGCATAGACCGGCATTTTGTAACCCATACTATATAATTTGGGAACTGGTCCTGAAGGACAGATACAGAATGCGATTGGTAGATCTTCCTTGTATTAGAGTAGCTTATGTCGTGGAACTGCCAGCGCGGGCACGAAGTCTTCACGTTGCTAATGGGCAAGGGAGAGTTACCCTACATGAACCCCTCGACTGAGTTTGTAGAGGGGAATTTCTAGAAAGTAGAGGAGCCTTTTCTGTATCTGCAAAGCCTCGCCTTGCCAGCTAGCGTTCCGTAGGCTCACTACGCACACAAAATGATAGCGCAAGTTTGTTTTCGTTCCTGAACATGCATGTCTATCAGCCCGAAGCTCGATAATTGGATCGGCCCGGCCCCAGCGCGACAGTGCTTATCTAACGAGACGCTCAGGACGTTCTCAGGCGGCAGACCAACAATGCAAATACTTCAGTCGATCTTCAGTAGTCATGAAGCAAAACCCGAGGCAATCGCTTTCGTTACAATGTTAGACATCAGCAGCGCGCTCAATTGCCCCAGGTGTATGACGAGGTGGCGGCGACTCTGCTCATCATGTCGGGTACGATATGTGTTTGCTCGGTGGTGGCGATATCGAGAGCATGGGCGTACAGAGGAAGGGTTCGAGATCAAGGAAGGCCCCCACTGGCACAGTGGGCTGTCCCGGTGGCAAGTTGCACTGGTTGGTAAAAACATCTATCCGCGGACGATAGAAGACGGTAAGGTTCAAAGCGAGTCCTATAATATATCGTGGAGAGACCGGCCGATTATGATGGCCGCTACCTAGAGACTGTCTGCGACTTGTCAAGGCCTCCGCCGAACAAGCATCATTACTATCCCCAAAAGACGGCTCCACCCCTTCGGTAGATCGGCAGGGAATATTCGATTTCAGGTCGCAAACACGCATGCTGATTCTAAACCCAGTTCGGCGAGTCCAAAATCCAACATAATACTATTCGGCAGACCTTGTCTCAGAATCTCAGTTCCGTCGTATTAAATGCAAAGGTAACAGCCAAGGAGATCTATTCGACCAGGCTAAACCCCTAGTCCGAGACGTGTACAGCACTATCAACGGCCCACCAGTATAATTTCGAGCTACGTACCTTGCTCAAGACATTCGCACTATCCTCGATCAGGTGATAATAATGCTCCCGGCCAGATACAGTACCCATCGCGTTGTCTGCCCGTCTGTACGTTGCTGGAAAAATAAGCCTATTGACGCCCACGACGAAGGAATGCAGCGATCGTAGCGCTATACGGACCGCTTAGAAAAAAACCGGGGGCGAAGCCAGGTCATTCCAATTCAAACTCCAGTGCTTACAAACCTTTAGCTTGACCTTCACTAGTGTCCAGCGTTCGTAGCGGTACCGTATTATACCGTGGACTAGACGAGCATCTCATACTTCCAACTTAGCGTGTCCTTTAGATTTTTCATCACAAAGGATTTAAAACATGCGTATCTGGCTTACATTAGTGCTCTTACTCAAAGCCGCGTGCGCCAACACTGCGTAGCAGTAGGCGAACCTGGAGGGTCCACCGCATGAAGGGATCGATTCAGTCTGCGAGTCGAGGCTCTAAAGGATGCCCGGTCGCATCTTACAGCCGGGAGTTGATCTGATGTTGCCTAGCCGACCACGCGACTGCCCTCACTTGACACATAGCATTCTGTGACGAAGCATGTTGTATGACAGGATTCTCTTAAACCCATACGTTTTACTTATAATTCACATTGGTGAGGGTTATCATAATTCTCTAGCAGCATGACTTATTAACGGAGCTGAACCTTTCAGTCGGAAGATGCTGGAACCGACCGCCTGATGTGCGTCGAACCTTAGCCGGTTGTAGACGGCTGGTGTCGCACTTCGTCTTAGGGAGCGACTTCAGGATGAGGGCCCAAATCTGGCAGTATGCAGTATTAATTCTGGGCTTTCTTGTGCTACAATTCAAAAGAATGCCCGGAGTCCTTCGGGGTGGTTAATCTGCAGACCATGCGTTAATGATAATAACATTAAATAATTTGAGCGTCTTATCATCATTGCTTATACCACAGATGGGTGGAGTGGATATCTAGAGCATCCCTTTGTGTCAACGTGTTTGCGGCATGCCATAGCTGGAAAAGCACATTGCTTTGAGACATCCTTCGAGCGTTCCTGCGCGATCCCCGGGTCAAGGACCTTCTACAGTACGCTACGAGTGTTCAAGGTGATGCAGTGCTCCTTAAATCAAGCTCCAAACCTCGCACGTGTACACCAAGTTGGTTAATCCTTTTTGAACGGGGGAAGAAAAACTATCTGGTCACAAAGCAGTATTCCATGGCAGTCTGAATATGTAACAAGAAGCCCCGTAGATTTTGCAAGCGCTGAAGCTGAATCCGTGATGGGTGGGTGACCGAGACCTCTGAACGCACATCCAACACTTCGGGAATTGCTG", 5)
occurrences_str = ' '.join(map(str, ANS))
print(occurrences_str)