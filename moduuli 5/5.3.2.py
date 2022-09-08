
x = int(input("syötä luku : "))
isPrimeNumber = False

for i in range (2, x) :
    t=x%i
    if t==0 :
        isPrimeNumber = True
        break

if isPrimeNumber:
    print("luku ei ole alkuluku")

else:
    print("Luku on alkuluku")