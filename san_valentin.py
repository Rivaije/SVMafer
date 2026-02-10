import streamlit as st
import time

# Configuración de la página
st.set_page_config(
    page_title="💖 San Valentín 💖",
    page_icon="❤️",
    layout="centered"
)

# Estado para controlar la historia
if "paso" not in st.session_state:
    st.session_state.paso = 0

st.title("❤️ Para mi preciosa Mafer ❤️")

# PASO 0
if st.session_state.paso == 0:
    st.write("Oye… tengo algo muy importante que decirte 💌")
    if st.button("Siguiente 💖"):
        st.session_state.paso = 1

# PASO 1
elif st.session_state.paso == 1:
    st.write(
        "Desde el **20 de diciembre**, cuando hablamos por primera vez, "
        "todo ha sido mucho más bonito 💕"
    )
    if st.button("Siguiente ✨"):
        st.session_state.paso = 2

# PASO 2
elif st.session_state.paso == 2:
    st.write(
        "Cada momento contigo es especial, "
        "y hoy quería preguntarte algo… ❤️"
    )
    if st.button("Siguiente 💫"):
        st.session_state.paso = 3

# PASO 3 — PROGRESO + SPINNER + PREGUNTA
elif st.session_state.paso == 3:
    st.write("Preparando la pregunta importante para ti💖")

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)


    st.markdown("## 💘 ¿Quieres ser mi San Valentín? 💘")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Sí 💖"):
            st.session_state.paso = 4

    with col2:
        if st.button("Claro que sí 😍"):
            st.session_state.paso = 4

# PASO 4 — FINAL FELIZ 💖
elif st.session_state.paso == 4:
    st.balloons()

    st.markdown("## 💖 Gracias por hacerme tan feliz 💖")
    st.write("Prometo cuidar este momento contigo ❤️")
    st.write("Hoy, mañana y siempre, mi enojona 💘")
    st.write("❤️ ❤️ ❤️ ❤️ ❤️")

    if st.button("Volver a empezar 🔁"):
        st.session_state.paso = 0