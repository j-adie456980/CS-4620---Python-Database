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
    if option == '1': print("Inserting 1")
    elif option == '2': print("Inserting 2")
    elif option == '3': print("Inserting 3")
    elif option == '4': print("Inserting 4")
    elif option == '5': print("Inserting 5")
    elif option == 'x': break
    else: print("Invalid option")