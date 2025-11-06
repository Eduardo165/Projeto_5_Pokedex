import streamlit as st
import json 
import requests

st.set_page_config(layout="wide")

with open('pokemon_index.json' , 'r' , encoding='utf-8') as arquivo:
    nomes_pokemons = json.load(arquivo)

nome = st.selectbox('Escolha um pokemon' , nomes_pokemons.values())

url = f'https://pokeapi.co/api/v2/pokemon/{nome}'

pokemon = requests.get(url).json()

col1, col2, col3 = st.columns(3)

with col1:
    st.image(pokemon['sprites']['front_default'] , width=300)
    st.markdown('## Normal')

with col2:
    st.title(nome.capitalize())
    st.audio(pokemon['cries']['latest'])
    st.audio(pokemon['cries']['legacy'])

with col3:
    st.image(pokemon['sprites']['front_shiny'] , width=300)
    st.markdown('## Shiny')
    
col1, col2, col3 = st.columns(3)
altura = pokemon['height'] / 10
peso = pokemon['weight'] / 10
imc = peso/(altura**2)

with col1:
    st.metric('Altura' , f'{altura} M')

with col2:
    st.metric('IMC' , f'{imc:.2f}')

with col3:
    st.metric('Peso', f'{peso} KG')



tipos, status, locais, habilidades = st.tabs(['Tipos', 'Status' , 'Locais' , 'Habilidades'])

with tipos:
    for tipo in pokemon['types']:
        st.markdown(f'-{tipo['type']['name']}')

with status:
    hp , ataque , defesa, ataque_esp, defesa_esp, velocidade = st.columns(6)

    with hp:
        st.metric('HP', pokemon['stats'][0]['base_stat'])

    with ataque:
        st.metric('ATAQUE', pokemon['stats'][1]['base_stat'])

    with defesa:
        st.metric('DEFESA', pokemon['stats'][2]['base_stat'])

    with ataque_esp:
        st.metric('ATAQUE ESPECIAL', pokemon['stats'][3]['base_stat'])

    with defesa_esp:
        st.metric('DEFESA ESPECIAL', pokemon['stats'][4]['base_stat'])

    with velocidade:
        st.metric('VELOCIDADE', pokemon['stats'][5]['base_stat'])



with locais:
    locais = requests.get(pokemon['location_area_encounters']).json()
    for local in locais:
        st.markdown(f'- {local['location_area']['name']}')

with habilidades:
    for habilidades in pokemon['abilities']:
         st.markdown(f'-{habilidades['ability']['name']}')