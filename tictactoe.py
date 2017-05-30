from time import sleep
from copy import deepcopy

class TicTacToe:

    def displayBoard(self):
        for i in xrange(9):
            if i%3==0:
                print ""
            if self.board[i]=='X':
                print "X |",
            elif self.board[i]=='O':
                print "O |",
            else:
                print "  |",

        print "\n"
    
    def __init__(self,human_choice):
        self.board = [0,1,2,3,4,5,6,7,8]
        self.human = human_choice
        if (human_choice=='X'):
            self.computer = 'O'
        else:
            self.computer='X'

    def winCheck(self,board,player):
        if (
             (board[0] == player and board[1] == player and board[2] == player) or
             (board[3] == player and board[4] == player and board[5] == player) or
             (board[6] == player and board[7] == player and board[8] == player) or
             (board[0] == player and board[3] == player and board[6] == player) or
             (board[1] == player and board[4] == player and board[7] == player) or
             (board[2] == player and board[5] == player and board[8] == player) or
             (board[0] == player and board[4] == player and board[8] == player) or
             (board[2] == player and board[4] == player and board[6] == player)
             ):
            return True
        else:
            return False

    def human_turn(self):
        print "Enter the row to play (row,col) format : "
        [row,col] = map(int,raw_input().split(','))
        self.board[(row-1)*3+col-1]=self.human
        self.displayBoard()
        if self.winCheck(self.board,self.human):
            print "YOU WON !"
            return
        elif len([i for i in self.board if i!='X' and i!='O'])==0:
            print "IT'S A TIE !"
            return 
        else:
            self.computer_turn()

    def computer_turn(self):
        print "COMPUTER IS THINKING"
        sleep(0.5)
        best_answer = self.minimax_algo(self.board,self.computer,0)
        self.board[best_answer["ifPlayed"]] = self.computer
        self.displayBoard()
        if self.winCheck(self.board,self.computer):
            print "YOU LOSE !"
            return
        if len([i for i in self.board if i!='X' and i!='O'])==0:
            print "IT's A TIE !"
            return
        else:
            self.human_turn()

    def play(self):
        if (self.human=='O'):
            self.board[0]='X'
            self.displayBoard()
            self.human_turn()

        elif (self.human=='X'):
            self.displayBoard()
            self.human_turn()

    def minimax_algo(self,board,player,level):
        emptySlots = [i for i in board if i!='X' and i!='O']
        scores = []
        objs = []
        for i in range(len(emptySlots)):
            newBoard = deepcopy(board)
            obj = {}
            obj['ifPlayed'] = emptySlots[i]
            newBoard[emptySlots[i]] = player
            if (player==self.computer and  self.winCheck(newBoard,player)):
                obj['score']=+10
            elif (player==self.human and self.winCheck(newBoard,player)):
                obj['score']=-10
            elif(len([i for i in newBoard if i!='X' and i!='O'])==0):
                obj['score']=0
            else:
                if player==self.human:
                    obj['score']=self.minimax_algo(newBoard,self.computer,level+1)
                else:
                    obj['score']=self.minimax_algo(newBoard,self.human,level+1)
            objs.append(obj)
            scores.append(obj['score'])

        if (level==0):
            maxi = max(scores)
            for i in xrange(len(scores)):
                if maxi==scores[i]:
                    return objs[i]
        else:
            if player==self.computer:
                return max(scores)
            elif player==self.human:
                return min(scores)


print "TIC TAC TOE !"
sleep(1)
print "PICK A SIDE X / O"
choice = raw_input()
Game = TicTacToe(choice)
Game.play()