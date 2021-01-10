import copy

board = [[0 for i in range(3)] for i in range(3)]
gameOver = False
max = 0
turn = True

class Player():
    def __init__(self, name):
        self.name = name
    def move(self):
        pos = input("What movement would you like to do?")
        if board[int(pos[0])][int(pos[2])] == 0:
            board[int(pos[0])][int(pos[2])] = int(self.name)
        else:
            print("that position is already taken")
            self.move()
        winner(board)
class Machine(Player):
    pass
    def move(self):
        a = self.choose()
        b = int(a[0])
        c = int(a[1])
        board[b][c] = 2
    def choose(self):
            freeP = findFreePosits(board)
            for i in freeP:
                a = int(i[0])
                b = int(i[1])
                tboard = copy.deepcopy(board)
                tboard[a][b] = 2
                if winner(tboard) == 2:
                    print("hey")
                    return i
                freeP2 = findFreePosits(tboard)
                for j in freeP2:
                    c = int(j[0])
                    d = int(j[1])
                    tboard2 = copy.deepcopy(tboard)
                    tboard2[c][d] = 1
                    if winner(tboard2) == 1:
                        return j
                        
            print("hi")
            return freeP[0]


def findFreePosits(board):
            freePos = []
            for i in range(3):
                    for j in range(3):
                            if board[i][j] == 0:
                                    freePos.append(str(i) + str(j))
            return freePos
    

def winner(board):
    winnerx = 0
    for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != 0:
                winnerx = board[i][0]
    
            if board[0][i] == board[1][i] == board[2][i] != 0:
                winnerx = board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != 0:
            winnerx = board[0][0]
    if board[2][0] == board[1][1] == board[0][2] != 0:
            winnerx = board[2][0] 
    return winnerx

def end():
    if winner(board) != 0:
        return True
    elif len(findFreePosits(board)) == 0:
        return True
    else:
        return False
def paintBoard():
    print("\n\n-----  -----  -----\n" + "  " + str(board[0][0]) + "      " + str(board[0][1]) + "      " + str(board[0][2]) + " \n-----  -----  -----\n" + "  " + str(board[1][0]) + "      " + str(board[1][1]) + "      " + str(board[1][2]) + "\n-----  -----  -----\n" + "  " + str(board[2][0]) + "      " + str(board[2][1]) + "      " + str(board[2][2]))

player1 = Player(1)
player2 = Machine(2)
while end() == False:
    if turn == 1:
        player1.move()
        turn = 2
    elif turn == 2:
        player2.move()
        turn = 1

    paintBoard()
if end() == True:
    if winner(board) != 0:
        print("Player " + str(winner(board)) + " won")
    elif winner(board) == 0:
        print("It was a draw")


