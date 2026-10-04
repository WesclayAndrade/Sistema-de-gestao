import os 

arquivo = open("Reads.txt", )


#arquivo.write("Quarta tentativa.. um dia aprendo a programar. vamos focar em código, mais prática")

conteudo = arquivo.read()
print("tipo de conteúdo", type(conteudo))

print("Conteúdo retornado pelo read")
print(repr(conteudo))


conteudo2 = arquivo.readline()
print("Conteúdo retornado pelo readline")
print(repr(conteudo2))
print(type(conteudo2))
proximo_conteudo = arquivo.readline()
print("Próximo conteúdo")
print(repr(proximo_conteudo))


conteudo3 = arquivo.readlines()

print(type(conteudo3))
print("Conteúdo retornado pelo realines ")
print(repr(conteudo3))







#arquivo.close()