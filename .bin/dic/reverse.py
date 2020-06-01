
wordsFile = open ("words.txt")

wordsList = wordsFile.readlines()

wordsList.reverse()

for i in wordsList:
		print i.strip()
