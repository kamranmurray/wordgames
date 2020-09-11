
def main():
	print(score("zqx"))


def score(word):

	scrabbleValue = 0


	for element in word:
		if element in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
			scrabbleValue = scrabbleValue + 1

		elif element in ['d', 'g']:
			scrabbleValue = scrabbleValue + 2
	
		elif element in ['b', 'c', 'm', 'p']:
			scrabbleValue = scrabbleValue + 3
	
		elif element in ['f', 'h', 'v', 'w', 'y']:
			scrabbleValue = scrabbleValue + 4

		elif element in ['k']:
			scrabbleValue = scrabbleValue + 5

		elif element in ['j', 'x']:
			scrabbleValue = scrabbleValue + 8

		elif element in ['q', 'z']:
			scrabbleValue = scrabbleValue + 10

	return scrabbleValue

main()