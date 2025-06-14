import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Vacunación COVID-19 Perú", layout="centered")
st.title("📊 Vacunación contra la COVID-19 en el Perú")
st.markdown("Fuente: [datosabiertos.gob.pe](https://www.datosabiertos.gob.pe/)")

@st.cache_data
def cargar_datos():
    df = pd.read_csv("datos/vacunacion_covid.csv", encoding='latin1')
    df.columns = df.columns.str.strip()
    if 'FECHA_VACUNACION' in df.columns:
        df['FECHA_VACUNACION'] = pd.to_datetime(df['FECHA_VACUNACION'], format='%Y%m%d', errors='coerce')
        df = df[df['FECHA_VACUNACION'].notna()]
    df = df.dropna(subset=["DEPARTAMENTO", "FECHA_VACUNACION", "DOSIS"])
    return df

df = cargar_datos()

# ---- Filtros ----
st.sidebar.header("Filtros")
departamentos = sorted(df['DEPARTAMENTO'].unique())
departamento = st.sidebar.selectbox("Selecciona un departamento", departamentos)

fecha_min = df['FECHA_VACUNACION'].min()
fecha_max = df['FECHA_VACUNACION'].max()
rango_fechas = st.sidebar.date_input("Rango de fechas", [fecha_min, fecha_max])

# ---- FIX para rango de fechas ----
if isinstance(rango_fechas, (list, tuple)):
    if len(rango_fechas) == 2:
        fecha_inicio, fecha_fin = rango_fechas
    elif len(rango_fechas) == 1:
        fecha_inicio = fecha_fin = rango_fechas[0]
    else:
        fecha_inicio = fecha_fin = fecha_min
else:
    fecha_inicio = fecha_fin = rango_fechas

df_filtrado = df[
    (df['DEPARTAMENTO'] == departamento) &
    (df['FECHA_VACUNACION'] >= pd.to_datetime(fecha_inicio)) &
    (df['FECHA_VACUNACION'] <= pd.to_datetime(fecha_fin))
]

st.write(f"Total de registros encontrados: {len(df_filtrado)}")

# ---- 1. Gráfico de líneas: Vacunas por día ----
st.subheader("📈 Vacunas aplicadas por día")
vacunas_por_dia = df_filtrado.groupby("FECHA_VACUNACION").size()
fig1, ax1 = plt.subplots()
vacunas_por_dia.plot(ax=ax1, color='#1475fa', marker='o')
ax1.set_xlabel("Fecha")
ax1.set_ylabel("Cantidad")
ax1.set_title("Vacunación diaria")
st.pyplot(fig1)

# ---- 2. Gráfico de barras: Tipo de dosis ----
st.subheader("📊 Distribución por tipo de dosis")
conteo_dosis = df_filtrado["DOSIS"].value_counts()
fig2, ax2 = plt.subplots()
conteo_dosis.plot(kind="bar", ax=ax2, color='#28a745')
ax2.set_xlabel("Tipo de Dosis")
ax2.set_ylabel("Cantidad")
ax2.set_title("Tipos de Dosis Aplicadas")
st.pyplot(fig2)

# ---- 3. Gráfico de pastel: Proporción de dosis ----
if len(conteo_dosis) > 1:
    st.subheader("🎂 Proporción por tipo de dosis")
    fig_pie, ax_pie = plt.subplots()
    conteo_dosis.plot.pie(
        ax=ax_pie,
        autopct='%1.1f%%',
        startangle=90,
        colors=['#4d6fa8', '#36a2eb', '#ffce56', '#ff6384'])
    ax_pie.set_ylabel('')
    ax_pie.set_title("Proporción de cada tipo de dosis")
    st.pyplot(fig_pie)

# ---- 4. Gráfico de barras horizontal: Top 10 departamentos ----
st.subheader("🏆 Top 10 Departamentos con más registros (en toda la base)")
top_deps = df['DEPARTAMENTO'].value_counts().head(10)
fig_top, ax_top = plt.subplots()
top_deps.sort_values().plot(kind='barh', ax=ax_top, color='#1475fa')
ax_top.set_xlabel("Cantidad de registros")
ax_top.set_ylabel("Departamento")
ax_top.set_title("Ranking de departamentos")
st.pyplot(fig_top)

# ---- Extra: Gráfico por grupo de riesgo (si existe) ----
if "GRUPO_RIESGO" in df.columns:
    st.subheader("👥 Grupo de riesgo")
    conteo_riesgo = df_filtrado["GRUPO_RIESGO"].value_counts()
    fig3, ax3 = plt.subplots()
    conteo_riesgo.plot(kind="barh", ax=ax3, color="#ff9800")
    ax3.set_xlabel("Cantidad")
    ax3.set_ylabel("Grupo de Riesgo")
    ax3.set_title("Distribución por grupo de riesgo")
    st.pyplot(fig3)

st.markdown("---")
st.markdown("Desarrollado por el Grupo 2 CERTUS - 2025")
