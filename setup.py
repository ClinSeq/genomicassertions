from setuptools import setup, find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt", session=False)

# reqs is a list of requirement
reqs = [str(ir.req) for ir in install_reqs if ir.req is not None]

setup(name='genomicassertions',
      author='Daniel Klevebring',
      author_email='daniel.klevebring@gmail.com',
      url='https://github.com/dakl/genomicassertions',
      description='A package to test common files in genomics (.vcf.gz, .bam)',
      version='0.2.1',
      download_url='https://github.com/dakl/genomicassertions/tarball/v0.2.1',
      packages=find_packages(exclude=('tests*', 'docs', 'examples')),
      keywords=['testing', 'genomics'],
      install_requires=reqs
      )
