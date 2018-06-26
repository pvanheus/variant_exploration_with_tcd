import intervaltree
from .combattb_db import get_gene_data

def make_gene_tree():
    gene_tree = intervaltree.IntervalTree()
    gene_data = get_gene_data()
    for gene in gene_data:
        # print(gene['min'], gene['max'])
        gene_tree[gene['min']:gene['max']] = dict(locus=gene['uniquename'])
    return gene_tree