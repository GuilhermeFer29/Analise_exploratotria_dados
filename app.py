# app.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_folium import folium_static
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Configurar a página
st.set_page_config(page_title="Análise de TI", layout="wide", background="#F5F5F5")
st.title("Análise Exploratória de Dados de TI")

# Carregar dados
df = pd.read_csv('./funcionarios_ti_nomes.csv')

# Seção 1:
st.header("Distribuição de Salários")
st.write(df['Salário'].describe())

# Gráficos
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.histplot(df['Salário'], bins=15, kde=True, color='green', ax=ax1)
st.pyplot(fig1)

# Seção 2:
st.header("Salário Médio por Cargo")
salario_por_cargo = df.groupby('Cargo')['Salário'].mean().sort_values(ascending=False)
st.bar_chart(salario_por_cargo)

# Seção 3:
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
    




st.header("Mapa de Profissionais")

# Configurar o geolocalizador
geolocator = Nominatim(
    user_agent="TI_Analysis_App/1.0",
    timeout=15
)
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

# Criar mapa
mapa = folium.Map(location=[-14.2350, -51.9253], zoom_start=4)

# Pré-processar cidades
cidades_validas = []
with st.spinner("Processando localizações..."):
    progress_bar = st.progress(0)
    total_cidades = len(df["Cidade"].unique())
    
    for i, cidade in enumerate(df["Cidade"].unique()):
        try:
            if pd.isna(cidade):
                continue
                
            
            location = geocode(f"{cidade}")
            
            if location:
                folium.Marker(
                    [location.latitude, location.longitude],
                    popup=f"{cidade}",
                    icon=folium.Icon(color="blue", icon="cloud")
                ).add_to(mapa)
                cidades_validas.append(cidade)
            
            progress_bar.progress((i + 1) / total_cidades)
            
        except Exception as e:
            st.error(f"Erro na cidade {cidade}: {str(e)}")
            continue

folium_static(mapa)

# Mostrar estatísticas
st.write(f"**Cidades mapeadas:** {len(cidades_validas)} de {total_cidades}")
