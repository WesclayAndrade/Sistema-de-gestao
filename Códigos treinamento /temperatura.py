tempratura = []
for dia in  range(1 , 8):
    temp = float(input(f"Informe a temperatura do dia {dia}:"))
    tempratura.append(temp)
menor = tempratura[0]
maior = tempratura[0]
soma = 0
   
for temp in tempratura:
    soma +=temp

    if temp < menor:
        menor =temp
    elif temp > maior:
        maior = temp

media = soma / len(tempratura)

acima_media = 0
for temp in tempratura:
    if temp > media:
        acima_media += 1

print(tempratura)
print(menor)
print(maior)
print(soma)
print(media)
print(acima_media)