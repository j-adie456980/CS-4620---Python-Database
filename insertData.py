from entityTypes import Chromosome, Interaction, Locus, Gene, Motif
import sqlite3
import pandas as pd

def insertChromosomes():
  conn = sqlite3.connect("DataTables.db")
  cursor = conn.cursor()

  option = input("""
---Select Insert Type---
1.) Import Data File
2.) Manually Input Data

x.) Go Back

Enter Here: """)
  if option == '1': 
    print("This will be implemented when a chromosome data file is defined . . .")
  elif option == '2': 
    temp = Chromosome("", "")
    temp.chromosomeID = input("Chromosome ID:  ")
    temp.cellType = input("Cell Type:  ")
    cursor.execute("INSERT INTO chromosomes VALUES (?, ?)", (temp.chromosomeID, temp.cellType))
    conn.commit()
    conn.close()
  elif option == 'x': return

  

def insertInteractions():
  conn = sqlite3.connect("DataTables.db")
  cursor = conn.cursor()

  option = input("""
---Select Insert Type---
1.) Import Data File
2.) Manually Input Data

x.) Go Back

Enter Here: """)
  if option == '1': 
    fileName = "Data/" + input("Enter file name:  ")
    temp = Interaction(None, None, None, None)
    temp.cellType = input("Cell Type:  ")
    dataFrame = pd.read_csv(fileName, sep="\t", names=["ID1", "ID2"])
    dataFrame = dataFrame.reset_index()
    for index, row in dataFrame.iterrows():
      temp.locusID1 = row['ID1']
      temp.locusID2 = row['ID2']
      temp.interactionID = temp.locusID1 + temp.locusID2
      cursor.execute("INSERT INTO interactions VALUES (?, ?, ?, ?)", (temp.interactionID, temp.locusID1, temp.locusID2, temp.cellType))
    conn.commit()
    conn.close()
  elif option == '2': 
    temp = Interaction(None, None, None, None)
    temp.locusID1 = input("Locus ID 1:  ")
    temp.locusID2 = input("Locus ID 2:  ")
    temp.cellType = input("Cell Type:  ")
    temp.interactionID = temp.locusID1 + temp.locusID2
    cursor.execute("INSERT INTO interactions VALUES (?, ?, ?, ?)", (temp.interactionID, temp.locusID1, temp.locusID2, temp.cellType))
    conn.commit()
    conn.close()
  elif option == 'x': return
  

def insertLoci():
  conn = sqlite3.connect("DataTables.db")
  cursor = conn.cursor()
  option = input("""
---Select Insert Type---
1.) Import Data File
2.) Manually Input Data

x.) Go Back

Enter Here: """)
  if option == '1': 
    print("This will be implemented when a Locus data file is defined . . .")
  elif option == '2': 
    temp = Locus(None, None, None, None)
    temp.chromosome = input("Chromosome:  ")
    temp.start = input("Start Pos:  ")
    temp.end = input("End Pos:  ")
    temp.locusID = "{}:{}:{}".format(temp.chromosome, temp.start, temp.end)
    cursor.execute("INSERT INTO loci VALUES (?, ?, ?, ?)", (temp.locusID, temp.chromosome, temp.start, temp.end))
    conn.commit()
    conn.close()
  elif option == 'x': return

def insertGenes():
  conn = sqlite3.connect("DataTables.db")
  cursor = conn.cursor()
  option = input("""
---Select Insert Type---
1.) Import Data File
2.) Manually Input Data

x.) Go Back

Enter Here: """)
  if option == '1': 
    fileName = "Data/" + input("Enter file name:  ")
    temp = Gene(None, None, None, None, None, None, None)
    dataFrame = pd.read_csv(fileName, sep=",", names=["name", "chromosome", "start", "end", "DNexp", "length", "PGNexp"])
    dataFrame = dataFrame.reset_index()
    for index, row in dataFrame.iterrows():
      temp.name = row['name']
      temp.chromosome = row['chromosome']
      temp.start = row['start']
      temp.end = row['end']
      temp.DNexp = row['DNexp']
      temp.length = row['length']
      temp.PGNexp = row['PGNexp']
      cursor.execute("INSERT INTO genes VALUES (?, ?, ?, ?, ?, ?, ?)", (temp.name, temp.chromosome, temp.start, temp.end, temp.DNexp, temp.PGNexp, temp.length))
    conn.commit()
    conn.close()
  elif option == '2': 
    temp = Gene(None, None, None, None, None, None, None)
    temp.name = input("Gene Name:  ")
    temp.chromosome = input("Chromosome:  ")
    temp.start = input("Start Pos:  ")
    temp.end = input("End Pos:  ")
    temp.DNexp = input("DN Expression Level:  ")
    temp.PGNexp = input("PGN Expression Level:  ")
    temp.length = input("Length:  ")
    cursor.execute("INSERT INTO genes VALUES (?, ?, ?, ?, ?, ?, ?)", (temp.name, temp.chromosome, temp.start, temp.end, temp.DNexp, temp.PGNexp, temp.length))
    conn.commit()
    conn.close()
  elif option == 'x': return

def insertMotifs():
  conn = sqlite3.connect("DataTables.db")
  cursor = conn.cursor()
  option = input("""
---Select Insert Type---
1.) Import Data File
2.) Manually Input Data

x.) Go Back

Enter Here: """)
  if option == '1': 
    fileName = "Data/" + input("Enter file name:  ")
    temp = Motif(None, None, None, None, None, None, None, None)
    temp.cellType = input("Cell Type:  ")
    dataFrame = pd.read_csv(fileName, sep="\t", names=["locusChromo", "locusStart", "locusEnd", "locusID", "chromosome", "start", "end", "name", "threshold", "direction"])
    dataFrame = dataFrame.reset_index()
    for index, row in dataFrame.iterrows():
      temp.name = row['name']
      temp.familyName = "missing for data format"
      temp.chromosome = row['chromosome']
      temp.start = row['start']
      temp.end = row['end']
      temp.threshold = row['threshold']
      temp.locusID = row['locusID']
      temp.motifID = "{}:{}:{}".format(temp.chromosome, temp.start, temp.end)
      cursor.execute("PRAGMA foreign_keys = 1")
      cursor.execute("INSERT INTO motifs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (temp.motifID, temp.name, temp.familyName, temp.chromosome, temp.start, temp.end, temp.threshold, temp.cellType, temp.locusID))
    conn.commit()
    conn.close()
  elif option == '2': 
    temp = Motif(None, None, None, None, None, None, None, None, None)
    temp.name = input("Motif Name:  ")
    temp.familyName = input("Family Name:  ")
    temp.chromosome = input("Chromosome:  ")
    temp.start = input("Start Pos:  ")
    temp.end = input("End Pos:  ")
    temp.threshold = input("Threshold Value:  ")
    temp.cellType = input("Cell Type:  ")
    temp.locusID = input("Locus ID:  ")
    temp.motifID = "{}:{}:{}".format(temp.chromosome, temp.start, temp.end)
    cursor.execute("PRAGMA foreign_keys = 1")
    cursor.execute("INSERT INTO motifs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (temp.motifID, temp.name, temp.familyName, temp.chromosome, temp.start, temp.end, temp.threshold, temp.cellType, temp.locusID))
    conn.commit()
    conn.close()
  elif option == 'x': return

def insertData():
  while 1:
    option = input("""
---Select Data Type---
1.) Chromosome
2.) Interaction
3.) Locus 
4.) Gene
5.) Motif

x.) Go Back

Enter Here: """)
    if option == '1': insertChromosomes()
    elif option == '2': insertInteractions()
    elif option == '3': insertLoci()
    elif option == '4': insertGenes()
    elif option == '5': insertMotifs()
    elif option == 'x': break
    else: print("Invalid option")