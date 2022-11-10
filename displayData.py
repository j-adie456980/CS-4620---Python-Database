import sqlite3

def displayData():
  print("\nDisplaying data . . . ")
  conn = sqlite3.connect("example.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM chromosomes")
  print(cursor.fetchall())
  cursor.execute("SELECT * FROM interactions")
  print(cursor.fetchall())
  cursor.execute("SELECT * FROM loci")
  print(cursor.fetchall())
  cursor.execute("SELECT * FROM genes")
  print(cursor.fetchall())
  cursor.execute("SELECT * FROM motifs")
  print(cursor.fetchall())
  conn.close()