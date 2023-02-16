import random

p = int(input("p = "))
q = int(input("q = "))

n = p * q
phin = (p-1)*(q-1)
print("Phi(n) = ",phin)

def GCD(x,y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

'''while True:
    #print("while1")
    e=random.choice(range(1,phin+1))
    if GCD(e,phin) == 1:
        break'''

e=int(input('e = '))

i = 1
while True:
    #print("while2")
    df = (phin*i + 1)/e
    di = (phin*i + 1)//e
    #print(df,di,i)
    i+=1
    if di == df or i == 10:
        print('i=',i)
        break

print("Public Key =(",e,',',n,')',"\nPrivate key =(",di,',',n,')')