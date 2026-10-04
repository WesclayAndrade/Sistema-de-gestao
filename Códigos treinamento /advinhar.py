import random
num_secreto = random.randint(1, 50)
tentativas = 0
print("Jogo da advinhação...")
while (True):
    num = int(input("Escolha um número entre 1 e 50.."))
    tentativas += 1
    if num == num_secreto:
        print(f"Você acertou.. O número sorteado foi  {num_secreto}"
              f"Você precisou de {tentativas}")
        break
        
    else:
        print(f"Infelizmente você errou.. tente novamente.. ")
    continuar = input("Você deseja tentar novamente? [S/N]")
    if continuar == "N" or continuar == "n":
            print("Saindo..")
            break
    else:
            print("Nova tentativa.")
            
