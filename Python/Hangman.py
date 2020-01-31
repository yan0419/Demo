# Hangman Game

#!/usr/bin/env python3
import random

isStart = True
life = 3
abcLetterList = "abcdefghijklmnopqrstuvwxyz"
wordList = ['cat', 'dog', 'monkey', 'bird', 'chicken', 'lion']
secertWord = ""
blankWordList = []
guessedList = []
correct = 0


def randomSecertWord():
	global secertWord
	global blankWordList

	secertWord = random.choice(wordList)
	blankWordList = ["X"] * len(secertWord)


def guessWord():
	global correct
	isInvalid = True

	tempLetter = input("Guess a Letter. ").lower()
	while isInvalid: 
		if tempLetter == "":
			tempLetter = input("Cannot be empty. Try again. ")
		elif tempLetter not in abcLetterList:
			tempLetter = input("Please input a valid letter. ")
		elif tempLetter in guessedList:
			tempLetter = input("You have already guessed this letter. Try again. ")
		else:
			isInvalid = False
			print("You entered " + str(tempLetter))
			guessedList.append(tempLetter)
			if tempLetter in secertWord:
				print("BINGO~ You got " + str(tempLetter))
				for i in range(0, len(secertWord)):
					if str(tempLetter) == secertWord[i]:
						blankWordList[i] = str(tempLetter)
						correct += 1
				print("")
				printBlankWord()
			else:
				print("Oops, you are wrong. ")
				lostLife()
	

def lostLife():
	global life
	life -= 1
	print("You lost a ♥. ")


def isFinished():
	global isStart
	if life < 1:
		isStart = False
		gameOver()
	elif correct == len(secertWord):
		isStart = False
		win()
	else:
		print("\n\n========================\n\n")


def win():
	printWinner()
	printSecertWord()
	print("You still have " + "♥" * life + " left. ")
	printGuessedList()
	print("\n\n================================================\n\n ")


def gameOver():
	printGameOver()
	printSecertWord()
	printGuessedList()
	print("\n\n================================================\n\n ")


def printNumOfLife():
	print("You have " + "♥" * life)


def printGuessedList():
	print("You have guessed: " + str(guessedList) + "\n")


def printSecertWord():
	print("The secert word is " + secertWord)


def printBlankWord():
	print(str(blankWordList) + "\n")


def printGameStart():
	print("\n\n================================================\n\n ")
	print("  _____                  _____ _           _   ")
	print(" |   __|___ _____ ___   |   __| |_ ___ ___| |_ ")
	print(" |  |  | .'|     | -_|  |__   |  _| .'|  _|  _|")
	print(" |_____|__,|_|_|_|___|  |_____|_| |__,|_| |_|  ")
	print("                                               ")
	print("\n\n================================================\n\n ")


def printGameOver():
	print("\n\n================================================\n\n ")
	print(" _____                   _____                ")
	print("|   __| ___  _____  ___ |     | _ _  ___  ___ ")
	print("|  |  || .'||     || -_||  |  || | || -_||  _|")
	print("|_____||__,||_|_|_||___||_____| \_/ |___||_|  ")
	print("                                              ")
	print("\n\n------------------------------------------------\n\n ")


def printWinner():
	print("\n\n================================================\n\n ")
	print(" _ _ _ _ _____ _____ _____ _____              ")
	print("| | | |_|   | |   | |   __| __  |             ")
	print("| | | | | | | | | | |   __|    -|             ")
	print("|_____|_|_|___|_|___|_____|__|__|             ")
	print("                                              ")
	print("\n\n------------------------------------------------\n\n ")


if __name__ == "__main__":
	printGameStart()
	randomSecertWord()

	while isStart:
		printBlankWord()
		printNumOfLife()
		printGuessedList()

		guessWord()
		
		isFinished()