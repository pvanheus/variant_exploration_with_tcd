import pytest
from ..snptools.genetree import make_gene_tree

@pytest.fixture
def gene_tree():
    return make_gene_tree()

def test_gene_tree_size(gene_tree):
    num_h37rv_genes = 4018
    assert len(gene_tree) == num_h37rv_genes, "Expected to find {} genes in tree, found {}".format(num_h37rv_genes, len(gene_tree))

def test_dnaa_location(gene_tree):
    start = 1
    end = 1524
    locus = 'Rv0001'
    # subtract 1 to get to 0-based coordinates that gene_tree uses
    gene_set = gene_tree.search(start-1)
    assert len(gene_set) == 1, "Expected to find dnaA gene at {}".format(start-1)
    assert len(gene_set) == 1, "Expected to find dnaA gene at {}".format(end-1)
    assert list(gene_set)[0].data.get('locus') == locus, "Expected to find {} (dnaA), found Interval {}".format(locus, list(gene_set)[0])
    
def test_intergenic_region(gene_tree):
    outside = 1524 # this is just past the first M.tb gene
    gene_set = gene_tree.search(outside)
    assert len(gene_set) == 0, "Expected to find nothing at the zero-based position {}".format(outside)
