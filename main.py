# biblioteca de funções matematicas
import math

# Volume do cilindro
def VolumeCilindro(r, h):
    return 3.14 * (r**2) * h
# Volume do Cone
def VolumeCone(r, h):
    return (1/3) * 3.14 * (r**2) * h
# Volume do Cubio
def VolumeCubo(a):
    return a**3


solido = input('(p)oliedro ou (c)orpo redondo\n')

if(solido == 'p'):
    print('Você escolheu poliedro')
    poly = input('Escolha o tipo de Poliedro: prisma ou piramide')
    base = input('Exemplos: cubo, pirâmide, prisma, tetraed')
elif solido == 'c':
    print('Você escolheu corpo redondo')
    corpo = input('cilindro ou cone\n')
    if corpo == 'cilindro':
        r = float(input('Raio do cilindro: '))
        h = float(input('Altura do cilindro: '))
        print (f'O volume do cilindro é: {VolumeCilindro(r, h)}')
    elif corpo == 'cone':
        r = float(input('Raio do cone: '))
        h = float(input('Altura do cone: '))
        print (f'O volume do cone é: {VolumeCone(r, h)}')
    else:
        print('Opção inválida')
else:
    print('opção inválida')
    
