
from os import listdir
import os.path
import pandas as pd
from .count_variants_per_gene import process_vcf
from .genetree import make_gene_tree

def make_variant_count_matrix(input_directory, output_filename):
    gene_tree = make_gene_tree()
    locus_names = sorted([ interval.data['locus'] for interval in gene_tree ])
    
    matrix = []
    futures = []
    for filename in sorted(listdir(input_directory)):
        if filename.endswith('.vcf.gz') or filename.endswith('.vcf'):
            path = os.path.join(input_directory, filename)
            counts = process_vcf(path, gene_tree)
            row = [ counts.get(locus, 0) for locus in locus_names ]
            matrix.append(row)        
    
    sample_names = [ filename.split('.')[0] for filename in sorted(listdir(input_directory)) 
                        if filename.endswith('.vcf.gz') or filename.endswith('.vcf') ]
    data = pd.DataFrame(matrix, index=sample_names, columns=locus_names)
    data.to_csv(output_filename)