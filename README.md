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

1) python scripts/get_dnds.py out.fasta output_file

### Example output

```
YN00 ../../Downloads/paml4.8/examples/abglobin.nuc

ns =   5	ls = 285

Codon position x base (3x4) table for each sequence.

human
position  1:    T:0.12982    C:0.25965    A:0.21404    G:0.39649
position  2:    T:0.29474    C:0.26667    A:0.30526    G:0.13333
position  3:    T:0.18947    C:0.41404    A:0.03509    G:0.36140

goat-cow
position  1:    T:0.13684    C:0.23509    A:0.22807    G:0.40000
position  2:    T:0.30526    C:0.24211    A:0.31228    G:0.14035
position  3:    T:0.21754    C:0.39649    A:0.03509    G:0.35088

rabbit
position  1:    T:0.14386    C:0.24912    A:0.24561    G:0.36140
position  2:    T:0.29474    C:0.23860    A:0.32982    G:0.13684
position  3:    T:0.19298    C:0.40351    A:0.04912    G:0.35439

rat
position  1:    T:0.14737    C:0.22807    A:0.24561    G:0.37895
position  2:    T:0.28070    C:0.23860    A:0.32632    G:0.15439
position  3:    T:0.25965    C:0.38596    A:0.07018    G:0.28421

marsupial
position  1:    T:0.17895    C:0.22105    A:0.24561    G:0.35439
position  2:    T:0.28772    C:0.27018    A:0.30877    G:0.13333
position  3:    T:0.25965    C:0.38596    A:0.06316    G:0.29123

Average
position  1:    T:0.14737    C:0.23860    A:0.23579    G:0.37825
position  2:    T:0.29263    C:0.25123    A:0.31649    G:0.13965
position  3:    T:0.22386    C:0.39719    A:0.05053    G:0.32842

Codon usage for each species
----------------------------------------------------------------------------------------------------------------------
Phe TTT   5   8   3   3   6 | Ser TCT   4   2   6   7   6 | Tyr TAT   3   2   3   1   1 | Cys TGT   2   1   1   2   2
    TTC  10   9  13  11   8 |     TCC   6   7   7   3   8 |     TAC   3   3   3   5   5 |     TGC   1   1   1   3   3
Leu TTA   0   0   0   0   0 |     TCA   0   0   0   0   1 | *** TAA   0   0   0   0   0 | *** TGA   0   0   0   0   0
    TTG   0   2   1   4   5 |     TCG   0   1   0   0   2 |     TAG   0   0   0   0   0 | Trp TGG   3   3   3   3   4
----------------------------------------------------------------------------------------------------------------------
Leu CTT   1   1   0   1   3 | Pro CCT   7   2   4   7   3 | His CAT   2   4   4   5   6 | Arg CGT   1   2   1   2   1
    CTC   5   4   4   4   7 |     CCC   3   6   5   4   7 |     CAC  16  11  15  14  12 |     CGC   0   1   0   0   0
    CTA   1   2   0   2   1 |     CCA   2   0   1   0   0 | Gln CAA   0   0   0   0   1 |     CGA   0   0   0   0   0
    CTG  29  28  30  21  15 |     CCG   2   2   1   0   0 |     CAG   4   4   5   5   7 |     CGG   1   0   1   0   0
----------------------------------------------------------------------------------------------------------------------
Ile ATT   0   0   1   4   1 | Thr ACT   3   4   4   3  10 | Asn AAT   1   5   5   3   2 | Ser AGT   2   3   5   2   1
    ATC   0   0   3   2   7 |     ACC  12  11  12   9   9 |     AAC   9   7   7   8   4 |     AGC   4   4   3   5   3
    ATA   0   0   0   1   0 |     ACA   1   0   0   1   0 | Lys AAA   4   3   5   5   3 | Arg AGA   0   1   0   0   2
Met ATG   3   3   2   4   5 |     ACG   0   0   0   0   0 |     AAG  18  21  19  19  21 |     AGG   4   3   4   4   2
----------------------------------------------------------------------------------------------------------------------
Val GTT   5   5   4   4   6 | Ala GCT   8  11   8  13  10 | Asp GAT   5   8   1  11   6 | Gly GGT   5   4   5   6  10
    GTC   4   6   2   4   3 |     GCC  21  18  16  18  19 |     GAC  10  10  10   8  10 |     GGC  14  15  14  12   5
    GTA   0   0   0   1   1 |     GCA   0   1   1   3   2 | Glu GAA   2   2   7   4   4 |     GGA   0   1   0   3   3
    GTG  21  19  21  14  14 |     GCG   7   4   3   0   0 |     GAG  10   9  10   5   6 |     GGG   1   1   1   2   2
----------------------------------------------------------------------------------------------------------------------


Sums
------------------------------------------------------
Phe TTT  25 | Ser TCT  25 | Tyr TAT  10 | Cys TGT   8
    TTC  51 |     TCC  31 |     TAC  19 |     TGC   9
Leu TTA   0 |     TCA   1 | *** TAA   0 | *** TGA   0
    TTG  12 |     TCG   3 |     TAG   0 | Trp TGG  16
------------------------------------------------------
Leu CTT   6 | Pro CCT  23 | His CAT  21 | Arg CGT   7
    CTC  24 |     CCC  25 |     CAC  68 |     CGC   1
    CTA   6 |     CCA   3 | Gln CAA   1 |     CGA   0
    CTG 123 |     CCG   5 |     CAG  25 |     CGG   2
------------------------------------------------------
Ile ATT   6 | Thr ACT  24 | Asn AAT  16 | Ser AGT  13
    ATC  12 |     ACC  53 |     AAC  35 |     AGC  19
    ATA   1 |     ACA   2 | Lys AAA  20 | Arg AGA   3
Met ATG  17 |     ACG   0 |     AAG  98 |     AGG  17
------------------------------------------------------
Val GTT  24 | Ala GCT  50 | Asp GAT  31 | Gly GGT  30
    GTC  19 |     GCC  92 |     GAC  48 |     GGC  60
    GTA   2 |     GCA   7 | Glu GAA  19 |     GGA   7
    GTG  89 |     GCG  14 |     GAG  40 |     GGG   7
------------------------------------------------------



(A) Nei-Gojobori (1986) method



Nei & Gojobori 1986. dN/dS (dN, dS)
(Note: This matrix is not used in later ML. analysis.
Use runmode = -2 for ML pairwise comparison.)

human
goat-cow             0.2507 (0.0863 0.3443)
rabbit               0.2627 (0.0867 0.3301) 0.2943 (0.1054 0.3581)
rat                  0.2045 (0.1261 0.6164) 0.2462 (0.1493 0.6065) 0.2178 (0.1348 0.6187)
marsupial            0.1902 (0.1931 1.0148) 0.1891 (0.1910 1.0099) 0.2184 (0.2111 0.9668) 0.2716 (0.2404 0.8852)


(B) Yang & Nielsen (2000) method

Yang Z, Nielsen R (2000) Estimating synonymous and nonsynonymous substitution rates under realistic evolutionary models. Mol. Biol. Evol. 17:32-43

(equal weighting of pathways)

seq. seq.     S       N        t   kappa   omega     dN +- SE    dS +- SE

   2    1   183.7   671.3   0.5169  1.5804  0.1625 0.0818 +- 0.0115  0.5031 +- 0.0930
   3    1   177.5   677.5   0.5033  1.5804  0.1642 0.0815 +- 0.0114  0.4967 +- 0.0927
   3    2   180.1   674.9   0.5627  1.5804  0.1929 0.0997 +- 0.0128  0.5169 +- 0.0925
   4    1   191.3   663.7   0.9075  1.5804  0.1308 0.1216 +- 0.0144  0.9301 +- 0.1987
   4    2   192.4   662.6   0.9642  1.5804  0.1557 0.1447 +- 0.0159  0.9297 +- 0.2091
   4    3   187.0   668.0   0.9790  1.5804  0.1262 0.1298 +- 0.0149  1.0286 +- 0.2614
   5    1   189.3   665.7   2.1638  1.5804  0.0711 0.1853 +- 0.0184  2.6055 +- 3.9344
   5    2   190.4   664.6   1.2984  1.5804  0.1416 0.1842 +- 0.0184  1.3008 +- 0.1995
   5    3   185.2   669.8   1.3214  1.5804  0.1554 0.2023 +- 0.0194  1.3020 +- 0.2026
   5    4   194.5   660.5   1.5554  1.5804  0.1591 0.2354 +- 0.0215  1.4797 +- 0.5173


(C) LWL85, LPB93 & LWLm methods

Li W.-H., C.-I. Wu, Luo (1985) A new method for estimating synonymous and nonsynonymous rates of nucleotide substitutions considering the relative likelihood of nucleotide and codon changes. Mol. Biol. Evol. 2: 150-174.
Li W-H (1993) Unbiased estimation of the rates of synonymous and nonsynonymous substitution. J. Mol. Evol. 36:96-99
Pamilo P, Bianchi NO (1993) Evolution of the Zfx and Zfy genes - rates and interdependence between the genes. Mol. Biol. Evol. 10:271-281
Yang Z (2006) Computational Molecular Evolution. Oxford University Press, Oxford. Eqs. 2.12 & 2.13

2 (goat-cow) vs. 1 (human)

L(i):      540.5     153.5     161.0  sum=    855.0
Ns(i):   16.5000   19.0000   24.5000  sum=  60.0000
Nv(i):   29.0000    6.5000   16.5000  sum=  52.0000
A(i):     0.0325    0.1491    0.2038
B(i):     0.0568    0.0442    0.1147
LWL85:  dS =  0.3495 dN =  0.0856 w = 0.2450 S =  212.2 N =  642.8
LWL85m: dS =  0.2861 dN =  0.0924 w = 0.3230 S =  259.2 N =  595.8 (rho = 0.640)
LPB93:  dS =  0.2918 dN =  0.0865 w = 0.2966

3 (rabbit) vs. 1 (human)

L(i):      540.0     157.5     157.5  sum=    855.0
Ns(i):   15.5000   21.5000   20.0000  sum=  57.0000
Nv(i):   29.5000    7.5000   16.0000  sum=  53.0000
A(i):     0.0305    0.1683    0.1629
B(i):     0.0579    0.0500    0.1136
LWL85:  dS =  0.3336 dN =  0.0862 w = 0.2584 S =  210.0 N =  645.0
LWL85m: dS =  0.2798 dN =  0.0919 w = 0.3285 S =  250.3 N =  604.7 (rho = 0.589)
LPB93:  dS =  0.2792 dN =  0.0866 w = 0.3101

3 (rabbit) vs. 2 (goat-cow)

L(i):      539.5     161.0     154.5  sum=    855.0
Ns(i):   23.0000   25.0000   17.0000  sum=  65.0000
Nv(i):   30.5000    9.5000   19.0000  sum=  59.0000
A(i):     0.0465    0.1993    0.1395
B(i):     0.0600    0.0628    0.1412
LWL85:  dS =  0.3624 dN =  0.1044 w = 0.2881 S =  208.2 N =  646.8
LWL85m: dS =  0.3217 dN =  0.1089 w = 0.3384 S =  234.5 N =  620.5 (rho = 0.497)
LPB93:  dS =  0.3112 dN =  0.1071 w = 0.3442

4 (rat) vs. 1 (human)

L(i):      543.5     157.5     154.0  sum=    855.0
Ns(i):   22.5000   28.5000   31.0000  sum=  82.0000
Nv(i):   42.0000   11.0000   29.0000  sum=  82.0000
A(i):     0.0452    0.2450    0.3288
B(i):     0.0839    0.0752    0.2363
LWL85:  dS =  0.6082 dN =  0.1265 w = 0.2080 S =  206.5 N =  648.5
LWL85m: dS =  0.5113 dN =  0.1347 w = 0.2634 S =  245.6 N =  609.4 (rho = 0.582)
LPB93:  dS =  0.5227 dN =  0.1272 w = 0.2434

4 (rat) vs. 2 (goat-cow)

L(i):      543.0     161.0     151.0  sum=    855.0
Ns(i):   33.0000   35.0000   29.0000  sum=  97.0000
Nv(i):   42.0000   12.5000   23.5000  sum=  78.0000
A(i):     0.0689    0.3170    0.2948
B(i):     0.0840    0.0844    0.1864
LWL85:  dS =  0.6044 dN =  0.1486 w = 0.2458 S =  204.7 N =  650.3
LWL85m: dS =  0.4955 dN =  0.1596 w = 0.3220 S =  249.6 N =  605.4 (rho = 0.613)
LPB93:  dS =  0.4927 dN =  0.1530 w = 0.3105

4 (rat) vs. 3 (rabbit)

L(i):      542.5     165.0     147.5  sum=    855.0
Ns(i):   26.5000   35.0000   29.5000  sum=  91.0000
Nv(i):   36.5000   16.5000   24.0000  sum=  77.0000
A(i):     0.0540    0.3156    0.3152
B(i):     0.0723    0.1116    0.1968
LWL85:  dS =  0.6301 dN =  0.1332 w = 0.2114 S =  202.5 N =  652.5
LWL85m: dS =  0.5123 dN =  0.1434 w = 0.2800 S =  249.1 N =  605.9 (rho = 0.616)
LPB93:  dS =  0.5122 dN =  0.1354 w = 0.2644

5 (marsupial) vs. 1 (human)

L(i):      547.5     151.5     156.0  sum=    855.0
Ns(i):   27.0000   34.5000   34.5000  sum=  96.0000
Nv(i):   62.0000   21.0000   49.0000  sum= 132.0000
A(i):     0.0548    0.3696    0.4588
B(i):     0.1284    0.1623    0.4947
LWL85:  dS =  0.9915 dN =  0.1926 w = 0.1943 S =  206.5 N =  648.5
LWL85m: dS =  0.8945 dN =  0.1995 w = 0.2231 S =  228.9 N =  626.1 (rho = 0.481)
LPB93:  dS =  0.9096 dN =  0.1906 w = 0.2096

5 (marsupial) vs. 2 (goat-cow)

L(i):      547.0     155.0     153.0  sum=    855.0
Ns(i):   28.0000   42.5000   31.5000  sum= 102.0000
Nv(i):   66.0000   15.5000   42.5000  sum= 124.0000
A(i):     0.0571    0.4668    0.3821
B(i):     0.1381    0.1116    0.4055
LWL85:  dS =  0.9423 dN =  0.1908 w = 0.2025 S =  204.7 N =  650.3
LWL85m: dS =  0.8451 dN =  0.1980 w = 0.2342 S =  228.2 N =  626.8 (rho = 0.485)
LPB93:  dS =  0.8302 dN =  0.1894 w = 0.2281

5 (marsupial) vs. 3 (rabbit)

L(i):      546.5     159.0     149.5  sum=    855.0
Ns(i):   29.5000   40.0000   32.5000  sum= 102.0000
Nv(i):   66.0000   24.5000   40.5000  sum= 131.0000
A(i):     0.0607    0.4432    0.4164
B(i):     0.1382    0.1842    0.3902
LWL85:  dS =  0.9436 dN =  0.2115 w = 0.2242 S =  202.5 N =  652.5
LWL85m: dS =  0.8251 dN =  0.2214 w = 0.2683 S =  231.6 N =  623.4 (rho = 0.516)
LPB93:  dS =  0.8205 dN =  0.2093 w = 0.2551

5 (marsupial) vs. 4 (rat)

L(i):      550.0     159.0     146.0  sum=    855.0
Ns(i):   32.0000   36.0000   35.0000  sum= 103.0000
Nv(i):   77.0000   25.0000   36.0000  sum= 138.0000
A(i):     0.0660    0.3765    0.4775
B(i):     0.1643    0.1888    0.3398
LWL85:  dS =  0.9004 dN =  0.2388 w = 0.2652 S =  199.0 N =  656.0
LWL85m: dS =  0.7500 dN =  0.2542 w = 0.3390 S =  238.9 N =  616.1 (rho = 0.584)
LPB93:  dS =  0.7646 dN =  0.2357 w = 0.3083

```
