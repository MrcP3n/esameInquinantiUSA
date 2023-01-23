from scipy import constants,fft
import numpy as np






def trFour_freq(arMean):
    sNyqu=0.5
    cofft=fft.fft(arrMean)
    cofFreq=sNyqu*fft.fftfreq(len(cofft) , d=1)
    
    return cofft , cofFre




