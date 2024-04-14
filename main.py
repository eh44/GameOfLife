
import time
import random


class Life:
    def __init__(self, size):
        self.__size = size
        self.__generation = []
        self.__genNum = 1
        for i in range(0, self.__size):
            self.__generation.append([])
        # Makes the first Generation
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if random.randint(1, 3) == 1:
                    self.__generation[i].append("X")
                else:
                    self.__generation[i].append(" ")

    # Prints the current Generation, with the generation number displayed below
    def printCurrentGen(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print(self.__generation[i][j], end= " ")
            print()
        print("\t\t\t\tGeneration " + str(self.__genNum) + "\n")

    # Returns the amount of alive neighbors for a specified index
    def amountOfNeighbors(self, currentGen, index1,index2):
            amountOfNeighbors = 0
            if currentGen[index1][index2] == "X":
                amountOfNeighbors -= 1
            for i in range(index1-1,index1+2):
                for j in range(index2-1,index2+2):
                    if (i < 0 or i >= len(currentGen)) or (j < 0 or j >= len(currentGen[i])):
                        continue
                    elif currentGen[i][j] == "X":
                        amountOfNeighbors += 1
            return amountOfNeighbors

    # Makes the next generation by determining which ones are dead or alive by a set of rules
    def makeNextGen(self):
        tempGen = []
        for i in range(0,len(self.__generation)):
            tempGen.append([])
            for j in range(0,len(self.__generation)):
                tempGen[i].append(self.__generation[i][j])
        for i in range(0, len(self.__generation)):
            for j in range(0, len(self.__generation)):
                if self.amountOfNeighbors(self.__generation, i,j) < 2 or \
                        self.amountOfNeighbors(self.__generation, i,j) > 3:
                    tempGen[i][j] = " "
                elif self.amountOfNeighbors(self.__generation,i,j) == 3 or \
                    (self.amountOfNeighbors(self.__generation,i,j) == 2 and self.__generation[i][j] == "X"):
                   tempGen[i][j] = "X"
        for i in range(0,len(self.__generation)):
            for j in range(0, len(self.__generation[i])):
                self.__generation[i][j] = tempGen[i][j]
        self.__genNum += 1

def main():
    conwayLife = Life(22)
    # Runs the program for 50 generations
    for i in range(0,50):
        conwayLife.printCurrentGen()
        conwayLife.makeNextGen()
        time.sleep(.3)
main()


