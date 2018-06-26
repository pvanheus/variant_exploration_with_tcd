#!/usr/bin/env python3

from os import listdir
import os.path
from snptools.count_variants_per_gene import process_vcf
from snptools.genetree import make_gene_tree

gene_tree = make_gene_tree()
locus_names = sorted([ interval.data['locus'] for interval in gene_tree ])
print(locus_names)
input_directory = '/home/pvh/Data/vcf/combine_vcfs'
for filename in listdir(input_directory):
    if filename.endswith('.vcf.gz') or filename.endswith('.vcf'):
        path = os.path.join(input_directory, filename)
        counts = process_vcf(path, gene_tree=gene_tree)


