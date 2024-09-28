import streamlit as st

def find_snps(seq1, seq2):
    """
    Finds SNPs between two DNA sequences
    """
    snps = []
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            snps.append(i)
    return snps

def main():
    st.title('SNP Detector')
    seq1 = st.text_input('Sequence 1')
    seq2 = st.text_input('Sequence 2')
    if st.button('Find SNPs'):
        snps = find_snps(seq1, seq2)
        if snps:
            st.write('SNPs found at positions:')
            st.write(snps)
        else:
            st.write('No SNPs found.')

if __name__ == '__main__':
    main()
