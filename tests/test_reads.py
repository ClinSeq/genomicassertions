import unittest
from genomicassertions.readassertions import ReadAssertions


class TestReads(unittest.TestCase, ReadAssertions):
    bam = "tests/3_178936091.bam"

    def test_has_coverage_as_pos(self):
	self.assertBamHasCoverageAt(self.bam, 324, 3, 178936091)

    def test_raises_if_incorrect_coverage(self):
	with self.assertRaises(AssertionError):
	    self.assertBamHasCoverageAt(self.bam, 323, 3, 178936091)
