import sys, os
from Bio import SeqIO
from Bio.Alphabet import IUPAC, Gapped
from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.PAML import baseml,yn00,codeml
from Bio.SeqRecord import SeqRecord

inputfile=sys.argv[1]
treefile=sys.argv[2]
outputfile=sys.argv[3]
filehandler=open(inputfile)
align = MultipleSeqAlignment([], Gapped(IUPAC.unambiguous_dna, "-"))

msa = "MSA.phy"
phylip=open(msa, 'w')
for record in SeqIO.parse(filehandler, 'fasta'):
	id=record.id
	sequence=str(record.seq)
	align.add_sequence(id, sequence)


phylip.write(align.format('phylip-sequential'))
phylip.close()

cml=codeml.Codeml(alignment="MSA.phy", tree=treefile, out_file = outputfile)

cml.set_options(seqtype=3)	# set this option bases on codon or aminoacid, values accepted 1,2 or 3
cml.set_options(model=3)
cml.set_options(NSsites="3")
cml.set_options(ncatG="3")
cml.run()
