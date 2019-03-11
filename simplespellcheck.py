# a Simple Spell Checker
# the app Take a text file and spell check it
# note: install pyspellchecker Library Standard for dictionary

import spellchecker
import re


spell = spellchecker.SpellChecker()
try: filename =raw_input("Enter the file name with extension:")
except NameError: pass
filename=input("Enter the file name with extension:")
f=open(filename,"r")
a=f.read()
s=re.findall('[a-zA-Z]+', a)
misspelled = spell.unknown(s)


# show suggestions based on dictionary
# includes the use of Levenshtein's Edit distance.
# For longer words the distance has to be 1 otherwise the distance will be 2

for word in misspelled:
	print("Mispelled: ", word)
	if(len(word)>8):
		spell.distance=1
		print( "may be:", spell.candidates(word))
		spell.distance=2
	else:
		print( "may be:", spell.candidates(word))
