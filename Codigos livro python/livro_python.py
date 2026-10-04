'''
profissional = float(input("Qual valor da hora profissional? "))
horas_trabalhada = int(input("Quantas horas trabalhadas neste mês?"))
horas_extra = float(input("Foi feito hora extra? Informe quantas?"))

total_receber = (horas_trabalhada + (horas_extra*2)) * profissional
print(total_receber)

inteiro = int(input("Número inteiro : "))
real1 = float(input("Insisra o primeiro número real: "))
real2 = float(input("Insisra o segundo número real: "))

'''

'''
while (inteiro <= 10):
    print(inteiro)
    inteiro += 1

for i in range(1, 11):
    tabuada = inteiro * i
    print("O valor de ",inteiro, "x", i , "tem como resultado:", tabuada)

if inteiro and real1 and real2 > 0:
    print("Todos os números são positivos, a soma é: ",inteiro+real2+real1)
elif inteiro and real1 > 0:
    print("o Segundo número é negativo então a soma é: ", real1+inteiro)
elif inteiro and real2 > 0:
    print("O primeiro número é negativo, então a soma é: ", real2 + inteiro)

while (True):
    numero = int(input("Digite um número diferente de zero(ao digitar zero o programa fecha): "))
    if numero != 0:
        if numero % 2 == 0:
            print("O número", numero,"é par.")
        else:
            print("O número", numero,"é ímpar.")
    else:
        print("Número zero digitado.. Saindo")
        break
while(True):
    inicio =  int(input("Digite o valor de inicio: "))
    fim = int(input("Digite o valor final: "))

    if fim < inicio:
        print("Erro: número fim menor que início")
    else:
        print("numero divisiveis por 5:", inicio,"e ", fim)
    
    if fim == inicio:
        print("Saindo...")
        break

    for i in range(inicio, fim+ 1):
        if i % 5 == 0:
            print( i ," ")

    print("Caso não queira mais calcular, so digitar zero e zero")
    '''
contador = 0
numero_maior = 0
numero_menor = 0
valor_total = 0
while(True):
    numero = int(input("Digite um número: "))
    print("Caso digite número nmegativo ou zero o programa é encerrado")

    if numero <= 0:
        print("Programa encerrado")
        break
    
    valor_total += numero
    contador += 1
    if contador == 1:
        numero_menor = numero
        numero_maior = numero
    else:
        if numero > numero_maior:
            numero_maior = numero
        elif numero < numero_menor:
            contador == 1
            numero_menor =numero

if contador > 0:
    media_total =  valor_total/contador
    print("Chegamos ao fim..\n"
      "O maior valor digitado foi:", numero_maior,"\n",
        "O menor valor foi: ", numero_menor,"\n"\
            "Foram informados um total de", contador, "números\n"\
                "A soma total dos números foi de", valor_total, "e a média é de ", media_total)

