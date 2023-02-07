import numpy as np
import pandas as pd
import Classi
import matplotlib.pyplot as plt
from scipy import constants , fft
import Funzioni as f

pstati='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiStati.csv'

rilStati=f.getRilevaz(pstati)

rilStati.sort(kind='mergesort')
#print(ril5Stati)

for h in rilStati:
    print(h.cStato, h.cContea, h.cStaz, h.data, h.mean)

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

print('------------------------')

for hh in stati[0].arrRil:
    print(hh.cStato,hh.data,hh.mean)


for i in range(34):
    print('-----Stato{:}------'.format(i))
    print('nRil', stati[i].nril)
print('Numero totale di stati: ',stati.size, 'codici', acod)

meanO3AZ , dateAZ =f.meanday(stati[0])
print(dateAZ,' Lunghezza ',len(dateAZ))



