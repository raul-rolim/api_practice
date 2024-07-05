file = open("manipulacao_arquivos/arquivo1.txt", "r")

for line in file.readlines():
    print(line)

file.close()