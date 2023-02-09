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
print('Numero totale di stati: ',stati.size, 'codici', acod)
print('------------------------')
'''
np.set_printoptions(threshold=sys.maxsize)
'''PRENDO ARRAY'''

meanO3AZ , dateAZ,arr  =f.meanday(stati[0])
meanO3CA , dateCA,arr  =f.meanday(stati[2])
meanO3CT , dateCT,arr  =f.meanday(stati[4])
meanO3DC , dateDC ,arr =f.meanday(stati[5])
meanO3FL , dateFL ,arr =f.meanday(stati[6])
meanO3IL , dateIL ,arr =f.meanday(stati[9])
meanO3IA , dateIA ,arr =f.meanday(stati[11])
meanO3ME , dateME ,arr =f.meanday(stati[14])
meanO3MD , dateMD ,arr =f.meanday(stati[15])
meanO3MA , dateMA ,arr =f.meanday(stati[16])
meanO3NH , dateNH ,arr =f.meanday(stati[19])
meanO3NY , dateNY ,arr =f.meanday(stati[21])
meanO3NC , dateNC ,arr =f.meanday(stati[22])
meanO3ND , dateND ,arr =f.meanday(stati[23])
meanO3OK , dateOK ,arr =f.meanday(stati[25])
meanO3OR , dateOR ,arr =f.meanday(stati[26])
meanO3PA , datePA ,arr =f.meanday(stati[27])
meanO3SC , dateSC ,arr =f.meanday(stati[28])
meanO3TN , dateTN ,arr =f.meanday(stati[29])
meanO3TX , dateTX ,arr =f.meanday(stati[30])
meanO3VA , dateVA ,arr =f.meanday(stati[31])


print('date' ,' Lunghezza ',len(dateDC))
print('meanO3MA' ,' Lunghezza ',len(meanO3DC))
#print(arr ,' Lunghezza ',len(arr))

'''Andamento Temporale'''



'''Trasformate e frequenze '''

'''Spettri'''

'''Periodicità e max'''

'''Correlazione con frequenze'''

'''Filtri '''

'''Dati originali rispetto a filtrati'''
