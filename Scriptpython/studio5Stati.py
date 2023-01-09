import numpy as np
import pandas as pd
import Stazione


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


#staz5Stati.sort(kind='mergesort')
print(ril5Stati)
print('Numero totale di rilevazioni:', ril5Stati.size)
    
#for h in ril5Stati:
#    print(h.cStato, h.cContea, h.cStaz, h.data, h.mean)


def getStazioni(arRil):
    """
    Funzione che crea un array di Stazione.stazioni a partire da un array ordinato di Stazione.rilevaz (arrRil)
    
    Due Stazioni consecutive, staz1 e staz2, sono raggruppati nello stesso evento (Event) se:
       h.cStaz==j.cStaz
    """

    stazioni = np.empty(0)
    for h in arRil:
        codePrec = arRil[0].cStaz
        if h.cStaz==arRil[0].cStaz :
            stazioni = np.append( stazioni, Stazione.stazione() )
            
        stazioni[-1].addril(h)
        codePrec = h.cStaz

    return stazioni


staz5Stati=getStazioni(ril5Stati)
print('Numero totale di stazioni: ', staz5Stati.size)



    
#trasformo string in int
#d=dateNY[0]
#s=int(d[3])
#print(d,s,s+100)
