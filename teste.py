soma = 0
x = int(input("Digite um valor (0 para sair): "))

while x != 0:
    soma += x
    x = int(input("Digite um valor (0 para sair): "))
print("Soma total:", soma)