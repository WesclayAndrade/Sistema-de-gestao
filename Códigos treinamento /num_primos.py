num_primo = int(input("Digite um número maior que 0? "))

if num_primo <= 1: #testando a condição 
    print(f"O número {num_primo} não é primo. ")
else:
    divisores = 0

    for i in range( 1, num_primo + 1):
        if num_primo % i == 0:
            divisores +=1

    if divisores ==2 :
        print(f"O número {num_primo} é Primo!")
    else:
        print(f"O número {num_primo} não é primo.")


