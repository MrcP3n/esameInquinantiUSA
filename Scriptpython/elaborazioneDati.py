import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#prendo dati


tab=pd.read_csv('/home/marco-ubu/esameInquinantiUSA/DatiProgetto/pollution_us_2008_2010.csv')


codStato=tab['State Code'].values
codContea=tab['County Code'].values
numSito=tab['Site Num'].values
date=tab['Date Local'].values
O3mean=tab['O3 Mean'].values  #parti per milione
#=tab[''].values
#=tab[''].values
#=tab[''].values
#=tab[''].values


#fai funzione per separare stati, giorni


#preparo gli array anche per tutti gli stati

codeStati=np.empty(0)
codeContee=np.empty(0)
numSiti=np.empty(0)
dateTot=np.empty(0)
O3meanTot=np.empty(0)


for i in range(len(codStato)-1):
    if(O3mean[i] != O3mean[i+1]):
        codeStati=np.append(codeStati,codStato[i])
        codeContee=np.append(codeContee,codContea[i])
        numSiti=np.append(numSiti,numSito[i])
        dateTot=np.append(dateTot,date[i])
        O3meanTot=np.append(O3meanTot,O3mean[i])

print(codeStati,codeContee,numSiti, dateTot,O3meanTot)
print(len(codeStati),len(codeContee),len(numSiti),len(O3meanTot),len( dateTot))

#preparo gli array anche per i 5 Stati contigui


code5Stati=np.empty(0)
codeContee5=np.empty(0)
numSiti5=np.empty(0)
date5Stati=np.empty(0)
O3mean5Stati=np.empty(0)


for i in range(len(codStato)-1):
    if(codStato[i]==51 or codStato[i]==36 or codStato[i]==9 or codStato[i]==24 or codStato[i]==42):
        if(O3mean[i] != O3mean[i+1]):
            code5Stati=np.append(code5Stati,codStato[i])
            codeContee5=np.append(codeContee5,codContea[i])
            numSiti5=np.append(numSiti5,numSito[i])
            date5Stati=np.append(date5Stati,date[i])
            O3mean5Stati=np.append(O3mean5Stati,O3mean[i])

print(code5Stati,codeContee5,numSiti5, date5Stati,O3mean5Stati)
print(len(code5Stati),len(codeContee5),len(numSiti5),len(O3mean5Stati),len( date5Stati))

#definisco funzione per creare dataframe 


def creaDataFrame(arr1,arr2,arr3,arr4,arr5,Names):
    nomiColonne = {Names[0]:arr1,Names[1]:arr2,Names[2]:arr3,Names[3]:arr4,Names[4]:arr5}
    mid_term_marks_df = pd.DataFrame(nomiColonne)
    return mid_term_marks_df

#creo dataframe e scrivo un file csv per Stati

statiColumns=(["cStati","cContea","nSit","dateTot","O3meanTot"])
dfstati=creaDataFrame(codeStati,codeContee,numSiti,dateTot,O3meanTot,statiColumns)
print(dfstati)

dfstati.to_csv("datiStati.csv")


#creo dataframe e scrivo un file csv per 5 Stati contigui

statiColumns=(["c5Stati","cContea5","nSit5","date5Stati","O3mean5Stati"])
df5stati=creaDataFrame(code5Stati,codeContee5,numSiti5,date5Stati,O3mean5Stati,statiColumns)
print(df5stati)

df5stati.to_csv("dati5Stati.csv")


'''
NYcolumns=(["cStatoNY","cConteaNY","nSitNY","dateNY","O3meanNY"])
dfNY=creaDataFrame(cStatoNY,cConteaNY,nSitNY,dateNY,O3meanNY,NYcolumns)
print(dfNY)

dfNY.to_csv("datiNY.csv")


#creo dataframe e scrivo un file csv per VA 

VAcolumns=(["cStatoVA","cConteaVA","nSitVA","dateVA","O3meanVA"])
dfVA=creaDataFrame(cStatoVA,cConteaVA,nSitVA,dateVA,O3meanVA,VAcolumns)
print(dfVA)

dfVA.to_csv("datiVA.csv")

#creo dataframe e scrivo un file csv per Pen 

Pencolumns=(["cStatoPen","cConteaPen","nSitPen","datePen","O3meanPen"])
dfPen=creaDataFrame(cStatoPen,cConteaPen,nSitPen,datePen,O3meanPen,Pencolumns)
print(dfPen)

dfPen.to_csv("datiPen.csv")

#creo dataframe e scrivo un file csv per CT

CTcolumns=(["cStatoCT","cConteaCT","nSitCT","dateCT","O3meanCT"])
dfCT=creaDataFrame(cStatoCT,cConteaCT,nSitCT,dateCT,O3meanCT,CTcolumns)
print(dfCT)

dfCT.to_csv("datiCT.csv")

#creo dataframe e scrivo un file csv per MD

MDcolumns=(["cStatoMD","cConteaMD","nSitMD","dateMD","O3meanMD"])
dfMD=creaDataFrame(cStatoMD,cConteaMD,nSitMD,dateMD,O3meanMD,MDcolumns)
print(dfMD)

dfMD.to_csv("datiMD.csv")
'''
    
'''
# 9 connecticut ; 24 Maryland; 36 New york ; 42 pennsylvania ; 51 Virginia

cStatoNY=np.empty(0)
cConteaNY=np.empty(0)
nSitNY=np.empty(0)
O3meanNY=np.empty(0)
dateNY=np.empty(0)
i=1

#Separo i dati di new york e prendo un valore di media al giorno

for i in range(len(codStato)):
    if(codStato[i]==36):
        if(O3mean[i]!=O3mean[i+1]):
            cStatoNY=np.append(cStatoNY,codStato[i])
            cConteaNY=np.append(cConteaNY,codContea[i])
            nSitNY=np.append(nSitNY,numSito[i])
            dateNY=np.append(dateNY,date[i])
            O3meanNY=np.append(O3meanNY,O3mean[i])
        
        
print(cStatoNY,cConteaNY,nSitNY, dateNY,O3meanNY)
print(len(cStatoNY),len(cConteaNY),len(nSitNY), len(dateNY),len(O3meanNY))

#Separo dati Pennsylvania e valore media

cStatoPen=np.empty(0)
cConteaPen=np.empty(0)
nSitPen=np.empty(0)
datePen=np.empty(0)
O3meanPen=np.empty(0)


for i in range(len(codStato)):
    if(codStato[i]==42):
        if(O3mean[i]!=O3mean[i+1]):
            cStatoPen=np.append(cStatoPen,codStato[i])
            cConteaPen=np.append(cConteaPen,codContea[i])
            nSitPen=np.append(nSitPen,numSito[i])
            datePen=np.append(datePen,date[i])
            O3meanPen=np.append(O3meanPen,O3mean[i])


print(cStatoPen,cConteaPen,nSitPen, datePen,O3meanPen)
print(len(cStatoPen),len(cConteaPen),len(nSitPen),len( datePen),len(O3meanPen))

#Separo dati Connecticut e valore media

cStatoCT=np.empty(0)
cConteaCT=np.empty(0)
nSitCT=np.empty(0)
O3meanCT=np.empty(0)
dateCT=np.empty(0)

for i in range(len(codStato)):
    if(codStato[i]==9):
         if(O3mean[i]!=O3mean[i+1]):
             cStatoCT=np.append(cStatoCT,codStato[i])
             cConteaCT=np.append(cConteaCT,codContea[i])
             nSitCT=np.append(nSitCT,numSito[i])
             dateCT=np.append(dateCT,date[i])
             O3meanCT=np.append(O3meanCT,O3mean[i])


print(cStatoCT,cConteaCT,nSitCT, dateCT,O3meanCT)
print(len(cStatoCT),len(cConteaCT),len(nSitCT),len( dateCT),len(O3meanCT))


#Separo dati Maryland e valore media

cStatoMD=np.empty(0)
cConteaMD=np.empty(0)
nSitMD=np.empty(0)
O3meanMD=np.empty(0)
dateMD=np.empty(0)


for i in range(len(codStato)):
    if(codStato[i]==24):
         if(O3mean[i]!=O3mean[i+1]):
             cStatoMD=np.append(cStatoMD,codStato[i])
             cConteaMD=np.append(cConteaMD,codContea[i])
             nSitMD=np.append(nSitMD,numSito[i])
             dateMD=np.append(dateMD,date[i])
             O3meanMD=np.append(O3meanMD,O3mean[i])


print(cStatoMD,cConteaMD,nSitMD,dateMD,O3meanMD)
print(len(cStatoMD),len(cConteaMD),len(nSitMD), len(dateMD),len(O3meanMD))


#Separo dati Virginia e valore media

cStatoVA=np.empty(0)
cConteaVA=np.empty(0)
nSitVA=np.empty(0)
O3meanVA=np.empty(0)
dateVA=np.empty(0)

for i in range(len(codStato)):
    if(codStato[i]==51):
         if(O3mean[i]!=O3mean[i+1]):
             cStatoVA=np.append(cStatoVA,codStato[i])
             cConteaVA=np.append(cConteaVA,codContea[i])
             nSitVA=np.append(nSitVA,numSito[i])
             dateVA=np.append(dateVA,date[i])
             O3meanVA=np.append(O3meanVA,O3mean[i])


print(cStatoVA,cConteaVA,nSitVA,dateVA,O3meanVA)
print(len(cStatoVA),len(cConteaVA),len(nSitVA),len( dateVA),len(O3meanVA))

'''

'''def Scriviarr(arr1,arr2,arr3,arr4,arr5,path):
    j=1
    with open(path,'w',newline='') as file:
        writer=csv.writer(file)
        for j in range(len(arr1)):
            writer.writerow([arr1[j],arr2[j],arr3[j],arr4[j],arr5[j]])

    return True        
'''

'''


#file Stati

#/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv
Stati=Scriviarr(codeStati,codeContee,numSiti,dateTot,O3meanTot,'/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiStati.csv')
if(Stati==True):
    print('File Stati scritto')






#file NY

#/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv
NY=Scriviarr(cStatoNY,cConteaNY,nSitNY,dateNY,O3meanNY,'/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv')
if(NY==True):
    print('File NY scritto')

#file Pen

#/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv
Pen=Scriviarr(cStatoPen,cConteaPen,nSitPen,datePen,O3meanPen,'/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiPen.csv')
if(Pen==True):
    print('File Pen scritto')

    
#file CT

#/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv
CT=Scriviarr(cStatoCT,cConteaCT,nSitCT,dateCT,O3meanCT,'/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiCT.csv')
if(CT==True):
    print('File CT scritto')



#file VA

#/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv
VA=Scriviarr(cStatoVA,cConteaVA,nSitVA,dateVA,O3meanVA,'/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiVA.csv')
if(VA==True):
    print('File VA scritto')



#file MD

#/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv
MD=Scriviarr(cStatoMD,cConteaMD,nSitMD,dateMD,O3meanMD,'/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiMD.csv')
if(MD==True):
    print('File MD scritto')    
'''
