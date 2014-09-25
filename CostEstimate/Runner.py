"""
File Runner.py contains the main method for the Cost Estimate project.
It creates the databse connection with ZODB and asks for user input.
The user input is used to create Project objects from models.py
and it's related objects.
These are stored in the ProjectData database.
"""

from BTrees.OOBTree import OOBTree
import ZODB
import ZODB.FileStorage
import transaction
from models import Project, BudgetGroup, BudgetItem 

if __name__ == "__main__":
    # Create the database connection.
    storage = ZODB.FileStorage.FileStorage('ProjectData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root

    # Creat a projects table in the database using OOBTree.
    root.projects = OOBTree()
    
   # print "Make your selection\n1\tAdd data\n2\tDisplay data"

    # Enter data for constructing the objects.
    print ("Enter BudgetItem Name:")
    name = raw_input()

    print ("Enter BudgetItem Description:")
    desc = raw_input()

    print ("Enter BudgetItem Quantity:")
    quan = raw_input()
    quan = int(quan)

    print ("Enter BudgetItem Rate:")
    rate = raw_input()
    rate = int(rate)

    # Instantiate a BudgetItem.
    item = BudgetItem (name, desc, quan, rate)

    print ("Enter BudgetGroup Name:")
    name = raw_input()

    print ("Enter BudgetGroup Description:")
    desc = raw_input()

    # Instantiate a BudgetGroup object and add the BudgetItem to it.
    group = BudgetGroup(name, desc)
    group.add(item)

    print ("Enter Project Name:")
    name = raw_input()

    print ("Enter Project Description:")
    desc = raw_input()

    # Instantiate a Project and add the BudgetGroup to it.
    project = Project(name, desc)
    project.add(group)
    

    # Add the Project object to the database, using the Project name as the key
    root.projects[project.Name] = project

    # Commit the change to the database
    transaction.commit()

    # Print out the contents of the database.
    for key in root.projects.keys():
          print key + ':', root.projects[key]

    # Close the database
    connection.close()
    db.close()
    storage.close()
