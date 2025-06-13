import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Vacunación COVID-19 Perú", layout="centered")
st.title("📊 Vacunación contra la COVID-19 en el Perú")
st.markdown("Fuente: [datosabiertos.gob.pe](https://www.datosabiertos.gob.pe/)")

@st.cache_data
def cargar_datos():
    df = pd.read_csv("datos/vacunacion_covid.csv", encoding='latin1', parse_dates=["FECHA_VACUNACION"])
    df = df.dropna(subset=["DEPARTAMENTO", "FECHA_VACUNACION", "DOSIS"])
    return df

df = cargar_datos()

st.sidebar.header("Filtros")
departamentos = sorted(df['DEPARTAMENTO'].unique())
departamento = st.sidebar.selectbox("Selecciona un departamento", departamentos)

fecha_min = df['FECHA_VACUNACION'].min()
fecha_max = df['FECHA_VACUNACION'].max()
rango_fechas = st.sidebar.date_input("Rango de fechas", [fecha_min, fecha_max])

df_filtrado = df[
    (df['DEPARTAMENTO'] == departamento) &
    (df['FECHA_VACUNACION'] >= pd.to_datetime(rango_fechas[0])) &
    (df['FECHA_VACUNACION'] <= pd.to_datetime(rango_fechas[1]))
]

st.write(f"Total de registros encontrados: {len(df_filtrado)}")

st.subheader("📈 Vacunas aplicadas por día")
vacunas_por_dia = df_filtrado.groupby("FECHA_VACUNACION").size()
fig1, ax1 = plt.subplots()
vacunas_por_dia.plot(ax=ax1, color='navy')
ax1.set_xlabel("Fecha")
ax1.set_ylabel("Cantidad")
ax1.set_title("Vacunación diaria")
st.pyplot(fig1)

st.subheader("📊 Distribución por tipo de dosis")
conteo_dosis = df_filtrado["DOSIS"].value_counts()
fig2, ax2 = plt.subplots()
conteo_dosis.plot(kind="bar", ax=ax2, color='green')
ax2.set_xlabel("Tipo de Dosis")
ax2.set_ylabel("Cantidad")
ax2.set_title("Tipos de Dosis Aplicadas")
st.pyplot(fig2)

if "GRUPO_RIESGO" in df.columns:
    st.subheader("👥 Grupo de riesgo")
    conteo_riesgo = df_filtrado["GRUPO_RIESGO"].value_counts()
    fig3, ax3 = plt.subplots()
    conteo_riesgo.plot(kind="barh", ax=ax3, color="orange")
    ax3.set_xlabel("Cantidad")
    ax3.set_ylabel("Grupo de Riesgo")
    st.pyplot(fig3)

st.markdown("---")
st.markdown("Desarrollado por el Equipo Académico - 2025")
