import streamlit as st

st.set_page_config(page_title="Grupo los malditos de CERTUS", layout="centered")

st.title("👩‍🎓 Grupo los malditos de CERTUS")

st.markdown("## Integrantes")

# Puedes cambiar las rutas a URLs si las fotos están en la web
integrantes = [
    {
        "nombre": "Kevin Reategui Rios",
        "foto": "kevin.jpg"
    },
    {
        "nombre": "Pedro Martinez Mustiga",
        "foto": "pedro.jpg"
    },
    {
        "nombre": "Dana Sosa Abanto",
        "foto": "dana.jpg"
    },
    {
        "nombre": "Jose Luis Dongo Calderon",
        "foto": "jose.jpg"
    }
]

# Mostrar las tarjetas alineadas
cols = st.columns(len(integrantes), gap="large")

for i, integrante in enumerate(integrantes):
    with cols[i]:
        st.image(integrante["foto"], width=150, use_column_width=False, caption=integrante["nombre"])
        st.markdown(
            f"<div style='text-align:center; font-size:1.15em; margin-top:0.5em; font-weight:bold;'>{integrante['nombre']}</div>",
            unsafe_allow_html=True
        )

st.success("¡Somos el Grupo los malditos de CERTUS!")

st.markdown("---")
st.markdown('<footer style="text-align:center;font-size:0.9em;">Desarrollado por el Grupo la Manchita Colorida - 2025</footer>', unsafe_allow_html=True)
