import sqlite3

def querySet():
  print("do more stuff . . .")

def queryManual():
  conn = sqlite3.connect("DataTables.db")
  cursor = conn.cursor() 
  temp = input("\nEnter query here: ")
  cursor.execute("PRAGMA foreign_keys = 1")
  cursor.execute(temp)
  conn.commit()
  conn.close()

def queryData():
  option = None
  while 1:
    option = input("""
---Select Query Type---
1.) Preset Queries
2.) Input Custom Query

x.) Go Back

Enter Here: """)
    if option == '1': querySet()
    elif option == '2': queryManual()
    elif option == 'x': break
    else: print("Invalid option")