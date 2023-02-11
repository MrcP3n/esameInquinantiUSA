import numpy as np
import pandas as pd
import Classi
import matplotlib.pyplot as plt
from scipy import constants , fft
import Funzioni as f



p5stati='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/dati5Stati.csv'

ril5Stati=f.getRilevaz5(p5stati)

ril5Stati.sort(kind='mergesort')

'''
for h in ril5Stati:
    print(h.cStato, h.cContea, h.cStaz, h.data, h.mean)
'''
print('Numero totale di rilevazioni:', ril5Stati.size)

staz5Stati=f.getStazioni(ril5Stati)
staz5Stati.sort(kind='mergesort')

print('--------------------------------')
print('Numero totale di stazioni: ', staz5Stati.size)
'''
for hh in staz5Stati[3].arrRil:
    print(hh.cStato, hh.cContea , hh.cStaz, hh.data ,hh.mean)
'''    

for i in range(35):
    print('-----Stazione{:}------'.format(i))
    print('nRilevazioni', staz5Stati[i].nril)
print('Numero totale di stazioni: ', staz5Stati.size)  


'''Estrazione array'''

CT2Date ,CT2Mean  = f.takeArr(staz5Stati[2])
CT3Date ,CT3Mean = f.takeArr(staz5Stati[3])
CT1Date ,CT1Mean = f.takeArr(staz5Stati[1])
NY8Date , NY8Mean =f.takeArr(staz5Stati[8])
NY9Date , NY9Mean =f.takeArr(staz5Stati[9])
VA29Date , VA29Mean =f.takeArr(staz5Stati[29])
VA31Date , VA31Mean =f.takeArr(staz5Stati[31])
VA33Date , VA33Mean =f.takeArr(staz5Stati[33])
VA34Date , VA34Mean =f.takeArr(staz5Stati[34])
PA13Date , PA13Mean =f.takeArr(staz5Stati[13])
PA15Date , PA15Mean =f.takeArr(staz5Stati[15])
PA20Date , PA20Mean =f.takeArr(staz5Stati[20])
PA24Date , PA24Mean =f.takeArr(staz5Stati[24])
MD5Date , MD5Mean =f.takeArr(staz5Stati[5])

'''Andamenti temporali'''
#Decidi se mettere CT1,CT2 ecc.. o lasciare così
if False:
    title='Confronto 2 stazioni Connecticut'
    f.graphInTime2(CT2Date,CT2Mean,CT3Date,CT3Mean,title,'red')
    title='Confronto 2 stazioni New York'
    f.graphInTime2(NY8Date,NY8Mean,NY9Date,NY9Mean,title,'cyan')
    title='Confronto 2 stazioni della Virginia '
    f.graphInTime2(VA29Date,VA29Mean,VA33Date,VA33Mean,title,'orchid')
    title='Confronto altre 2 stazioni della Virginia '
    f.graphInTime2(VA29Date,VA29Mean,VA34Date,VA34Mean,title,'orchid')
    title='Confronto 2 stazioni Pennsylvania'
    f.graphInTime2(PA13Date,PA13Mean,PA15Date,PA15Mean ,title,'green')
    title='Confronto stazione Pennsylvania con stazione New york'
    f.graphInTime2(PA20Date,PA20Mean,NY8Date,NY8Mean,title,'darkviolet')
    title='Confronto altre stazioni Pennsylvania con altre della Virginia'
    f.graphInTime2(PA24Date,PA24Mean,VA31Date,VA31Mean,title,'midnightblue')
    title='Confronto stazione Maryland con stazione New york'
    f.graphInTime2(MD5Date,MD5Mean,NY9Date,NY9Mean,title,'limegreen')
    title='Confronto 5 Stazioni degli stati contigui'
    f.graphInTime5(CT1Date,CT1Mean,MD5Date,MD5Mean,NY9Date ,NY9Mean,PA20Date,PA20Mean,VA31Date,VA31Mean,title)


'''CORRELAZIONE'''


'''Trasformate di fourier e estrazione di frequenze e max'''
#trasformata di fourier e freq 2 3 5 8 9 13 15 20 24 29 31 33 34
coffCT1 , cofFreqCT1 , maxCT1 = f.trFour_freq(CT1Mean)
coffCT2 , cofFreqCT2 , maxCT2 = f.trFour_freq(CT2Mean)
coffCT3 , cofFreqCT3 , maxCT3 = f.trFour_freq(CT3Mean)
coffMD5 , cofFreqMD5 , maxMD5 = f.trFour_freq(MD5Mean)
coffNY8 , cofFreqNY8 , maxNY8 = f.trFour_freq(NY8Mean)
coffNY9 , cofFreqNY9 , maxNY9 = f.trFour_freq(NY9Mean)
coffPA13 , cofFreqPA13 , maxPA13 = f.trFour_freq(PA13Mean)
coffPA15 , cofFreqPA15 , maxPA15 = f.trFour_freq(PA15Mean)
coffPA20 , cofFreqPA20 , maxPA20 = f.trFour_freq(PA20Mean)
coffPA24 , cofFreqPA24 , maxPA24 = f.trFour_freq(PA24Mean)
coffVA29 , cofFreqVA29 , maxVA29 = f.trFour_freq(VA29Mean)
coffVA31 , cofFreqVA31 , maxVA31 = f.trFour_freq(VA31Mean)
coffVA33 , cofFreqVA33 , maxVA33 = f.trFour_freq(VA33Mean)
coffVA34 , cofFreqVA34 , maxVA34 = f.trFour_freq(VA34Mean)

modcofCT1 = np.absolute(coffCT1)**2
modcofMD5 = np.absolute(coffMD5)**2
modcofNY9 = np.absolute(coffNY9)**2
modcofPA20 = np.absolute(coffPA20)**2
modcofVA31 = np.absolute(coffVA31)**2

'''PERIODICITÀ'''
if False:
    print('Stazione CT: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(modcofCT1[maxCT1], cofFreqCT1[maxCT1], 1/cofFreqCT1[maxCT1]))
    print('Stazione MD: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(modcofMD5[maxMD5], cofFreqMD5[maxMD5], 1/cofFreqMD5[maxMD5]))
    print('Stazione NY: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(modcofNY9[maxNY9], cofFreqNY9[maxNY9], 1/cofFreqNY9[maxNY9]))
    print('Stazione PA: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(modcofPA20[maxPA20], cofFreqPA20[maxPA20], 1/cofFreqPA20[maxPA20]))
    print('Stazione VA: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(modcofVA31[maxVA31], cofFreqVA31[maxVA31], 1/cofFreqVA31[maxVA31]))

if False:
    title='Spettro di potenza delle stazioni più rilevanti nei 5 stati contigui in funzione della frequenza'
    f.graphSpettri5(coffCT1 , cofFreqCT1,coffMD5 , cofFreqMD5,coffNY9 , cofFreqNY9,coffPA20 , cofFreqPA20, coffVA31 , cofFreqVA31,title)
    title='Spettro di potenza delle stazioni più rilevanti nei 5 stati contigui in funzione del periodo'
    f.graphSpettri5Per(coffCT1 , cofFreqCT1,coffMD5 , cofFreqMD5,coffNY9 , cofFreqNY9,coffPA20 , cofFreqPA20, coffVA31 , cofFreqVA31,title)


'''FILTRI'''
#sistema valori di soglia
filCT1=f.trInv(coffCT1,0.3,CT1Mean)
filCT2=f.trInv(coffCT2,0.3,CT2Mean)
filCT3=f.trInv(coffCT3,0.3,CT3Mean)
filNY8=f.trInv(coffNY8,0.45,NY8Mean)#0.5 sinu
filNY9=f.trInv(coffNY9,0.45,NY9Mean)
filPA13=f.trInv(coffPA13,0.25,PA13Mean)
filPA15=f.trInv(coffPA15,0.2,PA15Mean)
filPA20=f.trInv(coffPA20,0.3,PA20Mean)
filPA24=f.trInv(coffPA24,0.25,PA24Mean)
filVA29=f.trInv(coffVA29,0.1,VA29Mean)#togli una di PA
filVA31=f.trInv(coffVA31,0.2,VA31Mean)
filVA33=f.trInv(coffVA33,0.1,VA33Mean)#togli una di VA
filVA34=f.trInv(coffVA34,0.15,VA34Mean)
filMD5=f.trInv(coffMD5,0.3,MD5Mean)

'''Dati originali rispetto a filtrati'''

if False:
    title='Grafico dati originali e filtrati di CT1,CT2,CT3 e NY8'
    f.graphFil(CT1Date,CT1Mean,filCT1,CT2Date,CT2Mean,filCT2,CT3Date,CT3Mean,filCT3,NY8Date,NY8Mean,filNY8,title)
    
    title='Grafico dati originali e filtrati di NY9,PA13,PA15 e PA24'
    f.graphFil(NY9Date,NY9Mean,filNY9,PA13Date,PA13Mean,filPA13,PA15Date,PA15Mean,filPA15,PA24Date,PA24Mean,filPA24,title)
    title='Grafico dati originali e filtrati di VA29,VA31,VA34 e MD5'
    f.graphFil(VA29Date,VA29Mean,filVA29,VA31Date,VA31Mean,filVA31,VA34Date,VA34Mean,filVA34,MD5Date,MD5Mean,filMD5,title)
    

'''RUMORI'''

if False:
    title='Grafico andamento della differenza tra dati originali e filtrati delle stazioni CT1 CT2 CT3 e NY8'
    f.graphRumori(CT1Date,CT1Mean,filCT1,CT2Date,CT2Mean,filCT2,CT3Date,CT3Mean,filCT3,NY8Date,NY8Mean,filNY8,title)
    title='Grafico andamento della differenza tra dati originali e filtrati delle stazioni  NY9 PA13,PA15 e PA24'
    f.graphRumori(NY9Date,NY9Mean,filNY9,PA13Date,PA13Mean,filPA13,PA15Date,PA15Mean,filPA15,PA24Date,PA24Mean,filPA24,title)
    title='Grafico andamento della differenza tra dati originali e filtrati delle stazioni VA29,VA31,VA34 e MD5'
    f.graphRumori(VA29Date,VA29Mean,filVA29,VA31Date,VA31Mean,filVA31,VA34Date,VA34Mean,filVA34,MD5Date,MD5Mean,filMD5,title)
    
    '''Individuazione tipo di rumore '''
    
    cofdiffCT1,freqdiffCT1,maxdiffCT1=f.trFour_freq(CT1Mean-filCT1)
    cofdiffCT2,freqdiffCT2,maxdiffCT2=f.trFour_freq(CT2Mean-filCT2)
    cofdiffNY8,freqdiffNY8,maxdiffNY8=f.trFour_freq(NY8Mean-filNY8)
    cofdiffNY9,freqdiffNY9,maxdiffNY9=f.trFour_freq(NY9Mean-filNY9)
    cofdiffPA13,freqdiffPA13,maxdiffPA13=f.trFour_freq(PA13Mean-filPA13)
    cofdiffPA15,freqdiffPA15,maxdiffPA15=f.trFour_freq(PA15Mean-filPA15)
    cofdiffPA24,freqdiffPA24,maxdiffPA24=f.trFour_freq(PA24Mean-filPA24)
    cofdiffVA29,freqdiffVA29,maxdiffVA29=f.trFour_freq(VA29Mean-filVA29)
    cofdiffVA31,freqdiffVA31,maxdiffVA31=f.trFour_freq(VA31Mean-filVA31)
    cofdiffMD5,freqdiffMD5,maxdiffMD5=f.trFour_freq(MD5Mean-filMD5)
    title='Spettro rumori CT1 CT2 NY8 NY9 e PA13'
    f.graphSpettri5(cofdiffCT1,freqdiffCT1,cofdiffCT2,freqdiffCT2,cofdiffNY8,freqdiffNY8,cofdiffNY9,freqdiffNY9,cofdiffPA13,freqdiffPA13,title)
    title='Spettro rumori PA15 PA24 VA29 VA31 e MD5'
    f.graphSpettri5(cofdiffPA15,freqdiffPA15,cofdiffPA24,freqdiffPA24,cofdiffVA29,freqdiffVA29,cofdiffVA31,freqdiffVA31,cofdiffMD5,freqdiffMD5,title)
    
'''In analogia alla luce bianca che è formata dalla sovrapposizione di onde elettromagnetiche di tutte le frequenze visibili. Rumore bianco ha spettro piatto di conseguenza sembrano tutti rumori bianchi '''
