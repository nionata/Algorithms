def spaceWords(words, wordDict):
	output, n = "", len(words)

	for i in range(1, n + 1):
		potentialWord = words[0:i]
		
		if potentialWord in wordDict:
			if i == n:
				return potentialWord

			nextPotentialWord = potentialWord + " " + spaceWords(words[i:], wordDict)
			
			if output == "" or len(nextPotentialWord) < len(output):
				output = nextPotentialWord

	return output

a = "ilikefacebook"
b = ["i", "like", "face", "book", "facebook"]

print(spaceWords(a, b))
