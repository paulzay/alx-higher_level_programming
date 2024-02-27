import unittest
from models.rectangle import Rectangle

class RectangleTest(unittest.TestCase):
	def test_area(self):
		rectangle = Rectangle(8, 2)
		self.assertEqual(rectangle.area(), 16)

	# def test_width_string(self):
	# 	rectangle = Rectangle("8", 2)
	# 	self.assertNotEqual()

	# def test_height_string(self):
	# 	rectangle = Rectangle(8, "2")
	# 	self.assertEqual
	def test_str(self):
		rectangle = Rectangle(4, 6, 2, 1, 12)
		self.assertEqual(rectangle.__str__(), "[Rectangle] (12) 2/1 - 4/6")
