#!/usr/bin/env python3

import argparse
#from snptools.vc_matrix_async import make_variant_count_matrix
from snptools.vc_matrix import make_variant_count_matrix

parser = argparse.ArgumentParser('Count variants in genes and make a matrix')
parser.add_argument('input_directory', default='/home/pvh/Data/vcf/combine_vcfs')
parser.add_argument('output_filename', default='snp_matrix.csv')
args = parser.parse_args()

make_variant_count_matrix(args.input_directory, args.output_filename)

