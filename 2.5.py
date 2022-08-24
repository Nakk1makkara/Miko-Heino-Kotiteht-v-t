leiviskät =float(input("Anna leiviskät : "))
naulat = float(input("Anna naulat : "))
luodit = float(input("Anna luodit : "))

paino = (luodit*13.3 + naulat*425.6 + leiviskät*8512) /1000

print(f"painosi nykyisten mittojen mukaan: \n{paino:4.1f}" + "kg")