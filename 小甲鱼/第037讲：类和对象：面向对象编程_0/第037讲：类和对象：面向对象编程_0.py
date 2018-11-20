
class Parkrate():

	
	def __init__(self):
		self.adult = 0
		self.childen = 0
		self.ordinary_rate = 100
		self.childen_rate = 50
		self.weekend_rate1 = 120
		self.weekend_rate2 = 60
    
	def ordrate(self):
		print("请输入到公园的人数：")
		self.adult = int(input("成年人： "))
		self.childen = int(input("儿童： "))
		
		return self.adult * self.ordinary_rate + self.childen * self.childen_rate
	
	def weekrate(self):
		print("请输入到公园的人数：")
		self.adult = int(input("成年人： "))
		self.childen = int(input("儿童： "))
		
		return self.adult * self.weekend_rate1 + self.childen * self.weekend_rate2
