# Casually OG stuff while learning python
factdict = {}
fibodict = {}
def fact(n):
    print('Getting called')
    if(n==1):
        return 1
    elif(n in factdict):
        return factdict[n]
    else:
        factdict[n] = n * factdict(n-1)
        return factdict[n]
        
def fibonacci(n):
    print('Calls')
    if(n<=1):
        return n
    if(n in fibodict):
        return fibodict[n]
    else:
        fibodict[n] = fibonacci(n-1) + fibonacci(n-2)
        return fibodict[n]
    
print(fibonacci(4))
print(fibonacci(7))
print(fibonacci(3))

# String reversal in one go, uses negative indexing
a = 'Sapt'
print(a[::-1])

# Array creations
a= [0,1] * 5
print(a)

# for 2d
a = [[0] * 5] * 4
print(a)

