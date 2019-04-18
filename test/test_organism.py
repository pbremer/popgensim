import unittest
from popgensim.organism import Organism, Allele, Genotype, Phenotype

class TestOrganism(unittest.TestCase):

    _homozygous_dominate = Organism((Allele.DOMINATE, Allele.DOMINATE))
    _homozygous_recessive = Organism((Allele.RECESSIVE, Allele.RECESSIVE))
    _heterozygous_dr = Organism((Allele.DOMINATE, Allele.RECESSIVE))
    _heterozygous_rd = Organism((Allele.RECESSIVE, Allele.DOMINATE))

    def test_mate(self):
        """
        Note: Unable to test the hetrozygous organisms due to the random
        nature of the function
        """
        self.assertEqual(self._homozygous_dominate.mate(), Allele.DOMINATE)
        self.assertEqual(self._homozygous_recessive.mate(), Allele.RECESSIVE)
    
    def test_genotype(self):
        self.assertEqual(self._homozygous_dominate.genotype(), Genotype.HOMOEZYGOUS_DOMINATE)
        self.assertEqual(self._homozygous_recessive.genotype(), Genotype.HOMOEZYGOUS_RECESSIVE)
        self.assertEqual(self._heterozygous_dr.genotype(), Genotype.HETEROZYGOUS)
        self.assertEqual(self._heterozygous_rd.genotype(), Genotype.HETEROZYGOUS)
    
    def test_phenotype(self):
        self.assertEqual(self._homozygous_dominate.phenotype(), Phenotype.DOMINATE)
        self.assertEqual(self._homozygous_recessive.phenotype(), Phenotype.RECESSIVE)
        self.assertEqual(self._heterozygous_dr.phenotype(), Phenotype.DOMINATE)
        self.assertEqual(self._heterozygous_rd.phenotype(), Phenotype.DOMINATE)


if __name__ == '__main__':
    unittest.main()
