class myBike:

	def __init__(self, stock):
		
		self.stock = stock
	def displayBike(self):
		print("Total Bikes",self.stock)
	def rentForBike(self,q):

		if q<=0:
			print("please enter positive value or greater than zero")
		if q>self.stock:
			print("sorry , your vlue is out of stock ,please check availability")
		else:
			print("Total price",q*100)
			print("Total Bike",self.stock-q)

while  True:
	obj=myBike(100)
	uc=int(input('''
1 Display Stocks
2 Rent a Bike
3 Exit	
				'''))
	if uc==1:
		obj.displayBike()
	elif uc==2:
		q=int(input("enter the Qty:---"))
		obj.rentForBike(q)
	else:
		break

	
		