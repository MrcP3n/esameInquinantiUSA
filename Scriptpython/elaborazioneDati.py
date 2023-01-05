import numpy as np
import pandas as pd
#prendo dati

tab=pd.read_csv('/home/marco-ubu/esameInquinantiUSA/DatiProgetto/pollution_us_2008_2010.csv')


codStato=tab['State Code'].values
codContea=tab['County Code'].values
numSito=tab['Site Num'].values
O3mean=tab['O3 Mean'].values  #parti per milione
#=tab[''].values
#=tab[''].values
#=tab[''].values
#=tab[''].values

#fai funzione per separare stati, giorni

    

# 9 connecticut ; 24 Maryland; 36 New york ; 42 pennsylvania ; 51 Virginia

cStatoNY=np.empty(0)
cConteaNY=np.empty(0)
nSitNY=np.empty(0)
O3meanNY=np.empty(0)
i=1

#Separo i dati di new york e prendo un valore di media al giorno

for i in range(len(codStato)):
    if(codStato[i]==36):
        if(O3mean[i]!=O3mean[i+1]):
            cStatoNY=np.append(cStatoNY,codStato[i])
            cConteaNY=np.append(cConteaNY,codContea[i])
            nSitNY=np.append(nSitNY,numSito[i])
            O3meanNY=np.append(O3meanNY,O3mean[i])
        
        
print(cStatoNY,cConteaNY,nSitNY,O3meanNY)
print(len(cStatoNY),len(cConteaNY),len(nSitNY),len(O3meanNY))

#Separo dati Pennsylvania e valore media

cStatoPen=np.empty(0)
cConteaPen=np.empty(0)
nSitPen=np.empty(0)
O3meanPen=np.empty(0)


for i in range(len(codStato)):
    if(codStato[i]==42):
        if(O3mean[i]!=O3mean[i+1]):
            cStatoPen=np.append(cStatoPen,codStato[i])
            cConteaPen=np.append(cConteaPen,codContea[i])
            nSitPen=np.append(nSitPen,numSito[i])
            O3meanPen=np.append(O3meanPen,O3mean[i])


print(cStatoPen,cConteaPen,nSitPen,O3meanPen)
print(len(cStatoPen),len(cConteaPen),len(nSitPen),len(O3meanPen))

#Separo dati Connecticut e valore media

cStatoCT=np.empty(0)
cConteaCT=np.empty(0)
nSitCT=np.empty(0)
O3meanCT=np.empty(0)


for i in range(len(codStato)):
    if(codStato[i]==9):
         if(O3mean[i]!=O3mean[i+1]):
             cStatoCT=np.append(cStatoCT,codStato[i])
             cConteaCT=np.append(cConteaCT,codContea[i])
             nSitCT=np.append(nSitCT,numSito[i])
             O3meanCT=np.append(O3meanCT,O3mean[i])


print(cStatoCT,cConteaCT,nSitCT,O3meanCT)
print(len(cStatoCT),len(cConteaCT),len(nSitCT),len(O3meanCT))


#Separo dati Maryland e valore media

cStatoMD=np.empty(0)
cConteaMD=np.empty(0)
nSitMD=np.empty(0)
O3meanMD=np.empty(0)


for i in range(len(codStato)):
    if(codStato[i]==24):
         if(O3mean[i]!=O3mean[i+1]):
             cStatoMD=np.append(cStatoMD,codStato[i])
             cConteaMD=np.append(cConteaMD,codContea[i])
             nSitMD=np.append(nSitMD,numSito[i])
             O3meanMD=np.append(O3meanMD,O3mean[i])


print(cStatoMD,cConteaMD,nSitMD,O3meanMD)
print(len(cStatoMD),len(cConteaMD),len(nSitMD),len(O3meanMD))


#Separo dati Virginia e valore media

cStatoVA=np.empty(0)
cConteaVA=np.empty(0)
nSitVA=np.empty(0)
O3meanVA=np.empty(0)


for i in range(len(codStato)):
    if(codStato[i]==51):
         if(O3mean[i]!=O3mean[i+1]):
             cStatoVA=np.append(cStatoVA,codStato[i])
             cConteaVA=np.append(cConteaVA,codContea[i])
             nSitVA=np.append(nSitVA,numSito[i])
             O3meanVA=np.append(O3meanVA,O3mean[i])


print(cStatoVA,cConteaVA,nSitVA,O3meanVA)
print(len(cStatoVA),len(cConteaVA),len(nSitVA),len(O3meanVA))


#preparo gli array anche per tutti gli stati

codeStati=np.empty(0)
codeContee=np.empty(0)
numSiti=np.empty(0)
O3meanTot=np.empty(0)


for i in range(len(codStato)-1):
    if(O3mean[i] != O3mean[i+1]):
        codeStati=np.append(codeStati,codStato[i])
        codeContee=np.append(codeContee,codContea[i])
        numSiti=np.append(numSiti,numSito[i])
        O3meanTot=np.append(O3meanTot,O3mean[i])

print(codeStati,codeContee,numSiti,O3meanTot)
print(len(codeStati),len(codeContee),len(numSiti),len(O3meanTot))










#Scrivo su un nuovo file csv
