# kahvin osto
# jos rahaa taskussa on >=5 osta latte
# jos ei mutta rahaa on >=3 osta normi kahvi
# muuten sinulla ei ole rahaa ostaa mitään

raha = int(input("Kuinka paljon rahaa on? : "))
maistuuko_kahvi = input("Maistuuko kahvi? ")



if raha>=5 and maistuuko_kahvi == "joo" :
    print("Voit ostaa laten.")
    raha = raha -5
elif raha>=3 and maistuuko_kahvi == "joo" :
    print("Voit ostaa normaalin kahvin.")
    raha = raha -3
elif raha >= 2 :
    print("2 eurolla saa teetä! ")
    raha = raha -2
else:
    print("Sinulla ei ole tarpeeksi rahaa ostaa kahvia.")

if raha == 0:
    print("Raha on loppu.")


print(f"Sinulla on vielä {raha} euroa jäljellä.")

