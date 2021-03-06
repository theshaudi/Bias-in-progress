

Flipping for ML Models: Initial case for Logistic Regression


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

alpha, pi = 6, 10 
s = np.random.normal( alpha, pi, 3000 )
s = 5 * ( s + abs(min(s)) ) / ( max(s) - min(s) )
s = s.round(0)
s = np.where(s == max(s), min(s), s) 
s = np.where(s == max(s), min(s), s)
print(s)
print(stats.mode(s))
print(max(s))
print(min(s))
ModeResult(mode=array([2.]), count=array([1225]))

count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
linewidth = 2, color='r')
plt.show()


round(np.random.uniform(0,1),0)


#Test: What output generates this input? do a sanity check

def eval_line(x, f, r):
  
    m,b = f
    return m*x + b + np.random.uniform(-r,r)

eval_line(5,(1,0),0.1)


def eval_parable(x, f, r):
  
    Function to generate an imperfect parable
    x: The point of evaluation
    f: The function defined like a tuple (m1, m2, b) of m1*x**2 + m2*x + b
    r: The grade of the imperfection [-r,r]
    returns m1*x**2 + m2*x + b +- r
  
    m1, m2, b = f
    return m1*x**2 + m2*x + b + np.random.uniform(-r,r)

eval_parable(3,(1,1,0),0.1)


  
    m1, m2, b = f
    return m1/(1 + np.exp(-m2*x) )+ b + np.random.uniform(-r,r)

def eval_sin(x, f, r):
   
    m1, m2, b = f
    return m1*np.sin(m2*x) + b + np.random.uniform(-r,r)
