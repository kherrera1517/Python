# Connect 4 Game Board

class Board:

    def __init__( self, width=7, height=6 ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        self.data = [[' ']*width for r in range(height)]

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def __repr__(self):
        """ this method returns a string representation
            for an object of type Board
        """
        s = ''   # the string to return
        for row in range( self.height ):
            s += '|'   # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--'*self.width    # add the bottom of the board
        s += '-\n'
        for col in range( self.width ):
            s += ' ' + str(col%10)
        s += '\n'
        return s       # the board is complete, return it

    def addMove(self, col, ox):
        """ Add the game piece ox (either 'X' or 'O') to column col. """
        i = self.height - 1
        while i >= 0:
            if self.data[i][col] == ' ':
                self.data[i][col] = ox
                break
            i -= 1
        

    def clear(self):
        """ Clear the game board of all game pieces. """
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = ' '

    def setBoard(self, moves):
        """ Set the board using an input string representation. """
        for i in range(len(moves)):
            i = int(i)
            if i%2 == 1:
                self.addMove(int(moves[i]), 'O')
            else:
                self.addMove(int(moves[i]), 'X')


    def allowsMove(self, col):
        """ Return True if adding a game piece in the given column is 
            permitted and return False otherwise. """
        return self.data[0][col] == ' '

    def isFull(self):
        """ Return True if the game board is full and False otherwise. """
        for element in self.data[0]:
            if element == ' ':
                return False
        return True

    def delMove(self, col):
        """ Delete the topmost game piece from the given column. """
        for row in range(self.height):
            if self.data[row][col] != ' ':
                self.data[row][col] = ' '
                break

    def winsFor(self, ox):
        """ Return True if the game has been won by player ox where ox
            is either 'X' or 'O'. """
        #Starting from top left corner, checks horizontal
        for row in range(self.height):
            for col in range(self.width-3):
                if self.data[row][col] == ox and self.data[row][col+1] == ox and self.data[row][col+2] == ox and self.data[row][col+3] == ox:
                    return True

        #Starting from top left corner, checks vertical
        for row in range(self.height-3):
            for col in range(self.width):
                if self.data[row][col] == ox and self.data[row+1][col] == ox and self.data[row+2][col] == ox and self.data[row+3][col] == ox:
                    return True
                #Checking down-right diagonal
                if col < self.width-3:
                    if self.data[row][col] == ox and self.data[row+1][col+1] == ox and self.data[row+2][col+2] == ox and self.data[row+3][col+3] == ox:
                        return True
                #Checking down-left diagonal
                if col > 2:
                    if self.data[row][col] == ox and self.data[row+1][col-1] == ox and self.data[row+2][col-2] == ox and self.data[row+3][col-3] == ox:
                        return True

        return False

        # #Starting from top left corner, checks down-right diagonal
        # for row in range(self.height-3):
        #     for col in range(self.width-3):
        #         if self.data[row][col] == ox and self.data[row+1][col+1] == ox and self.data[row+2][col+2] == ox and self.data[row+3][col+3] == ox:
        #             return True

        # #Starting from top left corner, checks down-left diagonal
        # for row in range(self.height-3):
        #     for col in range(3, self.width):
        #         if self.data[row][col] == ox and self.data[row+1][col-1] == ox and self.data[row+2][col-2] == ox and self.data[row+3][col-3] == ox:
        #             return True
        
        # return False