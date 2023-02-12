from scipy import constants,fft
import numpy as np
import statistics
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import (MultipleLocator,AutoMinorLocator)
import Classi


'''------------------------------
   Funzioni per creare le classi
   ------------------------------'''

def getRilevaz5(path):
    #Funzione legge file e restituisce array di rilevazioni
    df=pd.read_csv(path)
    staz = np.array([Classi.rilevazione( r['c5Stati'], r['cContea5'], r['nSit5'],r['date5Stati'],r['O3mean5Stati'] ) for i, r in df.iterrows() ])

    return staz

def getRilevaz(path):
    #Funzione legge file e restituisce array di rilevazione
    df=pd.read_csv(path)
    staz = np.array([Classi.rilStat( r['cStati'], r['cContea'], r['nSit'],r['dateTot'],r['O3meanTot'] ) for i, r in df.iterrows() ])

    return staz


def getStazioni(arRil):
  '''  
    Funzione che crea un array di Classi.stazioni a partire da un array ordinato di Classi.rilevaz (arrRil)
    
    Due rilevazioni in stesso luogo, ril1 e ril2, sono raggruppati nella stessa stazione se:
       ril1.cStaz!=ril2.cStaz
inoltre per evitare che rilevazione con lo stesso codice di stazione ma presa in luoghi differenti finiscano insieme a causa della ripetizione di questi codici in luoghi differenti, si aggiunge la seguente condizione:
       codeTest!=codePrecStatoContea
  che controlla che le due rilevazioni abbiano la somma tra codice di contea e stato diverse  
   '''

  stazioni = np.empty(0)
  codePrecStaz = arRil[0].cStaz
  codePrecStatoContea = arRil[0].cStato+ arRil[0].cContea
  stazioni=np.append(stazioni,Classi.stazione())
  for h in arRil:
      codeTest=h.cContea+h.cStato
      if (h.cStaz != codePrecStaz ) :
          stazioni = np.append( stazioni, Classi.stazione() )
      elif(codeTest!=codePrecStatoContea):
          stazioni = np.append( stazioni, Classi.stazione() )
          
      codePrecStatoContea = codeTest    
      codePrecStaz = h.cStaz   
      stazioni[-1].addril(h)    
  return stazioni
  

def getStati(arRil):
    '''
     Funzione che crea un array di Classi.stati a partire da un array ordinato di Classi.rilevaz (arrRil)
    
    Due rilevazioni nello stesso stato, ril1 e ril2, sono raggruppati nello stesso stato se:
       ril1.cStato==ril2.cStato
inoltre per evitare che si crei a ogni cambio di anno un nuovo stato che corrisponderebbe ad uno già esistente introduco un array che avrà i codici degli stati esistenti, così facendo aggiungendo la condizione  
   h.cStati in arrCod
riesco ad aggiungere le rilevazioni nel giusto stato facendo scorrere gli indici dell ultimo array creato
    '''
    stati = np.empty(0)
    arrCod = np.empty(0)
    codePrecStato = arRil[0].cStato
    arrCod =np.append(arrCod,arRil[0].cStato)
    stati=np.append(stati,Classi.stato())
    for h in arRil:
        if(h.cStato!=codePrecStato):
            present=h.cStato in arrCod
            if(present==False):
                stati=np.append(stati,Classi.stato())
                arrCod=np.append(arrCod,h.cStato)
            else:
                for i in range(len(arrCod)):
                    if(h.cStato == arrCod[i]):
                        stati[i].addRil(h)
        elif(h.cStato==codePrecStato):
            present=h.cStato in arrCod
            if(present==True):
                for i in range(len(arrCod)):
                    if(h.cStato == arrCod[i]):
                        stati[i].addRil(h)
                        
            
        codePrecStato = h.cStato     
            
    return stati 

'''------------------------------
   Funzioni per creare array da 
   analizzare dalle classi
   ------------------------------'''

def takeArr(staz):
    average = np.empty(0)
    date = np.empty(0)
    for h in staz.arrRil:
        average = np.append(average ,h.mean)
        date = np.append(date ,h.data)
        
    return date , average 

def meanDay(stato):
    aMeanday=np.empty(0)
    aDate=np.empty(0)
    date=np.empty(0)
    rip=np.array([0])
    rip1=np.empty(0)
    j=0
    z=0
    arr=np.empty(0)
    aMediaDay=np.empty(0)
    '''
    Codice che prende un solo dato giornaliero facendo 
    la media dei dati nell' intervallo in cui si ripetono i dati, ricavo la
    ripetizione con rip e rip1 e li sfrutto in un altro ciclo per completare l' operazione
    '''
    for h in stato.arrRil:
        aMeanday = np.append(aMeanday ,h.mean)
        aDate = np.append(aDate ,h.data)
        
    for i in range(len(aDate)):
        if (i==(len(aDate)-1)):
            date=np.append(date,aDate[i])
            rip=np.append(rip,(i+1)-j)
            break
        if(aDate[i]!=aDate[i+1]):
            date=np.append(date,aDate[i])
            rip=np.append(rip,i-j)
            j=i

    for i in range(len(rip)-1):
        if(i>0):
            rip1=np.append(rip1,rip1[i-1]+rip[i])
        else:
            rip1=np.append(rip1,rip[i]+rip[i+1])
           
    for i in range(len(aMeanday)):
        arr=np.append(arr,aMeanday[i])
        if( i==rip1[z] ):
            m=statistics.mean(arr)
            aMediaDay=np.append(aMediaDay,m)
            arr=np.empty(0)
            if(z<(rip1.size)-1):
                z=z+1
        if(rip[z]==0):
            z=z+1
        if(i==(len(aMeanday)-1) and arr.size!=0 ):
            m=statistics.mean(arr)
            aMediaDay=np.append(aMediaDay,m)
            arr=np.empty(0)
                    
    return aMediaDay , date 


'''------------------------------
   Funzioni per l' analisi e la 
   creazione di grafici
   ------------------------------'''

def graphInTime2(arrx1,arry1,arrx2,arry2,title,cl):
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle(title)
    ax1.plot(arrx1, arry1, color=cl)
    ax2.plot(arrx2, arry2, color=cl)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Media Ozono [ppm]')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Media Ozono [ppm]')
    ax1.xaxis.set_major_locator(MultipleLocator(150))
    ax1.xaxis.set_minor_locator(MultipleLocator(30))
    ax2.xaxis.set_major_locator(MultipleLocator(150))
    ax2.xaxis.set_minor_locator(MultipleLocator(30))
    fig.set_figheight(8)
    fig.set_figwidth(12)
    plt.savefig(title)
    plt.show()
    return

def graphInTime5(arrx1,arry1,arrx2,arry2,arrx3,arry3, arrx4,arry4,arrx5,arry5,title):
    fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5)
    fig.suptitle(title)
    ax1.plot(arrx1, arry1, color='firebrick')
    ax2.plot(arrx2, arry2, color='limegreen')
    ax3.plot(arrx3, arry3, color='cyan')
    ax4.plot(arrx4, arry4, color='midnightblue')
    ax5.plot(arrx5, arry5, color='orchid')
    ax1.xaxis.set_major_locator(MultipleLocator(150))
    ax1.xaxis.set_minor_locator(MultipleLocator(30))
    ax2.xaxis.set_major_locator(MultipleLocator(150))
    ax2.xaxis.set_minor_locator(MultipleLocator(30))
    ax3.set_ylabel('Media Ozono [ppm]')
    ax3.xaxis.set_major_locator(MultipleLocator(150))
    ax3.xaxis.set_minor_locator(MultipleLocator(30))
    ax4.xaxis.set_major_locator(MultipleLocator(150))
    ax4.xaxis.set_minor_locator(MultipleLocator(30))
    ax5.set_xlabel('Date')
    ax5.xaxis.set_major_locator(MultipleLocator(150))
    ax5.xaxis.set_minor_locator(MultipleLocator(30))
    fig.set_figheight(7)
    fig.set_figwidth(10)
    plt.savefig(title)
    plt.show()
    
    return
    

def trFour_freq(arrMean):
    sNyqu=0.5
    cofft=fft.rfft(arrMean)
    cofFreq=sNyqu*fft.rfftfreq(len(arrMean) , d=1)
    mod = np.absolute(cofft)**2
    maxi = np.argmax(mod[1:cofft.size//2])+1
    return cofft , cofFreq , maxi


def graphSpettri5(acof1,afreq1,acof2,afreq2,acof3,afreq3,acof4,afreq4,acof5,afreq5,title):
    fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,sharex=True)
    fig.suptitle(title)
    ax1.plot(afreq1[1:int(acof1.size/2)],np.absolute(acof1[1:int(acof1.size/2)])**2,color='firebrick')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax2.plot(afreq2[:int(acof2.size/2)],np.absolute(acof2[:int(acof2.size/2)])**2,color='limegreen')
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax3.plot(afreq3[:int(acof3.size/2)],np.absolute(acof3[:int(acof3.size/2)])**2,color='cyan')
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    ax3.set_ylabel('$|c_{FFT}|^2$')
    ax4.plot(afreq4[:int(acof4.size/2)],np.absolute(acof4[:int(acof4.size/2)])**2,color='midnightblue')
    ax4.set_xscale('log')
    ax4.set_yscale('log')
    ax5.plot(afreq5[:int(acof5.size/2)],np.absolute(acof5[:int(acof5.size/2)])**2,color='orchid')
    ax5.set_xscale('log')
    ax5.set_yscale('log')
    ax5.set_xlabel('Frequenze [Hz]')
    fig.set_figheight(7)
    fig.set_figwidth(10)
    plt.show()

    return

def graphSpettri5Per(acof1,afreq1,acof2,afreq2,acof3,afreq3,acof4,afreq4,acof5,afreq5,title):
    fig, (ax1,ax2,ax3,ax4,ax5) = plt.subplots(5,sharex=True)
    fig.suptitle(title)
    ax1.plot(1/afreq1[1:int(acof1.size/2)],np.absolute(acof1[1:int(acof1.size/2)])**2,color='red')
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    ax2.plot(1/afreq2[1:int(acof2.size/2)],np.absolute(acof2[1:int(acof2.size/2)])**2,color='limegreen')
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax3.plot(1/afreq3[1:int(acof3.size/2)],np.absolute(acof3[1:int(acof3.size/2)])**2,color='cyan')
    ax3.set_xscale('log')
    ax3.set_yscale('log')
    ax3.set_ylabel('$|c_{FFT}|^2$')
    ax4.plot(1/afreq4[1:int(acof4.size/2)],np.absolute(acof4[1:int(acof4.size/2)])**2,color='midnightblue')
    ax4.set_xscale('log')
    ax4.set_yscale('log')
    ax5.plot(1/afreq5[1:int(acof5.size/2)],np.absolute(acof5[1:int(acof5.size/2)])**2,color='orchid')
    ax5.set_xscale('log')
    ax5.set_yscale('log')
    ax5.set_xlabel('Periodo [s]')
    fig.set_figheight(7)
    fig.set_figwidth(10)
    plt.show()

    return


def correlazione(mean1,mean2,mean3,mean4,mean5,col,inter):
    '''Funzione per ricavare una tabella di valori del coefficiente di correlazione
       minimo e maschere necessarie a causa delle diverse lunghezze degli array'''
    df=pd.DataFrame()
    minim=min(len(mean1),len(mean2),len(mean3),len(mean4),len(mean5))
    if(minim!=len(mean1)):
        if(inter==1):
            mask=np.ones(len(mean1),dtype=bool)
            mask[minim:len(mean1)]=False
            mean1=mean1[mask,...]        
        else:
            mask=np.ones(len(mean1),dtype=bool)
            mask[0:len(mean1)-minim]=False
            mean1=mean1[mask,...]
            
    if(minim!=len(mean2)):
        if(inter==1):
            mask=np.ones(len(mean2),dtype=bool)
            mask[minim:len(mean2)]=False
            mean2=mean2[mask,...]
        else:
            mask=np.ones(len(mean2),dtype=bool)
            mask[0:len(mean2)-minim]=False
            mean2=mean2[mask,...]                

    if(minim!=len(mean3)):
        if(inter==1):
            mask=np.ones(len(mean3),dtype=bool)
            mask[minim:len(mean3)]=False
            mean3=mean3[mask,...]
        else:
            mask=np.ones(len(mean3),dtype=bool)
            mask[0:len(mean3)-minim]=False
            mean3=mean3[mask,...]            
        
    if(minim!=len(mean4)):
        if inter==1 :
            mask=np.ones(len(mean4),dtype=bool)
            mask[minim:len(mean4)]=False
            mean4=mean4[mask,...]
        else:
            mask=np.ones(len(mean4),dtype=bool)
            mask[0:len(mean4)-minim]=False
            mean4=mean4[mask,...]
            
    if(minim!=len(mean5)):
        if (inter==1) :
            mask=np.ones(len(mean5),dtype=bool)
            mask[minim:len(mean5)]=False
            mean5=mean5[mask,...]
        else:
            mask=np.ones(len(mean5),dtype=bool)
            mask[0:len(mean5)-minim]=False
            mean5=mean5[mask,...]
            
    df[col[0]]=mean1
    df[col[1]]=mean2
    df[col[2]]=mean3
    df[col[3]]=mean4
    df[col[4]]=mean5
    
    return df.corr()



def trInv(coff,freq, fil, mean):
    '''funzione che mi restituisce la trasformata inversa con i coeff filtrati in ordine:
    freq array frequenze,fil valore di soglia,mean medie giornaliere'''
    mask = freq > fil
    cofFil = coff.copy()
    cofFil[mask] = 0
    arrFil = fft.irfft(cofFil, n=len(mean))
    return arrFil


def graphFil(data1,amean1,afil1,data2,amean2,afil2,data3,amean3,afil3,data4,amean4,afil4,title):
    fig, (ax1,ax2,ax3,ax4) = plt.subplots(4)
    fig.suptitle(title)
    ax1.plot(data1,amean1,color='red',label='Dati originali')
    ax1.plot(data1,afil1,color='chocolate',label='Dati filtrati')
    ax1.legend( loc='upper center',fontsize=7)
    ax2.plot(data2,amean2,color='limegreen',label='Dati originali')
    ax2.plot(data2,afil2,color='cyan',label='Dati filtrati')
    ax2.legend( loc='upper center',fontsize=7)
    ax3.plot(data3,amean3,color='midnightblue',label='Dati originali')
    ax3.plot(data3,afil3 ,color='y',label='Dati filtrati')
    ax3.legend( loc='upper center',fontsize=7)
    ax4.plot(data4,amean4,color='orchid',label='Dati originali')
    ax4.plot(data4,afil4 ,color='cornflowerblue',label='Dati filtrati')
    ax4.legend( loc='upper center',fontsize=7)
    ax1.xaxis.set_major_locator(MultipleLocator(150))
    ax1.xaxis.set_minor_locator(MultipleLocator(30))
    ax2.xaxis.set_major_locator(MultipleLocator(150))
    ax2.xaxis.set_minor_locator(MultipleLocator(30))
    ax2.set_ylabel('Media Ozono [ppm]')
    ax3.xaxis.set_major_locator(MultipleLocator(150))
    ax3.xaxis.set_minor_locator(MultipleLocator(30))
    ax3.set_ylabel('Media Ozono [ppm]')
    ax4.xaxis.set_major_locator(MultipleLocator(150))
    ax4.xaxis.set_minor_locator(MultipleLocator(30))
    ax4.set_xlabel('Date')
    fig.set_figheight(7)
    fig.set_figwidth(10)
    plt.savefig(title)
    plt.show()
  
    return


def graphRumori(data1,amean1,afil1,data2,amean2,afil2,data3,amean3,afil3,data4,amean4,afil4,title):
    fig, (ax1,ax2,ax3,ax4) = plt.subplots(4)
    fig.suptitle(title)
    ax1.plot(data1,amean1-afil1 , color='firebrick')
    ax2.plot(data2,amean2-afil2 , color='limegreen')
    ax3.plot(data3,amean3-afil3 , color='midnightblue')
    ax4.plot(data4,amean4-afil4 ,color='cornflowerblue')
    ax1.xaxis.set_major_locator(MultipleLocator(150))
    ax1.xaxis.set_minor_locator(MultipleLocator(30))
    ax2.xaxis.set_major_locator(MultipleLocator(150))
    ax2.xaxis.set_minor_locator(MultipleLocator(30))
    ax3.xaxis.set_major_locator(MultipleLocator(150))
    ax3.xaxis.set_minor_locator(MultipleLocator(30))
    ax3.set_ylabel('Differenza Ozono originale e filtrato [ppm]')
    ax4.xaxis.set_major_locator(MultipleLocator(150))
    ax4.xaxis.set_minor_locator(MultipleLocator(30))
    ax4.set_xlabel('Date')
    fig.set_figheight(7)
    fig.set_figwidth(10)
    plt.savefig(title)
    plt.show()
