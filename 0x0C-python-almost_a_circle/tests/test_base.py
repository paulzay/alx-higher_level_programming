import unittest
from models.base import Base

class BaseTest(unittest.TestCase):
    # def setUp(self):
    #     base = Base()

    def test_id_is_none(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

if __name__ == '__main__':
    unittest.main()
