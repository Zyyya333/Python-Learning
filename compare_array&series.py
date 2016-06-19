# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:13:47 2016

@author: Chandler
"""
from __future__ import division
import timeit
import pandas as pd
import os
import numpy as np
import matplotlib.pylab as plt

# Set working dir
os.chdir('C:\\Users\\Chandler\\Desktop\\Berkeley\\2016 Summer\\230I Fixed Income\\HW\\HW1')

df = pd.read_csv("HW1_data.csv")
p = df['Price'].values
t = df['Maturity'].values

p_s = df['Price']
t_s = df['Maturity']


# Calculate spot rate curve
df['SpotRate'] = 2*((100/p)**(1/(2*t))-1)
r = df['SpotRate'].values
plt.plot(t,r)

# Calculate forward rate curve
# df['ForwardRate'] = 2*((p[:-1]/p[1:])**(1/(2*(t[1:]-t[:-1])))-1)

def arr(p,t):
    y = 2*((p[:-1]/p[1:])**(1/(2*(t[1:]-t[:-1])))-1)
    return y
    
def ser(p_s,t_s):
    z = 2*((p_s[:-1]/p_s[1:])**(1/(2*(t_s[1:]-t_s[:-1])))-1)
    return z
    
setup = '''
import pandas as pd
df = pd.read_csv("HW1_data.csv")
p = df['Price'].values
t = df['Maturity'].values

def arr(p,t):
    y = 2*((p[:-1]/p[1:])**(1/(2*(t[1:]-t[:-1])))-1)
    return y
'''

print min(timeit.Timer('arr(p,t)',setup=setup).repeat(7,1000))



setup = '''
import pandas as pd
df = pd.read_csv("HW1_data.csv")
p_s = df['Price']
t_s = df['Maturity']
def ser(p_s,t_s):
    z = 2*((p_s[:-1]/p_s[1:])**(1/(2*(t_s[1:]-t_s[:-1])))-1)
    return z
'''

print min(timeit.Timer('ser(p_s,t_s)',setup=setup).repeat(7,1000))
