limite = 3
senha = "python"
tentativa = 0
while limite >0:
    chance = input("Digite a sua senha: (apenas caracteres)  ").strip().lower()
   
    if chance == senha:
        print("Você conseguiu desbloquear. Seja bem vindo")
        break
    else:
        limite -=1 
        tentativa +=1
        if limite > 0:
            print(f"Tentativa {tentativa} inválida... "
                 f"Voce ainda tem {limite} chances. ")
        else:
            print("SISTEMA BLOQUEADO")


