

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



expt_name = 'Census_flip_1'

rho_a = .14  
p_a = [1-rho_a, rho_a]
rho_z = .12 
p_z = [1-rho_z, rho_z]

beta = [0, .42] 
N = 600 
mu = [[1,4],[4,1]]
D = len(mu[0])
cov = [[2,0],[0,2]]

a = np.random.choice([0,1], p=p_a, size=N)
z = np.random.choice([0,1], p=p_z, size=N)
x = [np.random.multivariate_normal(mu[z_i],cov) for z_i in z]

y = [np.random.choice([zi,1-zi],p=[1-beta[ai], beta[ai]]) for ai,zi in zip(a,z)]
labels_protected = np.asarray([a,z,y]).T
x = np.asarray(x)
data = np.concatenate([labels_protected,x],axis=1)
labels =['a','z','y']
labels.extend(['x'+str(i) for i in range(D)])
df = pd.DataFrame(data=data, columns = labels)

df['x0'] = x[:,0]
df['x1'] = x[:,1]

df.head()

"""This notebook walks us through a case in which we are choosing a sample of a protected class of people from a certain demographic group, and generating insights by flipping labels of people from that sample """
