# EsameInquinantiUSA


Il progetto ha come scopo quello di analizzare l' inquinante Ozono (O3) negli USA, tutto questo è stato fatto per le stazioni in 5 stati contigui e successivamente per più stati. 

**Librerie utilizzate**: numpy, pandas, scipy, sys, matplotlib.pyplot, matplotlib.ticker,statistics

## Descrizione codice

1) Prima di tutto è stato creato uno script *elaborazioneDati.py* per estrarre un solo dato al giorno di O3:
Questo script crea due nuovi file csv  *dati5Stati.csv* e *datiStati.csv*; Il primo che ha solo i dati relativi delle stazioni dei 5 stati contigui mentre particolare: codice dello stato della contea e della stazione , data e media giornaliera corrispondente
il secondo è identico al primo ma con tutti gli stati che hanno delle rilevazioni

2) Lo script *Classi.py* è quello in cui sono definite la classi rilevazione,stazione,rilStato e stato ed implementa gli oggetti e i rispettivi metodi.

3) *Funzioni.py* è  il codice dove sono scritte tutte le funzioni utilizzate durante l' analisi e per l' estrazione di rilevazioni, stazioni e stati 

4) *studio5Stati.py* è lo script relativo a tutta l' analisi dati delle stazioni dei 5 stati contigui

5) *studioStati.py* è lo script relativo a tutta l' analisi dati degli stati nel loro insieme

## Esecuzione:

1) Non è necessario eseguire *elaborazioneDati.py* in quanto i file sono già stati salvati nella cartella apposita Dati progetto

2) Eseguire nell' ordine che si preferisce *studioStati.py* o *studio5Stati.py* per visualizzare grafici e tabelle relativi all' analisi dati richiesta
