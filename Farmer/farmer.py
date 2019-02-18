from search import *

# a translation of the farmer problem into one which can be solved with a
#a searching algorithm by a computer
class Farmer(ProblemState):
    #[farmer, wolf, goat, grain]

    #initializes with two lists farmer must always be in the 0 position, wolf
    #in 1, goat in 2, and grain in 3, with the corresponding positoin on the
    #other set containing ''
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB


    # returns a string representaiton of the current state
    def __str__(self):
        return str(self.pointA) + "," + str(self.pointB)


    #determines if the current state is illegal
    def illegal(self):
        if self.pointA == -1 or self.pointB == -1 : return 1
        if self.pointA[1] == 'wolf' and self.pointA[2] == 'goat' and self.pointA[0] != 'farmer' : return 1
        if self.pointB[1] == 'wolf' and self.pointB[2] == 'goat' and self.pointB[0] != 'farmer' : return 1
        if self.pointA[2] == 'goat' and self.pointA[3] == 'grain' and self.pointA[0] != 'farmer' : return 1
        if self.pointB[2] == 'goat' and self.pointB[3] == 'grain' and self.pointB[0] != 'farmer' : return 1
        return 0


    #returns if the states are equal
    def equals(self, state):
        return self.pointA == state.pointA and self.pointB == state.pointB

    #the action that moves the farmer from b to a without an animal
    def moveToA(self):
        if self.pointB[0] == 'farmer':
            newA = self.pointA[:]
            newB = self.pointB[:]
            newA[0] = 'farmer'
            newB[0] = ''
            return Farmer(newA,newB)
        return Farmer(-1, -1)


    #the action which moves the farmer from a to b without an action
    def moveToB(self):
        if self.pointA[0] == 'farmer':
            newA = self.pointA[:]
            newB = self.pointB[:]
            newA[0] = ''
            newB[0] = 'farmer'
            return Farmer(newA,newB)
        return Farmer(-1, -1)

    #moves wolf and farmer from a to b
    def moveWolfAtoB(self):
        if self.pointA[1] == 'wolf' and self.pointA[0] == 'farmer':
            newA = self.pointA[:]
            newB = self.pointB[:]
            newA[0] = ''
            newA[1] = ''
            newB[0] = 'farmer'
            newB[1] = 'wolf'
            return Farmer(newA, newB)
        return Farmer(-1, -1)

    #moves woalf and frarmer from b to a
    def moveWolfBtoA(self):
        if self.pointB[1] == 'wolf' and self.pointB[0] == 'farmer':
            newA = self.pointA[:]
            newB = self.pointB[:]
            newA[0] = 'farmer'
            newA[1] = 'wolf'
            newB[0] = ''
            newB[1] = ''
            return Farmer(newA, newB)
        return Farmer(-1,-1)


    #moves goat and farmer from a to b
    def moveGoatAtoB(self):
        if self.pointA[2] == 'goat' and self.pointA[0] == 'farmer':
            newA = self.pointA[:]
            newB = self.pointB[:]
            newA[0] = ''
            newA[2] = ''
            newB[0] = 'farmer'
            newB[2] = 'goat'
            return Farmer(newA, newB)
        return Farmer(-1, -1)

    #moves goat and farmer from b to a
    def moveGoatBtoA(self):
        if self.pointB[2] == 'goat' and self.pointB[0] == 'farmer':
            newA = self.pointA[:]
            newB = self.pointB[:]
            newA[0] = 'farmer'
            newA[2] = 'goat'
            newB[0] = ''
            newB[2] = ''
            return Farmer(newA, newB)
        return Farmer(-1,-1)

    #moves grain and farmer from a to b
    def moveGrainAtoB(self):
        if self.pointA[3] == 'grain' and self.pointA[0] == 'farmer':
            newA = self.pointA[:]
            newB = self.pointB[:]
            newA[0] = ''
            newA[3] = ''
            newB[0] = 'farmer'
            newB[3] = 'grain'
            return Farmer(newA, newB)
        return Farmer(-1, -1)

    #moves grain and farmer from b to a
    def moveGrainBtoA(self):
        if self.pointB[3] == 'grain' and self.pointB[0] == 'farmer':
            newA = self.pointA[:]
            newB = self.pointB[:]
            newA[0] = 'farmer'
            newA[3] = 'grain'
            newB[0] = ''
            newB[3] = ''
            return Farmer(newA, newB)
        return Farmer(-1,-1)

    #returns names of all actions
    def operatorNames(self):
        return ["moveToA", "moveToB", "moveWolfAtoB" , "moveWolfBtoA", "moveGoatAtoB", "moveGoatBtoA", "moveGrainAtoB", "moveGrainBtoA"]

    #returns the application of all acitons
    def applyOperators(self):
        return[self.moveToA(), self.moveToB(), self.moveWolfAtoB(), self.moveWolfBtoA(), self.moveGoatAtoB(), self.moveGoatBtoA(), self.moveGrainAtoB(), self.moveGrainBtoA()]


Search(Farmer(['farmer','wolf','goat','grain'],['','','','']), Farmer(['','','',''], ['farmer','wolf','goat','grain']))
