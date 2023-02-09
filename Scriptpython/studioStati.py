import numpy as np
import pandas as pd
import Classi
import matplotlib.pyplot as plt
from scipy import constants , fft
import Funzioni as f
import sys

pstati='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiStati.csv'

rilStati=f.getRilevaz(pstati)

rilStati.sort(kind='mergesort')
#print(ril5Stati)
'''
for h in rilStati:
    print(h.cStato, h.cContea, h.cStaz, h.data, h.mean)
'''
print('Numero totale di rilevazioni:', rilStati.size)
'''
stazStati=f.getStazioni(rilStati)
stazStati.sort(kind='mergesort')


for hh in stazStati[0].arrRil:
    print(hh.cStato, hh.cContea , hh.cStaz, hh.data ,hh.mean)

for i in range(141):
    print('-----Stazione{:}------'.format(i))
    print('nRilevazioni', stazStati[i].nril)

print('Numero totale di stazioni: ', stazStati.size)
'''
stati,acod=f.getStati(rilStati)
stati.sort(kind='mergesort')


'''
for hh in stati[0].arrRil:
    print(hh.cStato,hh.data,hh.mean)


for i in range(34):
    print('-----Stato{:}------'.format(i))
    print('nRil', stati[i].nril)
'''
print('Numero totale di stati: ',stati.size)
print('------------------------')

np.set_printoptions(threshold=sys.maxsize)
'''PRENDO ARRAY'''

meanO3AZ , dateAZ,arr  =f.meanDay(stati[0])
meanO3CA , dateCA,arr1  =f.meanDay(stati[2])
meanO3CT , dateCT,arr =f.meanDay(stati[4])
meanO3DC , dateDC ,arr =f.meanDay(stati[5])
meanO3FL , dateFL ,arr =f.meanDay(stati[6])
meanO3IL , dateIL ,arr =f.meanDay(stati[9])
#meanO3IA , dateIA ,arr =f.meanDay(stati[11])#????700
meanO3ME , dateME ,arr =f.meanDay(stati[14])
meanO3MD , dateMD ,arr =f.meanDay(stati[15])
meanO3MA , dateMA ,arr =f.meanDay(stati[16])
#meanO3NH , dateNH ,arr =f.meanDay(stati[19])#???717
meanO3NY , dateNY ,arr =f.meanDay(stati[21])
meanO3NC , dateNC ,arr =f.meanDay(stati[22])
meanO3ND , dateND ,arr =f.meanDay(stati[23])
meanO3OK , dateOK ,arr =f.meanDay(stati[25])
meanO3OR , dateOR ,arr =f.meanDay(stati[26])
meanO3PA , datePA ,arr =f.meanDay(stati[27])
meanO3SC , dateSC ,arr =f.meanDay(stati[28])#843
#meanO3TN , dateTN ,arr =f.meanDay(stati[29])#???681
meanO3TX , dateTX ,arr =f.meanDay(stati[30])
#meanO3VA , dateVA ,arr =f.meanDay(stati[31])#795

'''
print('dateCA',' Lunghezza ',len(dateFL))
print('meanO3MA' ,' Lunghezza ',len(meanO3FL))
print('arr1' ,' Lunghezza ',len(arr))
'''
'''Andamento Temporale'''
if False:
    #WEST COAST AND CENTER
    title='Andamenti Oregon, California, Arizona, Texas, Oklahoma'
    #f.graphInTime5(dateOR,meanO3OR,dateCA,meanO3CA,dateAZ,meanO3AZ,dateTX,meanO3TX,dateOK,meanO3OK,title)
    #EAST COAST AND CENTER
    title='Andamenti Maine, Maryland, Massachusetts, Pennsylvania, New York'
    f.graphInTime5(dateME,meanO3ME,dateMD,meanO3MD,dateMA,meanO3MA,datePA,meanO3PA,dateNY,meanO3NY,title)
    title='Andamenti Florida, Illinois, District of columbia, North Dakota, North Carolina'
    f.graphInTime5(dateFL,meanO3FL,dateIL,meanO3IL,dateDC,meanO3DC,dateND,meanO3ND,dateNC,meanO3NC,title)
    #EAST COAST
    title='Andamenti Connecticut, Pennsylvania, North Carolina, South Carolina, Florida'
    f.graphInTime5(dateFL,meanO3FL,dateIL,meanO3IL,dateDC,meanO3DC,dateND,meanO3ND,dateNC,meanO3NC,title)
    #GENERALE
    title='Andamenti Oregon, Pennsylvania, North Dakota, South Carolina, Illinois'#Cali al posto di illi
    f.graphInTime5(dateOR,meanO3OR,datePA,meanO3PA,dateND,meanO3ND,dateSC,meanO3SC,dateIL,meanO3IL,title)    
    

'''Trasformate e frequenze '''
coffAZ , cofFreqAZ , maxAZ = f.trFour_freq(meanO3AZ)
coffCA , cofFreqCA , maxCA = f.trFour_freq(meanO3CA)
coffCT , cofFreqCT , maxCT = f.trFour_freq(meanO3CT)
coffDC , cofFreqDC , maxDC = f.trFour_freq(meanO3DC)
coffFL , cofFreqFL , maxFL = f.trFour_freq(meanO3FL)
coffIL , cofFreqIL , maxIL = f.trFour_freq(meanO3IL)
coffME , cofFreqME , maxME = f.trFour_freq(meanO3ME)
coffMD , cofFreqMD , maxMD = f.trFour_freq(meanO3MD)
coffMA , cofFreqMA , maxMA = f.trFour_freq(meanO3MA)
coffNY , cofFreqNY , maxNY = f.trFour_freq(meanO3NY)
coffNC , cofFreqNC , maxNC = f.trFour_freq(meanO3NC)
coffND , cofFreqND , maxND = f.trFour_freq(meanO3ND)
coffOK , cofFreqOK , maxOK = f.trFour_freq(meanO3OK)
coffOR , cofFreqOR , maxOR = f.trFour_freq(meanO3OR)
coffPA , cofFreqPA , maxPA = f.trFour_freq(meanO3PA)
coffSC , cofFreqSC , maxSC = f.trFour_freq(meanO3SC)
coffTX , cofFreqTX , maxTX = f.trFour_freq(meanO3TX)

'''Spettri'''
if False:
    #WEST COAST AND CENTER
    title='Spettri Oregon, California, Arizona, Texas, Oklahoma'
    #f.graphSpettri5(coffOR , cofFreqOR,coffCA , cofFreqCA,coffAZ , cofFreqAZ,coffTX , cofFreqTX,coffOK , cofFreqOK,title)
    
    title='Spettri Maine, Maryland, Massachusetts, Pennsylvania, New York'
    f.graphSpettri5(coffME , cofFreqME,coffMD , cofFreqMD,coffMA , cofFreqMA,coffPA , cofFreqPA,coffNY , cofFreqNY,title)
    
    title='Spettri Florida, Illinois, District of columbia, North Dakota, North Carolina'
    f.graphSpettri5(coffFL , cofFreqFL,coffIL , cofFreqIL,coffDC , cofFreqDC,coffND , cofFreqND,coffNC , cofFreqNC,title)
    #EAST COAST
    title='Spettri Connecticut, Pennsylvania, North Carolina, South Carolina, Florida'
    f.graphSpettri5(coffCT , cofFreqCT,coffPA , cofFreqPA,coffNC , cofFreqNC,coffSC , cofFreqSC,coffFL , cofFreqFL,title)
    #GENERALE
    title='Spettro Oregon, Pennsylvania, North Dakota, South Carolina, Illinois'#Cali al posto di illi
    f.graphSpettri5(coffOR , cofFreqOR,coffPA , cofFreqPA,coffND , cofFreqND,coffSC , cofFreqSC,coffIL , cofFreqIL,title)   


'''Periodicità e max'''


'''Correlazione con frequenze'''

'''Filtri '''

'''Dati originali rispetto a filtrati'''
