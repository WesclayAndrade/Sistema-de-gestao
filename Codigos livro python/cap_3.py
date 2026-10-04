# num = int(input("Digite um número inteiro: "))
# contador = float(num)
# while True:
#     num_real = float(input("Digite um número real: "))

#     if num_real > 0:
#         soma = num + num_real
#         print("A soma foi", soma)
#         contador += soma 
#     elif num_real == 0:
#         print(f"O total somado foi {contador}")
#         break
    
# positivo = 0
# negativo = 0
# while True:
#     num = int(input("Digite seu número: "))
#     if num > 0:
#         positivo += 1
#     elif num == 0:
#         break
#     else:
#         negativo += 1

# print(f"O total de números positivos foi de {positivo}"\
#       f" já o total de números negativos foi de {negativo}")

# num = int(input("Digite seu número: "))
# real_maior = 0
# real_menor= 0
# while True:
#     num_real1 = float(input("Digite seu primeiro número real: "))    
#     num_real2 = float(input("Digite seu segundo número real: "))    
    
#     if num_real1 > num_real2:
#         real_maior = num_real1
#         real_menor = num_real2
#         print(f"O número escolhido foi {num} e o número {real_maior} é maior que o {real_menor}")
                       
#     elif num_real2 > num_real1:
#         real_menor = num_real1
#         real_maior = num_real2
#         print(f"O número escolhido foi {num} e o número {real_maior} é maior que o {real_menor}")
#         break
           
#     else:
#         print("Números iguais")


# real_maior = 0
# real_menor= 0
# while True:
#     num = int(input("Digite seu número: "))
#     num_real1 = float(input("Digite seu primeiro número real: "))    
#     num_real2 = float(input("Digite seu segundo número real: "))   

#     if num > 0 and num_real1 > 0 and num_real2 > 0:
#         if num_real1 > num_real2:
#             real_maior = num_real1
#             real_menor = num_real2
#             print(f"O número escolhido foi {num}, o {real_maior} é o maior real e o {real_menor} é o menor real")
#             break
#         elif num_real2 > num_real1:
#             real_maior = num_real2
#             real_menor = num_real1
#             print(f"O número escolhido foi {num}, o {real_maior} é o maior real e o {real_menor} é o menor real")
#             break
#     elif num < 0:
#         print(f"O número {num} é negativo, tente novamente..")
#     elif num_real1 < 0:
#         print(f"O número {num_real1} é negativo, tente novamente.. ")
#     elif num_real2 < 0:
#         print(f"O número {num_real2} é negativo, tente novamente..")


# maior = 0
# menor = 1
# contador = 0
# soma = 0
# while True:
#     num = int(input("Digite seu número: "))

#     if num <= 0:
#         print("Finalizando.. obrigado..")
#         break
#     else:
#         contador += 1
#         soma += num
       
#         if num > maior :
#             maior = num
#         elif num < menor:
#             menor = num

# media = soma / contador
# print(f" O maior número foi {maior}, já o menor número foi {menor}\n"
#       f" Foi informado um total de {contador} números onde a soma de todos os números foi de {soma}\n"
#       f"Já a média de de todos os valores informados foi de {media}")
# numero = 0
# num = 1
# while True:
#     num = int(input("Digite um número: "))
#     if num == 0:
#         print("finalizando o programa")
#         break
#     elif num % 2 == 0 and num % 3 == 0:
#         numero = num
#         print(f"O número {numero} é divisivel tanto por 2 quanto por 3..")
# pares = 0
# while True:
#     numero = int(input("Digite um número, não menor que 100 para iniciar: "))

#     if numero < 100:
#         print(f"O número {numero} é menor que 100.. tente novamente")
#     elif numero >= 100:
#         for i in range(numero + 1):
#             if i % 2 == 0:
#                 pares += i
#         break


# print(pares)
    
soma = 0

while True:
    min = int(input("Digite o valor mínimo: "))
    max = int(input("Digite o valor máximo:  "))
    if min > max:
        print(f"Por favor, repita a operação o valor {min} é maior que {max}")
    else: 
        for i in range(min, max + 1):
            if i % 5 ==0:
                soma += i
        break
       

print(soma)

