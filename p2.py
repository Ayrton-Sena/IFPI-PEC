d = int(input('Dias: '))
h = int(input('Horas: '))
m = int(input('Minutos: '))
s = int(input('Segundos: '))

total = d*24*60*60 + h*60*60 + m*60 + s
print (total)

print()

s = float(input('Salário: '))
p = float(input('Aumento%: '))
aumento = s * p / 100
novo = s + aumento
print(f'Aumento: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo:.2f}')

print()

m = float(input('Preço: '))
p = float(input('Desconto%: '))
desconto = m * p / 100
novo = m - desconto
print(f'Desconto: R$ {desconto:.2f}')
print(f'Preço a pagar: {novo:.2f}')

print()

d = float(input('Distância Km: '))
v = float(input('Vel. média Km/h: '))
t = d / v
print (f'Tempo: {t:.1f}')

print()

c = float(input('Celsius: '))
f = 9*c/5 + 32
print (f'{f:.2f} Fahrenheit')

print()

f = float(input('Fahrenheit: '))
c = (f - 32) * 5 / 9
print (f'{c:.2f} Celsius')

print()

km = float(input('Km rodados: '))
dias = int(input('Dias: '))
preço = 60*dias + 0.15*km
print (f'R$ {preço:.2f}')

print()

'Fazendo uma regra de três 1 dia = 1440 minutos = 144 cigarros '
cigarros = int(input('Cigarros dia: '))
anos = int(input('Anos fumados: '))

total_cigarros = anos * 365 * cigarros
dias = total_cigarros / 144
print (f'Você perdeu {dias:.1f} dias')
print()

'''Converter numeros para texto'''
print (len(str(2**100000)))

print()
'LER DOIS VALORES INTEIROS E IMPRIMIR O MAIOR DELES:'
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
if a > b:
    print ("O primeiro número é o maior!")
if b > a:
    print ("O segundo número é o maior!")

