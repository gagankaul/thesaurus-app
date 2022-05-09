#A Thesaurus application framework using dictionaries

import random

print("Welcome to the Thesaurus App")

thesaurus = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

print("\nChoose a word from the thesaurus and I will give you a synonym.")

print("\nHere are the words in the thesaurus:")
for key in thesaurus.keys():
    print("\t-" + key)

word_pick = input("\nWhat word would you like a synonym for: ").lower().strip()
random_index = random.randint(0,4)
print("A synonym for " + word_pick + " is " + thesaurus[word_pick][random_index] + ".")

choice = input("\nWould you like to see the whole thesaurus (y/n): ").lower().strip()

if choice.startswith("y"):
    for key,value in thesaurus.items():
        print("\n" + key.title() + " synonyms are:")
        for each in value:
            print("\t- " + each)
else:
    print("I hope you enjoyed the program. Thank you!")






