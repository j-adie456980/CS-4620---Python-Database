import sqlite3

def displayData():
  print("\nDisplaying data . . . \n")
  conn = sqlite3.connect("DataTables.db")
  cursor = conn.cursor()
  while 1:
    option = input("""
---Select Table---
1.) Chromosome
2.) Interaction
3.) Locus 
4.) Gene
5.) Motif
6.) Display All

x.) Go Back

Enter Here: """)
    if option == '1': 
      cursor.execute("SELECT * FROM chromosomes")
      for i in cursor.fetchall(): print(i)
    elif option == '2': 
      cursor.execute("SELECT * FROM interactions")
      for i in cursor.fetchall(): print(i)
    elif option == '3': 
      cursor.execute("SELECT * FROM loci")
      for i in cursor.fetchall(): print(i)
    elif option == '4': 
      cursor.execute("SELECT * FROM genes")
      for i in cursor.fetchall(): print(i)
    elif option == '5': 
      cursor.execute("SELECT * FROM motifs")
      for i in cursor.fetchall(): print(i)
    elif option == '6': 
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
    elif option == 'x': break
    else: print("Invalid option")

  
  conn.close()