#Exercícios da semana 03 e da atividade 03.
"""
01. Escreva um programa que leia o valor de um raio, calcule e mostre na tela o comprimento da circunferência, a área
do círculo, a área da esfera e o volume da esfera para o valor do raio lido. Mostre os valores com 6 casas decimais.
"""
raio = float(input("Digite o valor do raio: "))
pi = 3.14
comprimento_circ = 2 * pi * raio
area_circ = pi * raio**2
area_esfera = 4 * pi * raio**2
volume_esfera = 4 * pi * raio**3 / 3
print()
print(f'O valor do raio é {raio:.6f}.')
print(f'O comprimento do circulo é: {comprimento_circ:.6f}.')
print(f'A área da circunferência é: {area_circ:.6f}.')
print(f'A área da esfera é: {area_esfera:.6f}.')
print(f'A volume da esfera é: {volume_esfera:.6f}.')
print()
"""
02. Escreva um programa que leia o preço de um produto e mostre na tela o valor com 10% de desconto arredondado
para duas casas decimais.
"""
preço = float(input("Digite o valor do produto R$: "))
desconto = preço * 0.1
v_desconto = preço - desconto
print(f'O valor do produto é {preço:.2f} e com 10% de desconto fica {v_desconto} .')
print()
"""
03. Escreva um programa que leia dois valores, um dividendo e um divisor. Mostre o resultado da divisão e o resto da
divisão inteira dos valores.
"""
valor1 = int(input("Digiti o valor do dividendo: "))
valor2 = int(input('Digite o valor do divisor: '))
divisao = valor1 / valor2
resto = valor1 % valor2
print(f'A divisão dos valores é {divisao} e o resto {resto} .')
print()
'''
04. Escreva um programa que leia uma quantidade de minutos e mostre a quantidade de horas e minutos equivalente.
'''
minutos = int(input('Digite a quantidade de minutos: '))
horas = minutos // 60
min = minutos % 60
print(f"{minutos} minutos transformado em horas é: {horas}h e {min}min.")
print()
"""
5. A Bate Ponto LTDA bonifica seus funcionários de acordo o tempo de serviço na empresa Escreva um programa 
que leia o tempo de serviço de um funcionário e o valor do bônus por ano trabalhado. Mostre na tela quanto será a 
bonificação do funcionário.
"""
tempo_servico = int(input("Qual é o seu tempo de serviço em anos trabalhado: "))
valor_bonus = int(input("Qual o valor do bonus trabalhado: "))
valor = valor_bonus * tempo_servico
print()
print(f'A bonificação do funcionário será de R$: {valor}.')
input()

