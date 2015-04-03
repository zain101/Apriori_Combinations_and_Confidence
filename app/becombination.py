#!/bin/python
import copy
import pycsv as pc
import os
import itertools
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

import pylab as py
l = []
y = []
map = []
tmp = []
combi = []
pieCombi = []
globalRank = 0.0
ranks= range(0, 500)
for i in range(0, 500):
	ranks[i]= 0.0

def init():
	global l
	global y
	print "Reading from file output of Apriori .............................................{press enter to start}[start]"
	xx= raw_input()
	print ".....................................................................................................[started]"

	f= open('../output/frameset_Sum.txt', 'r')
	content= f.readline()
	l= content.strip('[]\n')
	con = f.readline()
	f.close()
	print ".....................................................................................................[Finished]"
	x= l.split(" ")
	y= con.split("\t")
	y= y[0:27]
	l= x
	j= 0
	for i in l:
		if ',' in i:
			l[j] = i.strip(',')
		j = j + 1
	l = list(set(l))

	print "Frame-set ==>", l
	print "Summation of columns ==>", y
	print "\n\nFinish reading and formatting the data............"

def giveNum(s):
    return int(s[1:])  #returns the integer hidden in column

def getVal(n):
    return y[n]

def genVal(m):
    z= []
    for i in m:
        n= giveNum(i)
        n= int(getVal(n-1))
        z+= [{i: n}]
    return z

'''
def genrateCombinations():
	print "\nGenrating the Combinations...........................................................................[Started]"
	global combi, cpy_combi
	global l
	for i in range(0,len(l)):
	   combi+= [l[i:i+1] + l[i+1:]+l[0:i]]

	for i in range(0,len(l)):
		for j in range(i+1,len(l)):              # This guy works for limited number of combinations, so don't use, kept for memories.
		    tmp = [l[i]]+[l[j]]
		    tmp1 = copy.copy(tmp)
		    combi += [tmp]
		    tmp1.reverse()
		    combi += [tmp1]

	print "\nCombinations genrated are ::"
	for i in combi:
		print i
'''

def rest(a, b):
    #print a, b
    for i in a:
        #print i
        try:
            b.remove(i)
        except:
            "not in list..."
    #print b , type(b)
    return b

def genrateCombinations():
    global l, combi
    j=0
    for i in range(1, len(l)):
        for x in itertools.combinations(l,i):
            #print x
            j = j+1
            combi.append(list(x))
    genXY()


def genXY():
    global l, combi
    j=0
    for i in combi:
        i.sort()
    for i in range(0,len(combi)):
        combi[i] = [combi[i]] + [rest(combi[i], copy.copy(l))]

def mapping(a):
    for i in map:
        if a in i:
            return i.values()
'''
def calRank():
	print "\nPress enter to start calculating the Confidence..............."
	xx= raw_input()
	j=0
	global ranks, combi, globalRank
	for a in combi:
		tmp= copy.copy(a)
		if(len(tmp) > 2):
			for i in range(0,len(a)):
				if (i == 0):
					tmp[i]= mapping(tmp[i])[0]
				else:
					tmp[i]= giveNum(tmp[i])
		else:
			for i in range(0, len(a)):
				tmp[i] = mapping(tmp[i])[0]
			#print tmp, len(tmp)
		if(len(tmp) > 2):
				ranks[j]= float(workForUnion(tmp[1:]))/float(tmp[0])
				j= j+1
		else:
			if((sum(tmp[1:])/tmp[0]) > -1):
				ranks[j]= float(sum(tmp[1:]))/float(tmp[0])
				j= j+1
'''
def stripping():
	global combi
	ii, jj, kk = 0, 0, 0
	tmp = copy.copy(combi)
	for i in tmp:
	    jj=0
	    for j in i:
	        kk=0
	        for k in j:
	            combi[ii][jj][kk] = giveNum(combi[ii][jj][kk]) -1
	            kk = kk+1
	        jj = jj+1
	    ii=ii+1

def calGlobalUnion():
	global combi, globalRank
	tmp = copy.copy(combi)
	globalRank = pc.workForUnion(tmp[0][0]+tmp[0][1])
	return globalRank

def calRank():
	print "\nPress enter to start calculating the Confidence......................................................[start]"
	xx= raw_input()
	j=0
	global ranks, combi, globalRank
	tmp = copy.copy(combi)
	for a in tmp:
		zzz =  pc.workForUnion(copy.copy(a[0]))
		# print a[0] ,type(a[0]) , zzz
		if(zzz == 0):
			ranks[j] =0.0
		else:
			ranks[j] = 	21.0/zzz
		j = j+1

def display():
	for i in range(0, len(combi)):
		print "combinations is %30s   |  confidence is %20s" %(combi[i], ranks[i])
	print ranks[0:10]

def plot_confidence():
	global combi
	n = len(ranks)
	tmp= []
	x_ax= ranks[0:n]#py.linspace(0,2,9,0.3)
	#x_ax= tuple(ranks[0:9])
	ind= range(0, n)
	width= 0.70
	x= range(0, len(ranks)+1)
	y= range(0, len(ranks)+1)
	for i in range(0, len(ranks)+1):
		x[i] = i
		y[i] = 0.9
	#py.subplot(x,y,'r')
	#fig, ax= plt.subplots()
	x_ax=tuple(x_ax)
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	dx=np.ones(n)
	dy=np.ones(n)
	dz=range(0,n)
	for i in range(0, n):
		ind[i] = ind[i]+2
		#rect1 = ax.bar3d([ind[i]], [x_ax[i]], zs=i, zdir='y', dx=1, dy=1,dz=1, width=0.70, color='#8B1C62', alpha=0.6)
		rect1 = ax.bar3d([ind[i]], i ,0, 0.5, 0.5, [x_ax[i]], color='#8B1C62')
	#ax.plot(x,y, zs=0, zdir='y', color= 'lightcoral', linewidth=2)


	#ax.set_title(' Apririo confidence graph for various combinations', fontsize=17)
	#ax.set_zlabel('(Confidence in % ) * 100', fontsize=15)
	#ax.set_ylabel('<===Factors affecting failure{on X-axis}',  labelpad=100 ,fontsize=15)
	ax.set_xticks(ind+[width])
	for i in combi:
		tmp+= i[0:2]
	# print tuple(tmp)
	ax.set_xticklabels(tuple(combi), fontsize=10, rotation= 90 )

	plt.margins(0.02)
	# Tweak spacing to prevent clipping of tick-labels
	plt.subplots_adjust(bottom=0.08)

	def autolabel():
		# attach some text labels
		for i in range(0, n):
			try:
				ax.text(int(ind[i])+1, i-2, x_ax[i]+0.05, str(x_ax[i])[0:4], color='#660066', backgroundcolor= '#c187e1', weight= 'bold', rotation='vertical', fontsize=10, horizontalalignment='left', verticalalignment='bottom')   	#autolabel(rect1)
			except:
				print "Fonts missing ......................................................................................[ERROR]"
	autolabel()
	mng = plt.get_current_fig_manager()
	mng.full_screen_toggle()
	plt.savefig('../output/bar.png')
	plt.show()

def pieChart():
	global ranks, combi
	tmp= []
	for i in combi:
		tmp+= i[0:2]
	labels= tuple(pieCombi)#'a', 'b', '2', '3', '4','5', '6', '7','5'
	colors_list = ['#8B8B00', '#FFD343', '#8B475D', 'lightcoral', '#FF9900', '#8B668B', '#8B7765','#61B2A7', '#2869AF']
	j = 0
	colors= range(0, len(ranks))
	for i in range(0, len(ranks)):
		colors[i] = colors_list[j]
		j = i%len(colors_list)

	explode_list= range(0, len(ranks))
	for i in range(0, len(ranks)):
		explode_list[i] = 0.1
	explode = tuple(explode_list)
	#cs=cm.Set1(np.arange(9)/9.)
	fracs= ranks[0:len(combi)]
	py.pie(fracs, labels=labels, colors= colors, explode= explode, autopct='%1.1f%%', shadow=True, startangle=90)
	py.title('Influence of each factor...', bbox={'facecolor':'#CCFF99', 'pad':20})
	mng = plt.get_current_fig_manager()
	mng.full_screen_toggle()
	py.savefig('../output/pie.png', bbox_inches='tight')
	py.show('equal')


def moreThan90():
	global ranks, combi, pieCombi
	r= []
	j=0
	for i in ranks:
		if i > 0.89:
			r += [i]
			pieCombi += [combi[j]]
		j=j+1
	ranks = r
	print len(ranks), len(pieCombi)


if __name__ == "__main__":
	os.system("javac AprioriAlgo.java")
	os.system("java AprioriAlgo > ../output/java_Apriori.txt")
	os.system("clear")
	os.system("cat ../output/java_Apriori.txt | tail -2 > ../output/frameset_Sum.txt")
	init()
	#map= genVal(l)
	#print map
	genrateCombinations()
	print "\nGenrating Combinations...........................................................................      [OK]"
	print "\nTotal no. of combinations are ==> ", len(combi)
	tmpu = copy.copy(combi)
	for i in tmpu:
		print i
	xx = raw_input()

	stripping()
	print "\nStripping Integers...............................................................................      [OK]"

	pc.readCSV()
	calGlobalUnion()
	print "\nCalculating Global union..........................................................................   [OK]"
	calRank()
	print "\nCalculating Confidence............................................................................      [OK]"
	display()
	moreThan90()
	print "\nFiltering results > 90............................................................................      [OK]"
	print "\nPress enter to plot Graphs {enter}.........................................................................!"
	xx=raw_input()
	plot_confidence()
	print  "\nBar Graph plotted and saved .....................................................................      [OK]"
	pieChart()
	print  "\nPIE Graph plotted and saved .....................................................................      [OK]"
	os.system("gedit ../output/java_Apriori.txt")
