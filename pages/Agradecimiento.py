import streamlit as st

st.set_page_config(page_title="Agradecimiento", layout="centered")

st.title("🙏 Agradecimiento")
st.markdown("""
<div style='background:#e3f1ff; border-radius:10px; padding:2em 1.2em; text-align:center; font-size:1.2em;'>
    <b>¡Gracias, profesor Christian Adolfo Aliaga!</b><br><br>
    Le agradecemos sinceramente por su dedicación, paciencia y por compartir sus conocimientos en el curso de <b>MATEMÁTICAS APLICADAS</b>.<br><br>
    Este proyecto es el reflejo de lo mucho que hemos aprendido y disfrutado en sus clases.<br>
    <br>
    <i>¡Seguiremos creciendo y aplicando lo aprendido gracias a su guía!</i>
</div>
""", unsafe_allow_html=True)
st.balloons()

st.markdown("---")
st.markdown('<footer style="text-align:center;font-size:0.9em;">Desarrollado por el Grupo la Manchita Colorida - 2025</footer>', unsafe_allow_html=True)
