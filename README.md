# genomicasserttions

[![Build Status](https://travis-ci.org/dakl/genomicsassertions.svg?branch=master)](https://travis-ci.org/dakl/genomicsassertions)

`genomicasserttions` is a python package which adds methods to test commonly generated files in the genomics field.
  
# Examples

Use the `VariantAssertions` mixin in your test class to get access to the methods.

~~~python
from genomicsassertions.variantassertions import VariantAssertions

class TestVariants(unittest.TestCase, VariantAssertions):
    vcf = "tests/variants.vcf.gz"
    vcf_with_genotypes = "tests/variants-with-genotypes.vcf.gz"

    def test_variant_at(self):
        self.assertVcfHasVariantAt(self.vcf, 3, 178936091)

    def test_variant_with_chrom_pos_ref_alt(self):
        self.assertVcfHasVariantWithChromPosRefAlt(self.vcf_with_genotypes, 1, 3062915, 'G', 'C')
        self.assertVcfHasVariantWithChromPosRefAlt(self.vcf_with_genotypes, 1, 3062915, 'G', 'T')

    def test_variant_with_id(self):
        self.assertVcfHasVariantWithChromPosId(self.vcf_with_genotypes, 1, 3062915, 'id3D')

~~~

The `test_vcf_has_variant_with_call()` asserts that individual items in a sample call are set. The parameter `call` is a dict with the items to test. The dict does not have to be complete, i.e. not all fields in the call have to be tested. 

~~~python    
    def test_vcf_has_variant_with_call(self):
        self.assertVcfHasVariantWithCall(self.vcf_with_genotypes, 1, 3184885, 'B',
                                         call={'GT': '1/2', 'DP': 10})
~~~

# Vcf requirements

`genomicasserttions` requires the vcf files to be compressed with `bgzip` and indexed with `tabix` in order to work. This is required for the random access to variants provided by the index, which gives a significant performance increase over using non-indexed vcf files. 

