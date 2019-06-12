import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def getDefinition(w):
	# Convert word to lowercase so that users can write word in upper or lowercase
	w = w.lower()

	if w in data:
		return data[w]

	elif w.title() in data:
		return data[w.title()]

	elif w.upper() in data:
		return data[w.upper()] # in case user enters acronyms such as "USA"
		# If word does not exist, recommend the best match. 
	elif len(get_close_matches(w, data.keys())) > 0:
		yesNo = input("Did you mean %s instead? Enter Y if yes, or N if no. >>"  %get_close_matches(w, data.keys())[0])
		yesNo = yesNo.lower()
		if yesNo == "y":
			return data[get_close_matches(w, data.keys())[0]]
		elif yesNo == "n":
			return "The word does not exist."
		else:
			return "We did not understand your entry, please try again. >> "
	else:
		return "The word does not exist."




word = input("Enter word: ")

output = getDefinition(word)


if type(output) == list:
	for item in output:
		print(item)

else:
	print(output)

