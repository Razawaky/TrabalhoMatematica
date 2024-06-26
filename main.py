# biblioteca de funções matematicas
import math

# Volume do cilindro
def VolumeCilindro(r, h):
    return 3.14 * (r**2) * h

# Volume do Cone
def VolumeCone(r, h):
    return 3.14 * (r**2) * h / 3

# Volume do Prisma Quadrangular
def VolumePrismaQ(a, h):
    return (a**2) * h
# Volume Paralelepipedo
def VolumePrismaR(a, b, c):
    return a * b * c
#  Volume Prisma Hexagonal
def VolumeHexagonal(l, h):
    areaBase = 3 * 1.73 * (l**2) / 2
    volumeH = areaBase * h
    return volumeH
# Volume Prisma Triangular
def VolumeTriangular(tipo, l, h, H,):
    if tipo == 'E':
        AreaBase = (l**2) * 1.73 / 4
        VolumeEquilatero = AreaBase * H
        return VolumeEquilatero
    elif tipo == 'I':
        AreaBase = (l * h) / 2
        VolumeI = AreaBase * H
        return VolumeI
    elif tipo == 'Es':
        AreaBase = (l * h) / 2
        VolumeEscaleno = AreaBase * H
        return VolumeEscaleno
    else:
        print('opção inválida')
        return None
    
#       Volume Piramide
#Volume Piramide base Quadrada
def VolumePiramideQ(a, h):
        return (a**2) * h / 3
#Volume Piramide base Triangular
def VolumePiramideT(tipo, a, h, H):
    if tipo == 'E':
        areaBase = (a**2) * 1.73 / 4
        return areaBase * H / 3
    elif tipo == 'I':
        areaBase = (a * h) / 2
        return areaBase * H / 3
    elif tipo == 'Es':
        areaBase = (a * h) / 2
        return areaBase * H / 3
    else:
        print('opção inválida')
        return None
#Volume Piramide Base Hexagonal
def VolumePiramideH(a, h):
    areaBase = 6 * (a**2) * 1.73 / 4
    VolumePH = areaBase * h / 3
    return VolumePH

def main():
    while True:
        solido = input('(p)oliedro ou (c)orpo redondo\n')

        if solido == 'p':
            print('----Você escolheu poliedro----')
            poly = input('Escolha o tipo de Poliedro: prisma ou piramide\n')
            base = input('Qual a base: \n(Q)uadrada\n(R)etangular\n(T)riangular\n(H)exágono-Regular\n')
            if poly == 'prisma' and base == 'Q':
                a = float(input('Medida do lado da base: '))
                h = float(input('Altura do prisma: '))
                print(f'O volume do prisma é: {VolumePrismaQ(a, h)}')
            elif poly == 'prisma' and base == 'R':
                a = float(input('Medida do lado 1 da base: '))
                b = float(input('Medida do lado 2 da base: '))
                c = float(input('Altura do prisma: '))
                print(f'O volume do paralelepipedo é: {VolumePrismaR(a, b, c)}')
            elif poly == 'prisma' and base == 'H':
                l = float(input('Medida do lado da base: '))
                h = float(input('Altura do prisma: '))
                print(f'O volume do prisma hexagonal é: {VolumeHexagonal(l, h)}')
            elif poly == 'prisma' and base == 'T':
                l = float(input('Medida do lado: '))
                h = float(input('Altura da base: '))
                H = float(input('Altura do prisma triangular: '))
                tipo = input('Qual o tipo: (E)quilatero, (I)soceles, (Es)caleno\n')
                print(f'O volume do prisma triangular é: {VolumeTriangular(tipo, l, h, H,)}')
            elif poly == 'piramide' and base == 'Q':
                a = float(input('Medida do lado da base: '))
                h = float(input('Altura do piramide:'))
                print(f'O volume da Piramide de base Quadrada é: {VolumePiramideQ(a, h)}')
            elif poly == 'piramide' and base == 'T':
                a = float(input('Comprimento da base:'))
                h = float(input('Comprimento da altura da base:'))
                H = float(input('Altura da piramide:'))
                tipo = input('Qual o tipo: (E)quilatero, (I)soceles, (Es)caleno\n')
                print(f'O volume da Piramide de base Triangular é: {VolumePiramideT(tipo, a, h, H)}')
            elif poly == 'piramide' and base == 'H':
                a = float(input('Medida do lado da base:'))
                h = float(input('Altura da piramide:'))
                print(f'O volume da Piramide de base Hexagonal é: {VolumePiramideH(a, h)}')
            else:
                print('opção inválida')
        elif solido == 'c':
            print('----Você escolheu corpo redondo----')
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
        
        continuar = input('Deseja continuar? (s / n)\n')
        if continuar != 's':
            break

print(main())