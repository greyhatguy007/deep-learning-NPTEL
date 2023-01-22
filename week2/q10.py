# import necessary packages
import numpy as np

# function to calculate sigmoid
def f(w,b,x):
    return 1.0/(1.0-np.exp(w*x+b)) 

# function to calculate loss 
def loss(x,y):
    loss=0
    for x,y in zip(x,y):
        f_x = f(w,b,x)
        loss += 0.5 * (y-f_x)**2
    return loss

# assigning values for x,y,w,b
X = [0.4,0.3]
Y = [1.8,0.6]
w = 1.2
b = -1.4

# Calculating loss of the given values
print(loss(X,Y))

# Output : 0.4575478579920831
