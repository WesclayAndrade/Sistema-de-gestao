import os 
arquivo = open("exemplo.txt", 'a')

#exibir os atribuitos do arquivo
print("nome do aqrquivo", arquivo.name)
print("Modo de abertura do arquivo", arquivo.mode)
print("Arquivo está fechado", arquivo.closed)

#escrever no arquivoo


arquivo.write("\nread -> todo texto em uma única linha de conteúdo" \
"\n readline-> linha de arquivo com os caracteres finais " \
"\n readlines -> lista em que cada item é uma linha do arquivo ")
#fechar arquivo 
arquivo.close()
print("Arquivo está fechado", arquivo.closed)

relpath = os.path.relpath("exemplo.txt")
abspath = os.path.abspath('exemplo.txt')

print("Caminho relativo:", relpath)
print("Caminho absoluto:", abspath)



