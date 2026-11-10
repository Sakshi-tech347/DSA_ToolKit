import sys
from pathlib import Path
import unittest

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[2] / "src")
)

from pydsa.linked_lists.SinglyLL import SinglyLL

class TestSinglyLL(unittest.TestCase):
    def setUp(self):
        self.obj = SinglyLL()

    def get_values(self):
        values =[]
        temp = self.obj._first

        while temp is not None:
            values.append(temp.data)
            temp = temp.next

        return values

    def test_insert_first(self ):
        self.obj.InsertFirst(10)
        self.obj.InsertFirst(20)

        self.assertEqual(self.get_values(),[20,10])
        self.assertEqual(self.obj.Count(),2)

    def test_insert_last(self):
        self.obj.InsertLast(10)
        self.obj.InsertLast(20)

        self.assertEqual(self.get_values(),[10,20])
        self.assertEqual(self.obj.Count(),2)

    def test_delete_first(self):
    	self.obj.InsertLast(10)
    	self.obj.InsertLast(20)

    	self.obj.DeleteFirst()

    	self.assertEqual(self.get_values(), [20])
    	self.assertEqual(self.obj.Count(), 1)

    

    def test_delete_last(self):
        self.obj.InsertLast(10)
        self.obj.InsertLast(20)

        self.obj.DeleteLast()

        self.assertEqual(self.get_values(), [10])
        self.assertEqual(self.obj.Count(), 1)


if __name__ == "__main__":
    unittest.main()