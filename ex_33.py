"""
Problem 33:
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

s = set()
for i in range(10, 100):
  for j in range(10, 100):
    n1 = i // 10
    d1 = j // 10
    n2 = i % 10
    d2 = j % 10
    if (i != j and i%11!=0 and i%10!=0 and i/j <1):
        if (d1 != 0 and n1 != 0 and n2==d2):
            if (i / n1 == j / d1):
                s.add((i,j))
        if (d1 != 0 and n2 != 0 and n1==d2):
            if (i / n2 == j / d1):
                s.add((i,j))
        # n1 / d1, n2 / d2, n1 / d2, n2 / d1
        if (d2 != 0 and n1 != 0 and n2==d1):
            if (i / n1 == j / d2):
                s.add((i,j))
        if (d2 != 0 and n2 != 0 and n1==d1):
            if (i / n2 == j / d2):
                s.add((i,j))
def gcd(m,n):
    if (n==0):
        return m
    return gcd (n,m%n)
c1=1
c2=1
for i in s:
    m,n=i
    c1*=m
    c2*=n
print(c2//gcd(c1,c2))
