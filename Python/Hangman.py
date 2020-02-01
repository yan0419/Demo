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
	blankWordList = ["-"] * len(secertWord)


def gameStart():
	printWelcome()
	userName = input("May I have your name please? ")

	while True:
		if not userName or userName[0].isalpha() == False:
			userName = input("It is empty. Enter your name again. ")
		else:
			print("\n\n   Hello, " + userName + "\n")
			print("   Thanks for playing my Hangman Game, ")
			print("   At the beginning, You will have 3 ♥ and I ")
			print("   will random a secert word for you and you ")
			print("   have to make a guess for the letters. ")
			print("   If the letter you guessed is not contain ")
			print("   in the secert word, you will lost a ♥, ")
			print("   that means GAMEOVER if you make 3 mistakes. \n\n")
			break

	wannaStart = input("Are you ready~~~~?").upper()
	while True:
		if wannaStart == "YES" or wannaStart == "Y":
			print("OKAY~~ So good luck. " + userName + "\n")
			printGameStart()
			break
		elif wannaStart == "NO" or wannaStart == "N":
			sys.exit("Never mind. Then see you later. Bye")
		else:
			wannaStart = input("Sorry Yes or No only. ").upper()
			

def guessWord():
	global correct

	tempLetter = input("Guess a Letter. ").lower()
	while True: 
		if tempLetter == "":
			tempLetter = input("It cannot be empty so try again. ")
		elif tempLetter not in abcLetterList:
			tempLetter = input("Please input a valid letter. ")
		elif tempLetter in guessedList:
			tempLetter = input("You have already guessed this letter so try again. ")
		else:
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
			break
	

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


def printAccuracy():
	print("You accuracy is " + str(correct / len(guessedList) * 100.0) + "%. \n")


def win():
	printWinner()
	print("The secert word is " + secertWord.upper() + ". \n")
	print("You still have " + "♥" * life + " left. ")
	print("You have guessed: " + str(guessedList) + "\n")
	printAccuracy()
	print("\n\n================================================\n\n ")


def gameOver():
	printGameOver()
	print("The secert word is " + secertWord.upper() + ". \n")
	print("You have guessed: " + str(guessedList) + "\n")
	print("\n\n================================================\n\n ")


def printInfo(): 
	print(*blankWordList, sep = ' ')
	print("There are " + str(len(blankWordList)) + " of letters left. ")
	print("\nYou have " + "♥" * life)
	print("You have guessed: " + str(guessedList) + "\n")


def printBlankWord():
	print("There are " + str(len(blankWordList)) + " of letters left. ")
	print(*blankWordList, sep = ' ')
	print("")

def printWelcome():
	print("\n\n================================================\n\n ")
	print("        _ _ _     _                          ")
	print("       | | | |___| |___ ___ _____ ___        ")
	print("       | | | | -_| |  _| . |     | -_|       ")
	print("       |_____|___|_|___|___|_|_|_|___|       ")
	print("                                             ")
	print("                  _____                      ")
	print("                 |_   _|___                  ")
	print("                   | | | . |                 ")
	print("                   |_| |___|                 ")
	print("                                             ")
	print("   _____ _____ _____ _____ _____ _____ _____ ")
	print("  |  |  |  _  |   | |   __|     |  _  |   | |")
	print("  |     |     | | | |  |  | | | |     | | | |")
	print("  |__|__|__|__|_|___|_____|_|_|_|__|__|_|___|")
	print("                                             ")
	print("\n\n================================================\n\n ")


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
	print("  _____                   _____                ")
	print(" |   __| ___  _____  ___ |     | _ _  ___  ___ ")
	print(" |  |  || .'||     || -_||  |  || | || -_||  _|")
	print(" |_____||__,||_|_|_||___||_____| \_/ |___||_|  ")
	print("                                               ")
	print("\n\n------------------------------------------------\n\n ")


def printWinner():
	print("\n\n================================================\n\n ")
	print("        _ _ _ _ _____ _____ _____ _____         ")
	print("       | | | |_|   | |   | |   __| __  |        ")
	print("       | | | | | | | | | | |   __|    -|        ")
	print("       |_____|_|_|___|_|___|_____|__|__|        ")
	print("                                                ")
	print("\n\n------------------------------------------------\n\n ")


if __name__ == "__main__":
	gameStart()
	randomSecertWord()

	while isStart:

		printInfo()

		guessWord()
		# print("Test")
		# printInfo()
		# print("Test")
		isFinished()
		