import sqlite3

def createTables():
  conn = sqlite3.connect("example.db")
  cursor = conn.cursor()

  cursor.execute("""CREATE TABLE chromosomes (
    chromosomeID text,  
    cellType text,
    PRIMARY KEY (chromosomeID))""")

  cursor.execute("""CREATE TABLE interactions (
    interactionID text, 
    locusID1 text, 
    locusID2 text, 
    cellType text,
    PRIMARY KEY (interactionID) )""")

  cursor.execute("""CREATE TABLE loci (
    locusID text,
    chromosome text, 
    start text,
    end text,
    PRIMARY KEY (locusID) )""")

  cursor.execute("""CREATE TABLE genes (
    name text,
    chromosome text,
    start text,
    end text,
    DNexp text,
    PGNexp text,
    length text,
    locusID text,
    PRIMARY KEY (name), 
    FOREIGN KEY (locusID) REFERENCES loci(locusID) )""")

  cursor.execute("""CREATE TABLE motifs (
    motifID text,
    name text,
    familyName text,
    chromosome text,
    start text,
    end text,
    threshold text,
    cellType text,
    locusID text,
    PRIMARY KEY (motifID), 
    FOREIGN KEY (locusID) REFERENCES loci(locusID) )""")

  conn.commit()
  conn.close()