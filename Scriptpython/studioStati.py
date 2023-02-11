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
stati=f.getStati(rilStati)
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

#np.set_printoptions(threshold=sys.maxsize)
'''Creo array per ogni stato'''

meanO3AZ , dateAZ,arr  =f.meanDay(stati[0])
meanO3CA , dateCA,arr1  =f.meanDay(stati[2])
meanO3CA=np.append(meanO3CA,0.01672)
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
print('dateCA',' Lunghezza ',len(meanO3OR))
print('meanO3CA',' Lunghezza ',len(meanO3PA))
print( 'arr1'  ,' Lunghezza ',len(meanO3SC))
'''



'''Andamento Temporale'''
if False:
    #WEST COAST AND CENTER
    title='Andamenti Oregon, California, Arizona, Texas, Oklahoma'
    f.graphInTime5(dateOR,meanO3OR,dateCA,meanO3CA,dateAZ,meanO3AZ,dateTX,meanO3TX,dateOK,meanO3OK,title)
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
    f.graphSpettri5(coffOR , cofFreqOR,coffCA , cofFreqCA,coffAZ , cofFreqAZ,coffTX , cofFreqTX,coffOK , cofFreqOK,title)
    #EAST COAST
    title='Spettri Maine, Maryland, Massachusetts, Pennsylvania, New York'
    f.graphSpettri5(coffME , cofFreqME,coffMD , cofFreqMD,coffMA , cofFreqMA,coffPA , cofFreqPA,coffNY , cofFreqNY,title)
    #EAST COAST E CENTER
    title='Spettri Florida, Illinois, District of columbia, North Dakota, North Carolina'
    f.graphSpettri5(coffFL , cofFreqFL,coffIL , cofFreqIL,coffDC , cofFreqDC,coffND , cofFreqND,coffNC , cofFreqNC,title)
    #EAST COAST E CENTER
    title='Spettri Connecticut, New York, North Carolina, South Carolina, Florida'
    f.graphSpettri5(coffCT , cofFreqCT,coffNY , cofFreqNY,coffNC , cofFreqNC,coffSC , cofFreqSC,coffFL , cofFreqFL,title)
    #GENERALE
    title='Spettro Oregon, Pennsylvania, North Dakota, South Carolina, Illinois'#Cali al posto di illi
    f.graphSpettri5(coffOR , cofFreqOR,coffPA , cofFreqPA,coffND , cofFreqND,coffSC , cofFreqSC,coffIL , cofFreqIL,title)   


'''Periodicità'''
if True:
    print('Stato AZ: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffAZ[maxAZ])**2, cofFreqAZ[maxAZ], 1/cofFreqAZ[maxAZ]))
    print('Stato CA: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffCA[maxCA])**2, cofFreqCA[maxCA], 1/cofFreqCA[maxCA]))
    print('Stato CT: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffCT[maxCT])**2, cofFreqCT[maxCT], 1/cofFreqCT[maxCT]))
    print('Stato DC: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffDC[maxDC])**2, cofFreqDC[maxDC], 1/cofFreqDC[maxDC]))
    print('Stato FL: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffFL[maxFL])**2, cofFreqFL[maxFL], 1/cofFreqFL[maxFL]))
    print('Stato IL: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffIL[maxIL])**2, cofFreqIL[maxIL], 1/cofFreqIL[maxIL]))
    print('Stato ME: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffME[maxME])**2, cofFreqME[maxME], 1/cofFreqME[maxME]))
    print('Stato MD: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffMD[maxMD])**2, cofFreqMD[maxMD], 1/cofFreqMD[maxMD]))
    print('Stato MA: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffMA[maxMA])**2, cofFreqMA[maxMA], 1/cofFreqMA[maxMA]))
    print('Stato NY: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffNY[maxNY])**2, cofFreqNY[maxNY], 1/cofFreqNY[maxNY]))
    print('Stato NC: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffNC[maxNC])**2, cofFreqNC[maxNC], 1/cofFreqNC[maxNC]))
    print('Stato ND: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffND[maxND])**2, cofFreqND[maxND], 1/cofFreqND[maxND]))
    print('Stato OK: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffOK[maxOK])**2, cofFreqOK[maxOK], 1/cofFreqOK[maxOK]))
    print('Stato OR: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffOR[maxOR])**2, cofFreqOR[maxOR], 1/cofFreqOR[maxOR]))
    print('Stato PA: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffPA[maxPA])**2, cofFreqPA[maxPA], 1/cofFreqPA[maxPA]))
    print('Stato SC: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffSC[maxSC])**2, cofFreqSC[maxSC], 1/cofFreqSC[maxSC]))
    print('Stato TX: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(np.absolute(coffTX[maxTX])**2, cofFreqTX[maxTX], 1/cofFreqTX[maxTX]))

if False:
    #EAST COAST
    title='Spettro di potenza dei 5 stati nella East Coast in funzione del periodo'
    f.graphSpettri5Per(coffME , cofFreqME,coffMD , cofFreqMD,coffMA , cofFreqMA,coffPA , cofFreqPA,coffNY , cofFreqNY,title)
    #WEST COAST E CENTER
    title='Spettro di potenza dei 5 stati nella West Coast  Centro e in funzione del periodo'
    f.graphSpettri5Per(coffOR , cofFreqOR,coffCA , cofFreqCA,coffAZ , cofFreqAZ,coffTX , cofFreqTX,coffOK , cofFreqOK,title)
    #TUTTI SPARSI
    title='Spettro di potenza dei 5 stati in zone differenti in funzione del periodo'
    f.graphSpettri5Per(coffOR , cofFreqOR,coffPA , cofFreqPA,coffND , cofFreqND,coffSC , cofFreqSC,coffIL , cofFreqIL,title)
     #EAST COAST E CENTER
    title='Spettri di potenza di 5 stati nella East Coast e al centro in funzionde del periodo'
    f.graphSpettri5(coffFL , cofFreqFL,coffIL , cofFreqIL,coffDC , cofFreqDC,coffND , cofFreqND,coffNC , cofFreqNC,title)
    #EAST COAST E CENTER
    title='Spettri di potenza di 5 stati nella East Coast e al centro in funzionde del periodo'
    f.graphSpettri5(coffCT , cofFreqCT,coffNY , cofFreqNY,coffNC , cofFreqNC,coffSC , cofFreqSC,coffFL , cofFreqFL,title)

'''FILTRI '''

filAZ=f.trInv(coffAZ,0.3,meanO3AZ)
filCA=f.trInv(coffCA,0.7,meanO3CA)
filCT=f.trInv(coffCT,0.6,meanO3CT)
filDC=f.trInv(coffDC,0.4,meanO3DC)
filFL=f.trInv(coffFL,0.5,meanO3FL)
filIL=f.trInv(coffIL,0.4,meanO3IL)
filME=f.trInv(coffME,0.5,meanO3ME)
filMD=f.trInv(coffMD,1,meanO3MD)
filMA=f.trInv(coffMA,1,meanO3MA)
filNY=f.trInv(coffNY,0.4,meanO3NY)
filNC=f.trInv(coffNC,1,meanO3NC)
filND=f.trInv(coffND,1,meanO3ND)
filOK=f.trInv(coffOK,0.5,meanO3OK)
filOR=f.trInv(coffOR,1,meanO3OR)
filPA=f.trInv(coffPA,1,meanO3PA)
filTX=f.trInv(coffTX,0.4,meanO3TX)


'''Dati originali rispetto a filtrati'''
if False:
    title='Grafico dati e dati filtrati a confronto per AZ CA CT e DC'
    f.graphFil(dateAZ,meanO3AZ,filAZ,dateCA,meanO3CA,filCA,dateCT,meanO3CT,filCT,dateDC,meanO3DC,filDC,title)
    
    title='Grafico dati e dati filtrati a confronto per FL IL ME e MD'
    f.graphFil(dateFL,meanO3FL,filFL,dateIL,meanO3IL,filIL,dateME,meanO3ME,filME,dateMD,meanO3MD,filMD,title)
    title='Grafico dati e dati filtrati a confronto per MA NY NC e ND'
    f.graphFil(dateMA,meanO3MA,filMA,dateNY,meanO3NY,filNY,dateNC,meanO3NC,filNC,dateND,meanO3ND,filND,title)
    title='Grafico dati e dati filtrati a confronto per OK OR PA e TX'
    f.graphFil(dateOK,meanO3OK,filOK,dateOR,meanO3OR,filOR,datePA,meanO3PA,filPA,dateTX,meanO3TX,filTX,title)
    
'''RUMORI'''
if False:
    title='Grafico andamento della differenza tra dati originali e filtrati degli stati AZ CA CT e DC'
    f.graphRumori(dateAZ,meanO3AZ,filAZ,dateCA,meanO3CA,filCA,dateCT,meanO3CT,filCT,dateDC,meanO3DC,filDC,title)
    title='Grafico andamento della differenza tra dati originali e filtrati degli stati FL IL ME e MD'
    f.graphRumori(dateFL,meanO3FL,filFL,dateIL,meanO3IL,filIL,dateME,meanO3ME,filME,dateMD,meanO3MD,filMD,title)
    title='Grafico andamento della differenza tra dati originali e filtrati degli stati MA NY NC e ND'
    f.graphRumori(dateMA,meanO3MA,filMA,dateNY,meanO3NY,filNY,dateNC,meanO3NC,filNC,dateND,meanO3ND,filND,title)
    title='Grafico andamento della differenza tra dati originali e filtrati degli stati OK OR PA e TX'
    f.graphRumori(dateOK,meanO3OK,filOK,dateOR,meanO3OR,filOR,datePA,meanO3PA,filPA,dateTX,meanO3TX,filTX,title)



'''Che tipo di rumore è'''

if False:    
    cofdiffAZ,freqdiffAZ,maxdiffAZ=f.trFour_freq(meanO3AZ-filAZ)
    cofdiffCA,freqdiffCA,maxdiffCA=f.trFour_freq(meanO3CA-filCA)
    cofdiffCT,freqdiffCT,maxdiffCT=f.trFour_freq(meanO3CT-filCT)
    cofdiffDC,freqdiffDC,maxdiffDC=f.trFour_freq(meanO3AZ-filAZ)
    cofdiffFL,freqdiffFL,maxdiffFL=f.trFour_freq(meanO3AZ-filAZ)
    cofdiffME,freqdiffME,maxdiffME=f.trFour_freq(meanO3ME-filME)
    cofdiffMD,freqdiffMD,maxdiffMD=f.trFour_freq(meanO3MD-filMD)
    cofdiffMA,freqdiffMA,maxdiffMA=f.trFour_freq(meanO3MA-filMA)
    cofdiffNY,freqdiffNY,maxdiffNY=f.trFour_freq(meanO3NY-filNY)
    cofdiffND,freqdiffND,maxdiffND=f.trFour_freq(meanO3ND-filND)
    cofdiffNC,freqdiffNC,maxdiffNC=f.trFour_freq(meanO3NC-filNC)
    cofdiffOK,freqdiffOK,maxdiffOK=f.trFour_freq(meanO3OK-filOK)
    cofdiffOR,freqdiffOR,maxdiffOR=f.trFour_freq(meanO3OR-filOR)
    cofdiffPA,freqdiffPA,maxdiffPA=f.trFour_freq(meanO3PA-filPA)
    cofdiffTX,freqdiffTX,maxdiffTX=f.trFour_freq(meanO3TX-filTX)    
    title='Spettro rumori AZ CA CT DC e FL'
    f.graphSpettri5(cofdiffAZ,freqdiffAZ,cofdiffCA,freqdiffCA,cofdiffCT,freqdiffCT,cofdiffDC,freqdiffDC,cofdiffFL,freqdiffFL,title)
    title='Spettro rumori ME MD MA NY e ND'
    f.graphSpettri5(cofdiffME,freqdiffME,cofdiffMD,freqdiffMD,cofdiffMA,freqdiffMA,cofdiffNY,freqdiffNY,cofdiffND,freqdiffND,title)
    title='Spettro rumori NC OK OR PA e TX'
    f.graphSpettri5(cofdiffNC,freqdiffNC,cofdiffOK,freqdiffOK,cofdiffOR,freqdiffOR,cofdiffPA,freqdiffPA,cofdiffTX,freqdiffTX,title)

    '''Sembrano rumori bianchi spettro piatto tante frequenze piccole (Capisci bene texas probabilmente dovuto da filtro)'''
