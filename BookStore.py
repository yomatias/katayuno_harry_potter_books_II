def getTotalPriceForBooks(bookGroups):
	totalPrice = 0

	for bookGroup in bookGroups:
		totalPrice = totalPrice + bookGroup.quantity * 8

	discount = getDiscount(bookGroups)

	return totalPrice - totalPrice * discount

def getDiscount(bookGroups):
	availableDiscounts = {1: 0, 2: 0.05, 3: 0.1}

	return availableDiscounts[len(bookGroups)]
