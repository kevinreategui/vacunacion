import streamlit as st

st.set_page_config(page_title="Grupo los malditos de CERTUS", layout="centered")

# Título con gradiente
st.markdown("""
<h1 style='
    text-align:center;
    background: linear-gradient(90deg, #1475fa 30%, #00c7b7 70%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size:3em;
    font-weight: bold;
    margin-top: 0.5em;
    margin-bottom: 0.5em;
'>Grupo los malditos de CERTUS</h1>
""", unsafe_allow_html=True)

# Mensaje de bienvenida alegre
st.markdown(
    """
    <div style='
        text-align:center;
        font-size:1.25em;
        margin-top:2em;
        margin-bottom:2em;
        color:#222;
    '>
        ¡Bienvenid@ a nuestro espacio digital!<br><br>
        Somos el <b>Grupo la Manchita Colorida</b>, un grupo unido, creativo y siempre con ganas de aprender.<br>
        Hemos disfrutado mucho este proyecto colaborativo, aportando ideas, risas y esfuerzo.<br><br>
        <b>Nos sentimos contentos y orgullosos de lo que logramos juntos 🤝🚀</b><br>
        Usa el menú de la izquierda para explorar nuestras secciones:<br>
        <span style='color:#1475fa; font-weight:bold;'>Grupo, Departamentos y Agradecimiento</span>.
    </div>
    """, unsafe_allow_html=True
)

st.markdown("---")

# Footer elegante y minimalista
st.markdown(
    """
    <footer style='
        width:100%;
        text-align:center;
        font-size:1em;
        color:#aaa;
        margin-top:3em;
        padding:1.2em 0 0.6em 0;
    '>
        Desarrollado con 💙 por el Grupo los malditos de CERTUS &copy; 2025
    </footer>
    """,
    unsafe_allow_html=True
)
