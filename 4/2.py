class Sequence(object):

    def __init__(self, string: str) -> None:
        self.string = string

    def transcribe(self) -> None:
        raise NameError

    def hamming_distance(self, s2: str) -> int:
        diff = 0
        if len(self.string) != len(s2):
            raise ValueError('different length')
        else:
            for i in range(len(self.string)):
                if self.string[i] != s2[i]:
                    diff += 1
        return (diff)


class DNA(Sequence):

    def count_nucleotides(self) -> dict:
        A: int = self.string.count('A')
        T: int = self.string.count('T')
        G: int = self.string.count('G')
        C: int = self.string.count('C')
        return {'A': A, 'T': T, 'G': G, 'C': C}

    def transcribe(self) -> str:
        transcript_DNA = self.string.replace('T', 'U')
        return (transcript_DNA)

    def complement_dna(self) -> str:
        complement_dna = self.string
        complement_dna = complement_dna.replace('A', 'a')
        complement_dna = complement_dna.replace('T', 'A')
        complement_dna = complement_dna.replace('a', 'T')
        complement_dna = complement_dna.replace('G', 'g')
        complement_dna = complement_dna.replace('C', 'G')
        complement_dna = complement_dna.replace('g', 'C')
        return (complement_dna)


class RNA(Sequence):

    def transcribe(self) -> str:
        transcript_RNA = self.string.replace('U', 'T')
        return (transcript_RNA)

    def count_nucleotides(self) -> dict:
        A: int = self.string.count('A')
        U: int = self.string.count('U')
        G: int = self.string.count('G')
        C: int = self.string.count('C')
        return {'A': A, 'U': U, 'G': G, 'C': C}
a = DNA(input())
ab = a.hamming_distance(input())
print(ab)
ac = a.count_nucleotides()
print(ac)
ad = a.transcribe()
print(ad)
ae = a.complement_dna()
print(ae)
ra = RNA(input())
rb = ra.transcribe()
print(rb)
