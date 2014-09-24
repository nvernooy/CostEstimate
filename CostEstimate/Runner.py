from BTrees.OOBTree import BTree
from models import Project
import ZODB, ZODB.FileStorage, Project, transation

if __name__ == "__main__":
    # create db connection
    storage = ZODB.FileStorage.FileStorage('ProjectData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root

    # add a project to the db
    root.projects = BTree()
    root.projects['Project1'] = Project()

    # commit the change to the db
    transaction.commit()
