# defining a function by naming it hello then giving it a parameter called name with a defualt value of Person

def hello(name="Person"):
    print("hello", name)

hello("roger")
hello()

# creating a function that has a parameter called function then pring out "doubling parameter" then
# multiplies the parameter. the putting that function in a variable, then printing the result

def doubling(num):
    print("doubling", num)
    return num * num

n = doubling(5)
print(n)
