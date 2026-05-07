# 🤟 Traductor de Voz a Lengua de Señas Colombiana (LSC)

Este proyecto es una herramienta de accesibilidad desarrollada en **Python** que utiliza inteligencia artificial para capturar audio en tiempo real y traducirlo visualmente a **Lengua de Señas Colombiana (LSC)**.

## 🚀 Funcionalidades
- **Reconocimiento de voz:** Captura español colombiano y lo convierte a texto.
- **Traducción por secuencia:** Muestra videos o imágenes de señas de forma consecutiva.
- **Plan de respaldo (Dactilología):** Si una palabra no está en la base de datos, el sistema la deletrea automáticamente usando el alfabeto LSC.

## 🛠️ Tecnologías utilizadas
- **Python 3.x**
- **Streamlit:** Para la interfaz web.
- **SpeechRecognition:** Para el procesamiento de lenguaje natural (NLP) y audio.
- **GitHub:** Para el control de versiones.

## 📂 Estructura del Proyecto
- `app.py`: El motor principal de la aplicación.
- `requirements.txt`: Librerías necesarias para el despliegue.
- `assets/`: Carpeta que contiene los videos (.mp4) y las imágenes (.png) de las señas.
- `assets/alfabeto/`: Contiene las letras para el modo de deletreo.

## 🔧 Instalación y Uso Local
1. Clona este repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`.
3. Ejecuta la app: `streamlit run app.py`.

## 📌 Nota sobre el despliegue
Para que el micrófono funcione en la versión web (Streamlit Cloud), se requiere el uso de componentes WebRTC debido a las políticas de seguridad de los navegadores modernos.
