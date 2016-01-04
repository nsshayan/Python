# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 08:48:57 2015

@author: snaganan
"""
import time

def initialize():
    global sudoku
    input = open('C:\Personal\Projects\Python\sudokuInput.txt','r')
    n = int(input.readline())
    
    for i in range(n):
        row,col,num = input.readline().split()
        row,col,num = int(row),int(col),int(num)
        sudoku[row-1][col-1]=num
       
    return sudoku

def displayPuzzle(sudoku):
    print "**************************************"
    for i in range(9):
        print sudoku[i]
    print "**************************************"

def solveSudoku(problem):
    if matrixFull(problem):
        displayPuzzle(problem)
        return True
    else :
        row,col = FindUnassignedLocation(problem)
        print "row = ",row," col = ",col
        displayPuzzle(problem)
        for num in range(1,10):
            if isSafe(problem,row,col,num):
                problem[row][col]=num
                if solveSudoku(problem):
                    return True
                problem[row][col]=0
    displayPuzzle(problem)
    return False
        
def matrixFull(problem):
    for i in range(9):
        for j in range(9):
            if problem[i][j]==0:
                return False
    return True 

def FindUnassignedLocation(sudoku):
    for row in range(0,9):
        for col in range(0,9):
            if sudoku[row][col]==0:
                return row,col
    return -1,-1                
    
def isSafe(sudoku,row,col,num):
     if usedInRow(sudoku,row,num):
         return False
     if usedInCol(sudoku,col,num):
         return False
     if usedInBox(sudoku,row-row%3,col-col%3,num):
         return False
     return True

#     return ((not usedInRow(sudoku,row,num)) and (not usedInRow(sudoku,col,num)) and (not usedInBox(sudoku,row-row%3,col-col%3,num)))
 

def usedInRow(sudoku,row,num):
    for col in range(0,9):
        if sudoku[row][col]==num:
            return True
    return False

def usedInCol(sudoku,col,num):
    for row in range(0,9):
        if sudoku[row][col]==num:
            return True
    return False

def usedInBox(sudoku,boxRowStart,boxColStart,num):
    for row in range(0,3):
        for col in range(0,3):
           if  sudoku[row+boxRowStart][col+boxColStart] == num:
                return True
    return False

sudoku = [[0 for x in range(9)] for x in range(9)] 

print displayPuzzle(sudoku)
initialize()
print displayPuzzle(sudoku)
start = time.time()
print "Start = ",start
bool = solveSudoku(sudoku)
end = time.time()
print "End = ",end
if bool:
    print "Solved, time =",(end - start)
else:
    print "Cannot be solved, time =",(end-start)
