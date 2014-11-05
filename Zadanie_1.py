print ('Zadanie 1')

def odliczanie(n):
    for x in range(1,n): 
        if x % 3 ==0:
            print ('Fizz')
        elif x % 5==0:
            print ('Buzz')
        elif x %3==0 and n%5==0:
            print ('Fizz Buzz')
        else:
            print str(x)
    #return n
    
print odliczanie(20)
