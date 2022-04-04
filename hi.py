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
lobby = Room("Here is the brightly lit welcoming lobby, an exit outside is available north, there is also a receptionist. Type 'staff' to interact")
street = Room("A run down street, Theres an dimmly lit alley.")
alley = Room("An alleyway littered with a sleeping hobo, to get past you must have vodka. Type 'hobo' to interact")
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
#alley.west = hideout - will add later because hobo blocks the exit
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
@when("inv")
def player_inventory():
	print("You are carrying")
	for item in player_inv:
		print(item)


@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
@when("grab ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		player_inv.add(t)
		print(f"You pick up the {item}")
		print(t.description)
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
	if item in player_inv and item == "key" and current_room == kitchen:
		print("You used the key and unlock your front door")
		print("The door is open to the north")
		used_key = True 
		kitchen.north = hallway
	else:
		print("You cant use that here")


@when("look at ITEM")
def look_at(item):
	if item in player_inv:
		t = player_inv.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying a {item}")

@when("hobo")
def hobo():
	if "vodka" in player_inv and current_room == alley:
		print("You disrupt the hobo from his slumber, he demands vodka for you to pass. Luckily you grabbed that vodka from your kitchen. He takes it and now you are free to pass")
		alley.west = hideout
	elif current_room == alley:
		print("You wake the hobo but he seems angry, you have no vodka for him. Go back to your apartment and grab the vodka from the kitchen.")
	else:
		print("There is no hobo in this room.")

@when("staff")
def staff():
	if current_room == lobby:
		print("Hello there Alekseyevich, I must warn you before you leave, you must be careful out there. The Orekhovskaya gang are ruthless recently. As your receptionist 'Alexander Solonik' i must warn you of these things.")
		print("'Thank you' you reply")

	else:
		print("There is no staff in this room")


#####################
#MAIN FUNCTION
#####################

def main():
	print(current_room)
	start()
	
main()