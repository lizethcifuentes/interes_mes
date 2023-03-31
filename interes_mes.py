print("-----------------------")
print("------capital mes------")
print("-----------------------")

C= int(input("digite su capital: "))

intereses = 0
mes = 0
c2 = C + C 

while C < c2:
    intereses = C*0.05
    C = C + intereses
    mes = mes +1
print("la capital se duplico en " + str(mes) + "meses")     