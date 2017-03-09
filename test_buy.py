import unittest
from BookStore import getTotalPriceForBooks, getDiscount
from BookGroup import BookGroup

class Test(unittest.TestCase):
	def test_get_price_for_one_book(self):
		bookGroup = BookGroup()
		bookGroup.title = 'Harry I'
		bookGroup.quantity = 1
		bookGroups = [bookGroup]
		self.assertEqual(getTotalPriceForBooks(bookGroups), 8)

	def test_get_price_for_two_books_of_the_same_title(self):
		bookGroup = BookGroup()
		bookGroup.title = 'Harry I'
		bookGroup.quantity = 2

		bookGroups = [bookGroup]
		self.assertEqual(getTotalPriceForBooks(bookGroups), 16)

	def test_get_price_for_two_books_with_5_percent_discount(self):
		bookGroupI = BookGroup()
		bookGroupI.title = 'Harry I'
		bookGroupI.quantity = 1

		bookGroupII = BookGroup()
		bookGroupII.title = 'Harry II'
		bookGroupII.quantity = 1

		bookGroups = [bookGroupI, bookGroupII]
		self.assertEqual(getTotalPriceForBooks(bookGroups), 15.2)

	def test_get_price_for_three_books_with_10_percent_discount(self):
		bookGroupI = BookGroup()
		bookGroupI.title = 'Harry I'
		bookGroupI.quantity = 1

		bookGroupII = BookGroup()
		bookGroupII.title = 'Harry II'
		bookGroupII.quantity = 1

		bookGroupIII = BookGroup()
		bookGroupIII.title = 'Harry III'
		bookGroupIII.quantity = 1

		bookGroups = [bookGroupI, bookGroupII, bookGroupIII]
		self.assertEqual(getTotalPriceForBooks(bookGroups), 21.6)

	def test_get_discount_for_two_different_books(self):
		bookGroupI = BookGroup()
		bookGroupI.title = 'Harry I'
		bookGroupI.quantity = 1

		bookGroupII = BookGroup()
		bookGroupII.title = 'Harry II'
		bookGroupII.quantity = 1

		bookGroups = [bookGroupI, bookGroupII]
		self.assertEqual(getDiscount(bookGroups), 0.05)

	def test_get_discount_for_three_different_books(self):
		bookGroupI = BookGroup()
		bookGroupI.title = 'Harry I'
		bookGroupI.quantity = 1

		bookGroupII = BookGroup()
		bookGroupII.title = 'Harry II'
		bookGroupII.quantity = 1

		bookGroupIII = BookGroup()
		bookGroupIII.title = 'Harry III'
		bookGroupIII.quantity = 1

		bookGroups = [bookGroupI, bookGroupII, bookGroupIII]
		self.assertEqual(getDiscount(bookGroups), 0.1)

if __name__ == '__main__':
	unittest.main()
