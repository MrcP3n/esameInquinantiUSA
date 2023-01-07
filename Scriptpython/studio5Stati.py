import numpy as np
import pandas as pd
import Stazione
import csv




tabNY=pd.read_csv('/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv')
'''
cStatoNY=tabNY['cStatoNY'].values
cConteaNY=tabNY['cConteaNY'].values
nSitNY=tabNY['nSitNY'].values
dateNY=tabNY['dateNY'].values
O3meanNY=tabNY['O3meanNY'].values
'''
NY='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv'
Pen='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiPen.csv'
CT='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiCT.csv'
VA='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiVA.csv'
MD='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiMD.csv'

def getStazione(path):

    '''Funzione legge file e restituisce array di stazioni'''
    df=pd.read_csv(path)
    
    staz= hits = np.array([Stazione.Stazione( r['cStatoNY'], r['cConteaNY'], r['nSitNY'],r['dateNY'],r['O3meanNY'] ) for i, r in df.iterrows() ])

    return staz

#trasformo string in int
'''d=dateNY[0]
s=int(d[3])
print(d,'   ',s,s+100)
'''

stazNY = getStazione(NY)
stazPen = getStazione(Pen)
stazCT = getStazione(CT)
stazVA = getStazione(VA)
stazMD = getStazione(MD)

#hits = np.concatenate( (hitsM0, hitsM1, hitsM2, hitsM3) )

#np.sort(hits, kind='mergesort' )
#np.sort(stazNY, kind='mergesort')
stazNY.sort(kind='mergesort' )


print('Total Number of Station:', stazNY.size)
    
for h in staz.NY:
    print(h.cStato, h.cContea, h.cStaz, h.data, h.mean)
















