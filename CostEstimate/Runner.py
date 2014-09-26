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

def addData():
    # Enter data for constructing the objects.
    name = raw_input("\nEnter Project Name:\n")
    desc = raw_input("\nEnter Project Description:\n")

    # Instantiate a Project
    project = Project(name, desc)

    # Loop while adding groups and items
    while True:
        # The user has to enter "0" to stop the loop
        if "0" == raw_input ("\nEnter 0 to stop adding BudgetGroups: "):
                break
        
        name = raw_input("\nEnter BudgetGroup Name:\n")
        desc = raw_input("\nEnter BudgetGroup Description:\n")

        # Instantiate a BudgetGroup object
        group = BudgetGroup(name, desc)

        # Loop and add multiple Items
        while True:
            # The user has to enter "0" to stop the loop
            if "0" == raw_input ("\nEnter 0 to stop adding BudgetItems: "):
                break
            
            name = raw_input("\nEnter BudgetItem Name:\n")
            desc = raw_input("\nEnter BudgetItem Description:\n")
            quan = raw_input("\nEnter BudgetItem Quantity:\n")
            rate = raw_input("\nEnter BudgetItem Rate:\n")           

            # Instantiate a BudgetItem.
            item = BudgetItem (name, desc, int(quan), int(rate))
            group.add(item)
            
        project.add(group)
        

    # Return the Project will all the objects in it
    return project


if __name__ == "__main__":
    # Create the database connection.
    storage = ZODB.FileStorage.FileStorage('ProjectData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root

    # Creat a projects table in the database using OOBTree.
    root.projects = OOBTree()
    project = Project()


    while True:
        # Make a selection in the menu.
        select = raw_input("Make your selection\n"+
                           "1\tAdd a project\n"+
                           "2\tDisplay data\n"+
                           "3\tDisplay costs\n"+
                           "4\tExit\n")

        # Add a project and fill it
        if select == "1":
            # Run the addData method that returns a finished Project
            project = addData()
            
            # Add the Project object to the database, using the Project name as the key
            root.projects[project.Name] = project
            # Commit the change to the database
            transaction.commit()
        # Print out the contents of the database.
        elif select == "2":
            for key in root.projects.keys():
                print root.projects[key]
        # Print the subtotal, vat, and total of the Project
        elif select == "3":
            for key in root.projects.keys():                
                print (root.projects[key].Name + ": " +
                       root.projects[key].Description)
                print ("\tSubtotal: " + str(root.projects[key].subtotal()))
                print ("\tVAT: " + str(root.projects[key].vat()))
                print ("\tTotal: " + str(root.projects[key].total()))
        # End the loop if the user enters 4
        elif select == "4":
            break
            
        
    
    # Close the database
    transaction.commit()
    connection.close()
    db.close()
    storage.close()
