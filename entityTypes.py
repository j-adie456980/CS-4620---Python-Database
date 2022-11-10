class Chromosome:

    def __init__(self, chromosomeID, cellType):
        self.chromosomeID = chromosomeID
        self.cellType = cellType

    def __repr__(self):
        return "Chromosome: {} | {} ".format(self.chromosomeID, self.cellType)

class Interaction:

    def __init__(self, interactionID, locusID1, locusID2, cellType):
        self.interactionID = interactionID
        self.locusID1 = locusID1
        self.locusID2 = locusID2
        self.cellType = cellType

    def __repr__(self):
        return "Interaction: {} | {} | {} | {}".format(self.interactionID, self.locusID1, self.locusID2, self.cellType)

class Locus:

    def __init__(self, locusID, chromosome, start, end):
        self.locusID = locusID
        self.chromosome = chromosome
        self.start = start
        self.end = end

    def __repr__(self):
        return "Locus: {} | {} | {} | {}".format(self.locusID, self.chromosome, self.start, self.end)

class Gene:

    def __init__(self, name, chromosome, start, end, DNexp, PGNexp, length):
        self.name = name
        self.chromosome = chromosome
        self.start = start
        self.end = end
        self.DNexp = DNexp
        self.PGNexp = PGNexp
        self.length = length

    def __repr__(self):
        return "Gene: {} | {} | {} | {} | {} | {} | {} ".format(self.name, self.chromosome, self.start, self.end, self.DNexp, self.PGNexp, self.length)

class Motif:

    def __init__(self, motifID, name, familyName, chromosome, start, end, threshold, cellType):
        self.motifID = motifID
        self.name = name
        self.familyName = familyName
        self.chromosome = chromosome
        self.start = start
        self.end = end
        self.threshold = threshold
        self.cellType = cellType

    def __repr__(self):
        return "Motif: {} | {} | {} | {} | {} | {} | {} | {} ".format(self.motifID, self.name, self.familyName, self.chromosome, self.start, self.end, self.threshold, self.cellType)