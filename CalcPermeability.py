#Calculate Permeability from a grain size distribution
#Mutliple empirical or semi-empirical equations are available(with their best fittings):
#Beyer-Kresic: 0.06mm<d10<0.6mm 1<Cu<20
#Hazen: 0.1mm<d10<3mm Cu<5
#Gustafson:
#Kozeny-Carman: d50 < 3mm Here after Svensson 2014, Carrier 2003 and Amar
#Slichter: 0.01mm<d10<5mm
#Terzaghi: large grain sands
#USBR: medium grain sands, Cu<5

import numpy as np
import matplotlib.pylab as plt
import scipy.stats as st


def plotGraph(x1, y1): #,trendLine
    plt.figure()
    plt.plot(x1, y1, color='blue', label='Data WT1 after TIBKAT, 2007')
    #x2 = np.linspace(0, 50, 20)
    #y2 = trendLine[-3] * x2*x2 + trendLine[-2] * x2 + trendLine[-1]
    #plt.plot(x2, y2, color='red', label='Fitted polynomial')
    plt.legend(fontsize=15)
    plt.xlabel('Grain Sizes', fontsize=17)
    plt.ylabel('Percentage', fontsize=17)
    plt.grid(True)
    plt.xlim(0, 50)
    plt.xticks(np.linspace(0, 50, 21), fontsize=15)
    plt.ylim(0,1.05)
    plt.yticks(np.linspace(0, 1, 11), fontsize=15)
    plt.tight_layout()
    plt.show()

def solveQuadraticEquation(a, b, c, boundaries):
    x1 = (-b + (b**2 - (4*a*c))**(0.5)) / (2*a)
    x2 = (-b - (b**2 - (4*a*c))**(0.5)) / (2*a)
    if boundaries[0] < x1 < boundaries[1]:
        return x1
    else:
        return x2

def kfToK(kf): 
    #from https://www.sedgeochem.uni-bremen.de/perm_kf_en.html & 
    #https://rdrr.io/github/rogiersbart/groundwaterr/src/R/permeability_to_hydraulic_conductivity.R
    K = kf * 0.001308/(9.80605 * 999.7)
    return K
    
def BeyerKresic(d10, Cu):
    kf = 6 * 10**-4 * np.log10(500/Cu) * d10**2
    K = kfToK(kf)
    return K

def Hazen(d10, n):
    kf = 6 * 10**-4 *(1+10*(n-0.26)) * d10**2
    K = kfToK(kf)
    return K

def Gustafson(d10, Cu):
    E = 0.8 * 1/(2*np.log(Cu)) - 1/(Cu**2 - 1)
    gf = 1.3/(np.log10(Cu)) * (Cu**2 - 1)/Cu**1.8
    Ef = 10.2 * 10**6 * (E**3/(1+E)) * 1/(gf**2)    
    kf = Ef * (d10/1000)**2
    K = kfToK(kf)
    return K

def KozenyCarman_Sven(d10, d50, d60, n):
    phi = ((np.log(1/d10)/np.log(2)) - (np.log(1/d60)/np.log(2)))/1.53
    epsilon = n/(1-n) #from https://en.wikipedia.org/wiki/Void_ratio
    kf = d50**2/180 * (epsilon**3)/(1+epsilon) * np.exp(-0.48*phi**2 - 0.9*phi)
    K = kfToK(kf)
    return K

def KozenyCarman_Carr(middleRange, grainSizePerc, n):
    d_ave = np.zeros(len(middleRange))
    for x in range(0, len(middleRange)):
        d_ave[x] = grainSizePerc[x]/middleRange[x]
    d_eff = 1/np.sum(d_ave)
    SF = 7.0
    epsilon = n/(1-n)
    kf = 1.99e4 * d_eff**2 * (1/SF**2)*(epsilon**3/(1+epsilon))
    K = kfToK(kf)
    return K

def KozenyCarman_Amar(d10, d60, n):
    epsilon = n/(1-n)
    kf = d60**0.6 * d10**1.72 *(epsilon**3/(1+epsilon))
    K = kfToK(kf)
    return K

def Slichter(d10, n):
    kf = 10**-2 * n**3.287 * d10**2
    K = kfToK(kf)
    return K

def Terzaghi(d10, n):
    # 6.1e-3 < C < 10.7e-3
    C = 8.4 * 10**-3
    kf = C * ((n - 0.13)/ (1-n)**(1.0/3.0))**2 * d10**2
    K = kfToK(kf)
    return K

def USBR(d20):
    kf = 4.8 * 10**-4 * d20**0.3 * d20**2
    K = kfToK(kf)
    return K

def AURA():
    # after AURA Report p.55 with min. pF -> max. saturation
    kf = 100.0/(100.0*24.0*3600.0) #from 100cm/d to m/2
    K = kfToK(kf)
    return K

#Define the data from TIBKAT 2007 page 85
lowerRange = np.array([0.0, 2.0, 4.0, 8.0, 16.0, 32.0]) #in mm
upperRange = np.array([2.0, 4.0, 8.0, 16.0, 32.0, 64.0]) #in mm
#1st sample
grainSizePerc = np.array([3.8, 3.7, 9.6, 15.8, 41.3, 25.8]) #as percentage
#2nd sample
#grainSizePerc = np.array([0.5, 0.1, 1.2, 6.6, 52.1, 39.5]) #as percentage

#Transform data
#Transform from 100% to 1
grainSizePerc = grainSizePerc/100.0
#Calculate accumulated percentages
accuPerc = np.cumsum(grainSizePerc)
#Decide to Middle of the ranges
middleRange = (lowerRange + upperRange)/2

#Possible to fit a trendline to the data
#trendLine = np.polyfit(middleRange, accuPerc, 2)
#The Trendline is used to calculate data-characteristics
#dataBoundaries = [min(middleRange), max(middleRange)]
#d10 = solveQuadraticEquation(trendLine[0], trendLine[1], trendLine[2] - 0.1, dataBoundaries)

#Plot the accumulated Percentage
plotGraph(middleRange, accuPerc)
#distribution fraction read from the plotted graph
#1st sample
d10 = 3.75
d20 = 7.1 
d50 = 17.0
d60 = 19.9
#2nd sample
#d10 = 12.5
#d20 = 14.7
#d50 = 21.5
#d60 = 24
Cu = d60/d10 #after Vukovic&Soro 1992
n = 0.255 * (1 + 0.83**Cu) #after Vukovic&Soro 1992

print('Beyer-Kresic:')
K = BeyerKresic(d10, Cu)
print(K)
print('Gustafson:')
K = Gustafson(d10, Cu)
print(K)
print('Hazen:')
K = Hazen(d10, n)
print(K)
print('Kozeny-Carman after Svensson:')
K = KozenyCarman_Sven(d10, d50, d60, n)
print(K)
print('Kozeny-Carman after Carrier:')
K = KozenyCarman_Carr(middleRange, grainSizePerc, n)
print(K)
print('Kozeny-Carman after Amar:')
K = KozenyCarman_Amar(d10, d60, n)
print(K)
print('Slichter:')
K = Slichter(d10, n)
print(K)
print('USBR:')
K = USBR(d20)
print(K)
print('Terzaghi:')
K = Terzaghi(d10, n)
print(K)
print('AURA:')
K = AURA()
print(K)


