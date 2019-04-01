### Introduction

This is a python script to do multiple sequence alignment of gene sequences, write the alignment in phylip format and use PAML(yn00) for getting dN/dS ratio for pairwise sequences. PAML yn00 give dN/dS value using different methods - Nei-Gojobori (1986) method, Yang & Nielsen (2000) method,  LWL85, LPB93 & LWLm methods

### Requirement

1) python3
2) biopython
3) paml (installed in system)

### Usage:

you will need to generate a multiple sequence alignment file in fasta format using any tool. I use MAFFT or clustalo
1) mafft in.fasta > out.fasta
2) clustalo --in in.fasta --infmt=fasta --outfmt=fasta --out out.fasta

Then, run the python script

1) python scripts/get_dnds_with_yn00.py out.fasta output_file
2) python scripts/get_dnds_with_codeml.py multiple_seq_align.fasta treefile output_file
