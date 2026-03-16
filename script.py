import streamlit as st
from time import sleep

st.set_page_config(page_title='Gestor de Metas', page_icon='🎯', layout="centered")

st.title('Meu Dashboard de Metas')

if 'metas' not in st.session_state:
    st.session_state.metas = []

total = len(st.session_state.metas)
st.write(f'Você tem **{total}** metas cadastradas. ')

col1, col2 = st.columns(2)

with col1:
    meta = st.text_input('Qual a sua meta?')
with col2:
    categoria = st.selectbox('Categoria', ['Estudos' , 'Saúde' , 'Financeiro' ] )

concluido=st.checkbox('Meta conluída?')

col3, col4 = st.columns(2)

with col3:
    if st.button('Adicionar Meta'):
        if meta:
            st.session_state.metas.append({
                'nome': meta,
                'cat' : categoria,
                'status' : concluido
            })
            st.success('Meta adicionada com sucesso!')
        else:
            st.error('Por favor, digite uma meta antes de salvar.')

with col3:
    if st.button('Reiniciar Metas'):
        st.error('Resetando')
        sleep(0.25)
        st.session_state.metas = []
        st.rerun()   

st.divider() 

st.subheader('Minhas Metas: ')

if not st.session_state.metas:
    st.info('Nenhuma meta cadastrada.')

for item in st.session_state.metas:
    if item['status']:
        st.success(f'✅ **{item['nome']}** | Categoria: {item['cat']}')
    else:
        st.info(f'⏳ **{item['nome']}** | Categoria: {item['cat']}')