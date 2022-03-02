# Author: Tracy Vierra
# Date Created: 3/2/2022
# Date Modified: 3/2/2022

# Description:

# Usage:

class Computer:
	class Desktop:
		def __init__(self, cpu, ram, hdd, display):
			self.cpu = cpu
			self.ram = ram
			self.hdd = hdd
			self.display = display
		
		def getspecs(cpu, ram, hdd, display):
	            return "CPU: {}, RAM: {}, HDD: {}, DISPLAY: {}".format( cpu, ram, hdd, display )

		def displayspecs(display):
		    return "DISPLAY: {}".format(display)

		def __str__(self):
			return "CPU: {}, RAM: {}, HDD: {}".format(self.cpu, self.ram, self.hdd)

	class Laptop:
		def __init__(self, cpu, ram, hdd, display, weight):
			self.cpu = cpu
			self.ram = ram
			self.hdd = hdd
			self.display = display
			self.weight = weight

		def getspecs(cpu, ram, hdd, display, weight):
	            return "CPU: {}, RAM: {}, HDD: {}, DISPLAY: {}, WEIGHT: {}".format(cpu, ram, hdd, display, weight)

		def displayspecs(display):
	            return "DISPLAY: {}".format(display)

		def __str__(self):
		    return "CPU: {}, RAM: {}, HDD: {}, WEIGHT: {}".format(self.cpu, self.ram, self.hdd, self.weight)

	# def getspecs(self, cpu, ram, hdd, display, weight):
	#         return "CPU: {}, RAM: {}, HDD: {}, DISPLAY: {}, WEIGHT: {}".format(self.cpu, self.ram, self.hdd, self.display, self.weight)

	# def displayspecs(display):
	# 	return "DISPLAY: {}".format(display)

	def __init__(self, cpu, ram, hdd, display, weight):
		self.cpu = cpu
		self.ram = ram
		self.hdd = hdd
		self.display = display
		self.weight = weight

desktop = Computer.Desktop("i7", "16GB", "1TB", "15.6")
laptop = Computer.Laptop("i5", "8GB", "500GB", "15.6", "2.5") 

print(desktop)
print(laptop)
print(Computer.Laptop(cpu="i9", ram="32GB", hdd="2TB", display="17.6", weight="3.5"))
print(Computer.Desktop(cpu="i9", ram="48GB", hdd="4TB", display="26.6"))
print(Computer.Laptop.displayspecs(display="19.6"))
print(Computer.Desktop.displayspecs(display="35.9"))
print(Computer.Desktop.getspecs(cpu="i9", ram="64GB", hdd="3TB", display="26.6"))
print(Computer.Laptop.getspecs(cpu="i9", ram="32GB", hdd="2TB", display="17.6", weight="3"))

# Their solution: 

class Computer:
    def __init__(self, ram, memory, processor):
        self.ram = ram
        self.memory = memory
        self.processor = processor

    def getspecs(self):
        print('Please enter the details')
        self.ram = input('Enter Ram Size: ')
        self.memory = input('Memory size: ')
        self.processor = input('Enter processor: ')

    def displayspecs(self):
        print('Here are the specs of the computer')
        print(' Ram size is: ' + self.ram + ' Memory size is: ' + self.memory + ' processor is: ' + self.processor)


class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor

    def get_case_details(self):
        self.casecolor = input('Enter case color')

    def put_case_details(self):
        print('case color is: ' + self.casecolor)


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def getweight(self):
        self.weight = input('Enter weight')

    def displayweight(self):
        print('weight is: ' + self.weight)


comp = Laptop('');

comp.getspecs()

comp.getweight()

comp.displayspecs()

comp.displayweight()

