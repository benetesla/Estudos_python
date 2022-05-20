print ("Hello word")
x = 5
nome = "Ola mundo"
nota = 10.5
fez_inscricao = True
print (x)
print (nome)
print (nota)
print (fez_inscricao)
print (type(x))
print (type(nome))
print (type(nota))
print (type(fez_inscricao))
nome = input("Digite seu nome: ")
print ("Ola", nome)
#a função input() é usada para receber dados do usuário
#a função print() é usada para exibir dados para o usuário
#a função type() é usada para verificar o tipo de dado

print(
    "Olá %s, bem vindo a disciplina de programação python. Parabéns pelo seu primeiro hello world"
    % (nome))
print ("ola {}, bem vindo a disciplina de programação python. Parabéns pelo seu primeiro hello world".format(nome))
#operacao matematicas
#o operador de atribuição é o = e o operador de soma é o + e o operador de multiplicação é o * e o operador de divisão é o / e o operador de subtração é o - e o operador de exponenciação é o ** e o operador de resto é o % e o operador de potenciação é o ** e o operador de divisão inteira é o // e o operador de potenciação inteira é o **.

operacao1 = (5 + 3) * 2
print (operacao1)
#operacao matematicas
operacao2 = (5 - 3) * 2
print (operacao2)
#operacao matematicas
operacao3 = (5 / 3) * 2
print (operacao3)
#operacao matematicas
operacao4 = (5 // 3) * 2
print (operacao4)
#operacao matematicas
operacao5 = (5 % 3) * 2
print (operacao5)
#operacao matematicas
operacao6 = (5 ** 3) * 2
print (operacao6)
#a realização de uma operação matemática é feita através de uma expressão
#impressão de dados
print(f"operacao1 = {operacao1}")
print(f"operacao2 = {operacao2}")
print(f"operacao3 = {operacao3}")
print(f"operacao4 = {operacao4}")
print(f"operacao5 = {operacao5}")
print(f"operacao6 = {operacao6}")
#fim da impressão de dados

a = 5
b = 8.5
c = 2
x = input("Digite um valor um valor para a varivel x: ")
x = float(x)#converte o valor de x para float
y = a * x ** 2 + b * x + c
print (f"o resultado da expressao  de x e y é {x} e {y}")