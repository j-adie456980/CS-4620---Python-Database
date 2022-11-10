import sqlite3

def displayData():
  print("\nDisplaying data . . . \n")
  conn = sqlite3.connect("example.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM chromosomes")
  print("Chromosome Table:  ", cursor.fetchall())
  cursor.execute("SELECT * FROM interactions")
  print("Interaction Table: ", cursor.fetchall())
  cursor.execute("SELECT * FROM loci")
  print("Locus Table:       ", cursor.fetchall())
  cursor.execute("SELECT * FROM genes")
  print("Gene Table:        ", cursor.fetchall())
  cursor.execute("SELECT * FROM motifs")
  print("Motif Table:       ", cursor.fetchall())
  conn.close()