from enum import IntEnum
from typing import Tuple
from random import choice, choices

class Allele(IntEnum):
    DOMINATE = 2
    RECESSIVE = 1

class Genotype(IntEnum):
    HOMOEZYGOUS_DOMINATE = Allele.DOMINATE
    HOMOEZYGOUS_RECESSIVE = Allele.RECESSIVE
    HETEROZYGOUS = Allele.DOMINATE | Allele.RECESSIVE

class Phenotype(IntEnum):
    DOMINATE = Allele.DOMINATE
    RECESSIVE = Allele.RECESSIVE

class Organism:
    """
    Organism class
    """

    def __init__(self, alleles: Tuple[Allele, Allele]) -> None:
        self._alleles = alleles
    
    def mate(self) -> Allele:
        return choice(self._alleles)
    
    def genotype(self) -> Genotype:
        return Genotype(self._alleles[0] | self._alleles[1])

    def phenotype(self) -> Phenotype:
        return Phenotype(max(self._alleles))