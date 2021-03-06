"""
The models.py file contains the objects used in the Cost Estimate database.
The objects are derived from the Persistant class in order to be used with ZODB.
The objects form a hierachy with Project() at the top, which contains
BudgetGroup(), which contains BudgetItem().
"""
#global VAT = 0.14
from persistent import Persistent
from BTrees.OOBTree import OOSet

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

    def __init__(self, name = '', desc = ''):
        """
        The Project constructor takes a string name and desc as the Name of
        the project, and it's Description.
        The default values of Name and Description would be ''.
        It initialises with an empty set.
        """
        
        self.Name = name
        self.Description = desc
        self.GroupSet = OOSet()

    def add(self, group):
        """The add method adds a BudgetGroup object to the set."""
        self.GroupSet.add(group)

    def delete(self, group):
        """The delete method removes a BudgetGroup object from the set.
        Before removing an object it makes sure it is in the set.
        """
        if (group in self.GroupSet):
            self.GroupSet.remove(group)
            return "Confirmed."
        else:
            return "Not in set."
 
    def subtotal(self):
        """
        The subtotal function returns the total of the subtotal of all
        the BudgetGroup objects.
        """
        stotal = 0
        for group in self.GroupSet:
            stotal+=group.subtotal()

        return stotal
    

    def vat(self):
        """
        The vat function calculates the VAT percentage on the subtotal.
        Computing the percentage on the subtotal is more efficient than
        computing the percentage of each group and adding it.
        """
        #return (self.subtotal()*VAT)
        return (self.subtotal()*0.14)

   
    def total (self):
        """
        The total function computes the cost of the project plus VAT.
        Computing the subtotal increasing it with the VAT percentage is
        more efficient than computing the subtotal and VAT separately.
        """
        #return (self.subtotal()*(1+VAT))
        return (self.subtotal()*(1+0.14))
                

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
        If the set is not empty thereafter it prints
        all the BudgetGroups in the set.
        """

        output = self.Name + ": " + self.Description
        if self.GroupSet is not None:
            for group in self.GroupSet:
                output+=("\n\t"+str(group))
            
        return output

 
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

    def __init__(self, name = '', desc = ''):
        """
        The BudgetGroup constructor takes a string name and desc as the Name of
        the project, and it's Description.
        It initialises with an empty set.
        """
        self.Name = name
        self.Description = desc
        self.ItemSet = OOSet()

    def add(self, item):
        """The add method adds a BudgetItem object to the set."""
        self.ItemSet.add(item)

    def delete(self, item):
        """
        The delete method removes a BudgetGroup object from the set.
        Before removing an object it makes sure it is in the set.
        """
        if (item in self.ItemSet):
            self.ItemSet.remove(item)
            return "Confirmed."
        else:
            return "Not in set."

    def subtotal(self):
        """
        The subtotal function returns the total of the subtotal of all
        the BudgetItem objects.
        """
        stotal = 0
        for group in self.ItemSet:
            stotal+=group.subtotal()

        return stotal


    def vat(self):
        """
        The vat function calculates the VAT percentage on the subtotal.
        Computing the percentage on the subtotal is more efficient than
        computing the percentage of each item and adding it.
        """
        #return (self.subtotal()*VAT)
        return (self.subtotal()*0.14)

 
    def total (self):
        """
        The total function computes the cost of the BudgetGroup plus VAT.
        Computing the subtotal increasing it with the VAT percentage is
        more efficient than computing the subtotal and VAT separately.
        """
        #return (self.subtotal()*(1+VAT))
        return (self.subtotal()*(1+0.14))


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
        If the set is not empty thereafter it prints all
        the BudgetItems in the set.
        """
        output = self.Name + ": " + self.Description
        if self.ItemSet is not None:
            for item in self.ItemSet:
                output+=("\n\t\t"+str(item))
            
        return output


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

    def __init__(self, name = '', desc = '', quan = 0, rate = 0):
        """
        The BudgetItem constructor takes a string name and desc as the Name of
        the project, and it's Description.
        It takes quan and rate as numbers for Quantity and Rate.
        If Quantity or Rate is less than zero, print a message
        and set them to zero.
        """
        self.Name = name
        self.Description = desc
        self.Quantity = quan
        self.Rate = rate
        if ((self.Quantity < 0) or (self.Rate < 0)):
            self.Quantity = 0
            self.Rate = 0
                     
        
    def subtotal(self):
        """
        The subtotal function returns the product of the Quantity and Rate
        attributes as the cost of the items in this object.
        Covert the return type to int.
        """
        return (self.Quantity*self.Rate)*1.0


    def vat(self):
        """
        The vat function calculates the VAT percentage on the subtotal.
        It represents the VAT added to this item.
        """
        #return (self.subtotal()*VAT
        return (self.subtotal()*0.14)


 
    def total (self):
        """
        The total function adds the subtotal and VAT of this item.
        It represents the total cost of this item.
        """
        return (self.subtotal() + self.vat())


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
        




