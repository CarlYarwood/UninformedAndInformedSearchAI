from informedSearch import *

#Project 1
#Carl Yarwood
#last modified 2/17

#this class takes the eight puzzle problem and states it in a way
#such that it can be interpreted by a computer and solved with a search
#algorithm
class eightPuzzle(InformedProblemState):
    #initializes the eight puzzle object, taking a list as a parameter
    #note the puzzle is entered as a list of 9 elements, the first three of
    #which correspond to the top 3 elements of an eight puzzle
    #the next three correspond to the middle three elements
    #and the last three corresponding to the bottom elements, with the 0
    #representing the empty space
    def __init__(self, currentPuzzle):
        self.currentPuzzle = currentPuzzle


    #returns a string representation of your puzzle
    def __str__(self):
        if len(self.currentPuzzle) != 9:
            return str(-1)
        else:
            string = ''
            for i in range(3):
                for c in range(3):
                    if self.currentPuzzle[(i*3) + c] == 0:
                        string += ' '
                    else:
                        string += str(self.currentPuzzle[(i*3) + c])
                string += '\n'
            return string[:-1]

    
    #tests to see if the satate is illegal
    def illegal(self):
        if self.currentPuzzle == -1: return 1
        return 0

    
    #returns weather a state is equal to this puzzle
    def equals(self, state):
        for i in range(9):
            if self.currentPuzzle[i] != state.currentPuzzle[i]:
                return 0
        return 1

    
    #defines the transformation on the puzzle for moving the blank space
    #up
    def moveUp(self):
        #finds position of the blank space
        pos = self.currentPuzzle.index(0)
        #makes sure the blank space is not in the top row
        if int(pos/3) > 0:
            #copies the current puzzle into a new puzzle
            newPuzzle = self.currentPuzzle[:]
            #makes the necessary swap and returns a new puzzle
            newPuzzle[pos] = newPuzzle[pos - 3]
            newPuzzle[pos-3] = 0
            return eightPuzzle(newPuzzle)
        #returns that an illegal puzzle
        else: return eightPuzzle(-1)
    #defines the transformation of moving down
    def moveDown(self):
        #gets index of blank space
        pos = self.currentPuzzle.index(0)
        #makes sure blank is not in bottom row
        if int(pos/3) < 2:
            #coppies puzzle
            newPuzzle = self.currentPuzzle[:]
            #makes necessary swap and returns new puzzle state
            newPuzzle[pos] = newPuzzle[pos + 3]
            newPuzzle[pos + 3] = 0
            return eightPuzzle(newPuzzle)
        #returns illegal puzzle
        else: return eightPuzzle(-1)

    #definse tge transformaton of moving the blank space left
    def moveLeft(self):
        #finds index of zero
        pos = self.currentPuzzle.index(0)
        #makes sure zero is not in left most collumb
        if pos%3 > 0:
            newPuzzle = self.currentPuzzle[:]
            newPuzzle[pos] = newPuzzle[pos - 1]
            newPuzzle[pos - 1] = 0
            return eightPuzzle(newPuzzle)
        else: return eightPuzzle(-1)


    #defines the transfromation of moving the blank space right
    def moveRight(self):
        #finds index of blank space
        pos = self.currentPuzzle.index(0)
        #makes sure blank space is not in right most collum
        if pos%3 < 2:
            newPuzzle = self.currentPuzzle[:]
            newPuzzle[pos] = newPuzzle[pos + 1]
            newPuzzle[pos + 1] = 0
            return eightPuzzle(newPuzzle)
        else: return eightPuzzle(-1)

    #returns all the possible changes in state
    def applyOperators(self):
        return [self.moveUp(), self.moveDown(), self.moveLeft(), self.moveRight()]

    
    #names all teh possible changes in state
    def operatorNames(self):
        return [ 'moveUp' , 'moveDown', 'moveLeft', 'moveRight']


    #breath firs search heuristic
    #def heuristic(self, goal):
    #    return 0


    #is in right spot herisitic
    #def heuristic(self, goal):
    #    num = 0
    #    for i in range(9):
    #        if self.currentPuzzle.index(i) != goal.currentPuzzle.index(i):
    #            num += 1
    #    return num


    #manhattan distance heuristic
    def heuristic(self,goal):
        num = 0
        for i in range(9):
            pos1 = self.currentPuzzle.index(i)
            pos2 = goal.currentPuzzle.index(i)
            num += abs(int(pos1 / 3) - int(pos2/3)) + abs((pos1%3) - (pos2%3))
        return num
        
        
#InformedSearch(eightPuzzle([1,3,0,8,2,4,7,6,5]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
#InformedSearch(eightPuzzle([1,3,4,8,6,2,0,7,5]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
#InformedSearch(eightPuzzle([0,1,3,4,2,5,8,7,6]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
#InformedSearch(eightPuzzle([7,1,2,8,0,3,6,5,4]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
#InformedSearch(eightPuzzle([8,1,2,7,0,4,6,5,3]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
#InformedSearch(eightPuzzle([2,6,3,4,0,5,1,8,7]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
#InformedSearch(eightPuzzle([7,3,4,6,1,5,8,0,2]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
InformedSearch(eightPuzzle([7,4,5,6,0,3,8,1,2]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
