# biblioteca de funções matematicas
import math

# Volume do cilindro
def VolumeCilindro(r, h):
    return 3.14 * (r**2) * h
# Volume do Cone
def VolumeCone(r, h):
    return (1/3) * 3.14 * (r**2) * h
# Volume do Cubo
def VolumeCubo(a):
    return a**3
# Volume Paralelepipedo
def VolumePrismaR(a, b, c):
    return a * b * c
#  Volume Prisma Hexagonal
def VolumeHexagonal(l, h):
    areaBase = 3 * 1.73 * (l**2) / 2
    volumeH = areaBase * h
    return volumeH
# Volume Prisma triangular 
def VolumeTriangular(l, h, H):
    TipoBase = input('Escolha o tipo: (E)quilátero, (I)sósceles, (Es)caleno\n')
    if TipoBase == 'E':
        areaBase = (l**2) * 1.73 / 4
        volumeE = areaBase * h
        return volumeE
        #(3√3 * lado^2) / 2  1,73
    if TipoBase == 'I':
        areaBase = (l * h) / 2
        return areaBase
    if TipoBase =='Es':
        areaBase = (l * h) / 2
        return areaBase
#Volume Piramide
def VolumePiramide(l, h):
    areaBase = (l**2) * 1.73 / 4

solido = input('(p)oliedro ou (c)orpo redondo\n')

if(solido == 'p'):
    print('Você escolheu poliedro')
    poly = input('Escolha o tipo de Poliedro: prisma ou piramide\n')
    base = input('Qual a base: \n(Q)uadrada\n(R)etangular\n(T)riangular\n(H)exágono-Regular\n')
    if poly == 'prisma' and base == 'Q':
        a = float(input('Lado da base: '))
        print(f'O volume do cubo é: {VolumeCubo(a)}')
    if poly == 'prisma' and base == 'R':
        a = float(input('Lado 1 da base: '))
        b = float(input('Lado 2 da base: '))
        c = float(input('Altura do prisma: '))
        print(f'O volume do paralelepipedo é: {VolumePrismaR(a, b, c)}')
    if poly == 'prisma' and base == 'H':
        l = float(input('Lado da base: '))
        h = float(input('Altura do prisma: '))
        print(f'O volume do prisma hexagonal é: {VolumeHexagonal(l, h)}')
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

    
