"""
The models.py file contains the objects used in the Cost Estimate database.
The objects are derived from the Persistant class in order to be used with ZODB.
The objects form a hierachy with Project() at the top, which contains
BudgetGroup(), which contains BudgetItem().
"""

from persistent import Persistent

class Project(Persistent):
    """
    The Project object is at the top of the hierarchy.
    It contains a Name and Description attribute, and a set of
    BudgetGroup() objects.
    It has methods to add and remove BudgetGroups.
    It also has methods to calculate the subtotal, vat, and total of the
    BudgetGroups.
    The class is hashable and has a toString method.
    """

    VAT = 0.14

    def __init__(self):
        """The empty constructor."""
        
        self.Name = ''
        self.Description = ''
        self.GroupSet = set()

    def __init__(self, name, desc):
        """
        The Project constructor takes a string name and desc as the Name of
        the project, and it's Description.
        It initialises with an empty set.
        """
        
        self.Name = name
        self.Description = desc
        self.GroupSet = set()

    def add(self, group):
        """The add method adds a BudgetGroup object to the set."""
        self.GroupSet.add(group)

    def delete(self, group):
        """The delete method removes a BudgetGroup object from the set."""
        self.GroupSet.remove(group)
 
    def subtotal(self):
        """
        The subtotal function returns the total of the subtotal of all
        the BudgetGroup objects.
        """
        stotal = 0
        for group in self.GroupSet:
            stotal+=group.subtotal

        return stotal
    

    def vat(self):
        """
        The vat function calculates the VAT percentage on the subtotal.
        Computing the percentage on the subtotal is more efficient than
        computing the percentage of each group and adding it.
        """
        return subtotal()*VAT

   
    def total (self):
        """
        The total function computes the cost of the project plus VAT.
        Computing the subtotal increasing it with the VAT percentage is
        more efficient than computing the subtotal and VAT separately.
        """
        return (subtotal*(1+VAT))
                

    def __hash__(self):
        """This enables the class to be hashable"""
        return hash(self.Name)

    def __eq__(self, other):
        """This enables the class to be hashable"""
        return self.Name == other.Name

    def __str__(self):
        """
        The toString method returns a string of the name and
        description of the class.
        """
        return (self.Name + ": " + self.Description)

 
class BudgetGroup(Persistent):
    """
    The BudgetGroup class contains a set of BudgetItem objects
    and is contained by Project.
    It has Name and Description string attributes, and a set of BudgetItems.
    It has methods to add and delete BudgetItem instances from the set.
    BudgetGroup has functions to calculate the subtotal, vat, and total of
    the BudgetItems in the set.
    The class is hashable and has a toString method.
    """

    VAT = 0.14

    def __init__(self):
        """The empty constructor."""
        self.Name = ''
        self.Description = ''
        self.ItemSet = set()

    def __init__(self, name, desc):
        """
        The BudgetGroup constructor takes a string name and desc as the Name of
        the project, and it's Description.
        It initialises with an empty set.
        """
        self.Name = name
        self.Description = desc
        self.ItemSet = set()

    def add(self, item):
        """The add method adds a BudgetItem object to the set."""
        self.ItemSet.add(item)

    def delete(self, item):
        """The delete method removes a BudgetGroup object from the set."""
        self.ItemSet.remove(item)

    def subtotal(self):
        """
        The subtotal function returns the total of the subtotal of all
        the BudgetItem objects.
        """
        stotal = 0
        for group in self.ItemSet:
            stotal+=group.subtotal

        return stotal


    def vat(self):
        """
        The vat function calculates the VAT percentage on the subtotal.
        Computing the percentage on the subtotal is more efficient than
        computing the percentage of each item and adding it.
        """
        return subtotal()*VAT

 
    def total (self):
        """
        The total function computes the cost of the BudgetGroup plus VAT.
        Computing the subtotal increasing it with the VAT percentage is
        more efficient than computing the subtotal and VAT separately.
        """
        return (subtotal*(1+VAT))


    def __hash__(self):
        """This enables the class to be hashable"""
        return hash(self.Name)

                
    def __eq__(self, other):
        """This enables the class to be hashable"""
        return self.Name == other.Name
    

    def __str__(self):
        """
        The toString method returns a string of the name and
        description of the class.
        """
        return (self.Name + ": " + self.Description)


class BudgetItem(Persistent):
    """
    The BudgetItem class is at the bottom of the Cost Estimate hierarchy, 
    it is contained in the BudgetGroup class
    It has Name and Description string attributes, as well as Quantity
    and Rate number attributes.
    It has functions to calculate the subtotal, vat, and total of
    the items in the object.
    The class is hashable and has a toString method.
    """

    VAT = 0.14

    def __init__(self):
        """The empty constructor."""
        self.Name = ''
        self.Description = ''
        iself.Quantity = 0
        self.Rate = 0

    def __init__(self, name, desc, quan, rate):
        """
        The BudgetItem constructor takes a string name and desc as the Name of
        the project, and it's Description.
        It takes quan and rate as numbers for Quantity and Rate.
        """
        self.Name = name
        self.Description = desc
        self.Quantity = quan
        self.Rate = rate
    
        
    def subtotal(self):
        """
        The subtotal function returns the product of the Quantity and Rate
        attributes as the cost of the items in this object.
        """
        return self.Quantity*self.Rate


    def vat(self):
        """
        The vat function calculates the VAT percentage on the subtotal.
        It represents the VAT added to this item.
        """
        return subtotal()*VAT

 
    def total (self):
        """
        The total function adds the subtotal and VAT of this item.
        It represents the total cost of this item.
        """
        return (subtotal+vat)


    def __hash__(self):
        """This enables the class to be hashable"""
        return hash(self.Name)


    def __eq__(self, other):
        """This enables the class to be hashable"""
        return self.Name == other.Name


    def __str__(self):
        """
        The toString method returns a string of the name and
        description of the class.
        """
        return (self.Name + ": " + self.Description)
        




