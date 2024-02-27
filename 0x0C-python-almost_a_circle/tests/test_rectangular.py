import unittest
from models.rectangle import Rectangle

class RectangleTest(unittest.TestCase):
	def test_area(self):
		rectangle = Rectangle(8, 2)
		self.assertEqual(rectangle.area(), 16)
