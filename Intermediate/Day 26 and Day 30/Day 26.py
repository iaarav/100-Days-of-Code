import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

newDict = {code.letter: code.code for (letter, code) in data.iterrows()}
alphabets = [letter for letter in data.iterrows()]


def natoMaker():
    word = input("Enter a word: ").upper()

    try:
        finalDict = [newDict[n] for n in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        natoMaker()
    else:
        print(finalDict)


natoMaker()
