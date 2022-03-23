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
lobby = Room("Here is the brightly lit welcoming lobby, an exit to outside is available.")
street = Room("A run down street, Theres an dimmly lit alley.")
alley = Room("An alleyway, you can see something at the end of it")
hideout = Room("Finally the Orekhovskaya gang hideout, it appears to be larger than it initally seemed")
mansion = Room("WOAH, the Orekhovskaya gang underground mansion, its huge")

#####################
#DEFINE CONNECTIONS
#####################
bedroom.east = kitchen
kitchen.north = hallway
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
def check_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)


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

#####################
#MAIN FUNCTION
#####################
def main():
	start()

if __name__ == '__main__':
	main()