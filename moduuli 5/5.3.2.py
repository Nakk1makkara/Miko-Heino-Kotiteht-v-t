
x = int(input("syötä luku : "))
IsNotPrimeNumber = False

for i in range (2, x) :
    jakojäänne= x % i
    if jakojäänne==0 :
        IsNotPrimeNumber = True
        break

if IsNotPrimeNumber:
    print("luku ei ole alkuluku")

else:
    print("Luku on alkuluku")