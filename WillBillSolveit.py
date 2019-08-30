# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:21:54 2016

@author: snaganan
"""

import csv

file = open('C:\Personal\Projects\Python\will_bill_solve_it\\train\submissions.csv','r')
trainSubmissions = list(csv.reader(file))
file = open('C:\Personal\Projects\Python\will_bill_solve_it\\train\problems.csv','r')
trainProblems = list(csv.reader(file))
file = open('C:\Personal\Projects\Python\will_bill_solve_it\\train\users.csv','r')
trainUsers = list(csv.reader(file))
file = open('C:\Personal\Projects\Python\will_bill_solve_it\\test\\test.csv','r')
testData = list(csv.reader(file))
file = open('C:\Personal\Projects\Python\will_bill_solve_it\\test\\problems.csv','r')
testProblem = list(csv.reader(file))
file = open('C:\Personal\Projects\Python\will_bill_solve_it\\test\\users.csv','r')
testProblem = list(csv.reader(file))


X =[]
Y = []
usersDict = {}
#convert trainUsers in dictionary of users
for i in range(1,len(trainUsers)):
    usersDict[trainUsers[i][0]] = list(trainUsers[i][1:])

problemsDict = {}

for i in range(1,len(trainProblems)):
    problemsDict[trainProblems[i][0]] = list(trainProblems[i][2:])
    
#Reduce the number of rows in submissions csv 
submissionsDict = {}
for i in range(1,len(trainSubmissions)):
    subId = (trainSubmissions[i][0],trainSubmissions[i][1])
    if subId not in submissionsDict:
        submissionsDict[subId] = list(trainSubmissions[i][2:])
        
    if subId in submissionsDict:
        if submissionsDict[subId][0]== trainSubmissions[i][2] and submissionsDict[subId][1]==trainSubmissions[i][2]:
            continue
        if trainSubmissions[i][2] == 'SO':
            submissionsDict[subId] = list(trainSubmissions[i][2:])
        if trainSubmissions[i][2] == 'SO' and trainSubmissions[i][3] == 'AC':
            submissionsDict[subId] = list(trainSubmissions[i][2:])
    
#creating a matrix X
print "creating X"
L = len(submissionsDict)
for i in range(0,100000):
    x = []
    #if submissionsDict.keys()[i][0] in usersDict:
    x.extend(usersDict[submissionsDict.keys()[i][0]])
        
    #if submissionsDict.keys()[i][1] in problemsDict:
    x.extend(problemsDict[submissionsDict.keys()[i][1]])
    
    X.append(x)    
            


#for i in range(0,len(submissionsDict)):
#     x=[]
#     for j in range(1,len(trainUsers)):
#         if submissionsDict.keys()[i][0] in trainUsers[j]:
#             x.extend(trainUsers[j][1:])
#             break
#         
#     for k in range(1,len(trainProblems)):
#         if  submissionsDict.keys()[i][1] in trainProblems[k]:
#             x.extend(trainProblems[k][1:])
#             break
#        
#    
#     X.append(x)
print "Creating Y "
for i in range(0,100000):
    if submissionsDict[submissionsDict.keys()[i]][0]=='SO':
        Y.append(1)
    else:
        Y.append(0)
#create the Y vector
#
#for subId in submissionsDict:
#    if submissionsDict[subId][0] == 'SO':
#        Y.append(1)
#    else:
#        Y.append(0)
#

    
