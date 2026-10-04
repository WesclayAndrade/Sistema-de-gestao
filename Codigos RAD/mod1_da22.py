import os 

arquivo1 = open("Dados1.txt", 'w') #para criar um arquivo novo, open é para abrir a inclusão do w cria um para escrevar

print(os.path.abspath(arquivo1.name)) #mostra o caminho relativo do arquivo criado (path -> caminho; abs -> absoluto)

arquivo1.write("olá mundo." \
"Estamos aprendendo a criar um arquivo e escrever dentro dele" \
" Goodbye") # escrevendo no arquivo que já esta criado

print(os.path.relpath(arquivo1.name)) #caminho relativo 
print(arquivo1) #imprimindo o tipo de arquivo 

arquivo1.write("\nLembrar sempre de fechar o arquivo no final com nome_arquivo.close")
arquivo1.write("\n open()-> abrir o arquivo\n" \
"write -> escrever\n" \
"se não incluir o write o arquivo sempre abre como leitura (read)\n" \
"sempre que concluir a utilização do arquivo ffinalizar com o .close()\n" \
"o caminho absoluto (abspath)-> referência do arquivo no diretório\n" \
"caminho relativo (relpath)-> arquivo em outro diretório  \n" \
"append -> para aacrescentar algo já existente. pode usar o a támbem somente quando for chamar a abertura do arquivo.\n" \
"Lembrar que é necessário importar um OS antes de iniciar o código.\n" \
"")
arquivo1.close()
print(arquivo1.name)
print(arquivo1.mode)
print(arquivo1.closed)




