#Interpolação E Cálculo de Título
#Emmanuel Sousa Lodron

import streamlit as st
import time


def interpolacao(valor_possuido,valor_anterior1,valor_posterior1,valor_anterior2,valor_posterior2):
    valor_interpolado = (((valor_possuido-valor_anterior1)/(valor_posterior1-valor_anterior1))*(valor_posterior2-valor_anterior2))+valor_anterior2
    return(round(valor_interpolado,8))

def calc_tit(V_possuido, Vliq, Vvap):
    titulo = (V_possuido - Vliq) / (Vvap - Vliq)
    return(round(titulo,8))  

def calc_especific(x,pl,pv):
    p = (1-x)*pl + x*pv
    return(round(p,8))

def calc_calor(U1,U2,m,W):
    Q = ((U2-U1)*m + W)
    return(Q)

st.title('Calculadora Geral para Termodinamica')
st.sidebar.title('Programas')
programa_selecionado = st.sidebar.selectbox('Qual programa você quer utilizar?', ['Menu','Interpolador','Calculadora de Título','Calculadora de Propriedades Específicas','Quantidade de Calor'])

if programa_selecionado == 'Menu':
   st.image(image = 'https://www.coladaweb.com/wp-content/uploads/2014/12/termodinamica2.jpg')

elif programa_selecionado == 'Interpolador':
    try:
        n=0
        st.title('Insira os dados para realizar a Interpolação')
        V = st.number_input('Qual o valor possuído?')
        st.write('O valor possuído é: ', V)
        va1 = st.number_input('Qual o valor anterior ao possuído?')
        st.write('O valor anterior ao possuído é: ', va1)
        vp1 = st.number_input('Qual o valor posterior ao possuído?')
        st.write('O valor posterior ao possuído é:',vp1)
        va2 = st.number_input('Qual o valor referente ao anterior para o qual se deseja obter a interpolação?')
        st.write('O valor referente ao anterior para o qual se deseja obter a interpolação é:',va2)
        vp2 = st.number_input('Qual o valor referente ao posterior para o qual se deseja obter a interpolação?')
        st.write('O valor referente ao posterior para o qual se deseja obter a interpolação é:',vp2)
        interpolacao(V,va1,vp1,va2,vp2)
    except ZeroDivisionError:
        st.write('Aguardando valores...')          
    else:   
        st.write('O valor interpolado é:',interpolacao(V,va1,vp1,va2,vp2))

    
                    
elif programa_selecionado == 'Calculadora de Título':
    try:
        st.title('Insira os dados para Calcular o Título(x)')
        V = st.number_input('Qual o volume específico possuído?')
        st.write('O volume específico é:', V)
        vl = st.number_input('Qual o volume específico de líquido?')
        st.write('O volume específico de líquido é:', vl)
        vv = st.number_input('Qual o volume específico de vapor?')
        st.write('O volume específico de vapor é:', vv)
        calc_tit(V,vl,vv)
    except ZeroDivisionError:
           st.write('Aguardando valores...')
    else:
        st.write('Seu título é:',calc_tit(V,vl,vv))
    

elif programa_selecionado == 'Calculadora de Propriedades Específicas' :
    st.title('Insira os dados para calcular a Propriedade Específica desejada')
    x = st.number_input('Qual o título?',min_value = 0.0, max_value = 1.0)
    st.write('O título é: ', x)
    pl = st.number_input('Qual a propriedade específica de líquido?')
    st.write('A propriedade específica de líquido é:', pl)
    pv = st.number_input('Qual a propriedade específica de vapor?')
    st.write('A propriedade específica de vapor é: ', pv)
    st.spinner(text="In progress...")
    st.write('Seu valor especifico é:',calc_especific(x,pl,pv))

elif programa_selecionado == 'Quantidade de Calor':
    st.title('Insira os dados para calcular a Quantidade de Calor (Q)')
    U1 = st.number_input('Qual a energia específica interna 1?')
    st.write('A energia específica interna 1 é:',U1)
    U2 = st.number_input('Qual a energia específica interna 2?') 
    st.write('A energia específica interna 2 é:',U2)
    m = st.number_input('Qual a massa do sistema?')
    st.write('A massa do sistema é:',m)
    W = st.number_input('Qual o trabalho do sistema? (Insira com o sinal encontrado)')
    st.write('Seu calor calculado é:',calc_calor(U1,U2,m,W))