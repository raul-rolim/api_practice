def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}"

def executar(funcao):
    print("executando executar")
    return funcao("Aleph")

print(executar(mensagem))
print(executar(mensagem_longa))