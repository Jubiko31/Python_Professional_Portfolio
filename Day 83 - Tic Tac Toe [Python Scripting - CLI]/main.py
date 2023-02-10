from os import system
from gameboard import gameboard
from random import choice
from header import banner

PLAYERS = ['X', 'Y']
board = [' ' for _ in range(10)]

player_start = choice(PLAYERS)
print(f'Starts player {player_start}.')
gameboard(board)

def insert(plr, pos):
    if board[pos] == ' ':
        board[pos] = plr

def checkWinner(plr):
    # All winning conditions
    if board[1] == plr and board[2] == plr and board[3] == plr:
        return True
    if board[4] == plr and board[5] == plr and board[6] == plr:
        return True
    if board[7] == plr and board[8] == plr and board[9] == plr:
        return True
    if board[1] == plr and board[4] == plr and board[7] == plr:
        return True
    if board[2] == plr and board[5] == plr and board[8] == plr:
        return True
    if board[3] == plr and board[6] == plr and board[9] == plr:
        return True
    if board[1] == plr and board[5] == plr and board[9] == plr:
        return True
    if board[3] == plr and board[5] == plr and board[7] == plr:
        return True

def isOver(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def game():
    system("clear")
    print(banner)
    gameboard(board)

while not isOver(board):
    if checkWinner("X"):
        print("\Player X wins! 🏆")
        again = input("Play again? (Y/N): ").lower()
        if again == 'y' or again == 'yes':
            board = [' ' for _ in range(10)]
            continue
        else:
            print("GAME OVER")
            break
    if checkWinner("O"):
        print("\Player O wins! 🌿")
        again = input("Play again? (Y/N): ").lower()
        if again == 'y' or again == 'yes':
            board = [' ' for _ in range(10)]
            continue
        else:
            print("GAME OVER")
            break
        
    game()
    x_pos = int(input("\nX => Choose position: "))
    insert('X', x_pos)
    
    game()
    o_pos = int(input("\nO => Choose position: "))
    insert('O', o_pos)
    
        