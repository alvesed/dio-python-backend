#condicionais
print('condicionais')


#if ternario:
saldo = 1000
saque = 500
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} no saque.")

saldo = 10
saque = 200
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} no saque.")

#repeticao
print('repeticao')

texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("\nfinal de lacao")

print()


for numero in range(0, 11):
    if numero == 2:
        continue
    print(numero, end=" ")
print()

for numero in range(0, 51, 5):
    print(numero, end=" ")

print()

opcao = -1
while opcao !=0:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] Sair\n:"))

    if opcao == 1:
        print("sacando")
    elif opcao == 2:
        print("extrato")

while True:
    opcao = int(input("[1] sacar \n[2] extrato \n[0] Sair\n:"))

    if opcao == 1:
        print("sacando")
    elif opcao == 2:
        print("extrato")
    elif opcao == 0:
        print("break")
        break
