# Devo creare una funzione che prende come parametri due liste (l1 e l2)
# La seconda lista deve essere un parametro opzionale con i seguenti valori di default [1,2,3,4,5]
# La funzione deve ritornare la differenza tra le due liste, cioè la lista ritornata deve contenere tutti
# gli elementi di l1 che non sono presenti in l2

def sottrazione(l1, l2=[1, 2, 3, 4, 5]):
    result = list()
    flg = False

    for x in l1:
        flg = False
        for y in l2:
            if x == y:
                flg = True
                break
        if not flg:
            result.append(x)

    return result


def sottrazioneOttimizzata(l1, l2=[1, 2, 3, 4, 5]):
    result = list()

    for x in l1:
        if not x in l2:
            result.append(x)
    return result