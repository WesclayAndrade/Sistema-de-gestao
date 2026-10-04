import os

#abrindo o arquivo, já em modo de escrita
arquivo1 = open('Arquivo.txt', 'w')

#conferindo situação do arquivo. 
print("Nome do arquivo: ", arquivo1.name)
print("Modo de abertura: ", arquivo1.mode)
print("Arquivo está fechado? ", arquivo1.closed)

#escrevendo no arquivo
arquivo1.write("Olá, bem vindo. Primeira aula com código de RAD. \n" \
"Vamos tentar ampliar conceitos. \n" \
"quem sabe sair um programador de verdade. \n")

#fechando o arquivo
arquivo1.close()

#verificar se arquivo ta fechado
print("O Arquivo ta fechado?", arquivo1.closed)

#exibir caminho relativo e absopluto

relpath = os.path.relpath("Arquivo.txt")
abspath = os.path.abspath("Arquivo.txt")

print("Caminho relativo: ", relpath)
print("Caminho absoluto: ", abspath)

arquivo1 = open("Arquivo.txt")
conteudo = arquivo1.read()
print(repr(conteudo))
arquivo1.close
arquivo1 = open("Arquivo.txt")
conteudo2 = arquivo1.readline()
print(repr(conteudo2))
arquivo1.close
arquivo1 = open("Arquivo.txt")
conteudo3 = arquivo1.readlines()
print(repr(conteudo3))
arquivo1.close
#repr retrira a quebra de linha do \n
#necessário fechar o arquivo para fazer uma nova chamada de read

#arquivo com iteração nos dados 
arquivo1 = open("Arquivo.txt")
print("Iterando sobre o arquivo")
for linha in arquivo1:
    print(linha)


arquivo1.seek(0)
conteudo_seek = arquivo1.read()
print("conteúdo no metódo seek.\n\n", conteudo_seek)

arquivo1 = open("Arquivo.txt", "a")
arquivo1.write("Adicionando texto com o metódo a\n")
conteudo2_= arquivo1.read()
print(repr(conteudo2)


