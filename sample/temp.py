import matplotlib.pyplot as plt
from ImageLibrary import * 

myFile = pickAFile()
img = open('track.png','rb')

im = plt.imread(img)

plt.show()



 
