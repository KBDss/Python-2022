"""user_ice = int(input("how many ice creams do you want?"))
if user_ice <= 20:
	print("We will have those ready in no time")   
else:
	print("There isn't enough ice cream in stock")

user_km = int(input("How many km do you intend to travel?"))
if user_km >= 200:
	print("Remember to fill the gas tank before you leave")
else:
	print("You'll have enough gas for the trip")


user_age = int(input("How old are you"))
if user_age >= 18:
	print("You are an adult") 
else:
	print("You are not a adult")


user_mov = input("What is your favourite movie").lower()
if user_mov == "bananas in pajamas" :
	print("wow that mov is my fav")
else:
	print("Bad taste") 

user_loser = input("Have you heard of the tale of Darth Plagueis the wise") 
if user_loser == "no":
	print("arth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
else:
	print("What ev's")


user_director = input("Who Directed Passion of The Christ").lower()
if user_director == "mel gibson":
	print("correct")
else:
	print("wrong")
"""

score = 0
question1 = input("What is the strongest tower in btd6\n").lower() 
if question1 == "super monkey":
	print("correct")
	score = score + 1
else:
	print("wrong")

question2 = input("Can the banana farm kill camos\n").lower()
if question2 == "no":
	print("correct") 
	score = score + 1
else:
	print("wow you fat loser how do you think that a farm can kill anything, like what are you thinking you mentally deranged maniac")

question3 = input("Who featured in all in the family by KoRn\n").lower()
if question3 == "fred durst":
	print("correct")
	score = score + 1
else:
	print("smh not a real one")

question4 = input("how many hours does Hamish have in gmod\n").lower()
if question4 == "1000":
	print("corect")
	score = score + 1
else:
	print("wong")

question5 = input("finish the line - say__\n").lower()
if question5 == "what":
	print("Actual G")
	score = score + 1
else:
	print("no")

print(f"score = {score}/5") 



