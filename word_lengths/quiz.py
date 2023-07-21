import re
# For CLI definition of "string as input"
from sys import argv

#script, paragraph = argv

# Read the paragraph in from a file (easier than copying paragraph to the
# command line and worrying about escaping there).
with open("paragraph.txt", "r") as textFile:
	paragraph = textFile.read()

# Check loading.
#print(paragraph)

# Assume that we don't care about punctuation in terms of periods, commas,
# parentheses, etc. This has a bunch of corner cases - "don't"? - but for a
# quick sketch, picking it and going with it.
paragraphScrubbed = re.sub(r'[^a-zA-Z\s]', '', paragraph)

# Check scrubbing.
#print(paragraphScrubbed)

# No specific example, but the presence of '10 words with 1 letter' in the
# sample output strongly suggests that the count is based on overall occurrence
# and _not_ DISTINCT occurrences.

# Create list of individual words.
# (Leaving separator default to capture _any_ whitespace.)
words = paragraphScrubbed.split()

# Double-check splitting.
#print(words)

# Set up dictionary for word lengths, keep track of max word length.
wordLengths = {}
maxWordLength = 0

for word in words:
	wordLength = len(word)
	if wordLength > maxWordLength:
		maxWordLength = wordLength
	if wordLength in wordLengths:
		wordLengths[wordLength] += 1
	else:
		wordLengths[wordLength] = 1

for i in range(maxWordLength+1):
	if i in wordLengths:
		message = str(wordLengths[i]) + " word"
		# Extra logic to handle correct pluralization.
		if wordLengths[i] > 1:
			message += "s"
		message += " with " + str(i) + " letter"
		if i > 1:
			message += "s"
		message += "."
		print(message)
