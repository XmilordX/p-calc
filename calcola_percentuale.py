numero = float(input("Inserisci il numero: "))
percentuale = float(input("Inserisci la percentuale: "))
valore_100_percento = (numero / percentuale) * 100
percentuale_rimanente = 100 - percentuale
valore_percentuale_rimanente = (valore_100_percento * percentuale_rimanente) / 100
print(f"Il numero che corrisponde al 100% è: €{valore_100_percento:,.2f}")
print(f"Il numero che corrisponde al {int(percentuale_rimanente)}% è: €{valore_percentuale_rimanente:,.2f}")
input("Premi Invio per chiudere...")