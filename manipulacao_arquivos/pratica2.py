file = open("manipulacao_arquivos/arquivo2.txt", 'w')

file.write("Hamburg\n")
file.write("Poteto")

file.close()

file = open("manipulacao_arquivos/arquivo2.txt", 'r')

print(file.read())

file.close()