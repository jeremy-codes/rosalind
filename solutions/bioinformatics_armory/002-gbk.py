"""Solution for Bioinformatics Armory Problem ID: GBK

Problem Title: GenBank Introduction
Link: http://rosalind.info/problems/gbk
"""

# (Anthoxanthum[Organism]) AND ("2003/7/25"[Publication Date] : "2005/12/27"[Publication Date])

from Bio import Entrez

input_path = "data/rosalind_gbk.txt"
input_file = open(input_path, "r")
genus, date_start, date_end = [l.rstrip() for l in input_file.readlines()]

db = "nucleotide"
query = '(%s[Organism]) ' % (genus) \
        + 'AND ("%s"[Publication Date] : ' % (date_start) \
        + '"%s"[Publication Date])' % (date_end)

Entrez.email = "jeremybr.adams@gmail.com"
handle = Entrez.esearch(db=db, term=query)
dict = Entrez.read(handle)
print(dict["Count"])
