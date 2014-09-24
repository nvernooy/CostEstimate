from persistent import Persistent

# Project.py
# Root object
# Contains a collection of BudgetGroup objects and performs operations on them
class Project(Persistent):

    def __init__(self):
        self.Name = ''
        self.Description = ''
        self.Bgroups['BudgetGroups'] = BTree()

    def __init__(self, name, desc):
        self.Name = name
        self.Description = desc
        self.GroupSet = set()

    def add(self, group):
        self.GroupSet.add(group)

    def delete(self, group):
        self.GroupSet.remove (group)

    # makes this object hashable so it can be used in a set
    def __hash__(self):
        return hash(self.Name)

    #makes this object equitable so it can be hashable
    def __eq__(self, other):
        return self.Name == other.Name

    #tostring method
    def __str__(self):
        return (self.Name + ": " + self.Description)


# BudgetGroup.py
# Contains a collection of BudgetItem objects and performs operations on them
class BudgetGroup(Persistent):

    def __init__(self):
        self.Name = ''
        self.Description = ''
        self.ItemSet = set()

    def __init__(self, name, desc):
        self.Name = name
        self.Description = desc
        self.ItemSet = set()

    def add(self, item):
        self.ItemSet.add(item)

    def delete(self, item):
        self.ItemSet.remove(item)

    # makes this object hashable so it can be used in a set
    def __hash__(self):
        return hash(self.Name)

    #makes this object equitable so it can be hashable
    def __eq__(self, other):
        return self.Name == other.Name
    
    #tostring method
    def __str__(self):
        return (self.Name + ": " + self.Description)


# BudgetItem.py
# leaf object
# Contains attributes and performs operations on them
class BudgetItem(Persistent):

    def __init__(self):
        self.Name = ''
        self.Description = ''
        iself.Quantity = 0
        self.Rate = 0

    def __init__(self, name, desc, quan, rate):
        self.Name = name
        self.Description = desc
        self.Quantity = quan
        self.Rate = rate
    
        
    # returns the items multiplied by their rate 
    def subtotal(self):
        return self.Quantity*self.Rate

    # calculates the vat on this item
    def vat(self):
        return subtotal()*0.14

    # returns the subtotal plus vat
    def total (self):
        return (subtotal+vat)

    # makes this object hashable so it can be used in a set
    def __hash__(self):
        return hash(self.Name)

    #makes this object equitable so it can be hashable
    def __eq__(self, other):
        return self.Name == other.Name

    #tostring method
    def __str__(self):
        return (self.Name + ": " + self.Description)
        




