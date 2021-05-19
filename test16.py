# -*- coding: utf-8 -*-
"""
Created on Tue May 18 15:56:58 2021

@author: Gast Lokal
"""

import numpy.random as rnd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


global mean_points, std_points, mean_assists, std_assists, mean_rebounds, std_rebounds


points=[]
rebounds=[]
assists=[]
i=0
fobj = open("data.txt", 'r')
for line in fobj:
    #print line.rstrip()
    a=line.rstrip()
    rebound_pos=a.find(",")
    rebound=a[0:rebound_pos]
    new_string=a[rebound_pos+1:]
    assist_pos=new_string.find(",")
    assist=new_string[0:assist_pos]
    new_string_2=new_string[assist_pos:]
    point=new_string_2[1:]
    assists.append(int(assist))
    rebounds.append(int(rebound))
    points.append(int(point))
    i=i+1
#print(points)
fobj.close()


mean_points,std_points=norm.fit(points) 
#plt.hist(points, 50)
x_points = np.linspace(min(points), max(points), 100)
y_points = i*norm.pdf(x_points, mean_points, std_points)
#plt.plot(x_points, y_points)
#plt.show()

mean_assists,std_assists=norm.fit(assists)
#plt.hist(assists, 18)
x_assists = np.linspace(min(assists), max(assists), 100)
y_assists = i*norm.pdf(x_assists, mean_assists, std_assists)
#plt.plot(x_assists, y_assists)
#plt.show()


mean_rebounds,std_rebounds=norm.fit(rebounds)
#plt.hist(rebounds, 18)
x_rebounds = np.linspace(min(rebounds), max(rebounds), 100)
y_rebounds = i*norm.pdf(x_rebounds, mean_rebounds, std_rebounds)
#plt.plot(x_rebounds, y_rebounds)
#plt.show()

def statline():
    points=round(rnd.normal(mean_points, std_points, 1), 0)
    assists=round(rnd.normal(mean_assists, std_assists, 1), 0)
    rebounds=round(rnd.normal(mean_rebounds, std_rebounds, 1), 0)
    return points, assists, rebounds
    
def check(points, assists, rebounds):
    hit=False
    if points==27:
        if assists==7:
            if rebounds==7:
                 hit=True
    return hit



def run():
    hit=False
    i=0
    while hit==False:
        stat=statline()
        hit= check(stat[0], stat[1], stat[2])
        i=i+1
    return i


def t_runs():
    average=0
    i=0    
    while i<200:
        this_run=run()
        average=this_run+average
    
        i=i+1

    erg=average/(i+1)
    return erg
 

i=0
plot_y=[]
plot_x=[]
k=1000 
while i<k:
    number=t_runs()
    plot_y.append(number)
    i=i+1
    plot_x.append(i)



plt.plot(plot_x,plot_y)    
plt.show()
plt.hist(plot_y, k**(0.5))

mean_result,std_result=norm.fit(plot_y) 
x_result = np.linspace(min(plot_y)-300, max(plot_y), 100)
y_result = 50000*norm.pdf(x_result, mean_result, std_result)
plt.plot(x_result, y_result)
plt.show()
print(mean_result)
print(std_result)
