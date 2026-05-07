import streamlit as st
import speech_recognition as sr
import os
import time

st.set_page_config(page_title="Traductor LSC", layout="wide")
st.title("🤟 Intérprete de Secuencias LSC")

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.toast("Escuchando conferencia...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio, language="es-CO").lower()
        except:
            return None

if st.button("🎤 Iniciar Traducción en Tiempo Real"):
    frase = escuchar()
    
    if frase:
        st.subheader(f"Texto detectado: {frase}")
        palabras = frase.split() # Divide la frase en palabras individuales
        
        # Creamos un contenedor para que las imágenes/videos cambien en el mismo lugar
        espacio_visual = st.empty()
        
        for p in palabras:
            video_path = f"assets/{p}.mp4"
            imagen_path = f"assets/{p}.png"
            
            if os.path.exists(video_path):
                espacio_visual.video(video_path)
                time.sleep(2) # Tiempo para ver la seña
            elif os.path.exists(imagen_path):
                espacio_visual.image(imagen_path, caption=f"Seña: {p}", width=400)
                time.sleep(1.5)
            else:
                # Si la palabra no existe, la deletreamos rápido
                st.write(f"Deletreando: {p}")
                for letra in p:
                    ruta_letra = f"assets/alfabeto/{letra}.png"
                    if os.path.exists(ruta_letra):
                        espacio_visual.image(ruta_letra, caption=letra.upper(), width=200)
                        time.sleep(0.5)
        
        st.success("Traducción finalizada.")
