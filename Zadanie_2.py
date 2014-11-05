print ('Zadanie 2')

#Funkcja palindrom dla wyrazów:

##def palindrom(string):
##    dlugosc=len(string)/2
##    while dlugosc:
##        dlugosc-=1
##        if string[dlugosc] != string[-dlugosc-1]:
##            return False
##
##    return True
##
##print palindrom('kajak')

#Funkcja palindrom dla znadñ i wyrazów:

def palindrom(string):
    i=0
    j=len(string)-1
    while i:
        i=i+1
        if string[i]==' ':
            i-1
        elif string[j]==' ':
            j-1
        if string[i] != string[j]:
            return False
        return True

print palindrom("kobyla ma maly bok")
