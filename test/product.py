# importing the modules 
from datetime import date 
from dateutil.relativedelta import relativedelta 

# base class 


class Product: 

	name = "" 

	# printing the class in the constructor 
	def __init__(self): 
		print("super class Product") 

# getExpDate() returns the expiry date of product 
# since every product has different expiry date 
# therefore this method is overridden by child classes 
	def getExpDate(): 

		# gives exp date 
		print("Expiry date") 
		pass


# derived class 1 
class Snack(Product): 

	# months 
	shelfLife = 6
	price = 0

	# constructor - initializing variables 
	def __init__(self, name, price): 
		self.name = name 
		self.price = price 

	# prints the Snack product details 
	def printDetails(self): 
		print("name : " + self.name) 
		print("price : " + str(self.price)) 
		print("shelf life : " + str(self.shelfLife) + " months") 

	# calculates the expiry date using relativedelta library and returns 
	def getExpDate(self, pkdDate): 
		expDate = pkdDate + relativedelta(months=self.shelfLife) 
		return expDate 

# derived class 2 
class Beverage(Product): 

	# 2 years 
	shelfLife = 2
	price = 0

	# constructor - initializing variables 
	def __init__(self, name, price): 
		self.name = name 
		self.price = price 

	# prints the Beverage product details 
	def printDetails(self): 
		print("name : " + self.name) 
		print("price : " + str(self.price)) 
		print("shelf life : " + str(self.shelfLife) + " years") 

	# calculates the expiry date using relativedelta 
	# library and returns 
	def getExpDate(self, pkdDate): 
		expDate = pkdDate + relativedelta(years=self.shelfLife) 
		return expDate 


# derived class 3 
class Staples(Product): 

	# 1 year 
	shelfLife = 1
	price = 0

	# constructor - initializing variables 
	def __init__(self, name, price): 
		self.name = name 
		self.price = price 

	# prints the Staples product details 
	def printDetails(self): 
		print("name : " + self.name) 
		print("price : " + str(self.price)) 
		print("shelf life : " + str(self.shelfLife) + " year") 

	# calculates the expiry date using relativedelta 
	# library and returns 
	def getExpDate(self, pkdDate): 
		expDate = pkdDate + relativedelta(years=self.shelfLife) 
		return expDate 


def main(): 
	s = Snack('cookies', 60) 
	s.printDetails() 
	print(s.name + " will expire on " +
		str(s.getExpDate(date(2019, 10, 3))) + "months") 
	# yyyy-mm-dd 

	p = Product() 

	st = Staples('rice', 300) 
	st.printDetails() 
	print(st.name + " will expire on " + str(st.getExpDate(date(2020, 1, 23)))) 

	b = Beverage('coffee', 250) 
	b.printDetails() 
	print(b.name + " will expire on " + str(b.getExpDate(date(2018, 12, 17)))) 

	print("done till here") 


if __name__ == '__main__': 
	main() 
