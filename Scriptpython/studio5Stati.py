import numpy as np
import pandas as pd
import Stazione
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy import constants , fft
from scipy import stats

'''
tabNY=pd.read_csv('/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv')
cStatoNY=tabNY['cStatoNY'].values
cConteaNY=tabNY['cConteaNY'].values
nSitNY=tabNY['nSitNY'].values
dateNY=tabNY['dateNY'].values
O3meanNY=tabNY['O3meanNY'].values

tabVA=pd.read_csv('/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiVA.csv')
cStatoVA=tabVA['cStatoVA'].values
cConteaVA=tabVA['cConteaVA'].values
nSitVA=tabVA['nSitVA'].values
dateVA=tabVA['dateVA'].values
O3meanVA=tabVA['O3meanVA'].values

tabCT=pd.read_csv('/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiCT.csv')
cStatoCT=tabCT['cStatoCT'].values
cConteaCT=tabCT['cConteaCT'].values
nSitCT=tabCT['nSitCT'].values
dateCT=tabCT['dateCT'].values
O3meanCT=tabCT['O3meanCT'].values

tabMD=pd.read_csv('/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiMD.csv')
cStatoMD=tabMD['cStatoMD'].values
cConteaMD=tabMD['cConteaMD'].values
nSitMD=tabMD['nSitMD'].values
dateMD=tabMD['dateMD'].values
O3meanMD=tabMD['O3meanMD'].values

tabPen=pd.read_csv('/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiPen.csv')
cStatoPen=tabPen['cStatoPen'].values
cConteaPen=tabPen['cConteaPen'].values
nSitPen=tabPen['nSitPen'].values
datePen=tabPen['datePen'].values
O3meanPen=tabPen['O3meanPen'].values

tabStati=pd.read_csv('/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiStati.csv')
cStatoStati=tabStati['cStati'].values
cConteaStati=tabStati['cContea'].values
nSitStati=tabStati['nSit'].values
dateStati=tabStati['dateTot'].values
O3meanStati=tabStati['O3meanTot'].values



NY='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv'
MD='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiMD.csv'
CT='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiCT.csv'
VA='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiVA.csv'
Pen='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiPen.csv'
'''

p5stati='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/dati5Stati.csv'

def getRilevaz(path):

    #Funzione legge file e restituisce array di stazioni
    df=pd.read_csv(path)
    
    staz = np.array([Stazione.rilevazione( r['c5Stati'], r['cContea5'], r['nSit5'],r['date5Stati'],r['O3mean5Stati'] ) for i, r in df.iterrows() ])

    return staz


'''
stazNy = getStazione(NY)
stazVA  =  getStazione(VA)
stazCT =  getStazione(CT)
stazPen =  getStazione(Pen)
stazMD =  getStazione(MD)

print(stazNY)

hits = np.concatenate( (hitsM0, hitsM1, hitsM2, hitsM3) )
'''

ril5Stati=getRilevaz(p5stati)
#np.sort(hits, kind='mergesort' )
#np.sort(stazNY, kind='mergesort')


ril5Stati.sort(kind='mergesort')
#print(ril5Stati)

    
for h in ril5Stati:
    print(h.cStato, h.cContea, h.cStaz, h.data, h.mean)
print('Numero totale di rilevazioni:', ril5Stati.size)

#ardata=np.array([h.data for h in ril5Stati])
#armean=np.array([h.mean for h in ril5Stati])

#grafico andamento O3 al variare del tempo per tutte le stazioni 
#plt.title('Array medie in funzione del tempo')
#plt.plot(ardata , armean, marker='o' ,color='midnightblue')
#plt.show()

def getStazioni(arRil):
  '''  
    Funzione che crea un array di Stazione.stazioni a partire da un array ordinato di Stazione.rilevaz (arrRil)
    
    Due Stazioni consecutive, staz1 e staz2, sono raggruppati nello stesso evento (Event) se:
       h.cStaz==j.cStaz
 or h.cStato!= codePrecStato
   '''

  stazioni = np.empty(0)
  codePrecStaz = arRil[0].cStaz
  codePrecStato = arRil[0].cStato
  stazioni=np.append(stazioni,Stazione.stazione())
  for h in arRil:
      if (h.cStaz != codePrecStaz) :
          stazioni = np.append( stazioni, Stazione.stazione() )

      codePrecStaz = h.cStaz
      codePrecStato = h.cStato   
      stazioni[-1].addril(h)    
  return stazioni

'''
  stazioni= np.empty(0)
  for i in range(arRil.size):
      z=1
      for z in range((arRil.size -1)):
          if(arRil[i].cStaz!=arRil[z].cStaz):
              stazioni[-1].addril(z)
          else:
              stazioni=np.append(stazioni,Stazione.stazione())
                '''
i=0
cPrStaz=ril5Stati[0].cStaz
for h in ril5Stati:
    if(h.cStaz != cPrStaz):
        i=i+1
        cPrStaz=h.cStaz

print(i)

staz5Stati=getStazioni(ril5Stati)
print('Numero totale di stazioni: ', staz5Stati.size)  
#print(staz5Stati)
for hh in staz5Stati[25].arrRil:
    print(hh.cStato, hh.cContea , hh.cStaz, hh.data ,hh.mean ,staz5Stati[0])


'''
#trasformata di fourier e freq

cofft=fft.fft(armean)
sNyqu=0.5
cofFreq=sNyqu*fft.fftfreq(len(cofft),d=1)

#grafico spettro in funz freq

plt.plot(cofFreq[:int(cofft.size/2)],np.absolute(cofft[:int(cofft.size/2)])**2,'o', markersize=3)
plt.xscale('log')
plt.yscale('log')
plt.show()

#grafico spettro in funz di periodo

plt.plot(1/cofFreq[:int(cofft.size/2)],np.absolute(cofft[0:int(cofft.size/2)])**2,'o' ,markersize=3)
plt.xscale('log')
plt.yscale('log')
plt.show()
'''

#trasformo string in int
#d=dateNY[0]
#s=int(d[3])
#print(d,s,s+100)


