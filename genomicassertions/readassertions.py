import pysam


class ReadAssertions:
    def __init__(self):
	pass

    def assertBamHasCoverageAt(self, bam, coverage, chrom, pos):
	samfile = pysam.AlignmentFile(bam, "rb")
	iter = samfile.pileup('3', pos-1, pos, truncate=True)
	pile = iter.next()
	if pile.nsegments != coverage:
	    raise AssertionError("Coverage at {}:{} was not {} in {} (got {})".format(chrom, pos, coverage, bam, pile.nsegments))

    def assertBamHasHeaderElement(self, bam, header_element):
	samfile = pysam.AlignmentFile(bam, "rb")
	if header_element not in samfile.header:
	    raise AssertionError("Header element {} not in header of {}".format(header_element, bam))