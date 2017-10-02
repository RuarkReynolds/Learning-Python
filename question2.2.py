noun = input("Provide a noun: ")
adjective = input("Provide an adjective: ")
noun_two = input("provide another noun: ")
verb = input("Provide a verb: ")
objects = input("Provide an object: ")


print("{} ran {}, so {} {} {}.".format(noun, adjective, noun_two, verb, objects))


import random
import time

nouns = []
verbs = []
adjectives = []
directions = []
places = []

entries = 0

while entries < 4:
	noun_input = input("Provide a noun: ")
	nouns.append(noun_input)
	entries += 1

while entries < 7:
	verb_input = input("Provide a verb: ")
	verbs.append(verb_input)
	entries += 1

while entries < 10:
	adjectives_input = input("Provide an adjective: ")
	adjectives.append(adjectives_input)
	entries += 1

while entries < 14:
	directions_input = input("Provide a direction: ")
	directions.append(directions_input)
	entries += 1

while entries < 18:
	places_input = input("Provide an places: ")
	places.append(places_input)
	entries += 1

sentence_list = [nouns, verbs, adjectives, directions, places]

while entries < 24:
	choices = [random.choice(group) for group in sentence_list]  # MUST BE A LIST
	print(" ".join(choices))  # JOIN WORDS IN LIST WITH A SPACE
	time.sleep(2)
	entries += 1
