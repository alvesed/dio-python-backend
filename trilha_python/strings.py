import math

#strings
print('**** strings ****')

curso = "pYtHon"
print(curso.upper())
print(curso.lower())
print(curso.title())

texto = '  Olá mundo!  '
print(texto.strip())
print(texto.lstrip())
print(texto.rstrip())

menu = "Python"
print(menu.center(14))
print(menu.center(14,"#"))

print(".".join(menu))


#interpolação de variáveis
print('\n**** interpolação de variáveis ****')

nome = "Edson"
idade = 37
profissao = "Programador"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." 
      % (nome, idade, profissao, linguagem))

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = math.pi
print(PI)
print(f"PI = {PI:10.2f}")


#fatiamento
print('\n**** fatiamento ****')
nome = "Edson F. Alves"
print(nome[0])
print(nome[-1])
print(nome[-2])

print(nome[:5])

print(nome[10:])
print(nome[10:12])
print(nome[10:16:2])
print(nome[:])
print(nome[::-1])


#multiplas linhas
print('\n**** multiplas linhas ****')
mensagem = f'''
 Olá meu nome é {nome},
Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.
'''

print(mensagem)