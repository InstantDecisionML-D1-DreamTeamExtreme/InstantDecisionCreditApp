"""
Author: Wes Johnson
Date: Feb 1st 2020
Purpose: this program file simply opens the files and makes a few plots 
How ro run: python openDataFiles.py

Verion: Python 3.7.1
"""

#imports:
import csv 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

#define variables: 
dirData='../data/'
fileData='crx.data'
#fileNames='crx.names'
#fileNames='codeBook.names'
fileNames='credit.lisp'

def printRowsCsv(pathAndFile):
  """this function simply prints each row of data in given file for early data exploration"""
  with open(pathAndFile) as f:
    reader = csv.reader(f)
    for row in reader:
      print(row)

def openCsv(pathAndFile):
  """this function opens the files given and saves it as a python list"""
  with open(pathAndFile) as f:
    dataFrame = pd.DataFrame(list(csv.reader(f)), columns=['C0','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15'])
  return(dataFrame)
  
printRowsCsv(dirData+fileData)

df=openCsv(dirData+fileData)

print(df) #print the entire data frame, notice how pretty it looks 
#print(df[15]) #print the last line of the data frame, df 

df.C7 = df.C7.astype(float)#convert the data values to float 
df.C7.plot(kind='hist',bins=50)#plot the 7th column as a histogram
plt.show()
