import unittest

from models import Project, BudgetGroup, BudgetItem

class BudgetItem_Object_Tests(unittest.TestCase):

    def construct_BudgetItem(self):
        return BudgetItem("BITestName", "BITestDescription", 2, 5) 

    def test_budgetitem_string(self):
        budgetitem = self.construct_BudgetItem()
        self.assertEqual(str(budgetitem), "BITestName: BITestDescription")

    def test_budgetitem_subtotal(self):
        budgetitem = self.construct_BudgetItem()
        self.assertEqual(budgetitem.subtotal(), 10)

    def test_budgetitem_VAT(self):
        budgetitem = self.construct_BudgetItem()
        self.assertEqual(budgetitem.vat(), 1.4)

    def test_budgetitem_total(self):
        budgetitem = self.construct_BudgetItem()
        self.assertEqual(budgetitem.total(), 11.4)

    def test_budgetitem_is_hashable(self):
        budgetitem = self.construct_BudgetItem()
        self.assertEqual(budgetitem, collections.Hashable)

class BudgetGroup_Object_Tests(unittest.TestCase):

    def construct_Empty_BudgetGroup(self):
        return BudgetGroup("BGTestName", "BGTestDescription")

    def construct_Single_Item_BudgetGroup(self):
        group = BudgetGroup("BGTestName", "BGTestDescription")
        group.add (BudgetItem("ItemName", "ItemDescription", 5, 2))

    def test_BudgetGroup_Single_String(self):
        budgetgroup = self.construct_Empty_BudgetGroup()
        self.assertEqual(str(budgetgroup), "BGTestName: BGTestDescription")

    def test_BudgetGroup_Empty_Cost(self):
        budgetgroup = self.construct_Empty_BudgetGroup()
        self.assertEqual(0, budgetgroup.subtotal())

    def test_BudgetGroup_Empty_Adding(self):
        budgetgroup = self.construct_Empty_BudgetGroup()
        self.assertIsNone(budgetgroup.add(BudgetItem()))

    def test_BudgetGroup_Empty_Deleting(self):
        budgetgroup = self.construct_Empty_BudgetGroup()
        self.assertEqual("Not in set.", budgetgroup.delete(BudgetItem()))

    def test_BudgetGroup_Single_Cost(self):
        budgetgroup = self.construct_Single_Item_BudgetGroup()
        self.assertEqual(10, budgetgroup.subtotal)

    def test_BudgetGroup_Single_Deleting(self):
        budgetgroup = self.construct_Single_Item_BudgetGroup()
        self.assertEqual("Confirmed", budgetgroup.delete
                         (BudgetItem("ItemName", "ItemDescription", 5, 2)))

    def test_BudgetGroup_Multiple_Cost(self):
        budgetgroup = self.construct_Single_Item_BudgetGroup()
        budgetGroup.add(BudgetItem("SecondName", "SecondDescription", 10, 3))
        self.assertEqual(40, budgetgroup.subtotal)

    def test_BudgetGroup_Multiple_Strings(self):
        budgetgroup = self.construct_Single_Item_BudgetGroup()
        budgetGroup.add(BudgetItem("SecondName", "SecondDescription", 10, 3))
        self.assertEqual("BGTestName: BGTestDescription\n\t\t"+
                         "ItemName: ItemDescription\n\t\t"+
                         "SecondName: SecondDescription", str(budgetgroup))


    def test_BudgetGroup_Is_Hashable(self):
        budgetgroup = self.construct_Single_Item_BudgetGroup()
        self.assertEqual(budgetgroup, collections.Hashable)


     
class Project_Object_Tests(unittest.TestCase):

    def construct_Empty_Project(self):
        return Project("PojectTestName", "ProjectTestDescription")

    def construct_Single_Project(self):
        project = Project("PojectTestName", "ProjectTestDescription")
        groupone = BudgetGroup("BGTestName", "BGTestDescription")
        itemone = BudgetItem("BITestName", "BITestDescription", 2, 5)
        group.add(itemone)              
        project.add(groupone)

        return project

    def construct_Muliple_Project(self):
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
        project = self.construct_Empty_Project()
        self.assertEqual(str(projet), "PojectTestName: ProjectTestDescription")
                        
    def test_Empty_Project_Cost(self):
        project = self.construct_Empty_Project()
        self.assertEqual(projet.subtotal, 0)

    def test_BudgetGroup_Empty_Deleting(self):
        project = self.construct_Empty_Project()
        self.assertEqual("Not in set.", project.delete(BudgetGroup()))

    def test_Single_Project_Cost(self):
        project = self.construct_Empty_Project()
        self.assertEqual(projet.subtotal, 10)

    def test_Single_Project_Deleting(self):
        project = self.construct_Single_Project()
        self.assertEqual("Confirmed.", project.delete(BudgetGroup("BGTestName", "BGTestDescription")))


    def test_Multiple_Project_Subtotal(self):
        project = self.construct_Muliple_Project()
        self.assertEqual(70, project.subtotal())

    
    def test_Multiple_Project_VAT(self):
        project = self.construct_Muliple_Project()
        self.assertEqual(9.8, project.VAT())

    def test_Multiple_Project_String(self):
        project = self.construct_Multiple_Project()
        self.assertEqual("PojectTestName: ProjectTestDescription\n\t" +
                         "BGTestName: BGTestDescription\n\t\t"+
                         "BITestName: BITestDescription\n\t\t"+
                         "BITestNameTwo: BI Test Description Two\n\t"+
                         "BGTestNameTwo: BG Test Description Two\n\t\t"+
                         "BITestNameThree: BI Test Description Three\n\t\t"+
                         "BITestNameFour: BI Test Description Four", str(project))
                                       
                        
    def test_Project_Is_Hashable(self):
        project = self.construct_Single__Project()
        self.assertEqual(project, collections.Hashable)


if __name__ == '__main__':
    unittest.main()

