import streamlit as st
import speech_recognition as sr
import os
import time

st.set_page_config(page_title="LSC Translator", layout="wide")
st.title("🤟 Intérprete LSC")

# Opción para subir audio (es lo más estable en la web)
archivo_audio = st.file_uploader("Sube un audio (.wav) o graba uno desde tu celular", type=["wav"])
if archivo_audio is not None:
    r = sr.Recognizer()
    with sr.AudioFile(archivo_audio) as source:
        audio = r.record(source)
        try:
            frase = r.recognize_google(audio, language="es-CO").lower()
            st.subheader(f"Texto detectado: {frase}")
            
            palabras = frase.split()
            espacio_visual = st.empty()
            
            for p in palabras:
                video_path = f"assets/{p}.mp4"
                imagen_path = f"assets/{p}.png"
                
                if os.path.exists(video_path):
                    espacio_visual.video(video_path)
                    time.sleep(2)
                elif os.path.exists(imagen_path):
                    espacio_visual.image(imagen_path, caption=f"Seña: {p}", width=400)
                    time.sleep(1.5)
                else:
                    st.write(f"Deletreando: {p}")
                    for letra in p:
                        ruta_letra = f"assets/alfabeto/{letra}.png"
                        if os.path.exists(ruta_letra):
                            espacio_visual.image(ruta_letra, caption=letra.upper(), width=200)
                            time.sleep(0.5)
        except:
            st.error("No pude procesar ese audio. Intenta con un archivo .wav claro.")
