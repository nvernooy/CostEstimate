from BTrees.OOBTree import OOBTree
from models import Project, BudgetGroup, BudgetItem 
import ZODB, ZODB.FileStorage
import transaction

if __name__ == "__main__":
    # create db connection
    storage = ZODB.FileStorage.FileStorage('ProjectData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root

    root.projects = OOBTree()
    
   # print "Make your selection\n1\tAdd data\n2\tDisplay data"

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

    item = BudgetItem (name, desc, quan, rate)

    print ("Enter BudgetGroup Name:")
    name = raw_input()

    print ("Enter BudgetGroup Description:")
    desc = raw_input()

    group = BudgetGroup(name, desc)
    group.add(item)

    print ("Enter Project Name:")
    name = raw_input()

    print ("Enter Project Description:")
    desc = raw_input()

    project = Project(name, desc)
    project.add(group)
    

    # add a project to the db
    root.projects[project.Name] = project

    # commit the change to the db
    transaction.commit()

    #print it out
    for key in root.projects.keys():
          print key + ':', root.projects[key]

    #close the db
    connection.close()
    db.close()
    storage.close()
