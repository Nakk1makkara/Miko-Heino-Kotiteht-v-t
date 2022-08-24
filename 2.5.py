leiviskät =float(input("Anna leiviskät : "))
naulat = float(input("Anna naulat : "))
luodit = float(input("Anna luodit : "))


luodit = 13.3
naulat = 32*luodit
leiviskät = 20*naulat

paino = (luodit + naulat + leiviskät) /1000

print(f"painosi nykyisten mittojen mukaan: \n{paino:3.2f}" + "kg")