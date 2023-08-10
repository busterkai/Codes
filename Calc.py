#Calculadora Geral p/ Termodinâmica
#Emmanuel Sousa Lodron

import streamlit as st

def interpolacao(valor_possuido,valor_anterior1,valor_posterior1,valor_anterior2,valor_posterior2):
    valor_interpolado = (((valor_possuido-valor_anterior1)/(valor_posterior1-valor_anterior1))*(valor_posterior2-valor_anterior2))+valor_anterior2
    return(round(valor_interpolado,8))

def calc_tit(V_possuido, Vliq, Vvap):
    titulo = (V_possuido - Vliq) / (Vvap - Vliq)
    return(round(titulo,8))  

def calc_especific(x,pl,pv):
    p = (1-x)*pl + x*pv
    return(round(p,8))

st.title('Calculadora Geral para Termodinâmica')
st.sidebar.title('Programas')
programa_selecionado = st.sidebar.selectbox('Qual programa você quer utilizar?', ['Menu','Interpolador','Calculadora de Título','Calculadora de Propriedades Específicas'])

if programa_selecionado == 'Menu':
   st.image(image = 'https://www.coladaweb.com/wp-content/uploads/2014/12/termodinamica2.jpg')

elif programa_selecionado == 'Interpolador':
    try:
        n=0
        st.title('Insira os dados para realizar a Interpolação')
        V = st.number_input('Qual o valor possuído? (X3)')
        st.write('O valor possuído (X3) é: ', V)
        va1 = st.number_input('Qual o valor anterior ao possuído? (X1)')
        st.write('O valor anterior ao possuído (X1) é: ', va1)
        vp1 = st.number_input('Qual o valor posterior ao possuído? (X2)')
        st.write('O valor posterior ao possuído (X2) é:',vp1)
        va2 = st.number_input('Qual o valor referente ao anterior para o qual se deseja obter a interpolação? (Y1)')
        st.write('O valor referente ao anterior para o qual se deseja obter a interpolação ((Y1)) é:',va2)
        vp2 = st.number_input('Qual o valor referente ao posterior para o qual se deseja obter a interpolação? (Y2)')
        st.write('O valor referente ao posterior para o qual se deseja obter a interpolação (Y2) é:',vp2)
        interpolacao(V,va1,vp1,va2,vp2)
    except ZeroDivisionError:
        st.write('Aguardando valores...')          
    else:   
        st.write('O valor interpolado (Y3) é:',interpolacao(V,va1,vp1,va2,vp2))
                    
elif programa_selecionado == 'Calculadora de Título':
    try:
        st.title('Insira os dados para Calcular o Título(x)')
        V = st.number_input('Qual a propriedade específica possuída? (v/u/h/s)')
        st.write('A propriedade específica é:', V)
        vl = st.number_input('Qual a propriedade específica de líquido? (vl/ul/hl/sl)')
        st.write('A propriedade específica de líquido é:', vl)
        vv = st.number_input('Qual propriedade específica de vapor? (vv/uv/hv/sv)')
        st.write('A propriedade específica de vapor é:', vv)
        calc_tit(V,vl,vv)
    except ZeroDivisionError:
           st.write('Aguardando valores...')
    else:
        st.write('Seu título (x) é:',calc_tit(V,vl,vv))
    

elif programa_selecionado == 'Calculadora de Propriedades Específicas' :
    st.title('Insira os dados para calcular a Propriedade Específica desejada')
    x = st.number_input('Qual o título? (x)',min_value = 0.00000, max_value = 1.0)
    st.write('O título (x) é: ', x)
    pl = st.number_input('Qual a propriedade específica de líquido? (vl/ul/hl/sl)')
    st.write('A propriedade específica de líquido é:', pl)
    pv = st.number_input('Qual a propriedade específica de vapor? (vv/uv/hv/sv)')
    st.write('A propriedade específica de vapor é: ', pv)
    st.write('Sua propriedade específica é:',calc_especific(x,pl,pv))
