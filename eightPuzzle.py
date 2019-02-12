from informedSearch import *

class eightPuzzle(InformedProblemState):
    def __init__(self, currentPuzzle):
        self.currentPuzzle = currentPuzzle
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
    def illegal(self):
        if self.currentPuzzle == -1: return 1
        return 0
    def equals(self, state):
        for i in range(9):
            if self.currentPuzzle[i] != state.currentPuzzle[i]:
                return 0
        return 1
    def moveUp(self):
        pos = self.currentPuzzle.index(0)
        if int(pos/3) > 0:
            newPuzzle = self.currentPuzzle[:]
            newPuzzle[pos] = newPuzzle[pos - 3]
            newPuzzle[pos-3] = 0
            return eightPuzzle(newPuzzle)
        else: return eightPuzzle(-1)
    def moveDown(self):
        pos = self.currentPuzzle.index(0)
        if int(pos/3) < 2:
            newPuzzle = self.currentPuzzle[:]
            newPuzzle[pos] = newPuzzle[pos + 3]
            newPuzzle[pos + 3] = 0
            return eightPuzzle(newPuzzle)
        else: return eightPuzzle(-1)
    def moveLeft(self):
        pos = self.currentPuzzle.index(0)
        if pos%3 > 0:
            newPuzzle = self.currentPuzzle[:]
            newPuzzle[pos] = newPuzzle[pos - 1]
            newPuzzle[pos - 1] = 0
            return eightPuzzle(newPuzzle)
        else: return eightPuzzle(-1)
    def moveRight(self):
        pos = self.currentPuzzle.index(0)
        if pos%3 < 2:
            newPuzzle = self.currentPuzzle[:]
            newPuzzle[pos] = newPuzzle[pos + 1]
            newPuzzle[pos + 1] = 0
            return eightPuzzle(newPuzzle)
        else: return eightPuzzle(-1)
    def applyOperators(self):
        return [self.moveUp(), self.moveDown(), self.moveLeft(), self.moveRight()]
    def operatorNames(self):
        return [ 'moveUp' , 'moveDown', 'moveLeft', 'moveRight']
    def heuristic1(self, goal):
        return 0
    def heuristic2(self, goal):
        num = 0
        for i in range(9):
            if self.currentPuzzle.index(i) != goal.currentPuzzle.index(i):
                num += 1
        return num
    def heuristic3(self,goal):
        num = 0
        for i in range(9):
            pos1 = self.currentPuzzle.index(i)
            pos2 = self.currentPuzzle.index(i)
            num += abs(int(pos1 / 3) + int(pos2/3)) + abs((pos1%3) + (pos2%3))
        return num
    def heuristic(self,goal):
        num = 0
        for i in range(9):
            pos1 = self.currentPuzzle.index(i)
            pos2 = self.currentPuzzle.index(i)
            num += abs(int(pos1 / 3) + int(pos2/3)) + abs((pos1%3) + (pos2%3))
        return num
        
InformedSearch(eightPuzzle([1,3,0,8,2,4,7,6,5]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
InformedSearch(eightPuzzle([1,3,4,8,6,2,0,7,5]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
InformedSearch(eightPuzzle([0,1,3,4,2,5,8,7,6]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
InformedSearch(eightPuzzle([7,1,2,8,0,3,6,5,4]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
InformedSearch(eightPuzzle([8,1,2,7,0,4,6,5,3]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
InformedSearch(eightPuzzle([2,6,3,4,0,5,1,8,7]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
InformedSearch(eightPuzzle([7,3,4,6,1,5,8,0,2]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
InformedSearch(eightPuzzle([7,4,5,6,0,3,8,1,2]),eightPuzzle([1,2,3,8,0,4,7,6,5]))
