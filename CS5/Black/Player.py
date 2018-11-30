from random import *
from copy import deepcopy

class Player:

    def __init__(self, ox, tbt='RANDOM', ply=0):
        self.ox = ox
        self.tbt = tbt #either 'RANDOM', 'LEFT', or 'RIGHT'
        self.ply = ply

    def __repr__(self):
        output = ""
        output += "Player for "+self.ox+"\n"
        output += "  with tiebreak: " + self.tbt+"\n"
        output += "  and ply == " + str(self.ply)+"\n"
        return output
    
    def oppChar(self):
        """ Return the opposite game piece character. """
        if self.ox == "O": return "X"
        else: return "O"

    def scoreBoard(self, b):
        """ Return the score for the given board b."""
        if b.winsFor(self.ox):
            return 100.0
        elif b.winsFor(self.oppChar()):
            return 0.0
        else:
            return 50.0

    def tiebreakMove(self, scores):
        """ Return column number of move based on self.tbt. """
        max_score = max(scores)
        if self.tbt == 'LEFT':
            for i in range(len(scores)):
                if scores[i] == max_score:
                    return i

        elif self.tbt == 'RIGHT':
            for i in range(len(scores),0,-1):
                if scores[i-1] == max_score:
                    return i-1

        else:
            columns = [i for i in range(len(scores)) if scores[i] == max_score]
            return choice(columns)


    def scoresFor(self, b):
        """ Return a list of scores for board d, one score for each column
            of the board. """
        if b.winsFor(self.ox):
            return [100.0]*b.getWidth()
        elif b.winsFor(self.oppChar()):
            return [0.0]*b.getWidth()
        else:
            score_list = [50.0]*b.getWidth()

            for col in range(b.getWidth()):
                if self.ply != 0:
                    # b_copy = deepcopy(b)
                    b.addMove(col, self.ox)
                    print("addMove has been called", count1)
                    if b.winsFor(self.ox):
                        score_list[col] = 100.0
                    # elif b_copy.winsFor(self.oppChar()):
                    #     score_list[i] = 0.0
                    else:
                        opponent = Player(self.oppChar(), self.tbt, self.ply-1)
                        opp_scores = opponent.scoresFor(b)
                        score_list[col] = 100.0 - max(opp_scores)
                    b.delMove(col)
                    
        
            return score_list

    # def scoresFor(self, b):
    #     """ Return a list of scores for board b, one score for each column
    #         of the board. """
    #     H = b.height
    #     W = b.width
    #     D = b.data
    #     p = self.ply
    #     L = W*[50.0]
    #     for i in range(W):
    #         if not b.allowsMove(i):
    #             L[i]=-1.0
    #         elif b.winsFor(self.ox):
    #             L[i]=100.0
    #         elif b.winsFor(self.oppChar()):
    #             L[i]=0.0
    #         else:
    #             if p == 0:
    #                 L[i] = 50.0
    #             else:
    #                 b.addMove(i,self.ox)
    #                 if b.winsFor(self.ox):
    #                     L[i]=100.0
    #                 elif b.winsFor(self.oppChar()):
    #                     L[i]=0.0
    #                 else:
    #                     opponent = Player(self.oppChar(),self.tbt,self.ply-1)
    #                     oppScores = opponent.scoresFor(b)
    #                     oppMax = max(oppScores)
    #                     playerscore = 100.0 - oppMax
    #                     L[i] = playerscore
    #                 b.delMove(i)
    #     return L

    def nextMove(self, b):
        """ Takes a board as input and returns the next move for this player
            where a move is a column in which the player should place its
            game piece. """



	
