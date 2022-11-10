from entityTypes import Chromosome, Interaction, Locus, Gene, Motif
import sqlite3

def insertChromosomes():
  conn = sqlite3.connect("example.db")
  cursor = conn.cursor()

  option = input("""
---Select Insert Type---
1.) Import Data File
2.) Manually Input Data

x.) Go Back

Enter Here: """)
  if option == '1': 
    print("Inserting . . .")
  elif option == '2': 
    print("Inserting . . .")
    temp = Chromosome("", "")
    temp.chromosomeID = input("Chromosome ID:  ")
    temp.cellType = input("Cell Type:  ")
    cursor.execute("INSERT INTO chromosomes VALUES (?, ?)", (temp.chromosomeID, temp.cellType))
    conn.commit()
    conn.close()
  elif option == 'x': return

  

def insertInteractions():
  option = input("""
---Select Insert Type---
1.) Import Data File
2.) Manually Input Data

x.) Go Back

Enter Here: """)
  if option == '1': 
    print("Inserting . . .")
  elif option == '2': 
    print("Inserting . . .")
  elif option == 'x': return
  

def insertLoci():
  option = input("""
---Select Insert Type---
1.) Import Data File
2.) Manually Input Data

x.) Go Back

Enter Here: """)
  if option == '1': 
    print("Inserting . . .")
  elif option == '2': 
    print("Inserting . . .")
  elif option == 'x': return

def insertGenes():
  option = input("""
---Select Insert Type---
1.) Import Data File
2.) Manually Input Data

x.) Go Back

Enter Here: """)
  if option == '1': 
    print("Inserting . . .")
  elif option == '2': 
    print("Inserting . . .")
  elif option == 'x': return

def insertMotifs():
  option = input("""
---Select Insert Type---
1.) Import Data File
2.) Manually Input Data

x.) Go Back

Enter Here: """)
  if option == '1': 
    print("Inserting . . .")
  elif option == '2': 
    print("Inserting . . .")
  elif option == 'x': return

def insertData():
  option = None
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