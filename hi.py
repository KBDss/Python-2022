#####################
#IMPORTS
#####################
from adventurelib import *

Room.items = Bag()
#####################
#DEFINE ROOMS
#####################
bedroom = Room("This is your groggy bedroom, the walls are lined with grease.")
kitchen = Room("This is your kitchen... if you can call it that. There is a exit here to leave your apartment.")
hallway = Room("This is the hallway of the apartment complex. Theres an elevator to the lobby")
lobby = Room("Here is the brightly lit welcoming lobby, an exit outside is available north, there is also a receptionist to the east.")
street = Room("A run down street, Theres an dimmly lit alley.")
alley = Room("An alleyway, you can see something at the end of it")
hideout = Room("Finally the Orekhovskaya gang hideout, it appears to be larger than it initally seemed")
mansion = Room("WOAH, the Orekhovskaya gang underground mansion, its huge")

#####################
#DEFINE CONNECTIONS
#####################
bedroom.east = kitchen
#kitchen.north = hallway - will add later because it starts locked
hallway.east = lobby
lobby.north = street
street.north = alley
alley.west = hideout
hideout.north = mansion

#####################
#DEFINE ITEMS
#####################
Item.description = ""
Bottle_of_vodka = Item("vodka", "bottle of vodka")
Bottle_of_vodka.description = "Bottle of vodka, increases happiness when consumed, needed to give to the hobo in the alley"

Baseball_bat = Item("bat", "baseball bat")
Baseball_bat.description = "A baseball bat, could do some serious damage to those pesky gang members"

key = Item("key", "door key")
key.description = "A key for your apartment, will be needed to leave"

M82A3 = Item("gun", "M82A3", "sniper", "sniper rifle")
M82A3.description = "A M82A3. This thing could destory anything... especially gang members"

kitchen.items.add(Bottle_of_vodka)
bedroom.items.add(M82A3) 
bedroom.items.add(key)
hallway.items.add(Baseball_bat)
#####################
#DEFINE BAGS
#####################
player_inv = Bag()

#####################
#ADD ITEMS TO BAGS
#####################


#####################
#DEFINE ANY VARIABLES
#####################
current_room = bedroom
used_key = False 


#####################
#BINDS(eg '@when("look'))
#####################


@when("look")
def look():
	print(current_room)
	print(f"There are exits to the ",current_room.exits())
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)


@when("jump")
def jump():
	print("You jump")


@when("inventory")
@when("show inventory")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)


@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item)
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")


@when("go DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
	else:
		print("You can't go that way")


@when("use ITEM")
def use(item):
	if item == key and current_room == kitchen:
		print("You used the key and unlock your front door")
		print("The door is open to the north")
		used_key = True 
		kitchen.north=hallway
	else:
		print("You cant use that here")


@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying a {item}")


#####################
#MAIN FUNCTION
#####################

def main():
	print(current_room)
	start()
	
main()