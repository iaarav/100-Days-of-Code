import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

print(data)

newDict = {code.letter: code.code for (letter, code) in data.iterrows()}

word = input("Enter a word: ").upper()


finalDict = [newDict[n] for n in word ]

print(finalDict)
