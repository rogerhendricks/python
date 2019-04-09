#!/usr/local/bin/python3

class mammal(object):
	def legs(self):
		pass
	def talk(self):
		pass
	def eat(self):
		pass


class human(mammal):
	def legs(self):
		legs = 2
		limbs = 2 * int(legs)
		return legs, limbs
	def talk(self):
		talk = "English"
		return talk
	def eat(self):
		eat = "Hamburgers"
		return eat


class cat(mammal):
	def legs(self):
		print(4)
	def talk(self):
		print("Meow")
	def eat(self):
		print("kibble")
	def whiskers(self):
		print("I have whiskers!")


class dog(mammal):
	def legs(self):
		print(4)
	def talk(self):
		print("woof")
	def eat(self):
		print("bones")


name = input("What is your name?")
animalType = input("what type of animal? Human? Cat or dog?")

if animalType.lower() == "human":
	animalType = human()
	talk = animalType.talk().lower()
	legs = animalType.legs()
	eat = animalType.eat()
	print(f"You have {legs[0]} legs and {legs[1]} limbs, speak {talk} and you love {eat}.")
elif animalType.lower() == "cat":
	animalType = cat()
	animalType.talk()
	animalType.legs()
	animalType.eat()
	animalType.whiskers()
elif animalType.lower() == "dog":
	animalType = dog()
	animalType.talk()
	animalType.legs()
	animalType.eat()
else:
	print("Your not a mammal")



						
		