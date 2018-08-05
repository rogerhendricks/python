my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
my_foods.append('cheescake')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

favoriteFood = input("What is your favorite food?")
secondBest = "ice cream"
print("My Favorite food is %s and the next favorite food is always %s." % (favoriteFood, secondBest))
