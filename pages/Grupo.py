import streamlit as st

st.set_page_config(page_title="Grupo Web-iadores", layout="centered")

st.title("👩‍🎓 Grupo Las Machonas")

st.markdown("""
<div style='display:flex; justify-content:center; margin-top:2em;'>
  <table style='
      border-collapse:collapse;
      background:#f8fbff;
      border-radius:14px;
      box-shadow:0 2px 10px rgba(40,100,200,0.07);
      min-width:340px;
      font-size:1.13em;
      '>
    <thead>
      <tr>
        <th style='padding:14px 30px; background:#4d6fa8; color:#fff;'>N°</th>
        <th style='padding:14px 60px 14px 22px; background:#4d6fa8; color:#fff;'>Integrante</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style='padding:10px 0; text-align:center; border-bottom:1px solid #d2e4fa;'>1</td>
        <td style='padding:10px 0 10px 18px; border-bottom:1px solid #d2e4fa;'>Pamela Ramírez</td>
      </tr>
      <tr>
        <td style='padding:10px 0; text-align:center; border-bottom:1px solid #d2e4fa;'>2</td>
        <td style='padding:10px 0 10px 18px; border-bottom:1px solid #d2e4fa;'>Joselyn Díaz</td>
      </tr>
      <tr>
        <td style='padding:10px 0; text-align:center; border-bottom:1px solid #d2e4fa;'>3</td>
        <td style='padding:10px 0 10px 18px; border-bottom:1px solid #d2e4fa;'>Karen Huamán</td>
      </tr>
      <tr>
        <td style='padding:10px 0; text-align:center;'>4</td>
        <td style='padding:10px 0 10px 18px;'>Kevin Reategui</td>
      </tr>
    </tbody>
  </table>
</div>
""", unsafe_allow_html=True)

st.success("¡Somos el grupo Web-iadores")

st.markdown("---")
st.markdown('<footer style="text-align:center;font-size:0.9em;">Desarrollado por el Grupo Las Machonas - 2025</footer>', unsafe_allow_html=True)
