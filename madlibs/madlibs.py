#string concatenation

#I want to create a string that says "____, continue practicing python everyday!"
#variable
# name = "Raquel Michelon"

#a few ways to do the concatenation:
# print(name + ", continue practicing python everyday!")
# print("{}, continue practicing python everyday!".format(name))
# print(f"{name}, continue practicing python everyday!")

# Now the project itself

adjective = input("Give an adjective: ")
verb1 = input("Now a Verb: ")
verb2 = input("Another Verb: ")
famous_name = input("Famous person that you like: ")

madlib = f"Computer programming is so {adjective}! It is amazing because \ I really enjoy to {verb1}. Stay focoused and {verb2} like you are {famous_name}!"

print(madlib)