'''01. Escreva um programa que mostre na tela as mensagens:
        Alô, mundo!
        ALO MUNDO
        alô, mundo.
        ALo munDO
        Alô, Mundo!
'''
print("Alô, mundo!")
print()
print("ALO MUNDO")
print()
print("alô, mundo.")
print()
print("ALo munDO")
print()
print("Alô, Mundo!")
print()
#02. Escreva um programa que leia separadamente seu nome e o seu sobrenome e mostre na tela o nome completo.
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
print(nome,sobrenome)
print()
#03. Escreva um programa que leia dois números e mostre na tela a soma e a multiplicação deles.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
mult = num1 * num2
print(f'A soma %d e a multiplicação %d.' %(soma,mult))
print()
#04. Escreva um programa que ler o valor da variável x. Calcule e mostre o resultado da expressão:
#           9x - 4x + 10
x = int(input('Digite um numero: '))
expressao = 9*x - 4*x + 10
print(f'O valor da expressão numérica 9x-4x+10 é: %d.' %expressao)
print()
#05. No próximo final de semana seu time de futebol entrará em campo. Escreva um programa que leia o seu nível de empolgação para a partida, um número inteiro entre 1 e 10, e mostre a empolgação do lado de fora do estádio representando por letras "O" ao gritar GOL. Por exemplo:
#     Empolgação nível 1>>>Gol!
#     Empolgação nível 5>>>Goooool!

y = int(input('Digite o seu nível de empolgação de 1 a 10: '))
if y == 1:
 print ("Gol! %d." %y)
elif y == 2:
 print ("Gool! %d." %y)
elif y == 3:
 print ("Goool! %d." %y)
elif y == 4:
 print ("Gooool! %d." %y)
elif y == 5:
 print ("Goooool! %d." %y)
elif y == 6:
 print ("Gooooool! %d." %y)
elif y == 7:
 print ("Goooooool! %d." %y)
elif y == 8:
 print ("Gooooooool! %d." %y)
elif y == 9:
 print ("Goooooooool! %d." %y)
elif y == 10:
 print ("Gooooooooool! %d." %y)



 


