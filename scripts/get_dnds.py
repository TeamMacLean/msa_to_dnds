import sys, os
from Bio import SeqIO
from Bio.Alphabet import IUPAC, Gapped
from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.PAML import baseml,yn00
from Bio.SeqRecord import SeqRecord

inputfile=sys.argv[1]
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

yn=yn00.Yn00()
yn.alignment=msa
yn.out_file=sys.argv[2]
yn.run(verbose=True)
