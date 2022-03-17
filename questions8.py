"""
print("Hi, welcome to Ice Cream Maker")
order_complete = False
topping_count = 0
toppings_list = []
topping_available = ["vanilla", "strawberry", "chocolate", "sprinkles", "nuts", "raisins", "chocolate sauce", "flake", "m&ms",]
print(topping_available) 
print("These are the available toppings")



while order_complete == False:
topping = input("What topping? - push enter to finish")
	if topping == "": 
	print("Order Done")
	order_complete = True
elif topping in toppings_list: 
	print("You already have that topping")
else: 
	print("Great, adding it to the list")
	topping_count + 1
	toppings_list.append(topping)

if topping_count >= 6
	order_complete = True 
else
	order_complete = False 

print("Here are your toppings")

print(toppings_list.join(","))
"""

while True:
	print()
















