#####################
#IMPORTS
#####################
from adventurelib import *

Room.items = Bag()
#####################
#DEFINE ROOMS
#####################
bedroom = Room("This is your groggy bedroom, the walls are lined with grease. To your east there is a kitchen. There is a computer to your right.")
kitchen = Room("This is your kitchen... if you can call it that. There is a exit to leave the apartment but you have to use a key...")
hallway = Room("This is the hallway of the apartment complex. Theres an elevator to the lobby east")
lobby = Room("Here is the brightly lit welcoming lobby. A comfortable couch sits in the corner of the room, and a exit outside is available north. There is also a receptionist. Type 'talk to staff' to interact")
street = Room("A run down street, There is a broken down car on the side of the road. Theres an dimmly lit alley. Type 'search car' to interact")
alley = Room("An alleyway littered with a sleeping hobo. Type 'talk to hobo' to interact")
hideout = Room("A huge alpha male stands at the door to the Orekhovskaya gang underground mansion. You must tell him a password to enter. Type 'talk to alpha' to interact")
mansion_lobby = Room("WOAH, the Orekhovskaya gang underground mansion, its huge. As you swing open the front doors you realize a group of armed men in black suits have been waiting for you.")

#####################
#DEFINE CONNECTIONS
#####################
bedroom.east = kitchen
#kitchen.north = hallway - will add later because it starts locked
hallway.east = lobby
lobby.north = street
street.north = alley
#alley.west = hideout - will add later because hobo blocks the exit
hideout.north = mansion_lobby

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

maobar = Item("mao bar", "bar", "maobar")
maobar.description = "A mao bar, in the ingredients list there are countless amounts of illcit substances. Could be deadly"

bedroom.items.add(M82A3) 
bedroom.items.add(key)
hallway.items.add(Baseball_bat)
#street.items.add(mao_bar) - Will add later when car bind is used
#####################
#DEFINE BAGS
#####################
player_inv = Bag()

#####################
#ADD ITEMS TO BAGS
#####################
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

#####################
#DEFINE ANY VARIABLES
#####################
current_room = bedroom
used_key = False 
used_vodka = False


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

@when("connor rules")
def connor_rules():
	print("Connor Casey NOT KNIGHTS is the coolest person ever tbh")


@when("inventory")
@when("show inventory")
@when("inv")
def player_inventory():
	print("You are carrying")
	for item in player_inv:
		print(item)




@when("go DIRECTION")
@when("travel DIRECTION")
@when("n", direction="north")
@when("s", direction="south")
@when("e", direction="east")
@when("w", direction="west")
def travel(direction):
	global current_room
	room = current_room.exit(direction)
	if room:
		if room == mansion_lobby:
			print(room)
			print("The armed men gun you down until there is nothing left of you ")
			print("You DIE")
			quit()
		else:
			current_room=room
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
		player_inv.take("key")
	elif item in player_inv and item == "maobar" or item == "mao bar" or item == "bar":
		print("You eat the mao bar and see the copious amounts of lean and other substances in it. You slowly start to feel your insides burning.")
		print("You DIE")
		quit()
	elif item == "vodka":
		option = input("Are you sure you want to drink the vodka? It could come in handy later...")
		if option == 'yes':
			print("You drink the vodka, as you are skulling the bottle, visions of badland chugs come into your and you feel happiness, you forget to breath and drown in vodka.. could be worse.")
			print("You DIE")
			quit()
		else:
			print("You do not drink the vodka")

	elif item == 'computer':
		print("You boot up the old computer")
		option = input("What do you want to do? You can: browse the internet, play games\n")
		if option == 'browse the internet':
			print("You wait 20 seconds for internet explorer to open.")
			option = input("what do you want to search? You can: buy vodka, browse weddit\n")
			if option == "buy vodka":
				print("You open 'cheapvodka4u' and buy some vodka, it will be delivered outside your apartment door.")
				hallway.items.add(Bottle_of_vodka)
			elif option == 'browse weddit':
				print("You open up weddit and see a new post from user 'Lags_was_taken' on r/slipknot, he says slipknot copys MGK.")
				print("You reply with many hate comments and dm him multiple death threats.")
			else:
				print("that is not a valid search")
		elif option == 'play games':
			print("You play some tribes ascend")






		else:
			print("That is not a valid search")		




	else:
		print("You cant use that here or you do not have the item")


@when("look at ITEM")
def look_at(item):
	if item in player_inv:
		t = player_inv.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying a {item}")

@when("talk to alpha")
@when("alpha")
def alpha():
	option = input("The alpha stands at the door towering over you, he demands a password to pass.\n")
	if option == 'shipin is best':
		print("he responds 'Correct, you are free to pass' while giving an uncertain look.")
	else:
		print("He responds 'wrong' and stomps on you")
		print("You DIE")
		quit()


@when("search couch")
@when("couch")
def couch():
	print("You search the couch and find a thin stripe of paper that says 'Pass: shipin is best'.")

@when("talk to hobo")
@when("hobo")
def hobo():
	if "vodka" in player_inv and current_room == alley:
		print("You disrupt the hobo from his slumber, he demands vodka for you to pass. Luckily you grabbed that vodka from your kitchen. He takes it and now you are free to pass")
		alley.west = hideout
		used_vodka = True
		player_inv.take("vodka")
	elif current_room == alley:
		print("You wake the hobo but he seems angry, you have no vodka for him. Go back to your apartment and grab some vodka from the kitchen.")
	else:
		print("There is no hobo in this room.")

@when("talk to staff")
@when("staff")
def staff():
	if current_room == lobby:
		print("Hello there Alekseyevich, I must warn you before you leave, you must be careful out there. The Orekhovskaya gang are ruthless recently. As your receptionist 'Alexander Solonik' I must warn you of these things.")
		print("'Thank you' you reply")

	else:
		print("There is no staff in this room")

@when("search car")
@when("car")
def car():
	if current_room == street:
		if "bat" in player_inv and current_room == street:
			print("You use your bat to smash the car window open and see a food item. It says 'maobar'")
			street.items.add(maobar)
		elif current_room == street:
			print("You look into the car and see a food bar of some sort, you need a bat to smash open the window.")
		else:
			print("There is no car here")
	else:
		print("There is no car here.")


#####################
#MAIN FUNCTION
#####################

def main():
	print(current_room)
	start()
	
main()