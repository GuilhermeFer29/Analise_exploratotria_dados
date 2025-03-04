# 📊 Análise Exploratória de Dados (EDA) – Funcionários de TI

Este repositório contém um estudo de **Análise Exploratória de Dados (EDA)** sobre **funcionários da área de Tecnologia da Informação (TI)**. O objetivo é explorar padrões salariais, distribuição geográfica e insights relevantes utilizando **Python**, **Pandas**, **Seaborn** e **Folium**.

---

## 👉 Tecnologias Utilizadas
- 🐖 Python  
- 📊 Pandas & NumPy  
- 🌍 Folium (Mapas Interativos)  
- 🌄 Geopy (Geocodificação de cidades)  
- 📉 Seaborn & Matplotlib (Visualização de dados)  

---

## 📂 Estrutura do Projeto
```
📁 Analise_exploratotria_dados
│── 📄 funcionarios_ti_nomes.csv           # Base de dados usada na análise
│── 📄 analise_exploratoria.ipynb # Código da análise exploratória
│── 📄 README.md             # Documentação do projeto
```

---

## 🚀 Análises Realizadas
### 1️⃣ Salário Médio por Cargo
📉 Descobrimos quais cargos pagam mais e quais têm salários abaixo da média.

```python
df.groupby("Cargo")["Salário"].mean().sort_values(ascending=False)
```

👀 **Visualização**:
![Gráfico de Salários](https://via.placeholder.com/800x400?text=Gr%C3%A1fico+de+Sal%C3%A1rios)

---

### 2️⃣ Distribuição Geográfica dos Funcionários
💚 Criamos um **mapa interativo** para visualizar a concentração de funcionários por cidade.

```python
import folium
from geopy.geocoders import Nominatim
```

👀 **Mapa Interativo**:
![Mapa Interativo](https://via.placeholder.com/800x400?text=Mapa+Interativo)

---

### 3️⃣ Detecção de Outliers nos Salários
📉 Aplicamos o **Intervalo Interquartil (IQR)** para identificar salários fora do padrão.

```python
Q1 = df["Salário"].quantile(0.25)
Q3 = df["Salário"].quantile(0.75)
IQR = Q3 - Q1
```

💡 **Resultado**:
- Nenhum outlier encontrado ✅  
- Salários distribuídos de forma homogênea 📊  

---

## 💾 Como Executar o Projeto
1. **Clone o repositório**  
   ```sh
   git clone https://github.com/GuilhermeFer29/Analise_exploratotria_dados.git
   cd Analise_exploratotria_dados
   ```
2. **Instale as dependências**  
   ```sh
   pip install pandas numpy seaborn matplotlib folium geopy
   ```
3. **Execute a análise**  
   ```sh
   python analise_exploratoria.py
   ```

---

## 💪 Contribuições
Quer contribuir? Fique à vontade para abrir um **Pull Request** ou sugerir melhorias! 💡

---

## 📝 Licença
Este projeto está sob a licença **MIT** – sinta-se à vontade para usar e modificar. 😊  

---

📌 **Feito por [Seu Nome](https://www.linkedin.com/in/guilherme-fernandes-do-bem/) 🚀**
