# Tic Tac Toe game with AI (Greedy method)

import random

def draw_board(board):
	print('   |   |  ')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |  ')
	print('------------')
	print('   |   |  ')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |  ')
	print('------------')
	print('   |   |  ')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |  ')

# returns [player, computer]
def input_letters():
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print("Choose X or O: ")
		letter = input().upper()
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']
		
# if 0, computer goes first, else player goes first
def get_first_turn():
	if random.randint(0, 1) == 0:  
		return 'computer'
	else:
		return 'player'
		
def is_space_free(board, move):
	return board[move] == ' ' 		

def get_player_move(board):
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
		print('Next move?: ')
		move = input()
	return int(move)
	
def make_move(board, letter, move):
	board[move] = letter

#checking all diagonals, and verticle, horizontal lines
def is_winner(b, l): # b -> board, l -> letter
	return ((b[1] == l and b[2] == l and b[3] == l) or
			(b[4] == l and b[5] == l and b[6] == l) or
			(b[7] == l and b[8] == l and b[9] == l) or
			(b[1] == l and b[4] == l and b[7] == l) or
			(b[2] == l and b[5] == l and b[8] == l) or
			(b[3] == l and b[6] == l and b[9] == l) or
			(b[1] == l and b[5] == l and b[9] == l) or
			(b[3] == l and b[5] == l and b[7] == l))

def is_board_full(board):
	for i in range(1, 10):
		if is_space_free(board, i):
			return False
	return True
	
def play_again():
	print('Play Again?: (y/n): ')
	return input().lower().startswith('y')
	
	
# Functions for computer's turn

def get_copy_of_board(board):
	dup_board = []
	for i in board:
		dup_board.append(i)
	return dup_board

def choose_random_move(board, list):
	possible_moves = []
	for i in list:
		if is_space_free(board, i):
			possible_moves.append(i)
		
		if len(possible_moves) != 0:
			return random.choice(possible_moves)
		else:
			return None

def get_computer_move(board, computer_letter):
	if computer_letter == 'X':
		player_letter = 'O'
	else:
		player_letter = 'X'
	
	#Algorithm for implementing AI

	#check if computer can win the game
	for i in range(1, 10):
		copy = get_copy_of_board(board)
		if is_space_free(copy, i):
			make_move(copy, computer_letter, i)
			if is_winner(copy, computer_letter):
				return i
	
	#block player if he could win on next move
	for i in range(1, 10):
		copy = get_copy_of_board(board)
		if is_space_free(copy, i):
			make_move(copy, player_letter, i)
			if is_winner(copy, player_letter):
				return i

	#take corners if they are free
	move = choose_random_move(board, [1, 3, 7, 9])
	if move != None:
		return move

	#take center if it is free
	if is_space_free(board, 5):
		return 5
	
	#move on one of the sides
	return choose_random_move(board, [2, 4, 6, 8])

# STARTING POINT FOR EXECUTION
print('Game started!!!')

while True:
	main_board = [' '] * 10 # empty list of size 10
	player_letter, computer_letter = input_letters()
	turn = get_first_turn()
	print(turn + ' will go first..')
	is_playing = True
	
	while is_playing:
		if turn == 'player':
			draw_board(main_board)
			move = get_player_move(main_board)
			make_move(main_board, player_letter, move)
			
			if is_winner(main_board, player_letter):
				draw_board(main_board)
				print("You have won the game!")
				is_playing = False
			else:
				if is_board_full(main_board):
					draw_board(main_board)
					print('Tie!')
					break #finish game 
				else:
					turn = 'computer'
				
		else:
			move = get_computer_move(main_board, computer_letter)
			make_move(main_board, computer_letter, move)
			
			if is_winner(main_board, computer_letter):
				draw_board(main_board)
				print('Computer wins, You Lose!')
				is_playing = False
			else:
				if is_board_full(main_board):
					draw_board(main_board)
					print('Tie!')
					break # finish game
				else:
					turn = 'player'
	
	if not play_again():
		break
