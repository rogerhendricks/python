class mammal(object):
	def legs(self):
		pass
	def talk(self):
		pass
	def eat(self):
		pass


class human(mammal):
	def legs(self):
		print(2)
	def talk(self):
		print("English")
	def eat(self):
		print("Hamburger's!")


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

if animalType == "human" or animalType == "Human":
	animalType = human()
	animalType.talk()
	animalType.legs()
	animalType.eat()
elif animalType == "cat" or animalType == "Cat":
	animalType = cat()
	animalType.talk()
	animalType.legs()
	animalType.eat()
	animalType.whiskers()
elif animalType == "dog" or animalType == "Dog":
	animalType = dog()
	animalType.talk()
	animalType.legs()
	animalType.eat()
else:
	print("Your not a mammal")



						
		