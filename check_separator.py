import math

print("Welcome to the handy dandy check separator")


check_number = int(input("How many checks do you want to separate? "))
 
receipts = []
for i in range(check_number):				
	receipts.append(float(input("Total of check: ")))
 
print(receipts)	
receipts_total = sum(receipts)
receipts_total_float = float(receipts_total)
receipts_total_round = round(receipts_total_float, 2)
print("The total of all receipts is: $", receipts_total)

kendra_list = []
brett_list = []

def calculate(): 
	kendra_sum = (sum(kendra_list))
	kendra_sum_float = float(kendra_sum)
	brett_sum = sum(brett_list)
	brett_sum_float = float(brett_sum)
	brett_total = ((receipts_total_float - kendra_sum_float - brett_sum_float) / (2.00)) + (brett_sum_float)
	brett_total_round = round(brett_total, 2)
	print("Brett owes ${} of a total bill of ${}".format(brett_total_round, receipts_total_round))

def brett():
	brett_input = float(input("Brett expenditure: "))
	if brett_input == float("0"):
		calculate()
	else: 
		brett_input = float(brett_input)
		brett_list.append(brett_input)
		brett()

def kendra():
	kendra_input = float(input("Kendra expenditure: "))
	if kendra_input == float("0"):
		brett()
	else: 
		kendra_list.append(kendra_input)
		kendra()
	
kendra()