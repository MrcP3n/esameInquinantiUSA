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

def graphInTime2(arrx1,arry1,arrx2,arry2,title,cl):
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle(title)
    ax1.plot(arrx1, arry1, color=cl)
    ax2.plot(arrx2, arry2, color=cl)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Media Ozono')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Media Ozono')
    ax1.xaxis.set_major_locator(MultipleLocator(30))
    ax1.xaxis.set_minor_locator(MultipleLocator(5))
    ax2.xaxis.set_major_locator(MultipleLocator(30))
    ax2.xaxis.set_minor_locator(MultipleLocator(5))
    fig.set_figheight(8)
    fig.set_figwidth(12)
    plt.savefig(title)
    plt.show()
    return

def graphInTime5(arrx1,arry1,arrx2,arry2,arrx3,arry3, arrx4,arry4,arrx5,arry5,title):
    fig, (ax1, ax2 ,ax3 ,ax4 , ax5) = plt.subplots(5)
    fig.suptitle(title)
    ax1.plot(arrx1, arry1, color='red')
    ax2.plot(arrx2, arry2, color='limegreen')
    ax3.plot(arrx3, arry3, color='cyan')
    ax4.plot(arrx4, arry4, color='midnightblue')
    ax5.plot(arrx5, arry5, color='orchid')
    ax1.set_ylabel('Ozono CT')
    ax2.set_ylabel('Ozono MD')
    ax1.xaxis.set_major_locator(MultipleLocator(30))
    ax1.xaxis.set_minor_locator(MultipleLocator(5))
    ax2.xaxis.set_major_locator(MultipleLocator(30))
    ax2.xaxis.set_minor_locator(MultipleLocator(5))
    ax3.set_ylabel('Ozono NY')
    ax4.set_ylabel('Ozono PA')
    ax3.xaxis.set_major_locator(MultipleLocator(30))
    ax3.xaxis.set_minor_locator(MultipleLocator(5))
    ax4.xaxis.set_major_locator(MultipleLocator(30))
    ax4.xaxis.set_minor_locator(MultipleLocator(5))
    ax5.set_xlabel('Date')
    ax5.set_ylabel('Ozono VA')
    ax5.xaxis.set_major_locator(MultipleLocator(30))
    ax5.xaxis.set_minor_locator(MultipleLocator(5))
    fig.set_figheight(7)
    fig.set_figwidth(10)
    plt.savefig(title)
    plt.show()
    return
    

def trFour_freq(arrMean):
    sNyqu=0.5
    cofft=fft.fft(arrMean)
    cofFreq=sNyqu*fft.fftfreq(len(cofft) , d=1)
    return cofft , cofFreq

#METTI APPOSTO DIMENSIONI
def graphSpettri5(afreq1,acof1,afreq2,acof2,afreq3,acof3,afreq4,acof4,afreq5,acof5,title):
    fig, (ax1, ax2 ,ax3 ,ax4 , ax5) = plt.subplots(5)
    fig.suptitle(title)
    ax1.plot(afreq1[:int(acof1.size/2)],np.absolute(acof1[:int(acof1.size/2)])**2,'o', markersize=3 ,color='red')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax2.plot(afreq2[:int(acof2.size/2)],np.absolute(acof2[:int(acof2.size/2)])**2,'o', markersize=3 ,color='limegreen')
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax3.plot(afreq3[:int(acof3.size/2)],np.absolute(acof3[:int(acof3.size/2)])**2,'o', markersize=3 ,color='cyan')
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    ax3.set_ylabel('Coefficenti') #Migliora
    ax4.plot(afreq4[:int(acof4.size/2)],np.absolute(acof4[:int(acof4.size/2)])**2,'o', markersize=3 ,color='midnightblue')
    ax4.set_xscale('log')
    ax4.set_yscale('log')
    ax5.plot(afreq5[:int(acof5.size/2)],np.absolute(acof5[:int(acof5.size/2)])**2,'o', markersize=3 ,color='orchid')
    ax5.set_xscale('log')
    ax5.set_yscale('log')
    ax5.set_xlabel('Frequenze')
    plt.show()

    return



