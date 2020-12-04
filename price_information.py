from CleanCsvFiles import Cleaning

df = Cleaning().import_from_csv()


print('Namur') 
namur = df[df['locality'] == 'Namur'] 
print(namur['price'].describe()) 
print('-'*50)
print('Louvain') 
louvain = df[df['locality'] == 'Louvain'] 
print(louvain['price'].describe()) 
print('-'*50)
print('Turnhout') 
turnhout = df[df['locality'] == 'Turnhout'] 
print(turnhout['price'].describe()) 
print('-'*50)
print('Liège') 
liège = df[df['locality'] == 'Liège'] 
print(liège['price'].describe()) 
print('-'*50)
print('Nivelles') 
nivelles = df[df['locality'] == 'Nivelles'] 
print(nivelles['price'].describe()) 
print('-'*50)
print('Hal-Vilvorde') 
hal_vilvorde = df[df['locality'] == 'Hal-Vilvorde'] 
print(hal_vilvorde['price'].describe()) 
print('-'*50)
print('Anvers') 
anvers = df[df['locality'] == 'Anvers'] 
print(anvers['price'].describe()) 
print('-'*50)
print('Charleroi') 
charleroi = df[df['locality'] == 'Charleroi'] 
print(charleroi['price'].describe()) 
print('-'*50)
print('Bastogne') 
bastogne = df[df['locality'] == 'Bastogne'] 
print(bastogne['price'].describe()) 
print('-'*50)
print('Gand') 
gand = df[df['locality'] == 'Gand'] 
print(gand['price'].describe()) 
print('-'*50)
print('Courtrai') 
courtrai = df[df['locality'] == 'Courtrai'] 
print(courtrai['price'].describe()) 
print('-'*50)
print('Bruxelles') 
bruxelles = df[df['locality'] == 'Bruxelles'] 
print(bruxelles['price'].describe()) 
print('-'*50)
print('Huy') 
huy = df[df['locality'] == 'Huy'] 
print(huy['price'].describe()) 
print('-'*50)
print('Mons') 
mons = df[df['locality'] == 'Mons'] 
print(mons['price'].describe()) 
print('-'*50)
print('Bruges') 
bruges = df[df['locality'] == 'Bruges'] 
print(bruges['price'].describe()) 
print('-'*50)
print('Dinant') 
dinant = df[df['locality'] == 'Dinant'] 
print(dinant['price'].describe()) 
print('-'*50)
print('Audenarde') 
audenarde = df[df['locality'] == 'Audenarde'] 
print(audenarde['price'].describe()) 
print('-'*50)
print('Malines') 
malines = df[df['locality'] == 'Malines'] 
print(malines['price'].describe()) 
print('-'*50)
print('Verviers') 
verviers = df[df['locality'] == 'Verviers'] 
print(verviers['price'].describe()) 
print('-'*50)
print('Ath') 
ath = df[df['locality'] == 'Ath'] 
print(ath['price'].describe()) 
print('-'*50)
print('Alost') 
alost = df[df['locality'] == 'Alost'] 
print(alost['price'].describe()) 
print('-'*50)
print('Neufchâteau') 
neufchâteau = df[df['locality'] == 'Neufchâteau'] 
print(neufchâteau['price'].describe()) 
print('-'*50)
print('Marche-en-Famenne') 
marche_en_famenne = df[df['locality'] == 'Marche-en-Famenne'] 
print(marche_en_famenne['price'].describe()) 
print('-'*50)
print('Waremme') 
waremme = df[df['locality'] == 'Waremme'] 
print(waremme['price'].describe()) 
print('-'*50)
print('Arlon') 
arlon = df[df['locality'] == 'Arlon'] 
print(arlon['price'].describe()) 
print('-'*50)
print('Soignies') 
soignies = df[df['locality'] == 'Soignies'] 
print(soignies['price'].describe()) 
print('-'*50)
print('Virton') 
virton = df[df['locality'] == 'Virton'] 
print(virton['price'].describe()) 
print('-'*50)
print('Thuin') 
thuin = df[df['locality'] == 'Thuin'] 
print(thuin['price'].describe()) 
print('-'*50)
print('Termonde') 
termonde = df[df['locality'] == 'Termonde'] 
print(termonde['price'].describe()) 
print('-'*50)
print('Tielt') 
tielt = df[df['locality'] == 'Tielt'] 
print(tielt['price'].describe()) 
print('-'*50)
print('Ostende') 
ostende = df[df['locality'] == 'Ostende'] 
print(ostende['price'].describe()) 
print('-'*50)
print('Tournai') 
tournai = df[df['locality'] == 'Tournai'] 
print(tournai['price'].describe()) 
print('-'*50)
print('Philippeville') 
philippeville = df[df['locality'] == 'Philippeville'] 
print(philippeville['price'].describe()) 
print('-'*50)
print('Saint-Nicolas') 
saint_nicolas = df[df['locality'] == 'Saint-Nicolas'] 
print(saint_nicolas['price'].describe()) 
print('-'*50)
print('Hasselt') 
hasselt = df[df['locality'] == 'Hasselt'] 
print(hasselt['price'].describe()) 
print('-'*50)
print('Tongres') 
tongres = df[df['locality'] == 'Tongres'] 
print(tongres['price'].describe()) 
print('-'*50)
print('Mouscron') 
mouscron = df[df['locality'] == 'Mouscron'] 
print(mouscron['price'].describe()) 
print('-'*50)
print('Furnes') 
furnes = df[df['locality'] == 'Furnes'] 
print(furnes['price'].describe()) 
print('-'*50)
print('Eeklo') 
eeklo = df[df['locality'] == 'Eeklo'] 
print(eeklo['price'].describe()) 
print('-'*50)
print('Maaseik') 
maaseik = df[df['locality'] == 'Maaseik'] 
print(maaseik['price'].describe()) 
print('-'*50)
print('Roulers') 
roulers = df[df['locality'] == 'Roulers'] 
print(roulers['price'].describe()) 
print('-'*50)
print('Ypres') 
ypres = df[df['locality'] == 'Ypres'] 
print(ypres['price'].describe()) 
print('-'*50)
print('Dixmude') 
dixmude = df[df['locality'] == 'Dixmude'] 
print(dixmude['price'].describe()) 
print('-'*50)