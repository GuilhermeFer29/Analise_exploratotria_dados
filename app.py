# app.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Configurar a página
st.set_page_config(page_title="Análise de TI", layout="wide")
st.title("Análise Exploratória de Dados de TI")

# Carregar dados
df = pd.read_csv('funcionarios_ti_nomes.csv')

# Seção 1: Distribuição de Salários
st.header("Distribuição de Salários")
st.write(df['Salário'].describe())

# Gráficos
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.histplot(df['Salário'], bins=15, kde=True, color='green', ax=ax1)
st.pyplot(fig1)

# Seção 2: Salário Médio por Cargo
st.header("Salário Médio por Cargo")
salario_por_cargo = df.groupby('Cargo')['Salário'].mean().sort_values(ascending=False)
st.bar_chart(salario_por_cargo)

# Seção 3: Distribuição Geográfica
st.header("Distribuição Geográfica")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Top Cidades")
    cidades_comuns = df['Cidade'].value_counts().head(10)
    st.bar_chart(cidades_comuns)
with col2:
    st.subheader("Top Estados")
    estados_comuns = df['Estado'].value_counts().head(10)
    st.bar_chart(estados_comuns)
with col3:
    st.subheader("Top Países")
    paises_comuns = df['País'].value_counts()
    st.bar_chart(paises_comuns)

# Mapa (Folium)
st.header("Mapa de Profissionais")
import folium
from streamlit_folium import folium_static

mapa = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)
for cidade in df["Cidade"].unique():
    # Adicione lógica para geolocalização (exemplo simplificado)
    # (Substitua por sua implementação real)
    pass
folium_static(mapa)