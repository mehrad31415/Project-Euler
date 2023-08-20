'''
problem 32:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
def f (n):
    for i in range (1,n):
        if (n%i == 0):
            a = i
            b = n // i
            tot = str(a)+str(b)+str(n)
            tot = ''.join(set(tot))
            if len(tot) == 9 and '0' not in tot:
                print(a,b,n)
                return 1
    return 0
c=0
for i in range (1,10000):
    c+=f(i)
print(c)
