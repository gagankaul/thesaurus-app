#A Thesaurus application framework using dictionaries

print("Welcome to the Thesaurus App")

thesaurus = {
    "hot":[],
    "cold": [],
    "happy": [],
    "sad": [],
}

print("\nChoose a word from the thesaurus and I will give you a synonym.")

print("\nHere are the words in the thesaurus:")
for key in thesaurus.keys():
    print("\t-" + key)

word_pick = input("\nWhat word would you like a synonym for: ")

