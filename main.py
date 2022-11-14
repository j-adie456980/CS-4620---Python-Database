from insertData import insertData
from queryData import queryData
from displayData import displayData
from createTables import createTables

# I am new to python so this program might look unusual

def closeProg():
  print("Closing . . .")
  quit()

while 1:
  option = input("""
---Select an option---
1.) Insert Data
2.) Display Data
3.) Create Data Tables
4.) Make Query
x.) Close

Enter Here: """)

  if option == '1': insertData()
  elif option == '2': displayData()
  elif option == '3': createTables()
  elif option == '4': queryData()
  elif option == 'x': closeProg()
  else: print("Invalid option")