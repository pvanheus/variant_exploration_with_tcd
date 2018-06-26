import asyncio
from concurrent.futures import ProcessPoolExecutor
from os import listdir
import os.path
import pandas as pd
from .count_variants_per_gene import process_vcf
from .genetree import make_gene_tree

@asyncio.coroutine
def make_variant_count_matrix_async(input_directory, output_filename, process_count=3):
    p = ProcessPoolExecutor(process_count)
    loop = asyncio.get_event_loop()
    
    gene_tree = make_gene_tree()
    locus_names = sorted([ interval.data['locus'] for interval in gene_tree ])
    
    matrix = []
    futures = []
    for filename in sorted(listdir(input_directory)):
        if filename.endswith('.vcf.gz') or filename.endswith('.vcf'):
            path = os.path.join(input_directory, filename)
            future = loop.run_in_executor(p, process_vcf, path, gene_tree)
            futures.append(future)
    
    for counts in await asyncio.gather(*futures)
            row = [ counts.get(locus, 0) for locus in locus_names ]
            matrix.append(row)        

    sample_names = [ filename.split('.')[0] for filename in sorted(listdir(input_directory)) 
                        if filename.endswith('.vcf.gz') or filename.endswith('.vcf') ]
    data = pd.DataFrame(matrix, index=sample_names, columns=locus_names)
    data.to_csv(output_filename)
    
def make_variant_count_matrix(input_directory, output_filename, process_count=3):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(make_variant_count_matrix_async(input_directory, output_filename, process_count))