import numpy as np
import pandas as pd


#prendo dati

tab=pd.read_csv('/home/marco/esameInquinantiUSA/DatiProgetto/pollution_us_2008_2010.csv')


codStato=tab['State Code'].values
codContea=tab['County Code'].values
numSito=tab['Site Num'].values
O3Mean=tab['O3 Mean'].values  #parti per milione
#=tab[''].values
#=tab[''].values
#=tab[''].values
#=tab[''].values

#6 california ;36 New york ; 39 ohio; 42 pennsylvania ; 51 Virginia

cStatoNY=np.empty()
cConteaNY=np.empty()
nSitNY=np.empty()
O3meanNY=np.empty()

for i+1 in range(len(codStato)):
    if(codStato[i]==36):
        
        


        
        
