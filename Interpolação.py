#Interpolação E Cálculo de Título
#Emmanuel Sousa Lodron


n=0

def interpolacao(valor_possuido,valor_anterior1,valor_posterior1,valor_anterior2,valor_posterior2):
    valor_interpolado = (((valor_possuido-valor_anterior1)/(valor_posterior1-valor_anterior1))*(valor_posterior2-valor_anterior2))+valor_anterior2
    print()
    print(f'O valor interpolado é {round(valor_interpolado,8)}')
    print()

def calc_tit(V_possuido, Vliq, Vvap):
    titulo = (V_possuido - Vliq) / (Vvap - Vliq)
    print()
    print(f'O título é igual a {titulo}')
    print()
while n == 0:
    n = int(input('O que você deseja fazer? (1 p/ interpolar; 2 p/ cálculo de título)'))

    if n == 1:
        V = float(input('Qual o valor possuído? - '))
        va1 = float(input('Qual o valor anterior ao possuido? - '))
        vp1 = float(input('Qual o valor posterior ao possuido? - '))
        va2 = float(input('Qual o valor anterior de massa/volume específico ao possuído? - '))
        vp2 = float(input('Qual o valor posterior de massa/volume específico ao possuído? - '))    
        interpolacao(V,va1,vp1,va2,vp2)
        n=0

    else:
        if n == 2:
            V = float(input('Qual o volume especifico possuído? - '))
            vl = float(input('Qual o volume especifico de líquido? - '))
            vv = float(input('Qual o volume especifico de vapor? - '))
            calc_tit(V, vl,vv)
            n=0
        else:
            n = 0
