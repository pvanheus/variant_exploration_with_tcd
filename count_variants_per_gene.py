#!/usr/bin/env python3

from snptools.vc_matrix import make_variant_count_matrix

input_directory = '/home/pvh/Data/vcf/combine_vcfs'
output_filename = 'snp_matrix.csv'
make_variant_count_matrix(input_directory, output_filename)

