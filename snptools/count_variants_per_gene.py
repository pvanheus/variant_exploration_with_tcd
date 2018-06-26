from collections import Counter
import gzip
from sys import stderr
import vcf
from .genetree import make_gene_tree

def process_vcf(vcf_filename, gene_tree=None):
    """process_vcf(vcf_filename)
    
    """
    try:
        # if vcf_filename.endswith('.gz'):
        #     print(vcf_filename)
        #     input_file = gzip.open(vcf_filename)
        # else:
        #     input_file = open(vcf_filename)
        vcf_reader = vcf.Reader(filename=vcf_filename)
    except IOError as e:
        print('Error opening {}: {}'.format(vcf_filename, str(e)), file=stderr)
        return None

    if gene_tree is None:
        gene_tree = make_gene_tree()

    locus_list = []
    for record in vcf_reader:
        if record.is_snp:
            interval_set = gene_tree.search(record.affected_start)
            if interval_set:
                locus_name = list(interval_set)[0].data['locus']
                locus_list.append(locus_name)
                # print(record.affected_start, locus_name)

    snp_counter = Counter(locus_list)
    return snp_counter