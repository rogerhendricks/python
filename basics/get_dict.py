# The get() method on dicts
# and its "default" argument
# created a dictionary with {} brackets, inside is key:"value",

name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

print(greeting(382))
# print the keys / get the keys with variable.keys
print(list(name_for_userid.keys()))
# print the itms / get the keys with variable.items
print(list(name_for_userid.items()))
# print the values / get the keys with variable.values
print(list(name_for_userid.values()))

# to add a key and value to dictionary
name_for_userid[999] = "Fred"
# to show the added key:value pair
# print(name_for_userid)

# to remove a key use the pop 
# name_for_userid.pop('999')
# to show the new dictionary
# print(name_for_userid)

for user in name_for_userid:
    print(user, name_for_userid[user])

