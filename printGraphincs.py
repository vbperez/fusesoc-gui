
# sudo apt-get install python-matplotlib

#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
#Import matplotlib for generating a graphical.
import matplotlib.pyplot as plt

x=[]
mList=[]
nList=[]
def calcularX():
	f=open("xmemdata(LPB).hex")
	global x
	
	x1=float(f.readline())
	x.append(x1+1.0)
	
	i=2
	while i<=52:
		x1=float(f.readline())
		if(i%2==0):
			x.append(x1-1.0)
		else:
			x.append(x1+1.0)
		i=i+1
	return x
	
	
def calcularY(t,y):
	global x
	global mList
	global nList
	
	if(t==0):
		return 0
	if(t==1):
		return 0
	
	m=1.8*(calcularY(t-1,y))
	mList.append(m)
	n=0.81*(y[t-2])
	nList.append(n)
	y.append((0.0099*x[t])+ m - n)
	
	return y[t]
	
	
def printGrafphic():
  
    plt.plot(y)
    plt.show()
	 
	
if __name__ == '__main__':
	x= calcularX()
	
	y=[]
	y.append(0)
	y.append(0)
	calcularY(51,y)

	printGraphic()
	
