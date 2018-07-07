# Board Templates are there to help make the Board easily.
# To know the Board in detail, please check boardDetails.txt!

boardTemplate1 = [" ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
boardTemplate2 = ["_", "_", "_", "_", "|", "_", "_", "_", "_", "|", "_", "_", "_", "_"]
boardTemplate3 = [" ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
boardTemplate4 = [" ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
boardTemplate5 = ["_", "_", "_", "_", "|", "_", "_", "_", "_", "|", "_", "_", "_", "_"]
boardTemplate6 = [" ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
boardTemplate7 = [" ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]

# Board list will hold the values necessary to form up the Board!

Board = [boardTemplate1, boardTemplate2, boardTemplate3, boardTemplate4, boardTemplate5, boardTemplate6, boardTemplate7]
OldBoard = Board

# Resets the board to it's orignal state

def resetBoard():
    Board = OldBoard

# MoveColumnOrder and MoveRowOrder make us access 9 specific areas of
# Our 14x7 TicTacToe Board.

MoveColumnOrder = [0, 3, 6]
MoveRowOrder = [2, 6, 11]

# Prints The Board.

def printBoard():
	for _ in Board:
		print("\t\t", end="")
		for _indice in _:
			print(_indice, end="")
		print()
	print()

#Brings up the game introduction.

def introduction():
	tempIntroText = """
			TIC-TAC-TOE
	__________________________________________
	|   Welcome to the game of tic-tac-toe!  |
	|   Rules are pretty Simple. Just press  |
	|   The number coresponding to the cell  |   
	|   you want to place your token on.     |
	|   The Board is arranged as follow ->   |
	|________________________________________|
	"""
	tempBoardStr = """
			  1 | 2  | 3   
			____|____|____
			    |    |    
			  4 | 5  | 6    
			____|____|____
			    |    |    
			  7 | 8  | 9 
	"""
	print(tempIntroText)
	print(tempBoardStr)

# Function checks if a move player wants to make has been
# already made or not. It also checks if the move number
# exceeds the board limit or not.

def isMoveAlreadyMade(move):
	if move>=1 and move<=9:
		move = move-1
		modMove = move%3
		divMove = move//3
		if Board[int(MoveColumnOrder[divMove])][int(MoveRowOrder[modMove])] == " ":
			return False
		else:
			return True
	else:
		return True

# This is a driver function which makes the move as desired
# by the player on the board. Will throw invalid move error if
# move made is out of bounds of orignal board.

def makeMove(playerInfo, playerName, move):
	if isMoveAlreadyMade(move) == False:
		tempToken = playerInfo[playerName]
		move = move-1
		modMove = move%3
		divMove = move//3
		Board[int(MoveColumnOrder[divMove])][int(MoveRowOrder[modMove])] = str(tempToken)
		return True
	else:
		print("\tInvalid move! Please try again!")
		return False

# lets a player make his/her move on the Board.
# Asks repeatedly the player to input his move until
# he/she comes up with a legal move.

def letPlayerTakeTurn(playerInfo, playerName):
	isMoveSuccess = False
	while isMoveSuccess==False:
		print("\n\t" + str(playerName) + " make a move : ", end="")
		move = int(input())
		isMoveSuccess = makeMove(playerInfo, playerName, move)
	printBoard()

# Checks if the token that user has picked is valid
# to be placed on our board or not.

def isTokenValid(token):
	if len(token) != 1:
		return False
	else:
		return True

# This function lets both the players choose their respective
# tokens turn by turn.

def chooseToken(Player1, Player2):
	tokenDictionary = {}
	playerDictionary = {}

	while True:
		print("\t" + str(Player1)+ " please input your token : ", end="")
		tokenPlayerOne = input()
		if isTokenValid(tokenPlayerOne)==True:
			break
		else:
			print("\t" + "Token must be 1 character long only")

	tokenDictionary[tokenPlayerOne] = Player1
	playerDictionary[Player1] = tokenPlayerOne

	while True:
		while True:
			print("\t" + str(Player2)+ " please input your token : ", end="")
			tokenPlayerTwo = input()
			if isTokenValid(tokenPlayerTwo)==True:
				break
			else:
				print("\t" + "Token must be 1 character long only")

		if tokenPlayerTwo in tokenDictionary:
			print("\t" + "Token already taken! Please try again!")
		else:
			tokenDictionary[tokenPlayerTwo] = Player2
			playerDictionary[Player2] = tokenPlayerTwo
			break

	print("")

	for _ in tokenDictionary:
		print("\t\t -> " + tokenDictionary[_], end=" : ")
		print(_)

	return playerDictionary

################################################################
# The following functions check for winning conditions if any
# arises during the course of game. The check is by rows,
# columns and diagonals.

# The following function checks to see if winning condition
# is achieved on any rows.

def scanRows():
	isScanSuccess = False
	scanList = [True, True, True]
	i = -1

	for _ in MoveColumnOrder:
		i = i+1
		tempToken = Board[_][MoveRowOrder[0]]
		if tempToken== " ":
			scanList[i] = False
		for _index in MoveRowOrder:
			if Board[_][_index]!=tempToken:
				scanList[i] = False
				break
	
	for k in range(3):
		isScanSuccess = scanList[k] or isScanSuccess

	return isScanSuccess

# The following function checks to see if winning condition
# is achieved on any Columns

def scanColumns():
	isScanSuccess = False
	scanList = [True, True, True]
	i = -1

	for _ in MoveRowOrder:
		i = i+1
		tempToken = Board[MoveColumnOrder[0]][_]
		if tempToken== " ":
			scanList[i] = False
		for _index in MoveColumnOrder:
			if Board[_index][_]!=tempToken:
				scanList[i] = False
				break

	for k in range(3):
		isScanSuccess = scanList[k] or isScanSuccess

	return isScanSuccess

# The following function checks to see if winning condition
# is achieved on any Diagonals

def scanDiagonals():
	isLeftDiagonalScanSuccess = True
	isRightDiagonalScanSuccess = True

	rightDiagonalToken = Board[MoveColumnOrder[0]][MoveRowOrder[0]]
	leftDiagonalToken = Board[MoveColumnOrder[0]][MoveRowOrder[2]]

	if rightDiagonalToken != " ":
		for i in range(3):
			for j in range(3):
				if i==j:
					if Board[MoveColumnOrder[i]][MoveRowOrder[j]]!=rightDiagonalToken:
						isRightDiagonalScanSuccess = False
						break
	else:
		isRightDiagonalScanSuccess = False

	if leftDiagonalToken != " ":	
		for i in range(3):
			for j in range(3):
				if i+j==2:
					if Board[MoveColumnOrder[i]][MoveRowOrder[j]]!=leftDiagonalToken:
						isLeftDiagonalScanSuccess = False
						break
	else:
		isLeftDiagonalScanSuccess = False

	return isLeftDiagonalScanSuccess==True or isRightDiagonalScanSuccess==True

# This function recieves data from all the three above functions
# and returns if any winning condition is achieved or not

def hasAnyPlayerWon():
	return scanDiagonals()==True or scanColumns()==True or scanRows()==True

################################################################

# The following function is the main function, i.e it directs
# the flow of all commands in the following game.

def _main():
	introduction()
	Player1 = input("\tPlayer1 please enter your name : ")
	Player2 = input("\tPlayer2 please enter your name : ")
	print("")
	playerInfo = chooseToken(Player1, Player2)

	playerList = [Player1, Player2]
	totalPossibleMoves = 9
	i = 0

	while totalPossibleMoves!=0:
		letPlayerTakeTurn(playerInfo, playerList[i])
		totalPossibleMoves = totalPossibleMoves -1
		if totalPossibleMoves<=4:
			if hasAnyPlayerWon()==True:
				print("\n\tCongratulations ! " + str(playerList[i] + " has won the game!"))
				break
		if totalPossibleMoves==0:
			print("\n\tDraw !!!")
		if i==0:
			i = i+1
		else:
			i = i-1

# While loop drives the main program till the time users want
# to play the game.

while True:
	resetBoard()
	_main()
	print("\n\tPress Y to play again and Q to Quit the game : ", end="")
	choice = input()
	if choice=="Q" or choice=="q":
		break