print ('Zadanie 4')

def duplikaty(lista):
    for x in range(len(lista)):
       if lista.count(lista[x])>1:
           lista[x]=None
    for x in range(lista.count(None)):
            lista.remove(None)
    return lista

        

print duplikaty(["kot","pies","chomik","kot","pies","pies","wydra","okon"])

#Lub inna metoda:

##def duplikaty(lista):
##    lista=list(set(lista))
##
##    return lista
##print duplikaty(["ala","zosia","ala"])
    
