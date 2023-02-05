import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#prendo dati
# 9 connecticut ; 24 Maryland; 36 New york ; 42 pennsylvania ; 51 Virginia

tab=pd.read_csv('/home/marco-ubu/esameInquinantiUSA/DatiProgetto/pollution_us_2008_2010.csv')


codStato=tab['State Code'].values
codContea=tab['County Code'].values
numSito=tab['Site Num'].values
date=tab['Date Local'].values
O3mean=tab['O3 Mean'].values  #parti per milione

#Elaboro gli array per tutti gli stati

#condizione O3mean[i] != O3mean[i+1] non va bene ci sono stazioni che hanno più medie giornaliere

codeStati=np.empty(0)
codeContee=np.empty(0)
numSiti=np.empty(0)
dateTot=np.empty(0)
O3meanTot=np.empty(0)


for i in range(len(codStato)-1):
    if(date[i] != date[i+1]):
        codeStati=np.append(codeStati,codStato[i])
        codeContee=np.append(codeContee,codContea[i])
        numSiti=np.append(numSiti,numSito[i])
        dateTot=np.append(dateTot,date[i])
        O3meanTot=np.append(O3meanTot,O3mean[i])

print(codeStati,codeContee,numSiti, dateTot,O3meanTot)
print(len(codeStati),len(codeContee),len(numSiti),len(O3meanTot),len( dateTot))

#Elaboro gli array anche per i 5 Stati contigui


code5Stati=np.empty(0)
codeContee5=np.empty(0)
numSiti5=np.empty(0)
date5Stati=np.empty(0)
O3mean5Stati=np.empty(0)


for i in range(len(codStato)-1):
    if(codStato[i]==51 or codStato[i]==36 or codStato[i]==9 or codStato[i]==24 or codStato[i]==42):
        if(date[i] != date[i+1]):
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

#print(O3mean[120],O3mean[119],O3mean[123])
'''
NYcolumns=(["cStatoNY","cConteaNY","nSitNY","dateNY","O3meanNY"])
dfNY=creaDataFrame(cStatoNY,cConteaNY,nSitNY,dateNY,O3meanNY,NYcolumns)
print(dfNY)

dfNY.to_csv("datiNY.csv")


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



'''
'''
def Scriviarr(arr1,arr2,arr3,arr4,arr5,path):
    j=1
    with open(path,'w',newline='') as file:
        writer=csv.writer(file)
        for j in range(len(arr1)):
            writer.writerow([arr1[j],arr2[j],arr3[j],arr4[j],arr5[j]])

    return True        
'''

'''
#file NY

#/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv
NY=Scriviarr(cStatoNY,cConteaNY,nSitNY,dateNY,O3meanNY,'/home/marco-ubu/esameInquinantiUSA/DatiProgetto/datiNY.csv')
if(NY==True):
    print('File NY scritto')



