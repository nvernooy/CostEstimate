from persistent import Persistent
from BTrees.OOBTrees import BTree


# Project.py
# Root object
# Contains a collection of BudgetGroup objects and performs operations on them
class Project(Persistent):

    def __init__(self):
        self.Name = ''
        self.Description = ''
        self.Bgroups['BudgetGroups'] = BTree()

    def add(self, group):
        self.Bgroups[group.Name] = group

    def delete(self, group):
        # write
        print "need to write this"


# BudgetGroup.py
# Contains a collection of BudgetItem objects and performs operations on them
class BudgetGroup(Persistent):

    def __init__(self):
        self.Name = ''
        self.Description = ''
        self.Bitems['BudgetItems'] = BTrees.OOBTrees()

    def add(self, item):
        self.Bitems[item.Name] = item

    def delete(self, item):
        # write
        print "need to write this"


# BudgetItem.py
# leaf object
# Contains attributes and performs operations on them
class BugetItem(Persistent):

    def __init__(self):
        self.Name = ''
        self.Description = ''
        int self.Quantity = 0
        int self.Rate = 0
        

    def subtotal(self):
        return self.Quantity*self.Rate

    def vat(self):
        return subtotal()*0.14

    def total (self)
        return (subtotal+vat)
        




