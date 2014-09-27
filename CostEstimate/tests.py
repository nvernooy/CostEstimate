"""
File tests.py contains a collection of classes that perfrom unit tests on the
Cost Estimate objects - BudgetItem, BudgetGroup, and Project.
The tests are broken into separate classes, with each class covering an object.
Generally there are tests testing for string output correctness, correct cost
calculation, and if the object is hashable.
For the upper level in the hierarchy, separate tests are done for empty sets,
sets with one object, and sets with multiple objects.
"""

import unittest
import collections
from models import Project, BudgetGroup, BudgetItem

class BudgetItem_Object_Tests(unittest.TestCase):
    """
    The BudgetItem_Object_Tests class covers tests for the BudgetItem object.
    """

    def construct_BudgetItem(self):
        """The method returns a BudgetITem object with some values."""
        return BudgetItem("BITestName", "BITestDescription", 2, 5)

    def test_Negative_BudgetItem(self):
        """
        This method tests using negative numbers in the constructor.
        Numbers are by defeault set to zero, therefore total will be zero
        """
        item = BudgetItem("Negative", "Negative Description", -1, 5)
        self.assertEqual(0, item.total() )
        
    def test_budgetitem_string(self):
        """The method tests whether the object prints out correctly."""
        budgetitem = self.construct_BudgetItem()
        self.assertEqual(str(budgetitem), "BITestName: BITestDescription")

    def test_budgetitem_subtotal(self):
        """The method tests whether the subtotal is calculated correctly."""
        budgetitem = self.construct_BudgetItem()
        self.assertEqual(budgetitem.subtotal(), 10)

    def test_budgetitem_VAT(self):
        """The method tests if the VAT value is calculated correctly."""
        budgetitem = self.construct_BudgetItem()
        self.assertAlmostEqual(budgetitem.vat(), 1.4)

    def test_Budgetitem_Total(self):
        """The method tests if the VAT value is calculated correctly."""
        budgetitem = self.construct_BudgetItem()
        self.assertEqual(budgetitem.total(), 11.4)

    def test_Budgetitem_Is_Hashable(self):
        """
        The method tests whether the object is part of the hashable collection.
        Therefore it can be used in sets.
        """
        budgetitem = self.construct_BudgetItem()
        self.assertIsInstance(budgetitem, collections.Hashable)

class BudgetGroup_Object_Tests(unittest.TestCase):
    """
    The class contains methods testing the functionality of the
    BudgetGroup object.
    """

    def construct_Empty_BudgetGroup(self):
        """
        The method constructs a BudgetGroup object containing no BudgetItems.
        """
        return BudgetGroup("BGTestName", "BGTestDescription")

    def construct_Single_Item_BudgetGroup(self):
        """
        The method constructs a BudgetGroup object containing one BudgetItem.
        """
        group = BudgetGroup("BGTestName", "BGTestDescription")
        group.add (BudgetItem("ItemName", "ItemDescription", 5, 2))
        return group

    def test_BudgetGroup_Single_String(self):
        """The method tests if BudgetGroup prints out correctly."""
        budgetgroup = self.construct_Empty_BudgetGroup()
        self.assertEqual(str(budgetgroup), "BGTestName: BGTestDescription")

    def test_BudgetGroup_Empty_Cost(self):
        """
        The method tests if BudgetGroup calculates the cost correctly
        if it contains no BudgetItems.
        """
        budgetgroup = self.construct_Empty_BudgetGroup()
        self.assertEqual(0, budgetgroup.subtotal())

    def test_BudgetGroup_Empty_Adding(self):
        """
        The method tests if a BudgetItem can be added correctly if the
        BudgetGroup was initially empty.
        """
        budgetgroup = self.construct_Empty_BudgetGroup()
        self.assertIsNone(budgetgroup.add(BudgetItem()))

    def test_BudgetGroup_Empty_Deleting(self):
        """
        The method tests if BudgetGroup returns the correct output if an object
        that doesnt exist in the set is attempted to be removed from it.
        """
        budgetgroup = self.construct_Empty_BudgetGroup()
        self.assertEqual("Not in set.", budgetgroup.delete(BudgetItem()))

    def test_BudgetGroup_Single_Cost(self):
        """
        The method tests if the cost is calculated correctly with only
        a single BudgetItem in it.
        Note: since the other cost functions use only use the subtotal method,
        only it will be tested.
        """
        budgetgroup = self.construct_Single_Item_BudgetGroup()
        self.assertEqual(10, budgetgroup.subtotal())

    def test_BudgetGroup_Single_Deleting(self):
        """The method tests deleting an object from the set."""
        budgetgroup = self.construct_Single_Item_BudgetGroup()
        self.assertEqual("Confirmed.", budgetgroup.delete
                         (BudgetItem("ItemName", "ItemDescription", 5, 2)))

    def test_BudgetGroup_Multiple_Cost(self):
        """
        The method tests if the costs are calculated correctly with more
        than one BudgetItem in it.
        """
        budgetgroup = self.construct_Single_Item_BudgetGroup()
        budgetgroup.add(BudgetItem("SecondName", "SecondDescription", 10, 3))
        self.assertEqual(40, budgetgroup.subtotal())

    def test_BudgetGroup_Multiple_Strings(self):
        """
        The method checks the object prints out correctly
        with BudgetItems in it.
        """
        budgetgroup = self.construct_Single_Item_BudgetGroup()
        budgetgroup.add(BudgetItem("SecondName", "SecondDescription", 10, 3))
        self.assertEqual("BGTestName: BGTestDescription\n\t\t"+
                         "ItemName: ItemDescription\n\t\t"+
                         "SecondName: SecondDescription", str(budgetgroup))


    def test_BudgetGroup_Is_Hashable(self):
        """
        The method tests if this object is hashable, since it needs to
        be to be used in a set.
        """
        budgetgroup = self.construct_Single_Item_BudgetGroup()
        self.assertIsInstance(budgetgroup, collections.Hashable)


     
class Project_Object_Tests(unittest.TestCase):
    """
    The class contains methods testing the functionality of the
    Project object.
    """
    
    def construct_Empty_Project(self):
        """This method contructs an empty Project object and returns it."""
        return Project("PojectTestName", "ProjectTestDescription")

    def construct_Single_Project(self):
        """
        This method constucts a Project with one of each
        of the objects from the hierarchy and returns it.
        """ 
        project = Project("PojectTestName", "ProjectTestDescription")
        groupone = BudgetGroup("BGTestName", "BGTestDescription")
        itemone = BudgetItem("BITestName", "BITestDescription", 2, 5)

        groupone.add(itemone)              
        project.add(groupone)

        return project

    def construct_Multiple_Project(self):
        """
        This method constucts a Project with two of each
        of the objects from the hierarchy and returns it.
        """ 
        project = Project("PojectTestName", "ProjectTestDescription")
        groupone = BudgetGroup("BGTestName", "BGTestDescription")
        grouptwo = BudgetGroup("BGTestNameTwo", "BG Test Description Two")
        itemone = BudgetItem("BITestName", "BITestDescription", 2, 5)
        itemtwo = BudgetItem("BITestNameTwo", "BI Test Description Two", 10, 3)
        itemthree = BudgetItem("BITestNameThree", "BI Test Description Three", 5, 4)
        itemfour = BudgetItem("BITestNameFour", "BI Test Description Four", 2, 5)
                        
        groupone.add(itemone)
        groupone.add(itemtwo)
        grouptwo.add(itemthree)
        grouptwo.add(itemfour)
                        
        project.add(groupone)
        project.add(grouptwo)

        return project

    
    def test_Empty_Project_String(self):
        """This method test the Project prints out correctly."""
        project = self.construct_Empty_Project()
        self.assertEqual(str(project), "PojectTestName: ProjectTestDescription")
                        
    def test_Empty_Project_Cost(self):
        """
        This method tests if the costs are calculated
        correctly in an empty Project.
        """
        project = self.construct_Empty_Project()
        self.assertEqual(project.subtotal(), 0)

    def test_BudgetGroup_Empty_Deleting(self):
        """
        This project tests deleting on an empty Project.
        """
        project = self.construct_Empty_Project()
        self.assertEqual("Not in set.", project.delete(BudgetGroup()))

    def test_Single_Project_Cost(self):
        """This method tests if calculating cost with a single Item is correct."""
        project = self.construct_Single_Project()
        self.assertEqual(project.subtotal(), 10)

    def test_Single_Project_Deleting(self):
        """This method tests deleting one BudgetGroup from the Projet."""
        project = self.construct_Single_Project()
        self.assertEqual("Confirmed.", project.delete(BudgetGroup("BGTestName", "BGTestDescription")))


    def test_Multiple_Project_Subtotal(self):
        """
        This method tests if calculating the total cost of the
        Project is done correctly with multiple objects in the hierarchy."""
        project = self.construct_Multiple_Project()
        self.assertEqual(70, project.subtotal())

    
    def test_Multiple_Project_VAT(self):
        """This method tests if VAT is calculated correcly for the Project."""
        project = self.construct_Multiple_Project()
        self.assertEqual(9.8, project.vat())

    def test_Multiple_Project_String(self):
        """This method tests if the string output is correct."""
        project = self.construct_Multiple_Project()
        self.assertEqual("PojectTestName: ProjectTestDescription\n\t"+
                         "BGTestName: BGTestDescription\n\t\t"+
                         "BITestName: BITestDescription\n\t\t"+
                         "BITestNameTwo: BI Test Description Two\n\t"+
                         "BGTestNameTwo: BG Test Description Two\n\t\t"+
                         "BITestNameFour: BI Test Description Four\n\t\t"+
                         "BITestNameThree: BI Test Description Three",
                         str(project))
                                       
                        
    def test_Project_Is_Hashable(self):
        """This method tests if the object is hashable."""
        project = self.construct_Single_Project()
        self.assertIsInstance(project, collections.Hashable)


if __name__ == '__main__':
    unittest.main()

