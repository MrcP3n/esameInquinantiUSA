from scipy import constants,fft
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import (MultipleLocator,AutoMinorLocator)


def takeArr(staz):
    average = np.empty(0)
    date = np.empty(0)
    for h in staz.arrRil:
        average = np.append(average ,h.mean)
        date = np.append(date ,h.data)
        
    return date , average   

def graphInTime(arrx1,arry1,arrx2,arry2,title):
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle(title)
    ax1.plot(arrx1, arry1)
    ax2.plot(arrx2, arry2)
    ax1.set_xlabel('Media Ozono')
    ax1.set_ylabel('Date')
    ax2.set_xlabel('Media Ozono')
    ax2.set_ylabel('Date')
    ax1.xaxis.set_major_locator(MultipleLocator(30))
    ax1.xaxis.set_minor_locator(MultipleLocator(5))
    ax2.xaxis.set_major_locator(MultipleLocator(30))
    ax2.xaxis.set_minor_locator(MultipleLocator(5))
    plt.show()
    return
    

def trFour_freq(arMean):
    sNyqu=0.5
    cofft=fft.fft(arrMean)
    cofFreq=sNyqu*fft.fftfreq(len(cofft) , d=1)
    
    return cofft , cofFreq


def graphSpettri(arrx,arry):


    return



